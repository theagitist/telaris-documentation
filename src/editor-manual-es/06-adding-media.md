# Añadir medios

El cuerpo de un agujero de gusano es la descripción; sus **medios** son todo lo visual o sonoro con lo que la visitante se encuentra junto al cuerpo: una imagen, un fragmento de película, una grabación sonora, un documento PDF, un reproductor incrustado de otro sitio. Este capítulo recorre cada tipo, en el orden en que el modal los presenta.

Un agujero de gusano carga como máximo **un visual primario** a la vez. Imagen, Video y PDF son tres pestañas en el modal que comparten un único espacio subyacente; elegir una y guardar borra las otras. El cuarto tipo de medio, **audio**, es independiente del visual primario: un agujero de gusano con una imagen *y* una pista de audio reproduce el audio mientras la imagen permanece en pantalla.

La propia sección de medios tiene dos pestañas de nivel superior: **Clásico** y **Hotglue**. Todo lo descrito arriba (imagen, video, PDF, audio, código de incrustación) vive bajo **Clásico**, la opción predeterminada. **Hotglue** es otra manera de construir los medios de un agujero de gusano: en lugar de una sola imagen o un solo video, compones una página libre, colocando texto e imágenes donde quieras sobre un lienzo abierto. Las dos son alternativas; la pestaña que esté abierta al guardar es lo que ven las visitantes. Hotglue se trata al final de este capítulo.

## La pestaña Imagen

La pestaña por defecto, y la elección más común de medios. Úsala para fotografías, ilustraciones, escaneos, diagramas, cualquier cosa estática.

![Pestaña Imagen en el modal de nuevo agujero de gusano: campo URL y selector de archivo, más el conmutador Usar como icono del agujero de gusano](assets/images/editor-manual-es/05-new-wormhole-modal.png)

Dos formas de adjuntar una imagen:

- **URL o archivo de imagen**: pega la dirección de una imagen alojada en otro lugar de la web. Úsalo cuando el hogar de la imagen está en algún sitio estable (un archivo de museo, el sitio web de una comunidad, una CDN bajo tu control). La URL debe apuntar a la imagen misma, no a una página que la contiene.
- **Selector de archivo**: usa el selector de archivo de tu navegador y sube una imagen desde tu computadora. Telaris mantiene el archivo subido en tu instancia y lo sirve de vuelta a las visitantes.

En cualquiera de los dos casos, la imagen se vuelve el visual primario de la visitante cuando abre el agujero de gusano.

**Usar como icono del agujero de gusano** es un conmutador debajo de los campos de imagen. Cuando está encendido, la imagen reemplaza el icono 3D por defecto del tema: las visitantes ven la imagen *como* el agujero de gusano en la escena 3D, no solo dentro de la ficha. Útil cuando la imagen es la identidad del agujero de gusano (un retrato, una portada, un logo). Cuando está apagado, la escena 3D muestra el icono por defecto del tema y la imagen solo aparece dentro de la ficha abierta.

La **atribución de imagen** es un pequeño campo de texto libre que viaja con la imagen. Úsalo para crédito al fotógrafo, archivo de origen, nota de licencia, cualquier cosa que se adjuntaría a la imagen si apareciera en un libro impreso. Las visitantes lo ven junto a la imagen en la ficha.

## La pestaña Video

Úsala para fragmentos de película, entrevistas grabadas, animaciones, cualquier cosa que se mueva. Telaris soporta solo MP4 por ahora; otros formatos (WebM, MOV, AVI) necesitan transcodificarse primero o alojarse en un servicio de video e incrustarse (ver Código de incrustación más abajo).

![Pestaña Video en el modal de nuevo agujero de gusano: URL o archivo de video para un MP4](assets/images/editor-manual-es/07-media-video-tab.png)

Las mismas dos rutas que en imagen: pega una URL a un MP4 alojado en otro sitio, o sube un archivo. Una vez guardado el agujero de gusano, la ficha de la visitante muestra un reproductor de video con controles estándar (play, pausa, scrub, volumen, pantalla completa).

**El tamaño importa.** Los archivos de video son típicamente mucho más grandes que las imágenes; el límite de subida de una instancia puede detenerte mucho antes de que se acabe tu paciencia. Si la subida falla, pregúntale a tu operadora sobre el límite o aloja el video externamente y usa el campo URL.

Si tu video vive en un servicio de streaming (Vimeo, YouTube, archive.org), el campo Código de incrustación más abajo es la herramienta correcta, no la pestaña Video.

