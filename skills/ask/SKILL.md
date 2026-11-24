---
name: ask
description: "Úsala siempre que se vaya a planear algo: en plan mode antes de escribir el plan, o cuando digan \"planea\", \"armemos un plan\", \"pregúntame antes\" o \"/ask\". Sirve para proyectos nuevos, features y pivotes (y distingue cuál es), migraciones, arquitecturas, experimentos y demos. Entrevista antes de escribir, para que un pedido vago termine en un buen plan: solo preguntas necesarias, sin tope, cada una con opción recomendada y alternativas que son enfoques de verdad distintos. Entrega el plan en .md con diagramas Mermaid (.mmd). En bugs y ajustes chicos no hay entrevista. / Interview before planning: only necessary questions, each with a recommended option, until a vague request becomes a good plan (.md + Mermaid)."
---

# Ask: preguntar todo lo necesario antes de planear

"Un prompt malo hace un plan malo" solo es cierto si nadie pregunta. Esta skill existe para romper
eso: si el pedido es vago, está incompleto o parte de un supuesto equivocado, las preguntas lo
convierten en un buen plan. Un pedido flojo no es razón para preguntar menos, sino más.

Cada pregunta trae una opción recomendada. Así, aunque el usuario solo conteste "la recomendada"
una y otra vez, el plan sale bien pensado.

## 0. Qué tipo de plan es

No se planea igual algo que empieza de cero que algo que entra en un proyecto vivo. Antes de
preguntar nada, decide cuál de estos casos es y lee **solo** su archivo:

| Caso | Señales | Lee |
|---|---|---|
| **Proyecto nuevo** | Carpeta vacía o casi; sin `AGENTS.md`/`CLAUDE.md`, sin tests ni ADRs; "empecemos", "quiero hacer un…" | `references/proyecto-nuevo.md` |
| **Feature** | Ya hay código, tests, ADRs o un HANDOFF, y el pedido agrega o cambia una parte | `references/feature.md` |
| **Pivote** | El proyecto existe y el pedido cambia el rumbo: otro mercado o alcance, otra arquitectura, migrar de stack, rehacer algo grande | `references/pivote.md` |
| **Cambio chico** | Un bug, un ajuste, un renombre: algo que cabe en una sesión sin decisiones de fondo | Nada. Sin entrevista: plan corto con sus supuestos |

**Di el caso en una línea, con la evidencia:** "Vi `AGENTS.md`, 4 ADRs y 3,400 tests: lo planeo
como feature". Pregúntalo solo si dudas entre dos (casi siempre feature o pivote); entonces es la
primera pregunta, con tu recomendación. Equivocarse de caso cuesta toda la entrevista; confirmarlo
cuesta un clic.

Lo de abajo aplica a proyecto nuevo, feature y pivote. En un **cambio chico** no hay rondas ni
cierre (§3 y §4): pregunta solo lo indispensable, y el plan es corto, con sus supuestos y un
diagrama solo si ayuda. El archivo del caso dice qué preguntar de más, qué ejes dan enfoques
distintos y qué entregar.

## 1. Leer antes de preguntar

Antes de la primera pregunta, junta lo que ya está escrito: el `AGENTS.md`/`CLAUDE.md`, el
`HANDOFF.md`, los ADRs y los planes activos del proyecto, la memoria, y el código que toca el plan.
Una pregunta que el repo ya contesta le cuesta tiempo al usuario. Lo que encuentres conviértelo en
contexto de la pregunta ("Vi que X depende de una decisión pendiente") o en una opción recomendada, no en
una pregunta abierta.

## 2. Qué preguntar: solo lo necesario, pero todo lo necesario

Una pregunta es **necesaria** si cumple las dos cosas:
- **Cambia el plan:** su respuesta cambia qué se hace, cómo, en qué orden o cómo se verifica.
- **No te toca a ti:** no la puedes contestar leyendo, y no tiene un default obvio y barato de
  cambiar. Si lo tiene, decídelo tú y anótalo como supuesto.

No hay número fijo de preguntas. Sigue hasta que cada decisión necesaria esté tomada, sean 5 o 40.

Dimensiones que suelen esconder decisiones. Recórrelas y quédate con las que apliquen:

