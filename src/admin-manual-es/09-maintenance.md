# Mantenimiento y diagnósticos

Este capítulo reúne los cabos operativos sueltos: las pestañas **Llaves de API** e **Información de PHP**, cómo mantiene la instancia al día la estructura de su propia base de datos, y dónde viven los pocos ajustes a nivel de archivo. Visitarás estos rara vez, que es precisamente por lo que ayuda saber qué son antes de necesitarlos.

## Llaves de API

La propia interfaz de la instancia lee el contenido a través de una API interna, y esa API está protegida por una llave. La pestaña **Llaves de API** es donde se gestionan esas llaves: puedes ver las llaves que existen y generar una nueva.

Para una instancia que se configuró de forma normal, ya existe una llave predeterminada y todo funciona; nunca necesitas esta pestaña. Importa en dos situaciones:

- **Una instancia aprovisionada a mano sin llave.** Si una instancia se configuró a mano en vez de mediante la configuración normal, puede que no tenga llave predeterminada, y la escena de visitante o las vistas de administración fallan al cargar contenido (un error de "no se pudo cargar"). Generar una llave aquí lo arregla.
- **Rotar una llave.** Si una llave debe reemplazarse, genera una nueva aquí.

Salvo que estés resolviendo uno de esos problemas, deja esta pestaña en paz.

## Información de PHP

La pestaña **Información de PHP** reporta el entorno del servidor en el que corre la instancia: la versión de PHP, qué extensiones importantes están presentes, y la lista completa de extensiones cargadas. Es un diagnóstico de solo lectura. Su propósito es responder, rápido, "¿tiene este servidor lo que Telaris necesita?" cuando algo se comporta de forma extraña, sin que inicies sesión en el servidor mismo. Si alguna vez reportas un problema a quien gestiona el servidor, la información de versión y de extensiones de aquí es lo que te pedirán.

## Cómo la estructura de la base de datos se mantiene al día

Telaris gestiona la estructura de su propia base de datos. Cuando la instancia corre una versión del código más nueva que aquella para la que se preparó la base de datos por última vez, pone la estructura al día por sí sola, añadiendo lo que la versión nueva necesita, la primera vez que se necesita. No hay un paso aparte de "ejecutar las migraciones" que tengas que realizar tras un despliegue; la instancia lo maneja.

Por esto desplegar una actualización es, en el caso normal, solo poner el código nuevo en su sitio; la instancia hace el resto en la siguiente petición. El **aviso de desajuste de esquema** (consulta *Respaldos e instantáneas*) es la excepción, la señal de que esta autoactualización no se completó, y el resto de ese capítulo cubre lo que significa.

## Los pocos ajustes a nivel de archivo

Casi todo lo que la administración fija vive en la consola y en la base de datos, que es donde deberías fijarlo. Un pequeño número de valores fundacionales, principalmente la conexión de base de datos que usa la instancia, viven en un archivo de configuración en el servidor en vez de en la consola, porque la instancia los necesita antes de poder llegar a su propia base de datos para leer cualquier otra cosa. Normalmente no tocarás ese archivo; se fija una vez cuando se instala la instancia. Los ajustes que *sí* cambias día a día, el correo, la dirección de la instancia, el idioma predeterminado, el interruptor de edición, están todos en *Ajustes globales*, en la consola, precisamente para que no tengas que editar archivos para operar la instancia.

Si no instalaste la instancia tú misma y algo a este nivel parece estar mal (la instancia no puede llegar a su base de datos, o los enlaces de correo apuntan a la dirección equivocada), ese es el punto para involucrar a quien montó el servidor, o para consultar la referencia de instalación propia del repositorio de código.

## Cosas que vale la pena saber

- **La mayoría de estas pestañas son "por si acaso", no "de todos los días".** Llaves de API e Información de PHP son superficies de resolución de problemas; una instancia sana rara vez necesita cualquiera de las dos.
- **Desplegar es poner el código nuevo en su sitio; la instancia actualiza su propia estructura.** No ejecutas migraciones a mano.
- **La consola es el lugar para los ajustes, no los archivos.** Si te encuentras queriendo editar un archivo para cambiar cómo se comporta la instancia, revisa *Ajustes globales* primero; el ajuste probablemente esté ahí.
