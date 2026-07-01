# Trabajo multigalaxia

A veces una idea vive a través de más de una galaxia: un tema de investigación que abarca dos colecciones; una exposición con varias salas; una serie de números relacionados. Telaris está construido para que el agujero de gusano se quede en su galaxia de origen y la *combinación* sea un arreglo de visualización, no uno estructural. Este capítulo recorre las tres formas en que puedes componer galaxias, y cuándo cada una es la elección correcta.

## Los tres caminos de composición

Telaris ofrece tres formas de poner varias galaxias en una sola vista:

1. **Etiquetas de galaxia** (capítulo 4): dos galaxias que comparten una etiqueta forman una *unión de galaxias*. Las visitantes llegan a la unión vía `/tag/<tag-slug>` y ven los agujeros de gusano de cada galaxia etiquetada juntos, manteniendo cada agujero de gusano el estilo visual de su galaxia de origen.
2. **Agrupación por prefijo entre corchetes**: las galaxias cuyos nombres empiezan con el mismo prefijo `[entre corchetes]` se unen automáticamente en `/[bracket]`. Un respaldo natural a las etiquetas de galaxia; el prefijo es también la señal visual para las editoras que navegan el selector.
3. **Listas explícitas de galaxias**: pasar una lista separada por comas en la URL `?galaxies=slug1,slug2` produce una unión puntual. Útil para compartir una combinación curada sin cambiar las galaxias subyacentes.

La elección entre las tres depende de **qué tan duradera es la combinación**:

- *Duradera*: etiquetas de galaxia. La conexión es editorial y persiste entre sesiones.
- *Convencional*: prefijo entre corchetes. Útil cuando las galaxias son hermanas por convención de nombre, no solo por etiqueta.
- *Puntual*: lista explícita. Útil para un correo o un enlace que lleva a una lectora por una combinación específica una sola vez.

## Compartir agujeros de gusano sin duplicar

El primer impulso en muchos sistemas de archivo es copiar un agujero de gusano a una segunda galaxia cuando una idea pertenece a ambos lugares. Telaris está construido contra este impulso: copiar crea dos agujeros de gusano que mantener, dos lugares que actualizar cuando la fuente cambia, dos lugares de los que retirar contenido cuando la comunidad de origen retira su consentimiento.

El camino pretendido es: deja el agujero de gusano en su única galaxia de origen y deja que **las palabras clave compartidas** lo conecten con otros. Las visitantes que siguen *intertidal* en la galaxia A llegan a los agujeros de gusano etiquetados con *intertidal* en la galaxia B; el contenido del agujero de gusano vive en un solo lugar; la conexión se computa desde la palabra clave.

Cuando eso no basta, las opciones de la editora son, en orden de cuán invasiva es cada una:

1. **Añade una etiqueta de galaxia** a las dos galaxias que comparten el tema. Las visitantes que siguen la etiqueta ven la unión.
2. **Coloca un portal** (capítulo 9) de una galaxia a la otra. El portal es un agujero de gusano, pero uno pequeño y deliberado; no duplica contenido.
3. **Duplica el agujero de gusano** (menú de acciones del capítulo 5). Solo cuando el contenido del agujero de gusano genuinamente necesita vivir en dos lugares (por ejemplo, una galaxia se está sembrando con material de otra, con la decisión editorial de levantar en vez de enlazar). El duplicado es independiente desde entonces; hay que mantener ambas copias.

Los dos primeros son casi siempre preferibles al tercero.

## La experiencia de visitante de una unión

Una visitante que llega a una unión por etiqueta de galaxia (por ejemplo `/tag/coast`) ve:

- Una escena compuesta de los agujeros de gusano de cada galaxia que carga la etiqueta.
- **Temas de origen por agujero de gusano**: cada agujero de gusano se representa con el tema de su galaxia de origen, no con un tema único unificado. Esto es intencional; la visitante ve la unión como el *encuentro de galaxias*, no como un aplanamiento de ellas.
- Una franja o selector de galaxia arriba mostrando las galaxias constituyentes, con la opción de cambiar a una sola.
- Las mismas funciones de descubrimiento que cualquier galaxia (fichas de palabras clave, agujeros de gusano relacionados, etc.), ahora extraídas de la unión.

La barra de URL de la visitante se queda en `/tag/<tag>` mientras está en la unión; hacer clic en un agujero de gusano abre su ficha sin salir de la unión.

## Cuándo añadir una etiqueta de galaxia

Una etiqueta es editorial. Dos preguntas a hacerse:

- **¿Es la relación entre estas galaxias duradera?** Una etiqueta persiste; si la relación es de una sola vez, una URL explícita es más limpia.
- **¿Es la relación simétrica?** Una etiqueta es simétrica (cada galaxia que carga la etiqueta es por igual un miembro). Si la relación es direccional (la galaxia A es la introducción a la galaxia B), un portal es más honesto.