## La pestaña PDF

Para documentos: artículos, guías de campo, fotocopias, informes, partituras, manuscritos.

![Pestaña PDF en el modal de nuevo agujero de gusano: URL o archivo de PDF](assets/images/editor-manual-es/08-media-pdf-tab.png)

Las mismas dos rutas. Una vez guardado, la ficha de la visitante incrusta un lector de PDF dentro de la página: puede desplazarse por el documento, buscar en él, copiar texto y descargarlo (las prestaciones del visor de PDF estándar).

Las subidas de PDF tienen un tope de tamaño fijado por tu operadora (comúnmente 25 MB). Si tu archivo es más grande, o lo partes, lo alojas externamente y lo enlazas con el campo URL, o le pides a tu operadora que suba el tope.

## Audio

El campo Audio aparece debajo de las pestañas del visual primario. Es independiente de la elección entre imagen / video / PDF; un agujero de gusano puede tener cualquier combinación de audio y un visual primario.

- **URL o archivo de audio**: pega una URL a un archivo de audio o sube uno. MP3 es la elección más segura; muchos navegadores también soportan OGG y WAV.

Cuando se adjunta audio, dos conmutadores controlan la reproducción:

- **Reproducir automáticamente**: cuando está encendido, el audio empieza tan pronto como la visitante abre la ficha del agujero de gusano. Cuando está apagado, la visitante ve un botón de play e inicia el audio ella misma. Reproducir automáticamente suele ser correcto para pistas cortas, ambientales o atmosféricas; apagado es correcto para palabra hablada, música, cualquier audio que exija atención.
- **En bucle**: cuando está encendido, el audio reinicia desde el principio cada vez que termina. Úsalo para bucles ambientales, drones, paisajes sonoros; apágalo para cualquier audio con un arco narrativo.

El audio suena de fondo de la ficha; la visitante puede pausarlo o moverlo en cualquier momento con los controles de audio estándar.

## Código de incrustación

La cuarta ruta de medios, para contenido alojado en otro servicio que ya provee un fragmento de incrustación: un iframe de Vimeo, un reproductor de Spotify, una pista de SoundCloud, un visor de archive.org, una escena 3D de SketchFab.

Busca el campo **Código de incrustación** (debajo de las pestañas del visual primario) y pega el fragmento exactamente como el servicio te lo da. Telaris no transforma ni sanea el código de embed; lo que pegas es lo que las visitantes reciben. Prueba el agujero de gusano después abriéndolo en la vista de visitante; si el embed está roto, el campo es el lugar para arreglarlo.

El código de embed y el visual primario no son mutuamente excluyentes (el embed aparece por separado en la ficha), pero por claridad suele tener sentido elegir uno u otro.

## La sustitución de icono

Debajo de los campos de medios aparece un **URL o archivo de icono**. Esto fija la apariencia del agujero de gusano en la escena 3D, *separadamente* del visual primario. Úsalo cuando:

- Quieres un icono 3D personalizado (un pequeño gráfico que representa el agujero de gusano a escala de escena), distinto de la imagen más grande que las visitantes ven dentro de la ficha.
- El conmutador Usar como icono del agujero de gusano en la pestaña Imagen no basta porque tienes una imagen *y* quieres que el icono de la escena sea otra cosa.

La mayoría de las editoras no necesitan esto; los iconos por defecto del tema cubren la mayoría de los casos. Cuando sí lo necesitas, provee una imagen cuadrada pequeña (PNG o SVG) y Telaris la usará en la escena 3D.

## Almacenamiento y qué viaja con un agujero de gusano

Los medios subidos se guardan en tu instancia. Las subidas de cada agujero de gusano viven bajo una carpeta identificada por el id del agujero de gusano; restaurar una instantánea trae las subidas con ella, eliminar un agujero de gusano elimina sus subidas.

Los medios enlazados por URL se quedan en su servidor original; si el servidor elimina el archivo, los medios del agujero de gusano se vuelven oscuros. Las editoras con referencias externas valiosas deberían considerar subir el archivo en vez de enlazarlo, para que el archivo sobreviva a su origen.

## Componer una página con Hotglue

A veces una sola imagen o un solo video no bastan. Quieres una pequeña composición: un título, un párrafo, dos fotografías una al lado de la otra, un pie de foto debajo, un enlace hacia afuera. **Hotglue** es el modo de medios para eso. En lugar de llenar un espacio fijo, compones una página libre donde cada elemento se puede colocar, dimensionar y disponer a mano, y esa página se convierte en los medios del agujero de gusano.

