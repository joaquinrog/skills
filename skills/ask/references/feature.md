# Caso: feature en un proyecto que ya existe

El proyecto ya tomó muchas decisiones. Los riesgos son contradecir una sin darse cuenta, duplicar
algo que ya existe o romper lo que funciona. Por eso aquí se lee mucho antes de preguntar, y las
preguntas son más estrechas: casi todas sobre cómo encaja el cambio, no sobre para qué existe el
proyecto.

## Qué leer antes de preguntar

- **El `AGENTS.md` del paquete,** además del de la raíz, si el repo los tiene por paquete.
- **El código donde viviría el cambio,** con sus tests.
- **Si ya existe algo parecido:** búscalo con `grep`. Muchas veces la mitad del feature ya está
  hecha.
- **Las convenciones:** nombres, estilo de tests, numeración de migraciones, formato de commits.

Llega a la entrevista con lo que encontraste, para que las preguntas se apoyen en eso.

## Qué preguntar de más

- **Qué problema resuelve el feature y para quién.** Solo si el pedido no lo dice.
- **Dónde vive:** extender un módulo que ya existe, uno nuevo, o un paquete aparte.
- **ADRs:** cuál toca, si alguno lo contradice, o si hace falta uno nuevo.
- **Datos:** tablas, migraciones y qué pasa con los datos que ya hay.
- **Compatibilidad:** si se vale romper algo, o si tiene que convivir con lo actual.
- **Cómo se prueba:** unitario, integración, de punta a punta, un eval, o una demo.
- **Cómo se libera:** detrás de un flag, solo en sandbox, o directo.
- **Qué no entra en este feature.**
- **Quién lo revisa,** en una sesión o en varias, de día o de noche.

## Ejes que dan enfoques distintos

- Extender lo que hay, hacer un módulo nuevo, o ponerlo detrás de un flag.
- Completo de una vez, o la rebanada mínima que ya sirve de punta a punta.
- Código determinista o un modelo.
- Una librería, o código propio.

## Qué entregar

El plan con la convención del proyecto (`PLANS.md`, `docs/planes/`). Si no hay, usa esta estructura:

1. **Objetivo y criterio de éxito.**
2. **Contexto** con rutas (`archivo:línea`) de lo que leíste.
3. **Decisiones de la entrevista.**
4. **Archivos que toca.**
5. **Pasos en orden,** con el test que falla primero y el comando que verifica cada uno.
6. **Migraciones** y qué pasa con los datos que ya hay.
7. **Riesgos y cómo se revierte.**
8. **ADR nuevo propuesto,** si aplica.
9. **Qué se actualiza al cerrar:** `HANDOFF.md`, `progress.json`, docs.

**Diagramas:** un `sequenceDiagram` del cambio, o un `flowchart` de antes y después. Un
`stateDiagram-v2` si el feature cambia estados.
