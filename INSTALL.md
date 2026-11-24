# Instalar `joaquinrog/skills` (instrucciones para el agente)

> Este archivo lo lee un agente de IA (Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot,
> Hermes…) cuando la persona le pide "instala las skills de joaquinrog/skills". Síguelo en orden y
> **no le pidas a la persona que abra otra terminal**: corre tú los comandos.

## 1. Detecta dónde estás

Identifica tu herramienta (tú sabes cuál eres). Si no puedes correr comandos, salta al paso 4.

## 2. Instala las skills

**Si eres Claude Code**, instala el plugin (trae skills y agentes, y se actualiza solo):

```bash
claude plugin marketplace add joaquinrog/skills
claude plugin install skills@joaquinrog
```

**Cualquier otro agente** (Codex, Gemini CLI, OpenCode, Cursor, Copilot, Windsurf, Amp, Hermes…):

```bash
npx -y skills@latest add joaquinrog/skills --skill '*' -a <tu-agente> -g -y
```

Cambia `<tu-agente>` por tu nombre en el instalador (`codex`, `gemini-cli`, `opencode`, `cursor`,
`github-copilot`…). Si no sabes el nombre exacto, corre `npx -y skills@latest add --help` y búscalo.
`-g` las instala para todos los proyectos de la persona; quítalo si pidió solo este proyecto.

## 3. Los dos agentes revisores (fuera de Claude Code)

`agents/revisor-de-plan.md` y `agents/verificador-de-cierre.md` son subagentes. Regístralos con el
formato de tu herramienta, sin investigarlo: aquí está. El cuerpo de cada archivo (sin el
encabezado `---`) son las instrucciones. Usa el mismo alcance que en el paso 2.

- **Codex:** un archivo por agente en `.codex/agents/<nombre>.toml` (global: `~/.codex/agents/`):
  ```toml
  name = "revisor-de-plan"
  description = "<la description del encabezado>"
  developer_instructions = '''
  <cuerpo del archivo>
  '''
  ```
- **OpenCode:** `.opencode/agents/<nombre>.md` (global: `~/.config/opencode/agents/`), con
  encabezado `description: …` y `mode: subagent`, y el cuerpo igual.
- **Gemini CLI, Cursor y otros sin subagentes:** no los registres; dile a la persona que existen y
  que puede usarlos como prompt de una sesión aparte.

Recomienda correrlos en el modelo más fuerte que tenga.

## 4. Si no puedes correr comandos

Descarga `https://github.com/joaquinrog/skills/archive/refs/heads/main.zip`, y copia cada carpeta de
`skills/` a la carpeta de skills de tu herramienta (por ejemplo `~/.agents/skills/`,
`~/.gemini/skills/`, `~/.claude/skills/`). Si tampoco puedes escribir archivos, explica a la persona
estos mismos pasos en lenguaje simple.

## 5. Instala también las compañeras

El kit recomienda dos skills de otros autores, que sirven para problemas muy específicos. Instálalas
junto con el kit, con el mismo alcance (global o de proyecto) y el mismo agente, sin preguntar:

| Skill | Para qué | Comando |
|---|---|---|
| `find-skills` (Vercel) | Buscar e instalar la skill indicada para un problema concreto | `npx -y skills@latest add vercel-labs/skills --skill find-skills -a <tu-agente> -g -y` |
| `skill-creator` (Anthropic) | Crear y mejorar tus propias skills | `npx -y skills@latest add anthropics/skills --skill skill-creator -a <tu-agente> -g -y` |

En Claude Code usa los mismos comandos `npx` con `-a claude-code`. Solo sáltalas si la persona dijo
que no las quiere.

## 6. Comprueba y cuéntale

1. Lista tus skills y confirma que aparecen `usando-el-kit`, `ask`, `progress`, `cierre-de-sesion`,
   `find-skills` y `skill-creator`.
2. Dile a la persona, en una o dos líneas, qué quedó instalado y dónde.
3. Si hace falta reiniciar la sesión para que las vea, díselo.
4. Sugiere el primer paso: *"Pídeme que planee algo y te entrevisto con `ask`"*.
