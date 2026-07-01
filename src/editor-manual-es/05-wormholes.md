# Agujeros de gusano

Un agujero de gusano es la unidad más pequeña de contenido en Telaris. Todo lo que una editora publica es, al final, un agujero de gusano: un pasaje de texto, una fotografía, una grabación de audio, un fragmento de película, un PDF, una cita, un único pensamiento. Este capítulo recorre la creación, la edición, los campos que le dan forma, y las elecciones que el formulario te invita a hacer.

## Crear un nuevo agujero de gusano

Desde el inicio del editor, selecciona la galaxia en la que estás trabajando, luego elige **Nuevo agujero de gusano**. Se abre un cuadro modal:

![Cuadro modal de nuevo agujero de gusano: formulario vacío con Nombre, Galaxia, Tipo, Palabras clave, Descripción, URL, y pestañas de medios visibles](assets/images/editor-manual-es/05-new-wormhole-modal.png)

El formulario tiene cuatro regiones amplias, en el orden en que las encuentras al bajar por el modal:

1. **Identidad** arriba: Nombre, Galaxia, Tipo de agujero de gusano, Palabras clave.
2. **Interruptores de comportamiento**: Acentuar agujero de gusano, Mostrar palabras clave.
3. **Cuerpo**: Descripción, URL.
4. **Medios**: imagen, video, audio, PDF, y la sustitución del icono.

Guarda con el botón al fondo del modal; el nuevo agujero de gusano aparece en la lista inmediatamente. Cancela o haz clic fuera del modal para descartar.

## Campos de identidad

### Nombre

Obligatorio. La etiqueta que la visitante lee en la escena 3D, en cualquier lista, y en la URL cuando la comparte. Elige un nombre que se lea limpio por sí solo; se citará fuera de contexto más a menudo de lo que crees.

Los nombres dentro de una galaxia deben ser únicos; el modal te avisará si un nombre está tomado antes de guardar. Entre galaxias, dos agujeros de gusano pueden compartir un nombre sin conflicto.

### Galaxia

Obligatorio, pero suele venir pre-llenado. El desplegable muestra todas las galaxias que puedes editar. Si empezaste desde una galaxia específica en el inicio del editor, esa galaxia queda seleccionada por defecto; si empezaste desde *Todas mis galaxias*, eliges aquí.

Cambiar la galaxia en este desplegable **mueve** el agujero de gusano a esa galaxia. Las palabras clave del agujero de gusano vienen con él, pero sus *posiciones* en el lienzo de la galaxia de destino pueden necesitar un retoque.

### Tipo de agujero de gusano

Un desplegable con dos valores:

- **Objeto** es la opción por defecto y la respuesta correcta para casi todos los agujeros de gusano. Un Objeto contiene contenido (descripción, medios).
- **Portal** convierte el agujero de gusano en una puerta a otra galaxia. Seleccionar Portal revela un segundo desplegable para la galaxia de destino. El capítulo 9 cubre los portales.

### Palabras clave

Una entrada de píldoras. Escribe una palabra clave y presiona **Enter** (o coma) para añadirla; haz clic en la **×** de una píldora para eliminarla. Las sugerencias aparecen a medida que escribes, extraídas de:

- Palabras clave ya usadas en **esta** galaxia.
- Palabras clave usadas en galaxias que comparten el prefijo `[entre corchetes]` de tu galaxia.

Elige palabras clave pensando en el camino de la visitante: cada palabra clave que adjuntas es una puerta desde este agujero de gusano a todos los demás agujeros de gusano que comparten la misma palabra. Cuantas menos palabras clave asignes, más deliberada se siente cada conexión; cuantas más asignes, más densa la red. El capítulo 7 cubre la estrategia de palabras clave.

## Interruptores de comportamiento

### Acentuar agujero de gusano

Apagado por defecto. Cuando está encendido, este agujero de gusano se representa más grande y prominente en la escena 3D. Úsalo con moderación: si acentúas todo, nada queda acentuado. La marca de acentuación también es la señal que la característica de recorrido automático puede usar para elegir sus paradas (capítulo 11).

### Mostrar palabras clave

Apagado por defecto. Cuando está encendido, la visitante ve las palabras clave de este agujero de gusano impresas junto a él en la escena 3D, antes de abrirlo. Útil para agujeros de gusano cuyo papel en la galaxia se entiende mejor a través de sus etiquetas (un documento de referencia; una pista de navegación; una definición).

## Cuerpo

### Descripción

El texto que la visitante lee al abrir el agujero de gusano. No hay límite de longitud; agujeros de gusano de una línea y ensayos largos son ambos posibles. El campo acepta formato markdown básico: párrafos (una línea en blanco), `**bold**`, `*italics*`, `[link](https://...)`, listas, y `code` en línea. Los encabezados y los medios incrustados no se representan dentro de la descripción; si necesitas un quiebre tipo encabezado, deja una línea en blanco y empieza un nuevo párrafo.

Escribe las descripciones en tu propia voz. Telaris no edita lo que escribes; la plataforma enmarca el contenido, el contenido es tuyo.

### URL

