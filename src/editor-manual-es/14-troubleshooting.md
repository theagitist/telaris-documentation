# Resolución de problemas

Las situaciones cotidianas con las que se encuentra una editora, qué intentar, y cuándo hablar con tu operadora. Este capítulo está organizado por el síntoma, no por la causa; busca lo que *tú* ves, no lo que *técnicamente* está pasando.

## No puedo iniciar sesión

**Lo que ves**: el formulario de inicio de sesión rechaza tus credenciales, o llegas a la página de inicio de sesión cuando esperabas estar ya conectada.

**Qué intentar**, en orden:

1. Confirma que la dirección de correo y la contraseña son correctas. Ambas distinguen mayúsculas y minúsculas.
2. Si tu cuenta no tiene contraseña, usa el botón **Envíame un enlace de acceso**: escribe tu correo, selecciónalo, y abre el enlace que llega a tu bandeja de entrada.
3. Si tienes contraseña y la olvidaste, abre la sección **Tengo contraseña** y usa el enlace **¿Olvidaste la contraseña?** debajo del botón **Iniciar sesión**. En menos de un minuto llega un correo con un enlace de restablecimiento.
4. Comprueba que estás en la dirección de tu instancia. Si tu operadora corre varias instancias, tu inicio de sesión está acotado a una.

**Cuándo preguntar a tu operadora**: si el enlace de restablecimiento no llega (revisa primero el spam), si tu correo de restablecimiento rebota, o si estás segura de que la contraseña es correcta y el formulario sigue rechazándola.

## Un agujero de gusano que creé desapareció

**Lo que ves**: un agujero de gusano que escribiste ya no está en la lista de agujeros de gusano.

**Qué intentar**:

1. Confirma que el desplegable **Galaxia actual** está en la galaxia correcta (o fijado en *Todas mis galaxias*). El agujero de gusano puede estar en una galaxia distinta a la que esperas, sobre todo si usaste el desplegable Galaxia dentro del modal del agujero de gusano.
2. Usa el cuadro de búsqueda en el inicio del editor. Busca por el nombre del agujero de gusano; si existe en cualquier galaxia que puedas editar, la búsqueda lo encuentra.
3. Confirma que estás en la pestaña **Agujeros de gusano**, no en la pestaña Plantillas ni en la de Contenido hotglue; la lista de agujeros de gusano solo se muestra bajo la primera pestaña.

**Cuándo preguntar a tu operadora**: si la búsqueda en Todas mis galaxias no devuelve nada y estás segura de que guardaste el agujero de gusano. El agujero de gusano puede haber sido eliminado (por ti, o por otra editora); tu operadora puede ser capaz de restaurarlo desde una instantánea.

## No puedo editar un agujero de gusano; el modal abre en modo visor

**Lo que ves**: hacer clic en una fila de agujero de gusano abre una ficha o una vista previa de solo lectura, no el modal de edición.

**Lo que podrías estar viendo**:

- El agujero de gusano está en una galaxia a la que tienes **acceso de lectura** pero no de edición (algunas instancias permiten a las editoras ver todas las galaxias pero solo editar algunas). El agujero de gusano es editable por otra editora.
- El agujero de gusano fue **importado** desde una fuente externa (un archivo hermano, una comunidad enlazada por bridge). Los agujeros de gusano importados son de solo lectura por diseño; los cambios deben ocurrir en la fuente.

**Cuándo preguntar a tu operadora**: si el agujero de gusano fue creado en esta instancia y deberías tener derechos de edición pero el modal sigue abriendo de solo lectura.

## Una subida falla

**Lo que ves**: el selector de archivo acepta el archivo, la subida empieza, luego aparece un error o el modal se cierra sin el archivo adjunto.

**Qué intentar**:

1. Revisa el tamaño del archivo. Los PDF suelen estar topados en 25 MB (tu operadora puede haber fijado otro tope); las imágenes y los videos pueden tener sus propios límites.
2. Revisa el tipo de archivo. Telaris soporta JPG y PNG (y la mayoría de otros formatos comunes) para imágenes; MP4 para video; MP3, OGG, y WAV para audio; PDF para documentos. Archivos de otros tipos son rechazados al momento de subir.
3. Prueba un archivo más pequeño o un formato distinto. Si el original es demasiado grande, comprime o transcodifica antes de subir.

**Cuándo preguntar a tu operadora**: si las subidas fallan consistentemente con archivos dentro de los límites declarados, o si necesitas que se suba el límite.

## La píldora de una palabra clave está en el lugar equivocado del lienzo

**Lo que ves**: una píldora en el lienzo de palabras clave se solapa con otra, está fuera del área visible, o flota en una posición que no coincide con donde recuerdas haberla puesto.

**Qué intentar**:

1. Arrastra la píldora a donde la quieres; la nueva posición se guarda automáticamente.
2. Si muchas píldoras están mal dispuestas, usa la opción **Restablecer todas las posiciones de las fichas** en la capa de ayuda del lienzo (el **?** en la parte superior).
3. Recarga la página; el lienzo vuelve a traer la última disposición.

**Cuándo preguntar a tu operadora**: rara vez. El lienzo es indulgente; casi todo problema se resuelve arrastrando.

## Un cambio que hice no aparece en la vista de visitante

**Lo que ves**: guardaste un cambio en el editor, pero una visitante (o tú en otra pestaña) no lo ve.

