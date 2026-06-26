# Introducción

Este manual es para cualquier persona que componga una **página de Hotglue**: una composición visual de formato libre donde el texto, las imágenes, el video y el sonido se ubican exactamente donde tú los colocas, sin una cuadrícula ni una plantilla que les diga dónde ir. Si un cuadro de texto normal te resulta demasiado rígido para el aspecto que quieres dar a un contenido, Hotglue es la superficie que te ofrece un lienzo en blanco en su lugar.

## Qué es Hotglue

Hotglue es un editor visual de páginas. Arrastras objetos a una página, los mueves y les cambias el tamaño a mano, y lo que organizas es lo que ve quien visita. No hay columnas que rellenar ni forma fija: una página puede ser tan ancha y tan alta como quieras, y un objeto puede solaparse con otro, situarse sobre un fondo de color o flotar donde tú lo pongas.

Dos cosas hacen que Hotglue se sienta distinto de la mayoría de los editores, y conviene tenerlas claras desde el principio:

- **No hay botón de Guardar.** Cada movimiento, cambio de tamaño y edición se guarda en el momento en que lo haces. Nunca tienes que acordarte de guardar, y tampoco existe un "descartar cambios". Si quieres dar marcha atrás ante un error, Hotglue conserva un historial (consulta *revisiones* en *El lienzo*).
- **Lo que editas es lo que se publica, de inmediato.** Cuando cambias una página, el cambio queda visible para quien visita al instante. No hay un paso de publicación aparte ni una caché que limpiar.

## De dónde viene Hotglue

Hotglue no es originalmente nuestro. Lo crearon Danja Vasiliev y Gottfried Haider y se hizo ampliamente conocido a través del servicio alojado en hotglue.me. Se construyó como una reacción deliberada contra las convenciones del diseño web habitual: en lugar de plantillas, columnas y jerarquías ordenadas, ofrece un lienzo libre donde la composición es no lineal y la ubicación depende enteramente de ti. Ese espíritu, romper con los estándares web de siempre e invitar a una composición creativa y no planificada, es justo por lo que Telaris lo usa.

El proyecto original ya no está en desarrollo activo aguas arriba. Su código sigue disponible y abierto, bajo la Licencia Pública General de GNU versión 3 (GPL-3.0):

- Proyecto original: <https://hotglue.me> y el código en <https://github.com/k0a1a/hotglue2>

## La versión de Hotglue de Telaris

Este manual describe **la versión de Hotglue de Telaris**, que mantenemos y desarrollamos activamente como una bifurcación. Sigue siendo de código abierto bajo la misma licencia GPL-3.0, y nuestro código es público:

- Bifurcación de Telaris: <https://github.com/theagitist/hotglue2>

Como lo desarrollamos nosotros, el Hotglue de Telaris tiene varias funciones que no están en el original. La mayor parte de lo que cubre este manual es común con el Hotglue clásico, pero lo siguiente se añadió o se mejoró sustancialmente para Telaris:

- **Compatibilidad con imágenes WebP**, junto a JPEG, PNG y GIF.
- **Una interfaz de edición renovada**, con un juego de iconos moderno y un aspecto más limpio con la identidad de Telaris.
- **Más fuentes de video.** Las incrustaciones funcionan con YouTube, Vimeo y PeerTube, incluidos los videos de PeerTube alojados en cualquier servidor federado.
- **Un editor de imágenes completo dentro de la página** (basado en miniPaint) para dibujar una imagen nueva o retocar una existente sin salir de la página.
- **Modo de mesa de sonido**, donde una página publicada se vuelve reproducible: tocas las baldosas de video para disparar clips, con audio autoalojado mezclado para que varios suenen a la vez.
- **Accesibilidad en teléfonos y pantallas pequeñas.** Las páginas publicadas se escalan automáticamente para caber en pantallas estrechas, de modo que una composición creada ancha sigue siendo utilizable en un teléfono.
- **Integración en Telaris**, que incluye el control de acceso por persona editora, la posibilidad de adjuntar páginas a agujeros de gusano y la vista de gestión **Contenido hotglue** que se describe más adelante en este manual.
- **Interfaz localizada.** El editor está disponible en español, inglés, portugués y francés: los menús del lienzo, las descripciones emergentes y los mensajes, el editor de imágenes integrado y los controles de Telaris a su alrededor (la vista de Contenido hotglue, la barra de herramientas, los botones y los diálogos) siguen todos el idioma en el que estés trabajando.

Cuando este manual menciona alguna de estas funciones, está describiendo específicamente la versión de Telaris. Si has usado Hotglue en otro sitio, esas son las diferencias que puedes esperar.

## Cómo está organizado este manual

Los capítulos avanzan desde cómo entras, al lienzo mismo, a cada tipo de contenido que puedes añadir, y después a la gestión de tus páginas y a cómo las ve quien visita.

1. **Cómo entrar.** Llegar al editor de Hotglue en Telaris, y quién puede editar qué.
2. **El lienzo.** El modo de edición, los dos menús, y cómo colocar, mover, redimensionar y organizar objetos.
3. **Añadir contenido.** Imágenes, texto, video web, dibujos, sonido y herramientas de objeto.
4. **Gestionar páginas.** La vista de Contenido hotglue: crear, nombrar, asignar y ordenar páginas.
5. **Cómo se ve en teléfonos.** Lo que ve quien visita en una pantalla pequeña, y consejos para componer teniéndolo presente.
6. **Atajos de teclado.** Todos los atajos en una sola tabla.
7. **Glosario.** Las piezas con nombre, definidas brevemente.

## Convenciones

- **Las rutas de menú** aparecen así: <span class="menu-path">menú PAGE &rarr; cambiar el color de fondo</span>.
- **Los botones y las descripciones emergentes** aparecen en negrita: **Nueva página**, **colocar en la página**, **Agujero de gusano asignado**.
- **Los atajos de teclado** usan <kbd>alt</kbd> + <kbd>o</kbd>.
- *La cursiva* introduce un término la primera vez que aparece.

> [!note] Cuando algo sale mal
> Si una página no carga, o el editor se comporta de una forma que este manual no describe, contacta con la persona que gestiona tu instancia (quien opera). Este manual se centra en lo que puedes hacer una vez que todo funciona como se espera.
