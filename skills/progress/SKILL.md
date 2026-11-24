---
name: progress
description: "Lleva en progress.json qué historias del proyecto funcionan de verdad: cada una con el comando que lo demuestra, y passes lo escribe solo el script al correrlo, nunca un agente a mano. Úsala al crear o cerrar una historia, al preguntar qué funciona, antes de un handoff o un PR. / Track which stories really work in progress.json: passes is written only by running each story's verify command, never by hand."
---

# Progress: qué funciona, con evidencia

Un agente que dice "ya quedó" no es evidencia. Esta skill separa **qué se dice** de **qué pasa**:
cada historia trae el comando que la prueba, y el campo `passes` solo lo escribe el script al
correrlo. Así el estado del proyecto sobrevive al cambio de sesión, de persona o de modelo.

## El archivo

Un `progress.json` por proyecto o por paquete (plantilla en `references/progress.template.json`):

```json
{
  "name": "mi-app",
  "stories": [
    {
      "key": "LOGIN-1",
      "title": "El usuario entra con correo y contraseña",
      "state": "in_progress",
      "verify": ["pytest tests/test_login.py -q"],
      "note": "Falta el caso de contraseña olvidada"
    }
  ]
}
```

- `state`: `not_started`, `in_progress`, `review`, `done` o `blocked`. Lo cambia una persona o un
  agente cuando cambia en la práctica.
- `verify`: comandos que salen con 0 si la historia funciona. Pruebas chicas y específicas, no la
  suite entera.
- `passes`, `verified_at`, `commit`: **solo los escribe el script.** Si un agente los edita a mano,
  es falta.
- Puedes agregar campos (`jira`, `owner`…): el script los conserva.

## Cómo se corre

```bash
python3 <ruta-de-esta-skill>/scripts/progress_check.py            # todos los progress.json
python3 <ruta-de-esta-skill>/scripts/progress_check.py --dry-run  # sin escribir
```

Copia el script a tu repo (por ejemplo `tools/progress_check.py`) y, si usas make, agrega un target
`progress-check`. Solo usa la biblioteca estándar de Python.

**Reglas que aplica:**
- Una historia pasa si **todos** sus comandos salen con 0.
- **Una prueba saltada no cuenta:** si la salida dice "N skipped", no pasa.
- Si una historia en `review` o `done` no pasa, el script sale con 1. Si está `in_progress`, solo
  se anota.
- `commit` lleva `+changes` cuando lo que pasó fue el árbol con cambios sin commit.

## Cuándo

- **Al crear una historia:** escribe primero su `verify` (la prueba que falla). Va de la mano de
  TDD.
- **Antes de decir "listo":** corre el script. Si no pasa, no está listo.
- **Al cerrar la sesión:** la skill `cierre-de-sesion` lo corre antes de escribir el handoff.
- **El agente `verificador-de-cierre`** usa este archivo como su lista de lo que debe comprobar.

Sigue con: **cierre-de-sesion**.
