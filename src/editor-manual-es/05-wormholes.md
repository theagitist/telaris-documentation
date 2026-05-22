# Agujeros de gusano

Un agujero de gusano es la unidad más pequeña de contenido en Telaris. Todo lo que una editora publica es, al final, un agujero de gusano: un pasaje de texto, una fotografía, una grabación de audio, un fragmento de película, un PDF, una cita, un único pensamiento. Este capítulo recorre la creación, la edición, los campos que le dan forma, y las elecciones que el formulario te invita a hacer.

## Crear un nuevo agujero de gusano

Desde el inicio del editor, selecciona la galaxia en la que estás trabajando, luego elige **New Wormhole**. Se abre un cuadro modal:

![Cuadro modal Add New Wormhole: formulario vacío con Name, Galaxy, Type, Keywords, Description, URL, y pestañas de medios visibles](assets/images/editor-manual-es/05-new-wormhole-modal.png)

El formulario tiene cuatro regiones amplias, en el orden en que las encuentras al bajar por el modal:

1. **Identidad** arriba: Name, Galaxy, Wormhole type, Keywords.
2. **Interruptores de comportamiento**: Accentuate, Show Keywords.
3. **Cuerpo**: Description, URL.
4. **Medios**: imagen, video, audio, PDF, y la sustitución del icono.

Guarda con el botón al fondo del modal; el nuevo agujero de gusano aparece en la lista inmediatamente. Cancela o haz clic fuera del modal para descartar.

## Campos de identidad

### Name

Obligatorio. La etiqueta que la visitante lee en la escena 3D, en cualquier lista, y en la URL cuando la comparte. Elige un nombre que se lea limpio por sí solo; se citará fuera de contexto más a menudo de lo que crees.

Los nombres dentro de una galaxia deben ser únicos; el modal te avisará si un nombre está tomado antes de guardar. Entre galaxias, dos agujeros de gusano pueden compartir un nombre sin conflicto.

### Galaxy

Obligatorio, pero suele venir pre-llenado. El desplegable muestra todas las galaxias que puedes editar. Si empezaste desde una galaxia específica en el inicio del editor, esa galaxia queda seleccionada por defecto; si empezaste desde *All my galaxies*, eliges aquí.

Cambiar la galaxia en este desplegable **mueve** el agujero de gusano a esa galaxia. Las palabras clave del agujero de gusano vienen con él, pero sus *posiciones* en el lienzo de la galaxia de destino pueden necesitar un retoque.

### Wormhole type

Un desplegable con dos valores:

- **Object** es la opción por defecto y la respuesta correcta para casi todos los agujeros de gusano. Un Object contiene contenido (descripción, medios).
- **Portal** convierte el agujero de gusano en una puerta a otra galaxia. Seleccionar Portal revela un segundo desplegable para la galaxia de destino. El capítulo 9 cubre los portales.

### Keywords

Una entrada de píldoras. Escribe una palabra clave y presiona **Enter** (o coma) para añadirla; haz clic en la **×** de una píldora para eliminarla. Las sugerencias aparecen a medida que escribes, extraídas de:

- Palabras clave ya usadas en **esta** galaxia.
- Palabras clave usadas en galaxias que comparten el prefijo `[entre corchetes]` de tu galaxia.

Elige palabras clave pensando en el camino de la visitante: cada palabra clave que adjuntas es una puerta desde este agujero de gusano a todos los demás agujeros de gusano que comparten la misma palabra. Cuantas menos palabras clave asignes, más deliberada se siente cada conexión; cuantas más asignes, más densa la red. El capítulo 7 cubre la estrategia de palabras clave.

## Interruptores de comportamiento

### Accentuate Wormhole

Apagado por defecto. Cuando está encendido, este agujero de gusano se representa más grande y prominente en la escena 3D. Úsalo con moderación: si acentúas todo, nada queda acentuado. La marca de acentuación también es la señal que la característica de recorrido automático puede usar para elegir sus paradas (capítulo 11).

### Show Keywords

Apagado por defecto. Cuando está encendido, la visitante ve las palabras clave de este agujero de gusano impresas junto a él en la escena 3D, antes de abrirlo. Útil para agujeros de gusano cuyo papel en la galaxia se entiende mejor a través de sus etiquetas (un documento de referencia; una pista de navegación; una definición).

## Cuerpo

### Description

El texto que la visitante lee al abrir el agujero de gusano. No hay límite de longitud; agujeros de gusano de una línea y ensayos largos son ambos posibles. El campo acepta formato markdown básico: párrafos (una línea en blanco), `**bold**`, `*italics*`, `[link](https://...)`, listas, y `code` en línea. Los encabezados y los medios incrustados no se representan dentro de la descripción; si necesitas un quiebre tipo encabezado, deja una línea en blanco y empieza un nuevo párrafo.