Opcional. Si lo rellenas, el agujero de gusano se vuelve cliqueable como enlace de salida: cuando la visitante abre la ficha del agujero de gusano, aparece un botón *Abrir enlace* que la lleva a la URL en una pestaña nueva.

Úsalo para referencias canónicas (un artículo, una página de libro, un archivo sonoro, el sitio web de una comunidad). Déjalo vacío cuando el agujero de gusano sea autosuficiente.

## Medios

Un agujero de gusano puede cargar un **visual primario** más una pista de **audio** opcional y una **sustitución de icono** opcional. El visual primario es lo que las visitantes ven en la parte superior de la ficha cuando abren el agujero de gusano; el audio suena de fondo; la sustitución de icono cambia cómo aparece el agujero de gusano en la escena 3D.

El modal organiza el visual primario como un conjunto de pestañas: **Imagen**, **Video (MP4)**, **PDF**. Elegir una y guardar borra las otras; solo un visual primario a la vez. El capítulo 6 cubre cada pestaña en detalle.

El campo de audio es independiente del visual primario; un agujero de gusano con una imagen y un archivo de audio reproduce el audio mientras la imagen está visible. El código de embed (por ejemplo un iframe de Spotify o Vimeo) se admite como alternativa a la imagen / video / PDF cuando el visual está alojado externamente.

## Editar un agujero de gusano existente

Para editar un agujero de gusano, haz clic en cualquier parte de su fila en la lista de agujeros de gusano, o abre el menú de acciones de la fila y elige **Editar**:

![Modal de editar agujero de gusano para Beach Strawberry: nombre completado, píldoras de palabras clave, descripción, pestañas de medios](assets/images/editor-manual-es/06-edit-wormhole-modal.png)

El modal es el mismo que el formulario de creación, con los valores existentes pre-cargados. El id del agujero de gusano aparece en la esquina superior derecha (aquí, `#279`); las editoras rara vez necesitan referirse a los ids, pero el número es útil al reportar un problema a tu operadora.

El botón Actualizar agujero de gusano persiste el cambio inmediatamente. Las visitantes que estén viendo la galaxia ven tu actualización en su próxima recarga de página.

## Duplicar, ver, eliminar

El menú de acciones en cada fila de agujero de gusano ofrece estas operaciones:

- **Ver** abre una vista previa de solo lectura de la ficha del agujero de gusano tal como la vería la visitante. Úsalo cuando quieras revisar un cambio antes de dar el trabajo por hecho.
- **Editar** abre el modal de arriba.
- **Duplicar** crea una copia del agujero de gusano, con el mismo contenido, en la misma galaxia, llamada "Nombre original (Copia)". El nuevo agujero de gusano recibe una posición fresca en la escena 3D; todo lo demás se traslada. Útil cuando quieres un casi duplicado como punto de partida.
- **Crear plantilla** guarda la forma del agujero de gusano como una plantilla reutilizable con la que podrás estampar nuevos agujeros de gusano más adelante. La sección Plantillas de abajo lo cubre en detalle.
- **Eliminar** elimina el agujero de gusano. Aparece primero un cuadro modal de confirmación; las eliminaciones son permanentes (tu operadora a veces puede restaurar desde una instantánea, pero la respuesta debería ser: no elimines a menos que lo quieras decir).

Duplicar y Crear plantilla responden a dos necesidades distintas: Duplicar te da un agujero de gusano más ahora mismo, en esta galaxia; Crear plantilla te da un molde que puedes reutilizar entre galaxias y entre sesiones.

## Ordenar la lista de agujeros de gusano

Haz clic en el encabezado de cualquier columna de la lista de agujeros de gusano para ordenar por esa columna; haz clic de nuevo para invertir el orden. Ordena por nombre para encontrar un agujero de gusano alfabéticamente, o por la columna de última modificación para traer tu trabajo más reciente arriba. El orden es solo una comodidad de vista; no cambia nada de los agujeros de gusano en sí ni de cómo se les aparecen a las visitantes.

## Plantillas

Una plantilla es un punto de partida reutilizable para nuevos agujeros de gusano. Si te encuentras creando un agujero de gusano tras otro con la misma forma (el mismo tipo, el mismo puñado de palabras clave, el mismo tono de descripción, el mismo tipo de medio incrustado), puedes capturar esa forma una vez y estampar nuevos agujeros de gusano a partir de ella, en lugar de rellenar los mismos campos a mano cada vez.

Las plantillas son **privadas para ti**. Las plantillas que creas son solo tuyas; otra persona editora en la misma instancia no ve las tuyas, y tú no ves las suyas. (Quien administra puede ver todas las plantillas, igual que puede ver todas las galaxias.)

### Crear una plantilla a partir de un agujero de gusano

No construyes una plantilla desde un formulario en blanco. La construyes a partir de un agujero de gusano que ya te gusta. Abre el menú de acciones de la fila del agujero de gusano y elige **Crear plantilla**:

![Un menú de acciones de fila de agujero de gusano abierto, mostrando Ver, Editar, Duplicar, Crear plantilla y Eliminar](assets/images/editor-manual-es/15-create-template-action.png)

