#!/usr/bin/env python3
"""Plan mode loads the `ask` skill before the plan is written, once per plan.

"The current plan" is everything since the session last switched into plan mode (the transcript
records `permissionMode` on the user's messages). Within it:
- UserPromptSubmit (arg `prompt`): while `ask` has not run, add a reminder to the model's context.
- PreToolUse on ExitPlanMode (arg `exit`): while `ask` has not run, deny presenting the plan, but
  only once per plan, so a session where nobody can answer (headless, no Skill tool) never gets
  stuck.
A typed user prompt with "sin ask" switches both off for the current plan. Any error lets the
action through: this hook must never lock a session.
"""

import json
import re
import sys

ASK_COMMAND = re.compile(r"<command-name>/?ask</command-name>|^\s*/ask\b")
SKIP = re.compile(r"\bsin ask\b", re.IGNORECASE)
DENIED_MARK = "[plan_ask:denied]"
REMINDER = (
    "Estás en plan mode. Antes de escribir el plan, carga la skill `ask` (herramienta Skill, "
    'skill: "ask") y haz la entrevista si este mensaje pide un plan. Si es un cambio chico, la '
    "skill dice que no hay entrevista."
)
DENIED = (
    f"{DENIED_MARK} Todavía no se ha cargado la skill `ask` en este plan. Cárgala (herramienta "
    'Skill, skill: "ask") y haz la entrevista; si es un cambio chico o nadie puede contestar, '
    "di por qué y vuelve a presentar el plan: esta revisión no se repite."
)
# Lines worth parsing; the rest of the transcript is skipped without json.loads.
NEEDLES = ('"permissionMode"', '"ask"', "/ask", "sin ask", DENIED_MARK)


def _typed_texts(message: dict):
    """Text the user typed: never tool results, hook output or meta entries."""
    content = message.get("content")
    if isinstance(content, str):
        yield content
        return
    if isinstance(content, list):
        if any(isinstance(b, dict) and b.get("type") == "tool_result" for b in content):
            return
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                yield block.get("text", "")


def _tool_result_texts(message: dict):
    for block in message.get("content") or []:
        if isinstance(block, dict) and block.get("type") == "tool_result":
            inner = block.get("content")
            if isinstance(inner, str):
                yield inner
            elif isinstance(inner, list):
                for b in inner:
                    if isinstance(b, dict) and b.get("type") == "text":
                        yield b.get("text", "")


def current_plan(transcript_path: str) -> dict | None:
    """What happened since the session last switched into plan mode."""
    state = {"ask": False, "skip": False, "denied": False}
    last_mode = None
    try:
        f = open(transcript_path, encoding="utf-8")
    except FileNotFoundError:  # first prompt of a session: nothing has happened yet
        return None
    with f:
        for line in f:
            if not any(n in line for n in NEEDLES):
                continue
            try:
                entry = json.loads(line)
            except ValueError:
                continue
            mode = entry.get("permissionMode")
            if mode is not None:
                if mode == "plan" and last_mode != "plan":
                    state = {"ask": False, "skip": False, "denied": False}
                last_mode = mode
            message = entry.get("message") or {}
            content = message.get("content")
            if isinstance(content, list):
                for block in content:
                    if (
                        isinstance(block, dict)
                        and block.get("type") == "tool_use"
                        and block.get("name") == "Skill"
                        and (block.get("input") or {}).get("skill") == "ask"
                    ):
                        state["ask"] = True
            typed = (
                entry.get("type") == "user"
                and not entry.get("isMeta")
                and not entry.get("isCompactSummary")
            )
            if typed:
                for text in _typed_texts(message):
                    if ASK_COMMAND.search(text):
                        state["ask"] = True
                    # Tags mean the harness wrote it (reminders, task notifications, command
                    # output), not the user.
                    if not text.lstrip().startswith("<") and SKIP.search(text):
                        state["skip"] = True
                if any(DENIED_MARK in t for t in _tool_result_texts(message)):
                    state["denied"] = True
    return state


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    data = json.load(sys.stdin)
    if data.get("agent_id"):  # a subagent: its plans are not the user's
        return
    if mode == "prompt":
        if data.get("permission_mode") != "plan":
            return
        prompt = data.get("prompt", "")
        if SKIP.search(prompt) or ASK_COMMAND.search(prompt):
            return
        plan = current_plan(data["transcript_path"])
        if plan and (plan["ask"] or plan["skip"]):
            return
        out = {"hookEventName": "UserPromptSubmit", "additionalContext": REMINDER}
        print(json.dumps({"hookSpecificOutput": out}, ensure_ascii=False))
    elif mode == "exit":
        plan = current_plan(data["transcript_path"])
        if plan is None or plan["ask"] or plan["skip"] or plan["denied"]:
            return  # without a transcript the denial could not be counted: let it through
        out = {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": DENIED,
        }
        print(json.dumps({"hookSpecificOutput": out}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:  # never lock a session because of this hook
        sys.exit(0)
