#!/usr/bin/env python3
"""Run every story's `verify` commands and record whether it passes.

The rule this script enforces: `passes`, `verified_at` and `commit` are written only here, never by
hand or by an agent's say-so. A story passes when every command in its `verify` exits 0 and none
reports skipped tests. A failing story in `review` or `done` fails the check (exit 1); one still in
progress is only recorded.

Usage:
  progress_check.py [--dry-run] [progress.json ...]

Without paths, it checks every `progress.json` under the current directory (skipping .git,
node_modules and virtualenvs). Commands run from the repository root (or the current directory
outside git). Standard library only, Python 3.9+.
"""

import argparse
import datetime as dt
import json
import re
import shlex
import subprocess
import sys
from pathlib import Path

BLOCKING = {"review", "done"}
SKIPPED = re.compile(r"\b\d+ skipped\b", re.IGNORECASE)
IGNORED_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build"}
TIMEOUT_S = 1800


def sh(command, cwd):
    try:
        done = subprocess.run(
            shlex.split(command), cwd=cwd, capture_output=True, text=True,
            check=False, timeout=TIMEOUT_S,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        return 1, str(error)
    return done.returncode, done.stdout + done.stderr


def passes(command, cwd):
    code, output = sh(command, cwd)
    return code == 0 and not SKIPPED.search(output), output


def repo_root(start):
    code, output = sh("git rev-parse --show-toplevel", start)
    return Path(output.strip()) if code == 0 and output.strip() else start


def current_commit(root):
    code, output = sh("git rev-parse --short HEAD", root)
    if code != 0 or not output.strip():
        return None
    commit = output.strip()
    _, status = sh("git status --porcelain", root)
    return commit + "+changes" if status.strip() else commit  # what passed was the working tree


def find_files(start):
    found = []
    for path in sorted(start.rglob("progress.json")):
        if not IGNORED_DIRS.intersection(path.relative_to(start).parts):
            found.append(path)
    return found


def check_file(path, root, commit, now, dry_run):
    data = json.loads(path.read_text(encoding="utf-8"))
    blocking = []
    for story in data.get("stories", []):
        verify = story.get("verify") or []
        if not verify:
            continue
        ok, failed_output, failed_command = True, "", ""
        for command in verify:
            ok, failed_output = passes(command, root)
            if not ok:
                failed_command = command
                break
        story.update(passes=ok, verified_at=now, commit=commit)
        mark = "ok  " if ok else "FAIL"
        print(f"{mark} {story.get('key', '?')} [{story.get('state', '?')}] {story.get('title', '')}")
        if not ok:
            print(f"     ✗ {failed_command}")
            if story.get("state") in BLOCKING:
                tail = "\n".join(failed_output.strip().splitlines()[-15:])
                blocking.append((story.get("key", "?"), failed_command, tail))
    if not dry_run:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return blocking


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--dry-run", action="store_true", help="report without writing")
    args = parser.parse_args(argv)

    cwd = Path.cwd()
    root = repo_root(cwd)
    files = [f.resolve() for f in args.files] or find_files(cwd)
    if not files:
        print("No progress.json found.")
        return 0
    commit = current_commit(root)
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")

    blocking = []
    for path in files:
        print(f"# {path}")
        blocking += check_file(path, root, commit, now, args.dry_run)

    if blocking:
        print(f"\n{len(blocking)} historia(s) en review/done no pasan y bloquean:")
        for key, command, tail in blocking:
            print(f"\n## {key}: {command}\n{tail}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