Telaris captura una copia de la estructura y el contenido de ese agujero de gusano: su tipo, palabras clave, descripción, URL, interruptores de comportamiento y ajustes de medios. Si el agujero de gusano lleva contenido de Hotglue, la plantilla también copia ese contenido, de modo que un agujero de gusano creado desde la plantilla se abre sobre su propia copia privada de la misma página de formato libre. El agujero de gusano original queda intacto; la plantilla es una cosa separada y autónoma desde el momento en que se crea. Editar o eliminar el agujero de gusano después no cambia la plantilla, y viceversa.

La nueva plantilla toma el nombre del agujero de gusano. Puedes cambiarle el nombre más tarde desde la pestaña Plantillas.

### Basar un nuevo agujero de gusano en una plantilla

Junto a **Nuevo agujero de gusano** en el inicio del editor hay un pequeño desplegable. Su valor por defecto es **Sin plantilla**, que te da el formulario en blanco de siempre. Elige en su lugar una plantilla del desplegable, y el próximo agujero de gusano que crees se abre con los campos de esa plantilla ya rellenados:

![La barra de herramientas del inicio del editor: el botón Nuevo agujero de gusano junto a un desplegable que dice Sin plantilla, con una lista de plantillas guardadas](assets/images/editor-manual-es/16-template-selector.png)

El modal que se abre es el modal de Nuevo agujero de gusano de siempre, prellenado. Todo sigue siendo editable: cambia el nombre (casi siempre querrás hacerlo, ya que el nombre de la plantilla es solo un marcador de posición), ajusta las palabras clave, reescribe la descripción. Nada queda bloqueado. La plantilla solo decide dónde empieza el formulario, no dónde termina. Si la plantilla incluía contenido de Hotglue, el nuevo agujero de gusano recibe su propia copia privada de ese contenido, que luego editas de forma independiente.

Elegir una plantilla es una decisión por creación. El desplegable no se queda "armado"; después de crear un agujero de gusano a partir de una plantilla, vuelve a **Sin plantilla**, así que tu próximo agujero de gusano queda en blanco a menos que elijas una plantilla de nuevo.

### Gestionar tus plantillas

El inicio del editor tiene tres pestañas en la parte superior: **Agujeros de gusano**, **Plantillas** y **Contenido hotglue**. La pestaña Plantillas lista todas las plantillas que posees:

![La pestaña Plantillas: una tabla de plantillas con columnas Nombre y Hotglue, un cuadro de búsqueda, y acciones por fila de Cambiar nombre y Eliminar](assets/images/editor-manual-es/17-templates-tab.png)

La lista tiene dos columnas: el **Nombre** de la plantilla, y una columna **Hotglue** que marca las plantillas que llevan contenido de Hotglue. Un cuadro de búsqueda filtra la lista por nombre. Haz clic en el encabezado de una columna para ordenar.

Las acciones de cada plantilla son:

- **Cambiar nombre** cambia el nombre de la plantilla. Es puramente una etiqueta para tu propio uso; no toca ningún agujero de gusano ya creado a partir de la plantilla.
- **Eliminar** quita la plantilla. Los agujeros de gusano que ya creaste a partir de ella no se ven afectados; ahora son agujeros de gusano ordinarios, sin ningún vínculo vivo de vuelta a la plantilla. Eliminar una plantilla no se puede deshacer.

En esta primera versión, cambiar el nombre y eliminar son las únicas ediciones. Para cambiar lo que contiene una plantilla, crea una plantilla fresca a partir de un agujero de gusano que tenga la forma que quieres, y elimina la antigua.

## Cosas que vale la pena saber

- **Guarda antes de cambiar de galaxia en el desplegable** si estás a mitad de una edición; cambiar puede cerrar el modal sin guardar.
- **La posición en la escena 3D es automática.** A cada agujero de gusano se le asigna una posición por el sistema al crearse. No necesitas elegir dónde se ubica en el espacio; el diseño se genera. Para volver a aleatorizar la posición de un agujero de gusano, duplícalo y elimina el original (el duplicado recibe una posición nueva).
- **Las palabras clave coinciden sin distinguir mayúsculas y minúsculas.** "Native" y "native" son la misma palabra clave; la píldora usará la forma que se haya usado primero en la galaxia.
- **Un agujero de gusano sin descripción está permitido pero es silencioso.** Las visitantes que lo abren ven solo el nombre. Usa este patrón cuando el papel del agujero de gusano sea puramente visual (una postal solo de imagen) o cuando sirva como pista de navegación.
- **Las píldoras de palabras clave de un agujero de gusano están coloreadas de manera determinista** por el texto de la palabra clave. La misma palabra clave siempre recibe el mismo pastel en cada galaxia de tu instancia; esto es intencional, para que las visitantes reconozcan *native* por color tanto como por escritura.
- **Los agujeros de gusano importados son de solo lectura.** Si tu instancia importa contenido desde una fuente externa (un archivo hermano, una comunidad de origen aguas arriba), esos agujeros de gusano aparecen en tu lista de editora pero no pueden editarse; el modal de edición abre en estado de visor. El cambio tiene que ocurrir en la fuente.