- **Objetivo:** qué se quiere lograr, por qué ahora, qué cambia si sale bien.
- **Éxito:** un criterio verificable, como un test, un número o una demo que funcione.
- **Alcance:** qué entra y, sobre todo, qué **no** entra.
- **Para quién:** quién lo usa, quién lo revisa o aprueba, a quién se le presenta.
- **Restricciones:** fecha, tope de gasto, modelos y herramientas, reglas del proyecto, cuentas.
- **Punto de partida:** qué existe ya, qué está bloqueado y por quién.
- **Riesgos:** qué puede fallar, qué tan reversible es, cuál es el plan B.
- **Datos:** de dónde salen, si son reales o sintéticos, qué es privado.
- **Entregables:** qué archivos salen, dónde viven y quién los lee.
- **Ejecución:** cuántas sesiones, qué va en paralelo, qué hace una persona y qué un agente.
- **Verificación:** con qué se comprueba cada paso y cómo se sabe que terminó.
- **Comunicación:** a quién hay que avisar, de qué y cuándo.

**Si el pedido parte de algo equivocado**, dilo en la pregunta y ofrece otra forma de plantearlo como opción. Por
ejemplo: pide algo que el código ya hace, mezcla dos problemas o apunta al síntoma y no a la causa.

Pregunta primero lo que cambia todo (objetivo, enfoque, alcance) y después los detalles. No tiene
caso preguntar un nombre de archivo si todavía no se sabe qué enfoque va.

## 3. Cómo preguntar: rondas sobre un árbol de decisiones

Arma un **árbol de decisiones**: cada decisión abre las que dependen de ella. Las decisiones que ya
puedes preguntar sin adivinar una respuesta que todavía no tienes son **la ronda**.

- **Cada ronda pregunta todas las de ese momento**, sin tope. Si son muchas, son muchas.
- **Después de cada ronda, recalcula:** lo decidido destapa preguntas nuevas, y algunas ya no hacen
  falta.
- **Los hechos los buscas tú, no el usuario.** Si una pregunta necesita un dato del repo, de una
  herramienta o de la web, búscalo antes (o con un subagente) y llega con la respuesta.
- **Termina cuando no queda nada:** cada rama del árbol está decidida o anotada como supuesto. No
  escribas el plan antes.

Usa `AskUserQuestion`. Acepta hasta 4 preguntas por llamada, pero eso no limita la ronda: dentro de
una ronda, encadena llamadas sin texto entre ellas hasta cubrirla. Entre rondas, una línea con lo
que quedó decidido.

Si la ronda es muy grande (más de unas 12 preguntas), o el usuario prefiere contestar todo de una,
ponla en el chat. Numera las preguntas, dale a cada una sus opciones y una línea `➡️ Recomendado:
…`, y redáctalas de modo que "sí a todo" acepte las recomendadas y "3: b" cambie solo la 3.

**Opciones que son enfoques distintos.** Cada opción tiene que ser otra forma de resolverlo: otra
estrategia, otro alcance, otro orden u otra herramienta. Si dos opciones se distinguen solo por un
detalle, júntalas y busca una alternativa diferente de verdad. Ejes que suelen dar enfoques
distintos:
- construir, reusar algo que ya existe o no hacerlo;
- completo de una vez o un piloto chico primero;
- código determinista o un modelo;
- de día con el usuario o de noche sin supervisión;
- local o en la nube.

Dos opciones buenas y distintas valen más que cuatro parecidas.

Esto vale para las preguntas de enfoque. Para un dato que solo sabe el usuario (una fecha, un tope
de gasto, quién aprueba), las opciones son los valores más probables según lo que leíste, y la
recomendada es tu mejor inferencia.

**Siempre una recomendada:** va primero, con "(Recomendado)" al final de la etiqueta, y su
descripción dice por qué la recomiendas y qué implica. Las demás dicen qué ganas y qué pierdes con
cada una.

**Cada pregunta se entiende sola.** El usuario puede ver solo el diálogo, no tu texto anterior. La
pregunta dice de qué habla y, si depende de algo que encontraste, lo menciona en una frase.

**`preview`** (solo en selección única): úsalo para comparar algo visible, como dos estructuras de carpetas, dos flujos en
texto o dos snippets. **`multiSelect`:** úsalo cuando las opciones no se excluyen.

**Después de cada llamada, adapta.** La siguiente sale de lo que contestó. Si eligió "Otro" o dejó
una nota, esa es la pista más valiosa: síguela.

