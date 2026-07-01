# Galaxias y cúmulos

Las pestañas **Galaxias** y **Cúmulos** son la vista de administración de todo el contenido de la instancia. Quien edita ve solo sus propias galaxias; tú ves cada galaxia, incluidas las importadas de otros sitios, y puedes agruparlas en cúmulos. Este capítulo cubre ambas pestañas.

## La pestaña Galaxias

![La pestaña Galaxias: una tabla de cada galaxia de la instancia con su cúmulo, su propietaria, y si está importada](assets/images/admin-manual-es/05-galaxies-list.png)

La pestaña Galaxias lista cada galaxia de la instancia, sin importar quién la hizo. De cada galaxia puedes ver a qué cúmulo pertenece (si a alguno), quién la posee, y si está **importada** de otra instancia. Desde aquí puedes llegar a los ajustes de una galaxia igual que lo haría su editora, y puedes mover una galaxia hacia dentro o fuera de un cúmulo.

La creación cotidiana de una galaxia (su tema, sus agujeros de gusano, sus palabras clave) es trabajo de edición y vive en el Manual del editor. Lo que es específico de ti como administración es la vista de toda la instancia: verlo todo a la vez, y las dos cuestiones de abajo, el contenido importado y los cúmulos.

## Galaxias importadas (de solo lectura)

Si tu instancia se suscribe a una galaxia publicada por otra instancia (consulta *Federación y el Pluriverse*), esa galaxia aparece aquí como **importada**. Una galaxia importada es una réplica: su contenido se copia a tu instancia para que quienes visitan puedan verlo, pero la autoridad sobre él se queda con la instancia que lo publicó.

- Las galaxias importadas son de **solo lectura** para todo el mundo en tu instancia, tanto para quien edita como para quien administra. No puedes cambiar su contenido, porque el cambio tiene que ocurrir en la fuente.
- Una acción **Refrescar** trae la última versión de una galaxia importada desde su fuente, para que tu réplica se ponga al día con las ediciones hechas aguas arriba. La federación también refresca las réplicas según un calendario; Refrescar es el botón manual de "ahora".
- Si la fuente deja de publicarte la galaxia, o dejas de suscribirte, la réplica se descarta. El contenido importado nunca fue tuyo para conservarlo; está presente solo mientras dura la suscripción.

El capítulo de federación cubre suscribirse, publicar y bloquear en detalle. Aquí basta con saber que las galaxias importadas aparecen en esta lista, son de solo lectura, y pueden refrescarse.

## La pestaña Cúmulos

Un **cúmulo** agrupa galaxias. Los cúmulos son como una familia de galaxias relacionadas se presenta junta y como algunos ajustes de la instancia se acotan a un subconjunto de galaxias en vez de a toda la instancia.

![La pestaña Cúmulos: una lista de cúmulos de galaxias, cada uno con las galaxias que contiene](assets/images/admin-manual-es/06-clusters-list.png)

Desde la pestaña Cúmulos puedes crear un cúmulo, nombrarlo, y meter galaxias en él. Una galaxia pertenece a lo sumo a un cúmulo a la vez. Los cúmulos le importan a la administración por dos razones:

- Son un nivel en la **cascada de edición** (consulta *Control de acceso de edición*): puedes apagar la edición de todo un cúmulo de una vez.
- Son un ámbito para el **emparejamiento de palabras clave**, más abajo.

El auto-registro también puede colocar automáticamente la galaxia personal de cada nueva persona editora en un cúmulo por instancia, para que todas las galaxias personales de una convocatoria abierta queden juntas en vez de dispersarse por la lista.

## Emparejamiento de palabras clave (exacto y aproximado)

Telaris traza conexiones entre agujeros de gusano que comparten una palabra clave. Por defecto el emparejamiento es **exacto**: dos agujeros de gusano se conectan solo cuando cargan exactamente la misma palabra. Puedes aflojarlo a un emparejamiento **aproximado**, para que grafías cercanas también se conecten: un plural y su singular, un pequeño error tipográfico, una variante menor.

El emparejamiento aproximado es un conmutador, y puede fijarse en dos ámbitos:

- para la **instancia entera** (el conmutador está en la pestaña Ajustes globales, consulta *Ajustes globales*), para que cada galaxia use emparejamiento aproximado, o
- para un **cúmulo** (en los propios ajustes de ese cúmulo), para que solo las galaxias de ese cúmulo lo hagan.

Está **apagado por defecto**; las conexiones se mantienen exactas hasta que lo enciendes. Un resguardo evita que el emparejamiento aproximado sobreconecte en palabras cortas muy comunes, así que encenderlo no inunda la red de enlaces espurios, pero sigue siendo un cambio que tus editoras verán (líneas de relación nuevas apareciendo entre palabras clave casi coincidentes entre galaxias). Enciéndelo cuando el vocabulario de tu contenido derive en la grafía y quieras que esas variantes se conecten; déjalo apagado cuando tus palabras clave estén controladas y quieras que solo las coincidencias exactas tracen una línea.

## Cosas que vale la pena saber

- **Tú lo ves todo; quien edita ve lo suyo.** La pestaña Galaxias es el único lugar con toda la instancia a la vista. Úsala para auditar qué existe, quién lo posee, y qué vino de fuera.
- **Lo importado no es tuyo.** Las galaxias importadas de solo lectura son una cortesía de otra instancia, presentes mientras dura la suscripción. No las trates como respaldo ni como tu contenido.
- **El emparejamiento aproximado es una elección editorial por instancia o por cúmulo**, no por agujero de gusano. Si tus editoras preguntan por qué las palabras clave casi coincidentes se conectan (o no), este conmutador es la respuesta.
