# El lienzo de palabras clave

El lienzo de palabras clave es donde haces autoría del mapa conceptual de una galaxia. Los agujeros de gusano te dan objetos; las palabras clave te dan formas de etiquetar esos objetos; el lienzo es donde dibujas, a mano, las relaciones **entre las palabras clave mismas**. Dos píldoras se acercan porque la editora decidió que pertenecen cerca. Dos píldoras tienen una línea trazada entre ellas porque la editora decidió decir *estas dos ideas están enlazadas, y aquí está por qué*.

Este capítulo recorre la superficie, sus prestaciones de dibujo, y la disciplina editorial de usarla bien.

## Abrir el lienzo

Selecciona desde el inicio del editor la galaxia en la que quieres trabajar. Cuando hay una galaxia específica seleccionada, aparecen tres botones junto al selector de galaxia; el tercero es **Canvas**. Selecciónalo. El lienzo abre en una pestaña nueva.

> [!warning] Solo escritorio
> El lienzo es una superficie solo de escritorio. En un teléfono o tableta, las interacciones de píldoras y líneas no se comportan bien; el botón Canvas se oculta en esos contextos. Si necesitas trabajar en el arreglo de palabras clave de una galaxia desde una pantalla pequeña, la lista de agujeros de gusano y el campo de palabras clave dentro del modal de cada agujero de gusano todavía funcionan; el lienzo no.

## Lo que ves

El lienzo abre en una escena oscura a pantalla completa con las palabras clave de la galaxia dispuestas como píldoras pastel sobre una cuadrícula de puntos:

![Lienzo de palabras clave: píldoras pastel con líneas de relación trazadas entre ellas, sobre un fondo oscuro con cuadrícula de puntos](assets/images/editor-manual-es/10-keyword-canvas.png)

Cada píldora es una palabra clave. El color de la píldora coincide con el color usado en el resto de la aplicación: *native* es el mismo verdoso aquí que en una fila de agujero de gusano. Las píldoras se desplazan ligeramente cuando el lienzo está inactivo (una simulación física suave las mantiene vivas); arrastrar una píldora la fija en su lugar desde ese momento.

Las líneas entre píldoras son **relaciones** que la editora ha dibujado. Cada línea tiene dos extremos (las píldoras que conecta), una nota opcional (una oración que explica la conexión), y un registro de quién la dibujó y cuándo.

La barra superior carga:
- **Back**: te devuelve al inicio del editor para esta galaxia.
- El nombre de la galaxia.
- **?**: abre una pequeña capa de ayuda que lista cada interacción de teclado y ratón del lienzo.
- **Ready** (o **Saving…**): un pequeño indicador de estado que confirma que el lienzo ha guardado tu cambio más reciente.

## Dibujar una relación

Dos formas de trazar una línea entre dos píldoras:

1. **Clic-clic**: haz clic en el punto de anclaje de una píldora (un círculo pequeño que aparece sobre la píldora cuando pasas el ratón encima), luego haz clic en el punto de anclaje de otra píldora. Una línea encaja en su lugar.
2. **Arrastrar**: presiona en el punto de anclaje de una píldora y arrastra a la otra píldora; suelta. Mismo resultado.

Cuando aparece la línea, una pequeña entrada en línea te permite escribir una nota opcional. Enter guarda la nota; Escape deja la línea sin nota. La nota es visible cuando una visitante (u otra editora) pasa el ratón sobre la línea después.

La línea **se pega a los bordes de las píldoras** a medida que mueves las píldoras. Arrastra la píldora *native* a través del lienzo; la línea hacia *salt-tolerant* la sigue. No hay enrutamiento manual de líneas; la geometría se cuida sola.

## Mover y disponer píldoras

- **Arrastra** una píldora para reposicionarla. La nueva posición se guarda automáticamente.
- El lienzo recuerda la posición **por editora**: cada editora tiene su propia vista del lienzo. Dos editoras trabajando en la misma galaxia no pelean por las posiciones de las píldoras; cada una ve su propio arreglo, y la vista de visitante usa el arreglo más reciente o uno combinado (consulta a tu operadora el ajuste de tu instancia).
- Las píldoras que no has movido flotan en una deriva suave, asentándose lentamente en una disposición influida por sus líneas de relación (las píldoras conectadas por una línea se atraen suavemente). La deriva se detiene una vez que arrastras una píldora; desde ese momento, la píldora queda fijada.

Este es el pequeño secreto del lienzo: la disposición que ves es en parte obra de la simulación y en parte de las elecciones editoriales que has hecho. Dos galaxias cuyas editoras no han dibujado ninguna relación parecen polvo sobre la cuadrícula; dos galaxias cuyas editoras han dibujado muchas parecen constelaciones.

