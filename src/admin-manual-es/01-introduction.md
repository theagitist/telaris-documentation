# Introducción

Este manual es para quien opera una instancia de Telaris: la administración. Administrar no es lo mismo que editar. Quien edita crea galaxias, agujeros de gusano y conexiones dentro del archivo; quien administra decide quién puede editar, cómo se comporta la instancia, si se conecta a otras instancias y cómo, y cómo se mantienen a salvo sus datos. Si tu trabajo diario es crear contenido, tu libro es el Manual del editor; este es para las superficies que quien edita nunca ve.

## Tres roles

Conviene mantener tres roles distintos, porque este manual, el Manual del editor, y el día a día de operar una red de Telaris le hablan cada uno a uno diferente.

- **Edición.** Alguien con una cuenta de edición en tu instancia. Inicia sesión, crea contenido, y solo ve la superficie de edición. El Manual del editor está escrito para esa persona.
- **Administración (tú).** Alguien con una cuenta de administración en tu instancia. Tú llegas a la **Consola de administración** y gestionas cuentas, galaxias, ajustes, respaldos, y la participación de tu instancia en la red más amplia. Este manual está escrito para ti.
- **Operación del Pluriverse.** Quien opera el sitio central de coordinación (el Pluriverse) por el que se federa una familia de instancias. Buena parte de ese trabajo es la misma consola de administración que ya conoces; las partes específicas de operar el Pluriverse se reúnen en el capítulo de federación. En una red pequeña, quien administra y quien opera el Pluriverse suelen ser la misma persona.

Una sola cuenta puede, por supuesto, ser a la vez de edición y de administración. La distinción es de *superficies*, no de personas: la consola de administración es un lugar aparte del inicio del editor, se alcanza por separado, y este manual es tu guía para ella.

## Llegar a la Consola de administración

La Consola de administración vive en la ruta `/admin` de tu instancia (por ejemplo, `https://tu-instancia.ejemplo.org/admin`). Debes haber iniciado sesión con una cuenta que tenga el rol de administración; una cuenta de edición ordinaria que abra `/admin` es rechazada.

A lo largo de la parte superior de la consola hay una fila de pestañas. Cada una es un capítulo de este manual:

- **Galaxias** y **Cúmulos**: la vista de administración de todo el contenido de la instancia, incluido el contenido importado de otros sitios. Se cubre en *Galaxias y cúmulos*.
- **Usuarias**: cada cuenta de la instancia, y las herramientas para crearlas, editarlas, verificarlas y eliminarlas. Se cubre en *Usuarias* y *Auto-registro de editores*.
- **Respaldo** e **Instantáneas**: hacer y restaurar copias de toda la instancia. Se cubre en *Respaldos e instantáneas*.
- **Ajustes globales**: el correo, la dirección propia de la instancia, el idioma predeterminado, y el interruptor de toda la instancia para la edición. Se cubre en *Ajustes globales*.
- **Pluriverse**: la participación de tu instancia en una federación de instancias. Se cubre en *Federación y el Pluriverse*.
- **Llaves de API** e **Información de PHP**: cabos operativos sueltos y diagnósticos. Se cubre en *Mantenimiento y diagnósticos*.

## Qué asume este manual

Asume que la instancia ya está instalada y funcionando, y que puedes iniciar sesión como administración. No cubre instalar Telaris en un servidor desde cero; eso depende del método de despliegue que elegiste (un checkout directo, una imagen de contenedor, o una instancia alojada aprovisionada para ti), y el README del repositorio de código es la referencia para ello. Lo que este manual cubre es todo lo que haces *después* de que la instancia está en marcha: operarla bien, mantenerla a salvo, y decidir qué tan abierta es.

## Una nota sobre el idioma y los términos

La consola, como el resto de Telaris, está completamente traducida. Las pantallas que se muestran aquí están en inglés; tu consola puede estar en español, portugués o francés, y las etiquetas cambian en consecuencia. Cuando este manual nombra un control, nombra la etiqueta en español; encuentra el mismo control en tu propio idioma por su posición, que es la misma en cada idioma.

Telaris también mantiene una separación deliberada entre las palabras que leen quienes visitan y editan y las palabras que usa el código. Verás *galaxia*, *agujero de gusano* y *portal* en la interfaz; los datos subyacentes los llaman *constellation*, *node* y *portal*. Este manual usa las palabras de la interfaz en todo momento. El glosario del final reúne los términos con los que se topa quien administra.
