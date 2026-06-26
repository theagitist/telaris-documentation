# Añadir contenido

Este capítulo cubre cada tipo de objeto que puedes poner en una página, y las herramientas que ofrece cada uno una vez que está en el lienzo. La mayoría los añades desde el **menú NEW** (un solo clic en el fondo vacío). Las herramientas propias de cada objeto aparecen como iconos pequeños a su alrededor cuando lo seleccionas.

## Imágenes

**Para añadir una imagen,** usa la herramienta de subida del menú NEW, o simplemente arrastra un archivo de imagen desde tu computadora y suéltalo en cualquier punto de la página. Hotglue acepta JPEG, PNG, GIF y WebP. Si sueltas una imagen muy grande, Hotglue la reduce automáticamente a un tamaño razonable para la página (los GIF animados se dejan en su tamaño original).

Cuando una imagen está seleccionada, sus herramientas te permiten:

- **Activar o desactivar el mosaico de la imagen**, para que la imagen se repita y rellene su caja como un patrón.
- **Restablecer el tamaño de la imagen** a sus dimensiones naturales. Mantén <kbd>shift</kbd> o <kbd>ctrl</kbd> mientras lo haces para conservar la proporción.
- **Ajustar la selección de la imagen** arrastrando, para mostrar solo una parte de la imagen.
- **Descargar el archivo original**.
- **Editar esta imagen en el editor de dibujo** (consulta *Dibujos* más abajo).

## Texto

**Para añadir texto,** elige "añadir un nuevo objeto de texto" en el menú NEW. Aparece un cuadro de texto. Haz clic en un cuadro de texto seleccionado para editar sus palabras en línea; pulsa <kbd>esc</kbd> para dejar de editar.

Las herramientas de un cuadro de texto te permiten darle forma en detalle:

- **Color de fondo** de la caja, o **hacer el fondo transparente**.
- **Tamaño de letra**: arrastra la herramienta para cambiarlo, haz clic para restablecerlo.
- **Color de letra**.
- **Tipografía**: haz clic para recorrer las fuentes disponibles.
- **Estilo de letra**: recorre normal, negrita y cursiva.
- **Altura de línea**, **espaciado entre letras** y **espaciado entre palabras**.
- **Alineación del texto**: izquierda, centro, derecha, y luego justificado.
- **Relleno** dentro de la caja.

Los cuadros de texto también entienden algunas macros que se rellenan solas automáticamente, como `$BASEURL$` y `$PAGE$`. Escríbelas en un cuadro de texto y se reemplazan cuando se muestra la página.

## Video web

**Para incrustar un video,** elige "incrustar un video de youtube, vimeo o peertube" en el menú NEW y pega la dirección del video cuando se te pida. Hotglue reconoce enlaces de YouTube, Vimeo y PeerTube (incluidos los videos de PeerTube en cualquier servidor federado) y crea el reproductor incrustado adecuado para cada uno.

Cuando el objeto de video está seleccionado, sus herramientas te permiten:

- **Activar o desactivar la reproducción automática** del video (el cambio surte efecto después de recargar la página publicada).
- **Activar o desactivar la repetición** del video (también tras recargar).

En el modo de edición, una pequeña franja de "arrastra aquí" se sitúa sobre el reproductor para que puedas mover el objeto sin que el video capture tus clics.

## Dibujos

Hotglue incluye un editor de imágenes completo dentro de la página (miniPaint) para crear o retocar una imagen sin salir del lienzo. Hay dos formas de entrar:

- Desde el menú NEW, elige **dibujar una imagen nueva** para empezar en un lienzo en blanco.
- Con una imagen seleccionada, elige **editar esta imagen en el editor de dibujo** para abrir esa imagen y modificarla.

El editor de dibujo se abre en una ventana con las habituales herramientas de pintura. Cuando termines, haz clic en **colocar en la página** para soltar el resultado de vuelta en tu página de Hotglue (aplana tus capas en una sola imagen), o en **cancelar** para descartarlo. Si estabas editando una imagen existente, la nueva versión ocupa su lugar.

## Sonido (la mesa de sonido)

La **mesa de sonido** convierte una página en algo que puedes reproducir. Es un ajuste por página que activas desde el menú PAGE: "activar o desactivar el modo de mesa de sonido". Cuando está activo, la página publicada trata tus baldosas de video como disparadores, y al tocar una baldosa empieza su clip.

Lo que la convierte en una mesa de sonido en lugar de simplemente varios videos es la mezcla de audio:

- **Los clips de video autoalojados** que subiste se reproducen a través de un único motor de audio compartido, de modo que varios clips pueden sonar a la vez y superponerse. Esto funciona tanto en teléfonos como en escritorio.
- **Los videos incrustados** (YouTube, PeerTube, Vimeo) se reproducen a través de los controles de su propio reproductor integrado. Varios pueden reproducirse en paralelo; esto es fiable en escritorio y más limitado en teléfonos.

El cambio surte efecto después de recargar la página publicada. El modo de mesa de sonido está desactivado salvo que lo actives, así que una página normal con videos se comporta con normalidad.

## Herramientas de objeto (cualquier objeto)

Más allá de las herramientas por tipo de arriba, cada objeto comparte un conjunto común:

- **Clonar** el objeto.
- **Cambiar la transparencia** arrastrando.
- **Convertir el objeto en un enlace**: apúntalo a una dirección web, a otra página o a un ancla, con la opción de abrirlo en una pestaña nueva.
- **Obtener el nombre de este objeto**, para poder enlazarlo desde otro lugar.
- **Hacer que este objeto aparezca en todas las páginas** (útil para un logotipo o un pie de página).
- **Bloquear** el objeto para que no se pueda mover ni redimensionar por accidente; haz clic de nuevo para desbloquearlo.
- **Voltear** el objeto.
- **Eliminar** el objeto.

> [!note] Sin código personalizado
> La versión de Telaris de Hotglue deja fuera, a propósito, los módulos que te permitirían pegar HTML o scripts arbitrarios. Todo lo que añades es uno de los tipos de contenido de arriba. Es una decisión de seguridad, no un descuido.