**Si nadie puede contestar** (`claude -p`, una sesión nocturna o un subagente: no tienes
`AskUserQuestion` ni hay alguien del otro lado), no preguntes ni cierres el turno con preguntas,
porque nadie las va a leer. Toma la recomendada en cada decisión, anótala en Supuestos con su
alternativa y sigue. Lo irreversible, lo que gasta dinero o lo que toca producción va a Preguntas
abiertas y no se ejecuta. Si falta `AskUserQuestion` pero el usuario sí está, pregunta en el chat
con el mismo formato.

**Pregunta débil:** "¿Qué quieres que haga el plan?", o cuatro opciones que solo cambian un número.
**Pregunta fuerte:** "¿Cómo probamos la integración antes de la demo? (a) Contra el servicio real
con una cuenta de prueba nuestra (Recomendado: es lo único que prueba el camino de verdad); (b) con
un simulador, que no gasta pero no prueba la conexión; (c) no probarla y enseñar el diseño."

## 4. Cerrar la entrevista

Antes de escribir, muestra en el chat tres listas cortas:
- **Decidido**, cada punto con quién lo decidió.
- **Supuestos** que tomaste tú, marcados como supuestos.
- **Preguntas abiertas**, con a quién le tocan.

Cierra con una última pregunta, "¿Hay algo que no te pregunté y que debería saber?", con opciones
"Nada, escribe el plan (Recomendado)" y "Falta algo". Muchas veces ahí sale lo más importante.

## 5. Escribir el plan (.md)

- **En plan mode** solo se puede escribir el archivo de plan del sistema. Escribe ahí el plan, con
  los diagramas como bloques ` ```mermaid `. Su **paso 0** es guardar el plan como `.md` en su ruta
  (la de abajo) y sacar cada bloque a su `.mmd`: al aprobarse el plan, es lo primero que se hace.
- **Fuera de plan mode:** si el proyecto tiene convención de planes (`PLANS.md`, `docs/planes/`),
  úsala con su plantilla. Si no, usa `planes/AAAA-MM-DD-<slug>.md`. Si el plan es interno o
  personal, pregunta dónde va: no lo metas a un repo compartido sin preguntar.
- **Estructura:** la del archivo del caso, y siempre con Decisiones, Supuestos, Fuera de alcance y
  Preguntas abiertas aunque el archivo no las nombre: ahí queda lo que salió de la entrevista. Si
  el proyecto trae su propia plantilla, gana la del proyecto. Sin ninguna de las dos, usa esta:
  1. Objetivo y criterio de éxito.
  2. Contexto, con las fuentes que leíste.
  3. Decisiones de la entrevista.
  4. Supuestos.
  5. Fuera de alcance.
  6. Pasos, cada uno con su verificación y quién lo hace.
  7. Riesgos y plan B.
  8. Preguntas abiertas.
  9. Diagramas.
- **Escritura:** frases cortas, sin relleno, y sin cifras ni capacidades que no vengan de una fuente
  o de la entrevista.

## 6. Diagramas (.mmd)

Haz al menos un diagrama cuando el plan tenga un flujo, una arquitectura, un calendario o estados:

| Qué muestra | Tipo de Mermaid |
|---|---|
| Flujo o arquitectura | `flowchart LR` / `flowchart TD` |
| Quién le habla a quién (agentes, servicios) | `sequenceDiagram` |
| Calendario o fases | `gantt` |
| Estados de algo | `stateDiagram-v2` |

- **Archivos:** un diagrama por archivo, `<slug>-<qué>.mmd`, junto al plan. Pon el mismo bloque
  ` ```mermaid ` dentro del .md para que se vea en GitHub y en el editor.
- **Que compile:** si existe `mmdc` (mermaid-cli), renderiza a `.svg` para comprobarlo. Si no
  existe, revísalo a mano:
  - Pon entre comillas las etiquetas con acentos, paréntesis o dos puntos: `A["Motor (sin LLM)"]`.
  - Usa ids sin espacios.
  - En `gantt`, usa `dateFormat YYYY-MM-DD`.

## 7. Entregar

Da las rutas de los archivos y un resumen de tres líneas: qué se va a hacer, cómo se sabrá que
quedó y qué sigue abierto. No empieces a ejecutar el plan hasta que el usuario lo pida; en plan
mode, aprobar el plan es esa orden.

Sigue con: el agente **revisor-de-plan** si el trabajo es grande o va a correr sin supervisión, y
la skill **progress** para escribir el `verify` de cada historia antes de construir.