En el modal de editar agujero de gusano, abre la sección **Medios** y elige la pestaña **Hotglue**, luego elige **Editar contenido hotglue**. Se abre un editor casi a pantalla completa sobre la página. Es un lienzo abierto: no hay filas ni columnas a las que ajustarse. Agregas un bloque de texto o una imagen y luego lo arrastras a donde quieras, lo redimensionas y superpones unos elementos sobre otros.

![El modal de editar agujero de gusano con la pestaña de medios Hotglue activa: una breve línea de ayuda y el botón Editar contenido hotglue](assets/images/editor-manual-es/14-media-hotglue-tab.png)

Los movimientos básicos:

- **Agregar texto.** Haz doble clic en un área vacía del lienzo para crear un bloque de texto y escribe. Haz clic fuera de él para terminar. Arrastra el bloque para reposicionarlo; arrastra su borde para redimensionarlo.
- **Agregar una imagen.** Arrastra un archivo de imagen desde tu computadora al lienzo, o usa la barra de herramientas para elegir una. La imagen se guarda con la página. Arrástrala y redimensiónala como cualquier otro elemento.
- **Disponer con libertad.** Los elementos pueden estar en cualquier lugar y superponerse. No hay cuadrícula; la disposición que construyas es la que ven las visitantes.
- **La página se guarda mientras trabajas.** No hay un botón de guardar aparte dentro del lienzo; tus cambios se conservan a medida que los haces. Cuando termines, cierra el editor.

De vuelta en el modal del agujero de gusano, deja seleccionada la pestaña **Hotglue** y guarda el agujero de gusano. A partir de entonces, abrir ese agujero de gusano muestra tu página compuesta en lugar de la imagen o el video clásicos. Las visitantes ven la página exactamente como la dispusiste; no pueden editarla.

Algunas cosas que tener presentes:

- **Solo editas páginas en galaxias en las que tienes un asiento.** La edición con Hotglue sigue la misma regla de acceso que el resto del agujero de gusano: puedes componer páginas en tus propias galaxias, y no en galaxias a las que no se te ha dado acceso.
- **Una página de Hotglue es una sola superficie compuesta.** A diferencia del resto de Telaris, no se traduce sola según el idioma de quien visita; el texto que colocas es el texto que ve todo el mundo. Si tu público es multilingüe, escribe la página teniéndolo en cuenta.
- **La disposición libre es el modo de medios más expresivo y el menos indulgente.** La colocación absoluta se ve exactamente como la fijaste, lo que también significa que no se reajusta para pantallas pequeñas ni para tecnología de asistencia como sí lo hace el texto ordinario. Úsala donde la composición importe; apóyate en las pestañas clásicas Imagen o PDF para documentos sencillos.
- **Clásico y Hotglue son alternativas, no una pila.** Un agujero de gusano muestra uno u otro, según qué pestaña esté abierta al guardar. Volver a Clásico no borra la página de Hotglue; solo deja de mostrarla, así que puedes regresar a ella más tarde reseleccionando la pestaña Hotglue.

## Cosas que vale la pena saber

- **Cambiar entre pestañas del visual primario borra el campo en el que estabas.** Un aviso de seguridad antes de guardar te lo advierte. Si cambias de idea, vuelve antes de guardar.
- **El audio en bucle puede resultar abrupto en la primera visita.** Si envías un bucle de audio, escucha el borde (el momento en que el bucle reinicia); la costura es lo que las visitantes notarán.
- **Una imagen en alta resolución es más útil que una de baja.** Telaris reduce las imágenes para la escena 3D automáticamente; subirlas en calidad completa significa una ficha más nítida, y significa que cambios futuros de formato no requieren volver a subir.
- **El texto del PDF es buscable en el visor dentro de la página**, pero solo si el PDF mismo tiene una capa de texto. Documentos escaneados sin OCR son imágenes planas dentro de un envoltorio PDF; el cuadro de búsqueda no encontrará nada.
- **Los archivos de video no se transmiten por fragmentos**: cuando una visitante abre el agujero de gusano, el archivo entero se descarga. Mantén los archivos de video cortos y bien comprimidos.
- **Los embeds externos pueden romperse con el tiempo.** Los servicios cambian su formato de embed, deprecan reproductores, o eliminan contenido. Un agujero de gusano que depende de un embed es uno cuya vida media es más corta que uno cuyos medios viven en tu instancia.
