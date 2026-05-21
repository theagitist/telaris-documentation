# Galaxias

Una galaxia es a la vez un contenedor, un punto de vista, y una posición editorial. Es la unidad que tu operadora te entrega cuando dice "puedes editar aquí"; es la unidad a la que llegan las visitantes; es la unidad que enmarcas, nombras, y das forma. Este capítulo recorre la creación de una galaxia, su configuración, y las operaciones cotidianas sobre ella.

## Seleccionar una galaxia

El desplegable **Current Galaxy** en la parte superior del inicio del editor es como eliges en qué galaxia estás trabajando. *All my galaxies* muestra agujeros de gusano de todos los lugares donde tienes acceso; seleccionar una galaxia específica filtra todo lo de abajo a esa galaxia.

Lo primero que el desplegable te enseña es la forma de tus responsabilidades editoriales: toda galaxia listada es una galaxia que puedes editar. Si falta la galaxia de una colega, tu operadora no te la ha asignado. (Las visitantes de tu instancia ven todas las galaxias públicas; las editoras solo ven las que tienen a su cargo.)

Cuando eliges una galaxia específica, aparecen tres botones nuevos junto al desplegable:

![Inicio del editor con una sola galaxia seleccionada: aparecen los botones View, Settings y Canvas](assets/images/editor-manual/03-editor-home-single-galaxy.png)

- **View** abre la galaxia en modo visitante, en una pestaña nueva. Úsalo cuando quieras comprobar cómo se lee un cambio desde el asiento de la visitante.
- **Settings** abre la configuración de la galaxia. La mayor parte de este capítulo trata sobre lo que hay dentro de ese cuadro modal.
- **Canvas** abre el lienzo de palabras clave, la superficie relacional de dibujo cubierta en el capítulo 8.

## Crear una galaxia

Si puedes crear una nueva galaxia depende de la configuración que haya hecho tu operadora; algunas instancias permiten a las editoras crear galaxias libremente, otras reservan la creación para administradoras. Si tienes el permiso, el botón de nueva galaxia está en la misma fila que el selector; si no, pídele a tu operadora y te configurará una.

Cuando se crea una nueva galaxia, llega vacía: cero agujeros de gusano, ninguna palabra clave, tema por defecto. El siguiente paso es completar sus ajustes.

## Ajustes de galaxia

Abre el botón **Settings** junto al selector. Se abre un cuadro modal:

![Cuadro modal Edit Galaxy: Name, Tagline, Visual Theme, Tags, acciones por lote, y conmutadores de descubrimiento](assets/images/editor-manual/04-galaxy-settings-modal.png)

El cuadro modal es el lugar central donde das forma a lo que una galaxia es y cómo se comporta. Los campos, en orden:

**Name** (obligatorio). El nombre que ven las visitantes en el selector de galaxia y en la parte superior de la escena. Los nombres de galaxia no son únicos en la red, pero dos galaxias con el mismo nombre en la misma instancia confunden; elige algo legible y distinto. Puedes cambiar el nombre de una galaxia en cualquier momento.

**Tagline** (opcional, corto). Una descripción de una línea que se muestra junto al nombre de la galaxia o debajo, en la interfaz de la visitante. La tagline no aparece en la escena 3D; su público principal es el selector y el listado público.

**Visual Theme**. Un desplegable que elige el aspecto de la escena 3D: *Cosmic* (estrellas, planetas, cohetes) es la opción por defecto y la más común; otros temas son *Simple*, *Abstract*, *Rectangles*, *Stripes*, y *Tech*. Elige el cuyo vocabulario calce con tu contenido. El tema puede cambiarse en cualquier momento; el cambio se aplica a todas las visitantes inmediatamente, pero no altera lo que escribiste, solo cómo se representa.

**Tags** (opcional). Etiquetas cortas que agrupan esta galaxia con otras galaxias. Dos galaxias que comparten una etiqueta forman una *unión de galaxias*: las visitantes que siguen la etiqueta ven los agujeros de gusano de ambas a la vez, manteniendo cada agujero el estilo visual de su galaxia de origen. Usa etiquetas cuando varias galaxias sean hermanas en algún arreglo más amplio. El campo Tags autocompleta a partir de etiquetas que has usado en tus otras galaxias y de etiquetas compartidas por galaxias con el mismo prefijo `[entre corchetes]`.

**Acciones por lote sobre agujeros de gusano**. Dos botones que aplican un único ajuste a todos los agujeros de gusano de esta galaxia a la vez.

