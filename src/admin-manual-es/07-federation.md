# Federación y el Pluriverse

Las instancias de Telaris pueden ir solas, o pueden unirse a una **federación**: una familia de instancias independientes que pueden ver y compartir las galaxias de las demás sin que ninguna esté al mando. Este capítulo cubre el lado de tu instancia en eso, y, para quien opera el sitio de coordinación, la superficie extra que viene con ello.

La federación es opcional. Muchas instancias nunca la encienden, y un curso o un archivo personal rara vez la necesita. Acude a este capítulo cuando quieras que tu instancia forme parte de una red más amplia de instancias de Telaris.

## La forma de esto

Una federación la coordina un **Pluriverse**: un sitio central que mantiene el directorio de instancias miembro y las ayuda a encontrarse y confiar entre sí. El Pluriverse es una coordinación, no una propiedad; no guarda el contenido de nadie, y ninguna instancia le responde por decisiones editoriales. Cada instancia sigue siendo soberana sobre sus propias galaxias.

Entre dos instancias, el compartir funciona en una dirección a la vez:

- una instancia **publica** una galaxia a un par en el que confía, y
- el par **se suscribe** y trae una **réplica de solo lectura** de esa galaxia (las galaxias importadas del capítulo anterior).

Nada se comparte hasta que existen tanto una relación de confianza como una decisión de publicar. La federación es de adhesión voluntaria en cada paso: eliges unirte, eliges en quién confías, eliges qué publicar, y puedes retirar cualquiera de ello.

## Unirse a un Pluriverse

La participación de tu instancia se gestiona desde la pestaña **Pluriverse** de la consola. Unirse es un flujo de solicitud y admisión: tu instancia solicita entrar a un Pluriverse, y quien opera ese Pluriverse la admite. Una vez admitida, tu instancia aparece en el directorio y puede empezar a formar confianza con pares.

![La pestaña Pluriverse en una instancia aún no federada: el formulario para unirse al Pluriverse con la URL, el nombre y el contacto de operación de la instancia](assets/images/admin-manual-es/08-pluriverse.png)

## La lista de pares

La pestaña Pluriverse muestra los pares que tu instancia conoce, cada uno con su estado: descubierto (conocido pero aún sin confianza), de confianza (existe una relación de confianza mutua), o bloqueado. Una acción **Actualizar ahora** actualiza la lista desde el Pluriverse en el momento, en vez de esperar a la actualización programada. También hay un camino avanzado para añadir un par a mano, para un par que conoces directamente, que te pide reconfirmar porque añadir un par a mano se salta la presentación del directorio.

## Establecer confianza

Antes de que dos instancias puedan compartir, establecen **confianza**: un apretón de manos en el que cada una confirma la identidad de la otra y ambas acuerdan ser pares. Inicias o aceptas un apretón de manos desde la lista de pares; cuando se completa, el estado del par pasa a de confianza (en lista blanca) en ambos lados. La confianza es mutua y simétrica; no comparte, por sí misma, ningún contenido. Solo hace posible el compartir.

## Publicar tus galaxias

Para dejar que un par de confianza replique una de tus galaxias, se la **publicas**. Publicar es por galaxia y por par: decides, para cada par, cuáles de tus galaxias puede traer. Una galaxia que no has publicado es invisible para los pares, incluso los de confianza.

Publicar comparte el contenido de la galaxia, incluidos sus medios, en una forma que el par puede verificar que vino de ti sin alterar. Puedes **retractar** una publicación más tarde; la réplica del par se descarta entonces en su siguiente traída. Publicar es una oferta permanente, no un envío único: mientras se mantiene, la réplica del par se pone al día con tus ediciones.

## Suscribirse a las galaxias de un par

La otra dirección: cuando un par de confianza te publica una galaxia, puedes **suscribirte** a ella y traer una réplica de solo lectura. La réplica aparece en tu pestaña Galaxias como una galaxia importada (capítulo anterior), de solo lectura, refrescable. Puedes cancelar la suscripción para descartar la réplica. A lo que puedes suscribirte es a lo que tus pares hayan elegido publicarte; no puedes traer una galaxia que no se te ha publicado.

## Bloquear a un par

Si necesitas cortar una relación, **bloquea** al par. El bloqueo es la parada fuerte: descarta cualquier réplica que trajiste de él, retira cualquier cosa que le publicaste, y detiene el compartir en ambas direcciones. El bloqueo es deliberadamente uniforme, no deja contenido a medio compartir, así que es la forma limpia de terminar una relación que ha ido mal. Desbloquear más tarde devuelve al par a meramente descubierto; no restaura el contenido que el bloqueo descartó, que tendría que volver a publicarse y volver a traerse.

## Para quien opera el Pluriverse

Si operas el sitio de coordinación en vez de solo una instancia miembro, tienes una responsabilidad extra: la **admisión**. Nuevas instancias solicitan entrar a tu Pluriverse, y tú decides cuáles admitir en el directorio. La admisión es un paso de verificación; estás decidiendo quién pertenece a esta federación en particular. La superficie de la consola para ello te deja revisar una solicitud pendiente y admitirla o declinarla. Más allá de la admisión, quien opera mantiene el directorio honesto: eliminando una instancia que ha quedado permanentemente en silencio, y respondiendo si una instancia miembro reporta un problema con un par.

Operar un Pluriverse no te da poder sobre el contenido ni las decisiones editoriales de las instancias miembro. Te da la lista de invitadas, no el archivo.

## Cosas que vale la pena saber

- **La federación es enteramente voluntaria y reversible.** Te unes por elección, confías por elección, publicas por elección, y puedes retirarte en cada nivel. Nada se federa por defecto.
- **Las galaxias importadas son de solo lectura e impermanentes** (capítulo anterior). Trata la galaxia publicada de un par como una vista en vivo, no como tu copia.
- **El bloqueo es uniforme y definitivo para el contenido que descarta.** Es la herramienta correcta para terminar una mala relación con limpieza; no es una pausa. Usa la confianza y publicar/retractar para ajustes más suaves.
- **La soberanía es de lo que se trata todo esto.** Ninguna instancia, ni el Pluriverse, anula las decisiones editoriales de otra. El único poder que una fuente tiene sobre una réplica es dejar de publicar; el único poder que tú tienes sobre lo que importaste es dejar de suscribirte.
