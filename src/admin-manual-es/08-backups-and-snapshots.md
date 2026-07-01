# Respaldos e instantáneas

Una instancia es contenido, y el contenido debería poder recuperarse. Telaris te da dos herramientas relacionadas: **respaldos** que descargas y conservas, e **instantáneas** que la instancia toma y almacena por ti, según un calendario si quieres. Este capítulo cubre ambas, y cómo restaurar.

## Respaldos (la pestaña Respaldo)

![La pestaña Respaldo: un panel de Descargar un respaldo y un panel de Restaurar desde un respaldo](assets/images/admin-manual-es/09-backup.png)

La pestaña **Respaldo** tiene dos mitades:

- **Descargar un respaldo** produce un único archivo que captura el contenido de la instancia, que tu navegador descarga. Guárdalo en un lugar seguro y fuera del servidor. Esta es la copia que tomas antes de cualquier cosa arriesgada, y la copia que usarías para mover una instancia o recuperarte de un servidor perdido.
- **Restaurar desde un respaldo** toma un archivo de respaldo y lo carga de vuelta en la instancia, reemplazando el contenido actual. Restaurar es destructivo para lo que hay ahora, así que Telaris confirma primero. Restaura sobre una instancia nueva o que se pretenda sobrescribir; no restaures sobre contenido que todavía quieres.

Un respaldo es portátil: puedes restaurarlo en otra instancia para clonar o migrar. Recuerda, de *Ajustes globales*, que la contraseña del correo nunca está en un respaldo; tras restaurar, vuelve a introducir los ajustes de correo para que la instancia restaurada pueda enviar.

## Instantáneas (la pestaña Instantáneas)

Donde un respaldo es un archivo que tú custodias, una **instantánea** es una copia que la instancia guarda por ti. La pestaña Instantáneas tiene tres partes:

- **Crear instantánea ahora** toma una instantánea a demanda. Hazlo antes de un cambio masivo o de cualquier edición de la que no estés segura, para que haya un punto reciente al que volver.
- **Programador de instantáneas** toma instantáneas automáticamente en un intervalo que fijas, y conserva un número rotatorio de ellas, para que siempre haya una instantánea reciente sin que tengas que acordarte de hacerla. Enciéndelo para cualquier instancia cuyo contenido importe.
- **Instantáneas disponibles** lista las instantáneas a mano, la más reciente primero, cada una restaurable en el sitio.

Las instantáneas son la red de seguridad de todos los días: baratas, frecuentes, y cerca. Los respaldos son el seguro fuera del sitio: menos, deliberados, y guardados lejos del servidor. Usa ambos, instantáneas para "deshacer", respaldos descargados para "el servidor se fue".

## Restaurar

Restaurar, ya sea desde un respaldo descargado o desde una instantánea almacenada, reemplaza el contenido actual con el contenido guardado. Como sobrescribe, trátalo como un acto meditado:

1. Asegúrate de que estás restaurando la versión que quieres. Las instantáneas llevan marca de tiempo; revisa la hora.
2. Entiende que las ediciones hechas desde ese punto se habrán ido tras la restauración.
3. Si tienes cualquier duda, descarga primero un respaldo del estado *actual*, para que incluso el estado que estás a punto de sobrescribir sea recuperable.

Cuando una restauración se completa, la consola lo confirma. Vuelve a iniciar sesión si la sesión se vio afectada, y revisa a ojo una galaxia para confirmar que el contenido es el que esperabas.

## El aviso de desajuste de esquema

Telaris mantiene la estructura de su base de datos al paso del código en ejecución automáticamente; cuando despliegas una versión nueva, la instancia pone su propia estructura al día por sí sola. Si el código y la estructura de la base de datos alguna vez discrepan de un modo que la instancia no puede reconciliar en silencio, la consola muestra un **aviso de desajuste de esquema**. Es una señal de que un despliegue no terminó con limpieza, no un estado rutinario. Si lo ves, la respuesta segura es asegurarte de que la instancia esté ejecutando la versión pretendida del código y dejar que complete su actualización de estructura; si persiste, ese es el momento de mirar el despliegue o preguntar a quien gestiona el servidor. No restaures un respaldo para "arreglar" un aviso de esquema; restaurar contenido no cambia el desajuste entre código y estructura.

## Cosas que vale la pena saber

- **Respalda antes de cualquier cosa irreversible.** Un cambio masivo, una restauración, una eliminación grande: toma una instantánea o descarga un respaldo primero. Cuesta segundos y salva el día que lo necesites.
- **Conserva al menos un respaldo fuera del servidor.** Una instantánea almacenada en el mismo servidor no ayuda si el servidor es lo que pierdes. Descarga un respaldo periódicamente y guárdalo en otro sitio.
- **La contraseña del correo no está en los respaldos ni en las instantáneas.** Tras restaurar o clonar, vuelve a introducir los ajustes de correo (*Ajustes globales*).
- **Prueba una restauración antes de depender de ella.** Si la recuperación importa, demuestra que un respaldo se restaura con limpieza en una instancia de repuesto una vez, en vez de descubrir un problema durante una recuperación real.
