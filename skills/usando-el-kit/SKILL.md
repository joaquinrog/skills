---
name: usando-el-kit
description: "Punto de entrada del kit: explica el ciclo de trabajo (entrevistar → planear → revisar el plan → construir con pruebas → verificar → cerrar) y qué skill o agente toca en cada paso. Úsala al empezar una sesión de trabajo, al retomar un proyecto o cuando no sepas qué skill sigue. / Entry point: the work cycle and which skill or agent comes next."
---

# Usando el kit

Este kit no te enseña a programar: te da un **ciclo de trabajo** con IA que funciona igual con
Claude, ChatGPT/Codex, Gemini o un modelo abierto. Lo que vale vive en archivos tuyos (el plan, el
`progress.json`, el `HANDOFF.md`, el `AGENTS.md`), no en la memoria de una herramienta.

## El ciclo

| Paso | Qué haces | Con qué |
|---|---|---|
| 0. Retomar | Lee el `HANDOFF.md` y el `AGENTS.md` del proyecto antes de tocar nada | (archivos) |
| 1. Entender | Entrevista hasta que el pedido sea un buen plan | skill **ask** |
| 2. Revisar el plan | Que un modelo más fuerte lo critique antes de escribir código | agente **revisor-de-plan** |
| 3. Construir | Cada historia con la prueba que la demuestra, escrita primero | skill **progress** |
| 4. Verificar | Que otro compruebe con evidencia, no con lo que dice la sesión | agente **verificador-de-cierre** |
| 5. Cerrar | Handoff para la siguiente sesión y retro de errores | skill **cierre-de-sesion** |

## Cuánto ciclo usar

No todo necesita el ciclo completo:
- **Un ajuste chico** (un typo, un bug de una línea): directo, con su prueba.
- **Un feature:** ask → progress → cierre.
- **Algo grande, de varias sesiones o sin supervisión:** el ciclo completo, con los dos agentes.

## Tres reglas que el ciclo protege

1. **Escribir antes de pedir:** un pedido vago se arregla con preguntas, no con más intentos.
2. **Evidencia antes que palabras:** "listo" significa que el `verify` pasa.
3. **El contexto vive en el repo:** cualquier persona, agente o modelo debe poder retomar leyendo
   archivos.
