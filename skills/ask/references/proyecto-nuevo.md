# Caso: proyecto nuevo (desde cero)

No hay código que leer, así que la entrevista es la fuente principal. Y ahora todo es barato de
decidir: el stack, la estructura, las convenciones y qué se construye primero salen casi gratis
hoy y carísimos en un mes. Por eso aquí se pregunta más que en cualquier otro caso, y con opciones más amplias:
enfoques completos, no detalles.

## Qué leer de todos modos

Lo que el usuario haya pasado (notas, un brief, un documento, una conversación anterior), su
memoria, y proyectos suyos parecidos que puedan servir de modelo para las convenciones.

## Qué preguntar de más

- **El problema:** qué duele hoy y a quién. Si el pedido trae la solución ("una app que…"),
  pregunta primero por el problema: a veces la solución pedida no es la mejor.
- **Para quién y por qué ahora.**
- **Qué no se va a construir:** es la pregunta que más tiempo ahorra.
- **Éxito:** cómo se va a saber en 2–4 semanas que va bien. Un número, un usuario que lo usa, una
  demo.
- **Primer hito:** la versión mínima que funciona de punta a punta, aunque sea fea. Arma eso primero
  y no una capa completa, porque así salen temprano los problemas de integración.
- **Stack:** lo que el usuario ya domina o algo nuevo, y por qué. Dónde corre (local o nube) y
  cuánto cuesta. Qué cuentas y llaves hacen falta, y quién las tiene.
- **Datos y legal:** de dónde salen, si son reales o sintéticos, y qué revisión hace falta antes de
  tocar datos o personas reales.
- **Quién trabaja:** una persona, agentes, sesiones en paralelo o de noche.
- **Convenciones desde el día uno:** idioma del código y de los textos, commits, tests, estructura
  de carpetas.
- **Contexto entre sesiones:** dónde vive lo que pasa de una sesión a otra (`AGENTS.md` o
  `CLAUDE.md`, `HANDOFF.md`, ADRs).
- **Riesgo de producto o técnico:** cuál es el que más asusta. Si es "nadie lo va a usar", el primer
  hito cambia: hay que validar eso antes de construir mucho.

## Ejes que dan enfoques distintos

- Construir, comprar o integrar algo que ya existe.
- Un prototipo para tirar, o la base sobre la que se va a crecer.
- Todo en un servicio, o separado desde el principio.
- Un agente, varios, o código sin modelo.
- Hacerlo a mano primero y automatizar después, o automatizar desde el inicio.

## Qué entregar

1. **Visión** en un párrafo: el problema, para quién y el éxito.
2. **Fuera de alcance.**
3. **Primer hito,** con pasos, cada uno con su verificación.
4. **Hitos siguientes** en un `gantt`.
5. **Decisiones iniciales** como ADRs propuestos: título y decisión en una línea cada uno.
6. **Estructura de carpetas** propuesta.
7. **Borrador del `AGENTS.md`/`CLAUDE.md` base,** corto (≤ 100 líneas): reglas, comandos y mapa.
8. **Riesgos y cómo se van a probar pronto.**

**Diagramas:** un `flowchart` de la arquitectura y un `gantt` de los hitos.
