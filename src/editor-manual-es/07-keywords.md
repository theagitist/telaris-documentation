# Palabras clave

Las palabras clave son etiquetas cortas que adjuntas a los agujeros de gusano. Son como Telaris conecta contenido sin carpetas. Una palabra clave es la diferencia entre una galaxia que es una *lista* y una galaxia que es una *red*; todo lo demás, en el día a día de la editora, se construye encima.

Este capítulo cubre cómo asignar palabras clave desde dentro del modal del agujero de gusano, la paleta de píldoras, y cómo trabajar con muchos agujeros de gusano a la vez. El **lienzo** de palabras clave (la superficie relacional de dibujo) tiene su propio capítulo (8).

## Asignar palabras clave

Las palabras clave se asignan dentro del modal del agujero de gusano, en el campo **Palabras clave** junto al nombre del agujero de gusano (ver el capítulo 5 para el modal completo). El campo es una entrada de píldoras:

- Escribe una palabra clave y presiona **Enter** o **coma** para añadirla como píldora.
- Haz clic en la **×** de una píldora para eliminarla.
- La misma palabra clave puede añadirse en cualquier caja; Telaris empareja sin distinguir mayúsculas, así que *native* y *Native* son la misma palabra clave.

A medida que escribes, aparecen sugerencias:

- Las palabras clave ya usadas en **esta galaxia** aparecen primero.
- Las palabras clave usadas en **galaxias hermanas** (galaxias que comparten el prefijo `[entre corchetes]` de tu galaxia actual) aparecen después.
- Otras palabras clave recientes aparecen al final.

Aceptar una sugerencia es lo mismo que escribir la palabra completa. Telaris no requiere que uses las sugerencias; siempre puedes escribir una palabra clave fresca, en cuyo caso la nueva palabra clave se incorpora a la galaxia.

## Elegir bien las palabras clave

La decisión más importante sobre palabras clave es **cuán pocas usar**. Un agujero de gusano etiquetado con tres palabras clave cuidadosamente elegidas es más legible que uno etiquetado con veinte. Cada palabra clave que añades es una conexión a todos los demás agujeros de gusano que cargan la misma palabra; si la conexión no es significativa, el camino de la visitante por la galaxia se vuelve más ruidoso.

Algunas reglas prácticas:

- **Una por cualidad que el agujero de gusano realmente encarne**. *Native* en una planta que es nativa; *edible* en una que de verdad se come. No *plant* en cada agujero de gusano de una galaxia de plantas; esa palabra clave no carga señal.
- **Reusa antes de inventar.** Cuando dos editoras describen la misma idea con palabras distintas (*medicinal* y *healing*), el enlace conceptual se vuelve oscuro. Mira el autocompletado; si ya existe una palabra cercana a la tuya, prefiérela.
- **Evita palabras clave que nunca buscarías.** Una palabra clave que nadie (visitante o editora) escribiría en un cuadro de búsqueda es una que no hace trabajo.

No hay cola de revisión ni vocabulario central. Cada editora decide las palabras clave de cada agujero de gusano; el sistema confía en ti. El capítulo 13 habla en detalle de la soberanía editorial.

## La paleta de píldoras

Cada palabra clave recibe un color pastel determinista, elegido por el texto de la palabra clave. El color es el **mismo** para esa palabra en cada galaxia de tu instancia: las visitantes que aprenden que *native* es la píldora verdosa en una galaxia la reconocerán al instante en otra.

Por esto también renombrar una palabra clave cambia el color: el color está vinculado al texto, no a un id interno. Si renombras *medicinal* a *healing*, el color de la píldora cambia. (En la práctica: renombra pocas veces; la fusión es una operación más limpia.)

## Editar palabras clave en un agujero de gusano existente

Abre el modal Editar del agujero de gusano (capítulo 5). El campo Palabras clave muestra las píldoras existentes. Añade píldoras como arriba; quita con la ×; guarda. Los cambios se aplican en la próxima recarga de página de la visitante.

## Actuar sobre muchos agujeros de gusano a la vez

Para encontrar y actuar sobre cada agujero de gusano que carga una palabra clave dada, escribe la palabra clave en el cuadro de búsqueda del inicio del editor. La lista se acota a los agujeros de gusano que coinciden, y puedes abrir el menú de acciones de cada uno para editarlo, moverlo (cambiando su galaxia en el modal Editar) o eliminarlo. Buscar primero, luego actuar por agujero de gusano, te mantiene mirando exactamente lo que estás a punto de cambiar, en vez de disparar una única acción global contra un conteo que no puedes ver.

## Alias (sinónimos por galaxia)

El modelo de palabras clave de Telaris trata el uso que dos galaxias hacen de la misma palabra como la **misma palabra clave**. No hay un mecanismo de alias por galaxia en la v1 del despliegue; si quieres que *medicinal* en una galaxia se trate como la misma palabra clave que *healing* en otra, el movimiento práctico es **renombrar una para que coincida con la otra** de manera que ambas galaxias converjan en una sola palabra.

Si la intención editorial es precisamente la contraria (una palabra que significa cosas distintas en dos galaxias y no debería conectarlas), usa palabras distintas en cada galaxia. La precisión conceptual es más útil que la astucia sintáctica aquí.

## Conteos de palabras clave en la vista de visitante

Cuando la función de descubrimiento **Fichas de palabras clave** de la galaxia está encendida (el capítulo 4 cubre el conmutador; el capítulo 10 cubre la experiencia de visitante resultante), la visitante ve una fila de píldoras al pie de la escena 3D mostrando las palabras clave más usadas. Hacer clic en una píldora atenúa cada agujero de gusano que *no* carga esa palabra clave.

Este es un filtro suave (no quita agujeros de gusano de la escena, solo los atenúa), y es una de las principales formas en que las visitantes navegan una galaxia sin instrucciones. Las palabras clave que eliges son la navegación: palabras clave claras significan una escena clara.

## Cosas que vale la pena saber

- **Un agujero de gusano sin palabras clave está permitido pero es silencioso.** Las visitantes todavía pueden alcanzarlo por búsqueda por nombre o haciendo clic en 3D; no lo alcanzarán por la capa de píldoras de palabras clave. Usa cero palabras clave cuando el papel del agujero de gusano sea puramente solitario.
- **Los nombres de palabras clave se buscan en el cuadro de búsqueda del inicio del editor** junto con nombres y descripciones de agujeros de gusano. Buscar por una palabra clave es la forma más rápida de auditar qué agujeros de gusano la cargan.
- **Renombrar una palabra clave la actualiza en todas partes de la instancia.** Renombrar *medicinal* la renombra en cada galaxia que use la palabra. No hay renombrado por galaxia.
- **Eliminar una palabra clave la quita de cada agujero de gusano que la cargaba.** Los agujeros de gusano sobreviven; la píldora de palabra clave cae de ellos. Eliminar una palabra clave (a través del lienzo de palabras clave, capítulo 8) quita la palabra; eliminar un agujero de gusano (a través del menú de acciones de su fila, capítulo 5) quita el contenido. Son operaciones distintas.
- **No hay un número máximo de palabras clave por agujero de gusano**, pero la legibilidad práctica sugiere que de tres a siete es suficiente. Pasadas las diez, la franja de píldoras en la ficha empieza a envolverse de manera incómoda.
