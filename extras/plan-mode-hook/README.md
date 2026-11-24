# Hook de plan mode (solo Claude Code, opcional)

Hace que Claude cargue la skill **ask** antes de presentar un plan en plan mode:
1. Al mandar un mensaje en plan mode, si `ask` no ha corrido en ese plan, le recuerda cargarla.
2. Si intenta presentar el plan sin haberla cargado, lo frena **una vez** por plan (nunca deja una
   sesión atorada).

Escribe "sin ask" en tu mensaje para saltarla en un plan. Si el hook falla, deja pasar.

## Instalar

1. Copia `plan_ask.py` a `~/.claude/hooks/`.
2. Agrega esto a `~/.claude/settings.json` (júntalo con tus hooks si ya tienes):

```json
{
  "hooks": {
    "UserPromptSubmit": [
      { "hooks": [{ "type": "command", "command": "python3 $HOME/.claude/hooks/plan_ask.py prompt" }] }
    ],
    "PreToolUse": [
      { "matcher": "ExitPlanMode",
        "hooks": [{ "type": "command", "command": "python3 $HOME/.claude/hooks/plan_ask.py exit" }] }
    ]
  }
}
```

3. Revisa en `/hooks` que aparezcan.

Otras herramientas (Codex, OpenCode) no tienen plan mode igual: ahí basta con pedir "usa ask antes
de planear" o ponerlo en tu `AGENTS.md`.