**Qué intentar**:

1. Recarga la pestaña de visitante. Telaris no empuja actualizaciones en vivo; el cambio aparece en la próxima recarga.
2. Comprueba que guardaste con el botón de guardar del modal, no que cerraste el modal con **Cancelar** o haciendo clic fuera.
3. Comprueba que estás mirando la misma galaxia. La pestaña de visitante puede estar en una galaxia distinta a la que editaste.

**Cuándo preguntar a tu operadora**: si guardaste y recargaste y el cambio sigue sin ser visible tras un minuto. Las cachés de borde pueden tardar un instante en invalidarse; si persiste, eso es territorio de operadora.

## Un botón está atenuado

**Lo que ves**: un botón en el inicio del editor o en un modal está visible pero no es cliqueable.

**Lo que podrías estar viendo**:

- El botón está **condicionado a algo que aún no has hecho**. Por ejemplo, el botón Ajustes junto al selector de galaxia solo se habilita cuando hay una galaxia específica seleccionada (no *Todas mis galaxias*).
- El botón está **acotado por tu rol**. Si eres editora y la acción es solo para administradoras, el botón puede aparecer pero quedar deshabilitado.

**Cuándo preguntar a tu operadora**: si crees que deberías tener acceso a la acción y el botón sigue deshabilitado. Tu rol puede necesitar ajuste.

## Mi sesión expiró a mitad de edición

**Lo que ves**: un guardado falla con un mensaje de "unauthenticated" o "please log in"; el editor te devuelve a la página de inicio de sesión.

**Qué intentar**:

1. Vuelve a iniciar sesión. Tu sesión expira periódicamente; esto es normal.
2. Si estabas editando un agujero de gusano cuando la sesión expiró y el cambio no se guardó, puedes haber perdido trabajo desde el último guardado. El texto en el modal a veces es recuperable a través del comportamiento de restauración de formularios del navegador; si no, el agujero de gusano vuelve a su último estado guardado.

**Cuándo preguntar a tu operadora**: si las sesiones expiran inusualmente rápido. La sesión por defecto dura 30 días con renovación por actividad; si te expulsa en minutos, algo está mal.

## Un mensaje que envié a otra editora parece perdido

**Lo que ves**: enviaste un mensaje dentro de la aplicación a otra editora (o a la operadora de una instancia) y la persona destinataria no ha respondido, o no encuentras el mensaje enviado.

**Lo que podrías estar viendo**:

- La persona destinataria aún no ha abierto la bandeja de entrada.
- La superficie de mensajería dentro de la aplicación puede vivir en una sección de la interfaz de administración a la que no tienes acceso. La mayor parte de la comunicación entre editoras se maneja mejor fuera de Telaris (correo, Signal, lo que tu operadora y tu equipo hayan acordado).

**Cuándo preguntar a tu operadora**: si la mensajería dentro de la aplicación es el canal canónico en tu instancia y un mensaje que enviaste por ahí no llega a la persona destinataria.

## Un agujero de gusano abre con la ficha en blanco

**Lo que ves**: hacer clic en un agujero de gusano abre la ficha pero sin descripción, sin medios, sin palabras clave.

**Qué intentar**:

1. Comprueba que el agujero de gusano que abriste es el que querías escribir contenido para. Los agujeros de gusano vacíos están permitidos; simplemente no tienen cuerpo.
2. Abre el agujero de gusano en el editor y confirma que el campo Descripción tiene el texto que esperas.
3. Si la descripción aparece en el editor pero no en la vista de visitante, recarga ambas pestañas del navegador.

**Cuándo preguntar a tu operadora**: si el agujero de gusano tiene contenido en el editor pero está en blanco en la vista de visitante después de recargar.

## La escena 3D está lenta o se traba

**Lo que ves**: la escena 3D de la visitante tarda mucho en cargar, anima a tirones, o se congela brevemente.

**Lo que podrías estar viendo**:

- Una galaxia densa en un dispositivo antiguo. La escena 3D corre en el navegador de la visitante; las galaxias muy densas son exigentes con hardware de menor potencia.
- Una galaxia con muchos agujeros de gusano iconizados por imagen (cada imagen se representa en la escena como una textura).

**Qué intentar**:

- Sugiere a la visitante que use el conmutador **vista 2D** (capítulo 10) si está habilitado en la galaxia.
- Para las galaxias que escribes, considera si todas las marcas de imagen-como-icono son necesarias; una galaxia con doce agujeros de gusano iconizados por imagen es más rápida que una con cincuenta.

**Cuándo preguntar a tu operadora**: si la lentitud es universal (cada visitante la ve) y no es específica de un dispositivo.

## No sé quién opera esta instancia

**Lo que ves**: este manual te sigue diciendo "pregúntale a tu operadora". Si no sabes quién es, necesitas saberlo.

**Qué intentar**:

- Revisa la dirección de tu instancia. Muchas instancias tienen una página de contacto en `/contact` o una página de gobernanza en `/governance` que nombra a quien opera.
- Mira el correo original que te invitó a ser editora. Quien envía es por lo general quien opera.
- Si nada más funciona, la siguiente editora o visitante con quien hables sobre Telaris probablemente sepa.

Si no puedes identificar a quien opera en absoluto, eso es en sí mismo una especie de problema que vale la pena resolver; una instancia sin una operadora alcanzable es una que deriva.