Escribe las descripciones en tu propia voz. Telaris no edita lo que escribes; la plataforma enmarca el contenido, el contenido es tuyo.

### URL

Opcional. Si lo rellenas, el agujero de gusano se vuelve cliqueable como enlace de salida: cuando la visitante abre la ficha del agujero de gusano, aparece un botón *Open Link* que la lleva a la URL en una pestaña nueva.

Úsalo para referencias canónicas (un artículo, una página de libro, un archivo sonoro, el sitio web de una comunidad). Déjalo vacío cuando el agujero de gusano sea autosuficiente.

## Medios

Un agujero de gusano puede cargar un **visual primario** más una pista de **audio** opcional y una **sustitución de icono** opcional. El visual primario es lo que las visitantes ven en la parte superior de la ficha cuando abren el agujero de gusano; el audio suena de fondo; la sustitución de icono cambia cómo aparece el agujero de gusano en la escena 3D.

El modal organiza el visual primario como un conjunto de pestañas: **Image**, **Video (MP4)**, **PDF**. Elegir una y guardar borra las otras; solo un visual primario a la vez. El capítulo 6 cubre cada pestaña en detalle.

El campo de audio es independiente del visual primario; un agujero de gusano con una imagen y un archivo de audio reproduce el audio mientras la imagen está visible. El código de embed (por ejemplo un iframe de Spotify o Vimeo) se admite como alternativa a la imagen / video / PDF cuando el visual está alojado externamente.

## Editar un agujero de gusano existente

Para editar un agujero de gusano, haz clic en cualquier parte de su fila en la lista de agujeros de gusano, o abre el menú de acciones de la fila y elige **Edit**:

![Modal Edit Wormhole para Beach Strawberry: nombre completado, píldoras de palabras clave, descripción, pestañas de medios](assets/images/editor-manual-es/06-edit-wormhole-modal.png)

El modal es el mismo que el formulario de creación, con los valores existentes pre-cargados. El id del agujero de gusano aparece en la esquina superior derecha (aquí, `#279`); las editoras rara vez necesitan referirse a los ids, pero el número es útil al reportar un problema a tu operadora.

Save persiste el cambio inmediatamente. Las visitantes que estén viendo la galaxia ven tu actualización en su próxima recarga de página.

## Duplicar, ver, eliminar

El menú de acciones en cada fila de agujero de gusano ofrece cuatro operaciones:

- **View** abre una vista previa de solo lectura de la ficha del agujero de gusano tal como la vería la visitante. Úsalo cuando quieras revisar un cambio antes de dar el trabajo por hecho.
- **Edit** abre el modal de arriba.
- **Duplicate** crea una copia del agujero de gusano, con el mismo contenido, en la misma galaxia, llamada "Original Name (Copy)". El nuevo agujero de gusano recibe una posición fresca en la escena 3D; todo lo demás se traslada. Útil cuando quieres un casi duplicado como punto de partida.
- **Delete** elimina el agujero de gusano. Aparece primero un cuadro modal de confirmación; las eliminaciones son permanentes (tu operadora a veces puede restaurar desde una instantánea, pero la respuesta debería ser: no elimines a menos que lo quieras decir).

## Cosas que vale la pena saber

- **Guarda antes de cambiar de galaxia en el desplegable** si estás a mitad de una edición; cambiar puede cerrar el modal sin guardar.
- **La posición en la escena 3D es automática.** A cada agujero de gusano se le asigna una posición por el sistema al crearse. No necesitas elegir dónde se ubica en el espacio; el diseño se genera. Para volver a aleatorizar la posición de un agujero de gusano, duplícalo y elimina el original (el duplicado recibe una posición nueva).
- **Las palabras clave coinciden sin distinguir mayúsculas y minúsculas.** "Native" y "native" son la misma palabra clave; la píldora usará la forma que se haya usado primero en la galaxia.
- **Un agujero de gusano sin descripción está permitido pero es silencioso.** Las visitantes que lo abren ven solo el nombre. Usa este patrón cuando el papel del agujero de gusano sea puramente visual (una postal solo de imagen) o cuando sirva como pista de navegación.
- **Las píldoras de palabras clave de un agujero de gusano están coloreadas de manera determinista** por el texto de la palabra clave. La misma palabra clave siempre recibe el mismo pastel en cada galaxia de tu instancia; esto es intencional, para que las visitantes reconozcan *native* por color tanto como por escritura.
- **Los agujeros de gusano importados son de solo lectura.** Si tu instancia importa contenido desde una fuente externa (un archivo hermano, una comunidad de origen aguas arriba), esos agujeros de gusano aparecen en tu lista de editora pero no pueden editarse; el modal de edición abre en estado de visor. El cambio tiene que ocurrir en la fuente.
