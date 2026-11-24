# Caso: pivote (el proyecto existe y cambia el rumbo)

Ejemplos: otro mercado o alcance, otra arquitectura, migrar de stack, sacar algo a otro servicio, o
meter algo grande que cambia lo que se estaba construyendo. Es el caso más difícil. Hay preguntas
de fondo, como en un proyecto nuevo, pero el proyecto ya carga:
- trabajo invertido;
- usuarios o datos;
- ramas y PRs a medias;
- decisiones escritas (ADRs) que hay que reemplazar a propósito y no por accidente.

## Qué leer antes de preguntar

- **El inventario de lo que existe:** qué funciona (tests que pasan, `progress.json`), qué se usa
  de verdad, qué está a medias (ramas, PRs abiertos, el HANDOFF) y qué ADRs están en vigor.
- **El disparador:** qué cambió para que haya que cambiar el rumbo. Una junta, un cliente, un límite
  técnico, un costo.

## Qué preguntar de más

- **El disparador y su porqué.** Si no está claro, todo lo demás se planea sobre arena.
- **Conservar, cambiar o tirar:** pieza por pieza de lo que existe. Es el centro de la entrevista.
- **Qué ADRs quedan reemplazados** y qué decisión los sustituye.
- **Datos y usuarios actuales:** se migran, conviven o se cortan.
- **El trabajo a medias:** ramas y PRs se terminan, se congelan o se cierran.
- **La transición:**
  - todo de golpe;
  - por partes, con lo nuevo creciendo al lado de lo viejo hasta reemplazarlo;
  - un piloto primero.
- **El punto de no retorno:** a partir de qué paso ya no se puede volver atrás, y qué se tiene que
  comprobar antes de llegar ahí.
- **Éxito del pivote:** cómo se va a saber que valió la pena.
- **Comunicación:** a quién hay que avisar (equipo, jefe, clientes) y cuándo.

## Ejes que dan enfoques distintos

- Reescribir, migrar por partes, o adaptar lo actual sin rehacerlo.
- El mismo repo o uno nuevo.
- Parar lo actual mientras se hace, o que convivan.
- Hacer el pivote completo, o solo la parte que el disparador exige.

## Qué entregar

1. **El disparador,** en un párrafo.
2. **Mapa de conservar, cambiar y tirar,** en una tabla por pieza.
3. **ADRs que se reemplazan** y el ADR nuevo propuesto que los sustituye.
4. **Transición por fases,** cada una con su verificación y su forma de volver atrás. Marca el punto
   de no retorno.
5. **Qué pasa con ramas, PRs y datos.**
6. **Comunicación:** a quién, qué y cuándo.
7. **Riesgos y plan B.**

**Diagramas:** un `flowchart` de antes y después, y un `gantt` de la transición.