Ejemplos que justifican una etiqueta:
- Una serie de colecciones de investigación relacionadas.
- Una exposición con varias salas.
- Una agrupación regional (galaxias que describen contenido de un solo paisaje, geografía, o comunidad).

Ejemplos que no:
- "Galaxias viejas que quiero juntar para un enlace puntual" (usa `?galaxies=...`).
- "Galaxias que comparten unas pocas palabras clave" (usa las palabras clave directamente).

## Cuándo usar la agrupación por prefijo entre corchetes

Telaris reconoce los nombres de galaxia que empiezan con el mismo `[entre corchetes]` como una familia. Una galaxia llamada `[demo] Coastal plants` y otra llamada `[demo] Tide pools` comparten el prefijo `[demo]`; las visitantes que siguen `/[demo]` ven ambas en unión.

El prefijo entre corchetes es más útil cuando:

- Tienes varias editoras trabajando en galaxias relacionadas, y el prefijo les señala que las galaxias son hermanas.
- Las galaxias forman una familia que también quieres ver-como-familia en el selector de editora (el selector agrupa galaxias por prefijo entre corchetes).
- Quieres comportamiento de unión sin tener que escribir explícitamente una etiqueta en cada galaxia.

El prefijo entre corchetes y una etiqueta de galaxia explícita no son mutuamente excluyentes; ambos aplican si ambos están presentes.

## Cuándo usar una lista explícita de galaxias

A veces quieres una unión puntual para un momento específico: un correo a una curadora mostrando una combinación particular; un enlace docente que lleva a una clase por tres galaxias lado a lado; una exposición temporal que no justifica una etiqueta duradera.

La forma de URL es `?galaxies=slug1,slug2,slug3` añadida a la dirección de tu instancia. El resultado es idéntico a una unión por etiqueta, pero la combinación existe solo como la URL misma.

Esta es la herramienta correcta para curaduría puntual. También sirve como una rápida prueba de cordura: si una combinación particular de galaxias se lee bien como URL explícita, tienes una candidata para una etiqueta permanente.

## Multigalaxia entre instancias

¿Y las galaxias que viven en **otras** instancias de Telaris? Eso pertenece al dominio de la operadora: el contenido entre instancias llega a tu superficie de editora vía federación o vía importes de bridges que la operadora configura. Desde el asiento de la editora, las galaxias federadas y bridged se comportan como galaxias locales (una galaxia es una galaxia es una galaxia), pero la editora no puede hacer autoría de uniones entre instancias; solo la operadora puede preparar la federación que las hace posibles.

## Cosas que vale la pena saber

- **Un agujero de gusano pertenece a exactamente una galaxia a la vez.** Multigalaxia es un concepto de *visualización*, no estructural. La galaxia de origen del agujero de gusano es su única fuente de verdad.
- **En una vista de unión, la galaxia de origen se señala en varios lugares.** Cuando hay más de una galaxia en la vista, el nombre de la galaxia del agujero de gusano aparece como prefijo antes del nombre del agujero de gusano en el modal de medios 3D, en la etiqueta emergente al pasar el cursor, y en el mapa 2D, para que dos agujeros de gusano con el mismo nombre de galaxias distintas sigan siendo distinguibles a un vistazo. El tema del icono del agujero de gusano es una pista adicional a un vistazo, y la ficha nombra la galaxia de origen en su pie.
- **Una galaxia en una unión no pierde su individualidad.** Las visitantes pueden hacer clic para entrar a una sola galaxia desde dentro de la vista de unión; la unión es una capa de visualización, no una fusión.
- **Las palabras clave son globales por texto** (capítulo 7). Las palabras clave de un agujero de gusano en la galaxia A son las mismas palabras clave que las mismas palabras en un agujero de gusano de la galaxia B. Una vista de unión consolida la franja de píldoras de palabras clave de todas las galaxias constituyentes; hacer clic en una palabra clave en la unión filtra la unión.
- **El lienzo de palabras clave sigue siendo por galaxia** (capítulo 8). No hay "lienzo de unión"; cada galaxia mantiene su propio arreglo de palabras clave. Las palabras clave mismas son compartidas (renombrar o fusionar se aplica en todas partes), pero la disposición de las píldoras y las relaciones dibujadas están acotadas a cada galaxia.
- **Tu operadora puede aflojar el emparejamiento de palabras clave.** Por defecto dos agujeros de gusano se conectan solo cuando cargan la *misma* palabra clave. Quien opera puede activar el emparejamiento aproximado para la instancia o un cúmulo, de modo que grafías cercanas (un plural, un pequeño error tipográfico) también tracen una línea de relación entre galaxias. Si ves conexiones entre palabras que se parecen pero no son idénticas, este ajuste es la razón; se controla del lado de administración, no por agujero de gusano.
