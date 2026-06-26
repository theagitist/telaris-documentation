# El lienzo

Este capítulo es el corazón del manual: cómo funciona la superficie de edición una vez que la has abierto.

## El modo de edición

Una página de Hotglue tiene dos estados: la vista publicada que ve quien visita, y el **modo de edición**, donde puedes cambiar cosas. Entras en el modo de edición a través de los botones descritos en *Cómo entrar*. En el modo de edición la página gana sus menús y cada objeto se vuelve arrastrable.

![Una página de Hotglue abierta en el lienzo de edición: una franja de título, un subtítulo y dos columnas de texto, cada una un objeto separado que puedes mover](assets/images/hotglue-manual-es/03-canvas.png)

## Los dos menús

Casi todo lo que haces empieza en uno de dos menús, y cuál de ellos obtienes depende de cómo haces clic en el fondo vacío de la página:

- **Haz un solo clic en el fondo** para abrir el **menú NEW**: las herramientas para añadir cosas a la página (subir un archivo, añadir texto, incrustar un video, dibujar una imagen). El atajo de teclado es <kbd>alt</kbd> + <kbd>o</kbd>.

  ![El menú NEW abierto en el lienzo: iconos pequeños para añadir un dibujo, texto, un archivo subido, una imagen y un video](assets/images/hotglue-manual-es/04-new-menu.png)

- **Haz doble clic en el fondo** para abrir el **menú PAGE**: las herramientas que afectan a toda la página (color e imagen de fondo, la cuadrícula). El atajo de teclado es <kbd>alt</kbd> + <kbd>p</kbd>.

  ![El menú PAGE abierto en el lienzo: una cuadrícula de herramientas de página completa que incluyen título, URL de la página, página de inicio, color e imagen de fondo, y la cuadrícula](assets/images/hotglue-manual-es/05-page-menu.png)

Cuando **seleccionas un objeto** (haciendo clic en él), aparece un tercer conjunto de herramientas: el **menú contextual** propio del objeto, un abanico de iconos pequeños alrededor del objeto. Los iconos varían según el tipo de objeto (una imagen tiene herramientas distintas que un cuadro de texto), y se tratan por tipo en *Añadir contenido*.

## Colocar, seleccionar y mover

**Añadir un objeto** lo pone donde hiciste clic (para los elementos del menú) o donde lo soltaste (para arrastrar y soltar). Después puedes moverlo a cualquier sitio.

**Seleccionar:**

- Haz clic en un objeto para seleccionarlo.
- Mantén <kbd>shift</kbd> y haz clic para añadir más objetos a la selección (o quitar uno).
- Haz clic en el fondo vacío para deseleccionar todo.
- <kbd>ctrl</kbd> + <kbd>A</kbd> selecciona todos los objetos, <kbd>ctrl</kbd> + <kbd>D</kbd> no selecciona ninguno, <kbd>ctrl</kbd> + <kbd>I</kbd> invierte la selección, y <kbd>tab</kbd> avanza por los objetos uno a uno.

**Mover:**

- Arrastra un objeto seleccionado con el ratón.
- Mantén <kbd>shift</kbd> mientras arrastras para bloquear el movimiento en un solo eje (puramente horizontal o puramente vertical).
- Mantén <kbd>ctrl</kbd> mientras arrastras para ignorar la cuadrícula de ajuste y colocar el objeto con libertad.
- Las teclas de flecha empujan una selección un píxel cada vez; <kbd>shift</kbd> + una tecla de flecha la mueve un paso de cuadrícula.

**Redimensionar:** arrastra el tirador de tamaño en la esquina de un objeto seleccionado. Una pequeña lectura muestra el ancho, el alto y la posición en vivo mientras arrastras. Mantén <kbd>ctrl</kbd> para redimensionar sin la cuadrícula.

**Eliminar:** pulsa <kbd>delete</kbd> con un objeto seleccionado, o usa el icono de eliminar propio del objeto.

## Capas y orden de apilamiento

Cuando los objetos se solapan, tú controlas cuál queda delante:

- Arrastra el icono de primer plano/segundo plano del objeto hacia la izquierda o la derecha para moverlo hacia adelante o hacia atrás un paso cada vez.
- <kbd>shift</kbd> + <kbd>page up</kbd> lleva la selección hasta el frente del todo; <kbd>shift</kbd> + <kbd>page down</kbd> la envía hasta el fondo del todo.

## La cuadrícula y el ajuste

De forma predeterminada, los objetos se ajustan a una cuadrícula invisible mientras los mueves y los redimensionas, lo que mantiene ordenada una composición. Desde el menú PAGE puedes mostrar u ocultar la cuadrícula, y puedes cambiar su espaciado arrastrando la herramienta de cuadrícula (la lectura muestra el tamaño como NxN). Para colocar un solo objeto fuera de la cuadrícula sin cambiar la cuadrícula misma, mantén <kbd>ctrl</kbd> mientras lo arrastras o lo redimensionas.

## El fondo

Desde el menú PAGE puedes:

- **Cambiar el color de fondo** con una rueda de colores (o hacer shift-clic en la rueda para escribir un valor exacto).
- **Subir una imagen de fondo** para la página.
- Alternar si la imagen de fondo se queda **fija** mientras la página se desplaza, o se desplaza con ella.
- Ajustar qué parte de la imagen de fondo se muestra, arrastrando.

## Guardado e historial

**No hay botón de Guardar.** Cada acción que realizas (mover, redimensionar, editar texto, cambiar un color) se guarda en el instante en que la terminas.

Por eso, tampoco hay un **deshacer** tradicional. En su lugar, Hotglue conserva un historial de una página llamado *revisiones*. Ábrelo con el botón **Revisiones** en el editor (o pulsa <kbd>ctrl</kbd> + <kbd>z</kbd>, que se ofrece a llevarte allí). En la vista de revisiones puedes mirar atrás entre las versiones anteriores de la página. Hotglue toma una instantánea automática de una página aproximadamente una vez por hora mientras se edita, y conserva esas instantáneas durante siete días.

> [!tip] Trabaja con movimientos pequeños y deliberados
> Como no hay deshacer y los cambios son inmediatos, conviene hacer los cambios de uno en uno y echar un vistazo al resultado. Si algo sale mal, el historial de revisiones es tu red de seguridad, no una tecla de deshacer.
