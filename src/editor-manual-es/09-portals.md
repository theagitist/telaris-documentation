# Portales

Un portal es un tipo especial de agujero de gusano. En vez de cargar contenido propio, carga un destino: otra galaxia. Una visitante que abre un portal lo atraviesa. La escena se desvanece, una nueva galaxia carga, el portal se cierra detrás. Los portales son como una editora construye puentes intencionales entre galaxias.

Este capítulo cubre cuándo usar un portal frente a una palabra clave compartida, cómo crear uno, y el pequeño conjunto de convenciones editoriales que mantienen legible una red de portales.

## Cuándo un portal es la herramienta correcta

Telaris ya te da dos formas de conectar contenido entre galaxias:

1. **Palabras clave compartidas**: un agujero de gusano en la galaxia A y otro en la galaxia B, ambos etiquetados con *intertidal*, forman una conexión *pasiva*. Una visitante que sigue *intertidal* en cualquiera de las dos llega a una vista que muestra ambos.
2. **Etiquetas de galaxia**: la galaxia A y la galaxia B compartiendo la etiqueta *coast* crean una unión; las visitantes que siguen `/tag/coast` ven los agujeros de gusano de ambas galaxias juntos.

Un portal es un tercer tipo de conexión, y mucho más *activo*: la editora dice, en efecto, *desde este agujero de gusano, ve allí ahora*. Es la herramienta correcta cuando:

- La conexión es **direccional y deliberada**. Una palabra clave compartida es una red; un portal es una flecha.
- La galaxia de destino es una **continuación de la conversación**, no solo un tema relacionado. La lectora debería dejar su galaxia actual y llegar a otra, no ojear ambas a la vez.
- Quieres que el portal mismo **aparezca en la escena 3D** como un objeto navegable. Un portal se representa como un nodo 3D distinto; las visitantes pueden reconocerlo y hacer clic deliberadamente.

Si nada de esto es cierto, una palabra clave o una etiqueta de galaxia suele ser mejor elección.

## Crear un portal

Un portal es un agujero de gusano cuyo Tipo de agujero de gusano está fijado a **Portal**. Desde el modal de nuevo agujero de gusano:

![Modal de nuevo agujero de gusano con el Tipo de agujero de gusano fijado a Portal: aparece un desplegable Galaxia destino](assets/images/editor-manual-es/11-portal-type-selector.png)

Pasos:

1. Abre **Nuevo agujero de gusano** desde el inicio del editor (o abre el modal de edición de un agujero de gusano existente y cambia su tipo).
2. Fija **Tipo de agujero de gusano** a **Portal**. Aparece un campo **Galaxia destino** con un desplegable que lista cada galaxia a la que tienes acceso.
3. Elige la galaxia de destino del desplegable. El botón junto a él, **Crear nueva galaxia**, es un atajo para el caso en que el destino aún no existe; seleccionarlo te permite hacer autoría del destino en línea. La mayoría del tiempo, eliges una galaxia existente.
4. **Nombra** el portal con algo legible. Un portal es un agujero de gusano, así que el nombre aparece en listas y en la escena 3D; elige un nombre que señale el viaje, no solo el destino. *To the tide pools* lee mejor que *Tide pools*.
5. Añade una **Descripción** si quieres un párrafo corto que aparezca cuando la visitante abra la ficha del portal. La descripción se muestra brevemente antes de que comience el viaje a la galaxia de destino; trátala como una oración umbral.
6. Opcional: asigna unas pocas **palabras clave**. Los portales pueden cargar palabras clave como cualquier otro agujero de gusano; esto ayuda a que el portal aparezca en el descubrimiento basado en palabras clave.
7. Guarda.

El portal aparece ahora en la lista de agujeros de gusano con una etiqueta **Portal** en la columna Tipo, y como un nodo distinguible en la escena 3D.

## Qué experimenta la visitante

Una visitante que hace clic en un portal en la escena 3D ve:

- La ficha del portal se abre, igual que cualquier otro agujero de gusano.
- La ficha muestra el nombre del portal, la descripción, y (dependiendo de los ajustes de la instancia) un botón de llamada a la acción llamado **Abrir el Portal** o algo similar.
- Activar la llamada a la acción cierra la galaxia actual y carga el destino.
- En la galaxia de destino, la visitante llega a la entrada de la galaxia (la posición de inicio por defecto), no a un agujero de gusano específico.

La visitante puede usar el botón Back del navegador para volver a la galaxia de origen. Telaris **no** coloca automáticamente un portal de retorno en la galaxia de destino; si quieres que el viaje sea de ida y vuelta, necesitas colocar un portal correspondiente manualmente.

## Portales de ida y vuelta

Cuando colocas un portal de A a B, considera si también quieres un portal de B a A. Los dos son independientes: cada uno es un agujero de gusano en su propia galaxia. No hay un concepto de "portales enlazados".

La decisión es editorial:

- **Sí, coloca un portal de retorno** cuando las dos galaxias son socias iguales en una conversación; las visitantes que lleguen a B deberían ser invitadas de vuelta a A tan naturalmente como fueron invitadas de A a B.
- **No, deja el retorno implícito** cuando el camino natural de la visitante es de una sola dirección (A es la galaxia que enmarca; B es la respuesta; la visitante regresa por el navegador, si es que regresa).

Si colocas un portal de retorno, nómbralo por el destino al que lleva, no por "volver". *To the coastal plants* lee mejor que *Back* o *Return*.

## Portales y el lienzo de palabras clave

Las píldoras de palabras clave de un portal aparecen en el lienzo de palabras clave como las de cualquier otro agujero de gusano. Un portal etiquetado con *intertidal* contribuye a la red de conexiones *intertidal*. A veces las editoras etiquetan los portales con una palabra clave específica como *portal* para poder filtrarlos del descubrimiento basado en palabras clave (algunas visitantes pueden no querer saltos densos en portales); en nuestra galaxia de demo, el agujero de gusano portal carga la etiqueta *portal* por exactamente esa razón.

## Cosas que vale la pena saber

- **Un portal solo puede apuntar a una galaxia a la vez.** Si quieres un "concentrador" que se abra hacia muchas galaxias, la respuesta son muchos portales, no uno. Puedes colocar varios portales en una sola galaxia, cada uno apuntando a un lugar distinto.
- **El desplegable de destino solo lista galaxias que puedes editar.** Si la galaxia a la que quieres portalar está en otra instancia, eso es territorio de federación y es del dominio de la operadora; la superficie de editora no hace autoría de portales entre instancias.
- **Un portal puede ser retargeteado** editándolo y eligiendo una galaxia distinta en el campo Galaxia destino. Las visitantes que habían marcado el portal seguirán aterrizando en la galaxia que ahora esté seleccionada. Considera esto al cambiar destinos después de publicar.
- **Un portal que apunta a su propia galaxia** está técnicamente permitido pero es funcionalmente inútil: la visitante aterriza de vuelta de donde vino. La interfaz de editora no te detendrá, pero el resultado es una operación nula.
- **Eliminar un portal elimina el agujero de gusano por completo.** La galaxia de destino queda intacta; solo se va la conexión. Los propios portales del destino (si los hay) siguen funcionando.
- **Los portales no cargan medios.** Tienen un nombre, una descripción, y palabras clave, más la galaxia de destino. Los campos de imagen, video, audio, y PDF siguen en el modal pero deberían quedar vacíos en los portales; si los rellenas, simplemente son ignorados por la experiencia de visitante del portal.