## Editar o eliminar una relación

Pasa el ratón sobre una línea; aparece un pequeño menú contextual con dos opciones:

- **Edit note**: cambia la nota en línea adjunta a la línea.
- **Delete**: elimina la relación por completo.

Las eliminaciones son permanentes a nivel de línea (no hay deshacer dentro del lienzo), pero los extremos de las píldoras permanecen en el lienzo. Puedes volver a trazar una relación entre las mismas dos píldoras después; la nueva línea es un registro fresco en el subyacente, no una restauración del antiguo.

## Renombrar y fusionar palabras clave

Haz clic derecho (o presiona largo en táctil) sobre una píldora para abrir sus opciones:

- **Rename**: cambia la palabra. El renombrado se aplica a cada agujero de gusano que carga la palabra clave en cada galaxia de la instancia, porque las palabras clave son globales por texto. El color de la píldora cambia para coincidir con el nuevo texto (los colores son deterministas por la palabra).
- **Merge into…**: selecciona otra píldora del lienzo para fusionar esta palabra clave dentro. Tras la fusión, cada agujero de gusano que cargaba la palabra clave de origen ahora carga la de destino. La píldora de origen desaparece.
- **Delete**: quita la palabra clave de cada agujero de gusano que la cargaba en la instancia.

Estas son herramientas afiladas. Fusionar es la más amable de las tres (sin pérdida de datos; solo un reetiquetado), luego renombrar (también sin pérdida de datos; la palabra cambia pero las conexiones permanecen), luego eliminar (la palabra clave se va; los agujeros de gusano sobreviven sin ella). Opera en un día tranquilo si una galaxia tiene muchas editoras.

## Reinicio por lote

El lienzo expone dos operaciones de reinicio por lote a través de la capa de ayuda **?**:

- **Reset all chip positions** en esta galaxia: cada píldora vuelve a una posición por defecto uniforme. Úsalo cuando la disposición ha acumulado costra y quieres empezar de nuevo.
- **Reset all relations** en esta galaxia: elimina cada línea de relación en esta galaxia. Las píldoras permanecen. Úsalo cuando quieras volver a dibujar el mapa conceptual desde cero.

Ambas están acotadas a la **galaxia actual**; no tocan otras galaxias.

## Cuándo usar el lienzo (y cuándo no)

El lienzo es más útil cuando:

- Las palabras clave de una galaxia cargan una estructura que vale la pena mostrar (algunas son hermanas, algunas son opuestas, algunas están acotadas específicamente a una subregión del contenido).
- Un punto editorial vive **entre** palabras clave en vez de dentro de una sola. *Native* por sí sola es solo una etiqueta; *native* dibujada cerca de *salt-tolerant* con una nota ("most natives here tolerate salt") es una observación.
- Quieres una superficie de trabajo para pensar. El lienzo es un cuaderno de bocetos para el vocabulario de la galaxia tanto como un artefacto público.

El lienzo es **menos útil** para:

- Galaxias diminutas (menos de diez agujeros de gusano; el conteo de píldoras suele ser demasiado pequeño para que la disposición sea interesante).
- Galaxias cuyas palabras clave son en su mayoría nombres propios o únicas a un solo agujero de gusano; el lienzo es para relaciones *entre* conceptos, y los conceptos únicos no tienen con qué relacionarse.

Si una galaxia nunca se siente como si justificara abrir el lienzo, ese es un resultado válido. El lienzo se ofrece, no se exige.

## Cosas que vale la pena saber

- **El lienzo guarda cada cambio automáticamente.** No hay botón Save. El indicador **Saving…** / **Ready** arriba a la derecha refleja el estado de persistencia.
- **No hay deshacer dentro de la superficie del lienzo.** Un movimiento equivocado se corrige con otro movimiento; una eliminación accidental volviendo a trazar la línea. Si algo sale muy mal, pregunta a tu operadora por una instantánea.
- **La visitante no ve las píldoras directamente.** El lienzo es una superficie de editora; lo que las visitantes ven en la escena 3D está influido por la disposición de las palabras clave (qué agujeros de gusano comparten palabras clave; qué píldoras tienen relaciones), pero las visitantes no miran la cuadrícula de píldoras misma.
- **Las notas de línea se exponen a las visitantes solo al pasar el ratón** en el panel de agujeros de gusano relacionados (el capítulo 10 tiene el detalle del lado visitante). La nota es parte del artefacto público; escríbela para una lectora futura, no para ti misma.
