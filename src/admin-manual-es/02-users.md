# Usuarias

La pestaña **Usuarias** es donde vive cada cuenta de la instancia. Este capítulo cubre las cuentas que creas tú; el siguiente cubre las cuentas que las personas crean por sí mismas mediante el auto-registro, que comparten la misma lista.

![La pestaña Usuarias: una tabla de cuentas con nombre, correo, rol, y acciones por fila](assets/images/admin-manual-es/02-users-list.png)

## La lista de cuentas

La lista muestra cada cuenta: administración y edición juntas. De cada cuenta ves su nombre, su dirección de correo, su rol, y, cuando corresponde, si ha sido verificada (el siguiente capítulo explica la verificación). Un recuento en el encabezado te dice cuántas cuentas existen.

Cada cuenta tiene un menú de acciones de fila para editarla y eliminarla, descrito abajo.

## Roles

Telaris tiene dos roles:

- **Edición.** Puede iniciar sesión y crear contenido, dentro del acceso que se le haya concedido (consulta *Control de acceso de edición*). No puede llegar a la consola de administración.
- **Administración.** Puede hacer todo lo que puede hacer quien edita, y puede llegar a la consola de administración. Concede este rol con moderación; toda persona que administra puede cambiar ajustes, leer cada cuenta, y eliminar contenido.

El rol de una cuenta se fija al crearla y puede cambiarse editando la cuenta.

## Crear una cuenta

Selecciona **Nueva cuenta**. Un formulario pide el nombre de la nueva cuenta, la dirección de correo, el rol y, opcionalmente, una contraseña.

- **Nombre** es cómo se muestra la persona, y cómo se nombran las galaxias propias de quien edita si usas las convenciones de nombre del siguiente capítulo.
- **Correo** es la identidad de la cuenta y la dirección a la que Telaris escribe (enlaces de acceso, notificaciones). Debe ser única en la instancia.
- **Rol** es edición o administración, como arriba.
- **Contraseña** es opcional. Si fijas una, la persona puede iniciar sesión con ella. Si la dejas en blanco, la cuenta inicia sesión con el enlace por correo sin contraseña que se describe abajo. Muchas personas que administran la dejan en blanco y dejan que la gente use enlaces por correo, así no hay contraseña que gestionar ni que se filtre.

Guarda, y la cuenta aparece en la lista de inmediato.

## Inicio de sesión sin contraseña

Las cuentas de Telaris no necesitan contraseña. Una cuenta sin contraseña inicia sesión pidiendo un enlace por correo: la persona introduce su correo en la página de inicio de sesión, Telaris le envía un enlace de un solo uso, y seguirlo la deja dentro. Es el mismo mecanismo que usa quien se auto-registra como editor.

Para que esto funcione, la instancia debe poder enviar correo. Si el correo no está configurado, los enlaces por correo no pueden entregarse y las cuentas sin contraseña no pueden iniciar sesión. El capítulo *Ajustes globales* cubre cómo configurar el correo y el aviso que muestra la consola cuando no está listo.

## Editar una cuenta

Abre el menú de acciones de una fila y elige **Editar** para cambiar el nombre, el correo, el rol, la contraseña, o el estado de verificación de una cuenta. Los cambios se guardan como una sola operación; si cambias varios campos a la vez, todos surten efecto juntos.

Cambiar el correo de una cuenta cambia la dirección a la que Telaris escribe y la identidad con la que la persona inicia sesión. Cambiar el rol de edición a administración concede acceso a la consola de inmediato; cambiarlo al revés lo quita.

## Importación masiva

Cuando necesitas crear muchas cuentas a la vez (una clase, una cohorte, un grupo de trabajo), usa la **importación masiva**. Toma una lista de cuentas, típicamente como un CSV con una columna por campo (nombre, correo, rol), y las crea en una sola pasada. Las cuentas cuyo correo ya existe se reportan en vez de duplicarse, así que volver a ejecutar una importación es seguro.

La importación masiva es la herramienta correcta para dar de alta a un grupo conocido. Para un grupo que no conoces de antemano (una convocatoria abierta a colaboradoras), el auto-registro, en el siguiente capítulo, encaja mejor.

## Eliminar una cuenta

Elige **Eliminar** en el menú de acciones de una fila. Telaris confirma primero, porque eliminar una cuenta es permanente.

Si la cuenta posee una **galaxia personal** (una galaxia creada para esa persona editora, según las convenciones de nombre del siguiente capítulo), Telaris pregunta qué hacer con ella: eliminar la galaxia junto con la cuenta, o conservar la galaxia y su contenido en su sitio. Eliminar la cuenta nunca borra contenido en silencio; siempre se te pregunta. Conserva la galaxia cuando el contenido deba sobrevivir al acceso de la persona; elimínala cuando la cuenta y su galaxia fueran un único desechable (una cuenta de prueba, una demostración de curso).

## Cosas que vale la pena saber

- **No hay forma de ver una contraseña.** Las contraseñas se almacenan de modo que ni siquiera tú puedes leerlas de vuelta. Si alguien olvida la suya, o bien la borras (para que use enlaces por correo) o fijas una nueva; no puedes recuperar la antigua.
- **Quien administra puede ver cada cuenta y cada galaxia.** La privacidad que acota a quien edita a su propio trabajo no te aplica. Trata la lista, y el contenido detrás de ella, con la discreción que ese acceso implica.
- **Eliminar la última cuenta de administración te dejaría fuera.** Telaris no dejará la instancia sin administración; conserva al menos una cuenta de administración con la que puedas iniciar sesión antes de eliminar otras.
