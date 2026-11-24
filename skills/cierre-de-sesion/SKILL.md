---
name: cierre-de-sesion
description: "Cierra una sesión de trabajo dejando el contexto listo para la siguiente, con cualquier agente o modelo: corre progress, actualiza el plan, propone decisiones escritas, reescribe el HANDOFF.md y propone cómo evitar los errores de la sesión. Úsala cuando digan \"cierra la sesión\", \"haz el handoff\", \"deja todo listo para mañana\" o antes de que se acabe el contexto. / Close a work session leaving a HANDOFF.md any agent can pick up."
---

# Cierre de sesión

La memoria de una sesión se pierde; el repo no. Esta skill deja escrito lo necesario para que la
siguiente sesión, con cualquier herramienta (Claude Code, Codex, OpenCode) o persona, arranque
leyendo un archivo y no dependiendo de que alguien se acuerde.

## Entrada

**El objetivo de la siguiente sesión.** Si no lo dieron, pregúntalo antes de escribir: el handoff se
redacta para ese objetivo, no como resumen de todo lo que pasó.

## Pasos

1. **Verifica:** si el proyecto tiene `progress.json`, corre la skill **progress**. Si una historia
   en `review` o `done` no pasa, dilo y no la escondas. Actualiza `state` si cambió en la práctica;
   nunca escribas `passes` a mano. Sin `progress.json`, corre las pruebas y el lint del proyecto y
   anota el resultado real.
2. **Plan activo:** si el trabajo tiene un plan (por ejemplo, de la skill **ask**), anota con fecha
   qué se hizo, qué sorprendió y qué se decidió. Si se terminó, escribe su retrospectiva.
3. **Decisiones:** si se decidió algo que cambia cómo se construye (un proveedor, una regla, una
   arquitectura), propón un registro de decisión (ADR) en la carpeta que use el proyecto
   (`docs/decisiones/`, `docs/adr/`). El handoff solo apunta a él.
4. **Reescribe el `HANDOFF.md`** (no le agregues abajo) con la plantilla de
   `references/handoff.template.md`. Máximo 60 líneas.
5. **Revisa** el lint y las pruebas del proyecto.
6. **Retro:** si hubo una tarea que tardó mucho más de lo esperado, un error que costó tiempo o una
   corrección del usuario, propón cómo evitar que se repita. En este orden de preferencia: un check
   que falle solo (test, regla de lint, hook), una línea en `AGENTS.md` o una skill. Máximo 3, cada
   una con el error que la motiva. No las apliques: el usuario decide.
7. **Commit:** muestra el `git status`, el resumen y la retro, y pregunta. Solo se commitea si el
   usuario lo autoriza. Nunca push sin que lo pida.

## Reglas

- **Ninguna credencial en el handoff.** Ni llaves, ni tokens, ni contraseñas, ni el contenido de
  `.env`. Si una llave quedó expuesta, el handoff dice "hay que rotar la llave X", nunca su valor.
- **El historial no va en el handoff:** está en git. Lo que ya no sirve para el objetivo se borra.
- **Fechas absolutas** ("23-nov-2026", no "ayer").
- **Lo verificado y lo dicho, separados:** en "Hecho y verificado" solo va lo que tiene evidencia.

Antes de declarar terminado un trabajo grande, puedes pedirle una revisión al agente
**verificador-de-cierre**. La siguiente sesión empieza con **usando-el-kit**.
