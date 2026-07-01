# Ajustes globales

La pestaña **Ajustes globales** contiene los interruptores de toda la instancia: cómo se llama la instancia, qué galaxia recibe a quien visita, qué tan grande puede ser una subida, cómo coinciden las palabras clave, cómo envía correo, en qué dirección responde, a qué idioma recurre por defecto, y si la edición está habilitada siquiera. Estos ajustes se guardan en la base de datos propia de la instancia, así que los cambias aquí en la consola en vez de editando archivos en el servidor.

![La pestaña Ajustes globales: el nombre de la instancia, la galaxia predeterminada, el límite de subida, el conmutador de coincidencia aproximada, y (más abajo) los ajustes de correo y del sitio](assets/images/admin-manual-es/07-global-settings.png)

## Aspectos básicos de la instancia

La parte superior de la pestaña reúne los datos simples de la instancia:

- **Nombre.** El nombre público de la instancia. Aparece del lado visitante y se convierte en la etiqueta de la instancia en el directorio del Pluriverse si solicitas publicar (capítulo 7). En blanco, toma por defecto la primera parte del nombre de host.
- **Galaxia predeterminada.** Qué galaxia ve quien visita en la raíz del sitio, antes de elegir una. Elige la galaxia que debería ser la puerta de entrada.
- **Tamaño máximo de PDF (MB).** El PDF más grande que puede llevar un agujero de gusano, en megabytes (25 por defecto). A quien edita y sube un archivo mayor se le avisa que el archivo supera el límite. Súbelo si tu contenido lo necesita y tu servidor tiene espacio.
- **Coincidencia aproximada de palabras clave.** El conmutador de toda la instancia para la coincidencia flexible descrita en *Galaxias y cúmulos*: cuando está encendido, las grafías cercanas conectan entre galaxias, no solo las palabras idénticas. Apagado por defecto. Un cúmulo puede anular este valor en sus propios ajustes.


## Ajustes de correo

Casi todo lo que Telaris envía por correo, enlaces de acceso, confirmaciones de registro, notificaciones, depende de que la instancia pueda enviar correo. El formulario de ajustes de correo es donde configuras eso:

- **Host SMTP** y **Puerto** de tu relé de correo.
- **Usuario** y **Contraseña** del relé.
- **Cifrado** (típicamente TLS).
- **Dirección de remitente** y **Nombre de remitente** que ven las personas destinatarias.

Dos ayudas acompañan al formulario:

- Un botón **Enviar correo de prueba** manda un mensaje de prueba a una dirección que le indiques, para que confirmes que los ajustes funcionan antes de depender de ellos.
- Un **aviso de no configurado**. Mientras el correo no está listo, la consola muestra un aviso, y los lugares que dependen del correo (los ajustes de auto-registro, por ejemplo) lo repiten, porque encender una función que necesita correo mientras el correo está roto solo produce fallos silenciosos.

Si el correo no está configurado, las cuentas sin contraseña no pueden iniciar sesión y el auto-registro no puede funcionar, porque ambos dependen de enlaces enviados por correo. Configura el correo antes de encender cualquiera de los dos.

> [!important] La contraseña del correo es el único secreto aquí
> La contraseña de SMTP es el único valor sensible en estos ajustes. Telaris la trata de forma especial: nunca se incluye en ningún respaldo, instantánea, o exportación de federación. Esto significa que es seguro compartir un respaldo, pero también que restaurar una instancia en otro sitio no llevará la contraseña; la vuelves a introducir después de una restauración. El capítulo *Respaldos e instantáneas* vuelve sobre esto.

## Ajustes del sitio

Estos le dicen a la instancia sobre sí misma:

- **Nombre de host público** y **URL base**: la dirección en la que se alcanza la instancia. Telaris los usa para construir los enlaces que pone en los correos, para que apunten al lugar correcto sin importar cómo llegó una petición dada. Fíjalos en tu dirección pública real.
- **Idioma predeterminado**: el idioma que ve quien visita antes de cualquier elección propia, uno de inglés, español, portugués o francés. Fíjalo en el idioma de tu público.

Fijar aquí el nombre de host y la URL base significa que no tienes que editar a mano archivos de configuración para que los enlaces de correo sean correctos; la consola es la fuente de verdad para ellos.

## Los interruptores de la instancia

Un interruptor aquí decide una función entera de la instancia:

- **Permitir edición.** El extremo a nivel de instancia de la cascada de edición (consulta *Control de acceso de edición*). Apágalo para congelar toda la edición de la instancia de una vez, por ejemplo cuando un proyecto ha terminado, conservando cada cuenta y todo lo creado. Encendido por defecto.

## Cosas que vale la pena saber

- **Estos ajustes viven en la base de datos, no en un archivo.** Cambiarlos aquí surte efecto sin tocar el servidor. También anulan los valores de reserva grabados en el archivo de configuración de la instancia, así que la consola es donde deberías cambiarlos.
- **Prueba el correo tras cualquier cambio.** El botón Enviar correo de prueba existe para que nunca descubras un relé roto a través de una persona editora que no pudo iniciar sesión. Úsalo siempre que toques los ajustes de correo.
- **La dirección de remitente debería ser una dirección real y con permiso de envío en tu dominio.** Los relés y las personas destinatarias rechazan cada vez más el correo cuya dirección de remitente no está autorizada a enviar; fíjala en algo que tu relé tenga permitido usar como remitente.