- **Use images as icons (all wormholes)** hace que cada agujero de gusano que tenga imagen represente esa imagen como el nodo 3D en lugar del icono por defecto del tema. Útil cuando tienes una galaxia de fotografías y quieres que las fotos *sean* la escena.
- **Revert all to theme icons** deshace lo anterior: cada agujero de gusano vuelve al icono del tema, tenga imagen o no.

Estos actúan por lote; cada agujero de gusano todavía puede invertirse uno por uno después (capítulo 5).

**Conmutadores de descubrimiento**. Un conjunto de interruptores al pie del cuadro modal que controlan cómo experimenta tu galaxia la visitante. Vienen apagados por defecto; enciende cada uno cuando quieras la característica correspondiente. Cada conmutador se cubre en el capítulo 10 (Vistas de visitante) donde también se muestra la característica que controla.

Guarda el modal con **Save**; cierra sin cambios con **Cancel** o haciendo clic fuera del modal. Los cambios se aplican a las visitantes inmediatamente.

## Marco editorial

El marco de una galaxia es el párrafo corto que la abre para las visitantes. Es la respuesta a la pregunta *qué es esta galaxia* antes de que la visitante haya conocido cualquier agujero de gusano. Dos lugares donde escribirlo:

1. El campo **Tagline** del modal de galaxia, para el resumen de una línea que aparece junto al nombre de la galaxia.
2. (Algunas instancias) un agujero de gusano dedicado al marco dentro de la galaxia, a menudo el primero que ve una visitante al entrar. Si tu instancia usa este patrón, tu operadora te lo dirá.

Ambos son elecciones editoriales, no técnicas. Escribe el marco en tu propia voz; la galaxia es tuya para presentarla.

## Compartir agujeros de gusano entre galaxias mediante etiquetas

Si tienes una galaxia cuyo contenido es parte de una constelación más amplia de trabajo (una exposición con varias salas; una revista con varios números; una serie de colecciones relacionadas), el campo **Tags** es como lo dices. Añade la misma etiqueta a cada galaxia que pertenezca al conjunto; la unión queda alcanzable para las visitantes en `/tag/<tag-slug>` (tu operadora puede compartir el enlace).

Las etiquetas no crean ni modifican agujeros de gusano. Son puramente una disposición de visualización: en la vista de unión, la visitante ve los agujeros de gusano de todas las galaxias etiquetadas a la vez, pero cada agujero de gusano se queda en su galaxia de origen. Edita una galaxia, las otras quedan intactas.

## Retirar una galaxia

No hay un botón de "eliminar galaxia" para editoras en la configuración típica de una instancia; si genuinamente necesitas retirar una galaxia, pídele a tu operadora y lo arreglará. La razón de la fricción es editorial: una galaxia a la que se ha enlazado desde fuera (por un recorrido, por un portal, por una unión por etiqueta, por el favorito de una visitante) no desaparece sin más; el enlace se vuelve oscuro. La operadora puede decidir cómo manejar el enlace oscuro.

El patrón más común no es eliminar una galaxia sino volverla invisible para las visitantes manteniéndola del lado editorial, para que la decisión editorial pueda revertirse después.

## Cosas que vale la pena saber

- **No puedes mover una galaxia.** Una vez que una galaxia tiene un slug (la parte `/<nombre-corto>` de la URL), el slug es permanente. Renombrar la galaxia cambia el nombre mostrado pero no el slug. Si un cambio de slug es crítico, la operadora puede arreglarlo, pero la URL cambia para todas las personas con el enlace anterior.
- **El selector de galaxias agrupa las galaxias con el mismo prefijo `[entre corchetes]`.** Si tu instancia usa prefijos entre corchetes (`[mocambos] Galaxia A`, `[mocambos] Galaxia B`), el selector las agrupa visualmente. Los corchetes son una convención, no una característica; úsalos cuando agrupar ayude a tus editoras a encontrar galaxias relacionadas.
- **Se permite una galaxia con cero agujeros de gusano.** Las galaxias nuevas empiezan vacías y siguen siendo editables. No hay requisito de tener un número mínimo de agujeros de gusano antes de guardar.
- **El tema visual solo cambia la apariencia de la escena.** Cambiar de Cosmic a Tech no cambia lo que hay en la galaxia; cambia cómo se *dibujan* los agujeros de gusano. Prueba un tema; si no calza, vuelve.
