# Vistas de visitante

El trabajo de la editora lo leen las visitantes. Casi cada elección editorial que haces termina apareciendo del lado visitante, ya sea directamente (la descripción, los medios, las palabras clave) o indirectamente (las relaciones dibujadas en el lienzo de palabras clave, la forma en que se etiquetan los agujeros de gusano). Este capítulo es tu mapa de lo que ven las visitantes, y de los interruptores del lado editorial que le dan forma.

A la vista de visitante se llega siguiendo cualquier URL de visitante de tu instancia: típicamente el slug de la galaxia, a veces sin slug en absoluto (tu operadora puede confirmar el camino de entrada).

![Escena 3D de visitante para la galaxia de demo Coastal plants](assets/images/editor-manual/13-visitor-scene.png)

## La escena 3D

La vista de visitante por defecto es una escena tridimensional donde cada agujero de gusano es un pequeño objeto flotando en el espacio sobre el fondo del tema elegido por la galaxia. El ratón de la visitante rota la vista; el scroll o el pellizco hace zoom; hacer clic en un agujero de gusano abre su ficha.

Lo que tú eliges como editora y se muestra aquí:

- **El tema de la galaxia** (capítulo 4) controla el aspecto: qué iconos representan los agujeros de gusano, cómo es el fondo, cómo se siente la iluminación.
- **El conmutador Use-as-wormhole-icon** de cada agujero de gusano (capítulo 5) decide si ese agujero de gusano se representa como su imagen (cuando está encendido) o como el icono por defecto del tema (cuando está apagado).
- **La marca Accentuate** en un agujero de gusano lo hace más grande y prominente en la escena.
- **La marca Show Keywords** imprime las palabras clave del agujero de gusano como etiquetas flotantes junto al icono.

Estas cuatro elecciones interactúan: una galaxia de agujeros de gusano acentuados, iconizados por imagen, y con palabras clave visibles es una escena cargada; una de agujeros de gusano iconizados por tema, planos, es una escena tranquila. No hay un modo "correcto"; elige el registro visual que coincida con el registro editorial del contenido.

## La ficha

Una visitante que hace clic en un agujero de gusano ve su **ficha** abrirse sobre la escena. La ficha contiene, en orden:

- El **nombre** del agujero de gusano arriba.
- El **visual primario** (imagen, video, o PDF) debajo del nombre, dimensionado al tamaño de la ficha.
- La **descripción** como párrafo de cuerpo.
- El **reproductor de audio** si hay audio adjunto.
- El **código de embed** si se proveyó alguno.
- Una fila de **píldoras de palabras clave** al pie de la ficha, cada una cliqueable.
- El botón **Open Link** si el agujero de gusano carga una URL.

Cuando la visitante hace clic en una píldora de palabra clave en la ficha, la escena atenúa los agujeros de gusano que no cargan esa palabra clave. La ficha se cierra. Esta es una de las formas principales en que las visitantes navegan por etiquetas en vez de por nombre.

## Los conmutadores de Discovery

El modal de ajustes de galaxia carga una sección Discovery (el capítulo 4 introdujo el modal; aquí está lo que hace cada conmutador del lado visitante):

![Modal de ajustes de galaxia desplazado a los conmutadores Discovery](assets/images/editor-manual/12-galaxy-discovery-section.png)

Cada conmutador está apagado por defecto. Enciende uno cuando quieras la característica correspondiente.

### Auto-tour

Un recorrido autorreproducido por la galaxia. Cuando está encendido, aparecen opciones adicionales:

- **Start mode** (manual, idle, immediate):
  - **Manual**: la visitante debe presionar un botón Play para iniciar el recorrido.
  - **Idle**: el recorrido empieza automáticamente cuando la visitante no ha interactuado con la escena por un número configurable de segundos.
  - **Immediate**: el recorrido empieza tan pronto como la visitante aterriza en la galaxia.
- **Node selection** (all, accentuated, random N, tagged keywords):
  - **All**: el recorrido visita cada agujero de gusano en la galaxia en orden.
  - **Accentuated only**: visita solo los agujeros de gusano marcados como acentuados.
  - **Random N**: elige N agujeros de gusano al azar cada sesión; el número es configurable.
  - **Tagged keywords**: visita solo los agujeros de gusano que cargan una de un conjunto elegido de palabras clave. La lista de palabras clave se fija en un subcampo que aparece cuando esta opción está seleccionada.
- **Dwell time** en segundos en cada parada, antes de que el recorrido pase al siguiente.
- **Loop**: cuando está encendido, el recorrido vuelve al principio tras la última parada; cuando está apagado, termina en silencio.

Un botón **Preview tour** aparece junto a los campos del Auto-tour; seleccionarlo abre la vista de visitante en una pestaña nueva con el recorrido corriendo, para que puedas comprobar el timing sin guardar la configuración.

El capítulo 11 profundiza en los recorridos.

### Idle spotlight

Cuando está encendido, la escena destaca suavemente un agujero de gusano distinto cada N segundos cuando la visitante está inactiva. A diferencia del Auto-tour, no mueve la cámara ni abre fichas; solo trae un agujero de gusano hacia adelante, suavemente, como un museo cambiando la iluminación de la sala.

Dos ajustes:

- **Idle threshold** en segundos antes de que empiece el foco.
- **Selection** (all, accentuated only).

Idle spotlight calza bien con galaxias de sensación ambiental (un ciclo de poemas; una secuencia de fotografías); le da a la sala algo que hacer cuando la visitante ha dejado de hacer clic.

### Keyword chips

Cuando está encendido, la escena pinta una franja de píldoras pastel al pie de la pantalla de la visitante, una píldora por cada palabra clave más usada en la galaxia. Las visitantes pueden hacer clic en una píldora para atenuar cada agujero de gusano que no la carga.

Úsalo cuando la galaxia tenga un vocabulario de palabras clave fuerte por el que las visitantes naturalmente navegarían; apágalo cuando las palabras clave sean demasiado granulares o demasiadas para que las píldoras sean útiles.

### Related wormholes

Cuando está encendido, una ficha abre con hasta cinco píldoras de agujeros de gusano **relacionados** al pie: otros agujeros de gusano (en esta o en galaxias hermanas) que comparten al menos una palabra clave con el abierto. La visitante puede hacer clic en una píldora para saltar directamente al agujero de gusano relacionado.

Esta es la forma principal en que las visitantes viajan lateralmente por una red sin abrir un portal. Enciéndelo cuando quieras que la visitante descubra la trama; apágalo cuando quieras que la visitante se mantenga enfocada en un agujero de gusano a la vez.

### 2D view

Cuando está encendido, aparece un pequeño conmutador **3D / 2D** en la parte superior de la pantalla de la visitante. Cambiar a 2D colapsa la escena en una cuadrícula plana de píldoras de agujeros de gusano: cada píldora es el icono del agujero de gusano más su nombre, ordenadas en filas. La vista 2D carga más rápido y es más fácil de ojear; algunas visitantes la prefieren para encontrar un agujero de gusano específico rápidamente.

La elección de la visitante entre 3D y 2D persiste en su navegador (no tiene que volver a elegir).

## Pies de procedencia y atribución

Cuando la procedencia editorial de un agujero de gusano carga una atribución (`Image attribution`, crédito a la comunidad de origen, o aviso de réplica federada), la ficha lo muestra como una pequeña línea de pie debajo de la descripción.

No hay un conmutador global para ocultar los pies de procedencia; si tu trabajo acredita a una fotógrafa o a una comunidad de origen, ese crédito aparece cada vez que el agujero de gusano se abre. La atribución autoral y el consentimiento de la comunidad de origen son preocupaciones editoriales de primera clase; el capítulo 13 cubre la disciplina editorial alrededor de ellos.

## Cosas que vale la pena saber

- **La visitante ve lo que has publicado, no tu borrador.** No hay un modo "preview" separado de la vista publicada; una vez que guardas un agujero de gusano o un ajuste de galaxia, la próxima recarga de página de la visitante refleja el cambio. Para previsualizar un cambio sin afectar a las visitantes, tendrías que hacer el cambio en una galaxia que aún no sea pública.
- **La escena 3D corre en el navegador de la visitante.** Dispositivos antiguos o computadoras de poca potencia pueden tener dificultades con galaxias muy densas. El conmutador 2D view es el remedio estándar.
- **El audio que se autorreproduce puede ser bloqueado por el navegador de la visitante.** La mayoría de los navegadores no permiten que el audio empiece sin la interacción de la visitante. Si enciendes Autoplay (capítulo 6) y una visitante reporta que no hay sonido, esta es la causa más probable; el primer clic de la visitante en la página suele desbloquear el audio.
- **Los conmutadores Discovery son independientes entre sí.** Auto-tour e idle spotlight pueden estar encendidos al mismo tiempo (el foco se activa si el recorrido termina o no se ha iniciado). Elige las combinaciones que calcen con tu intención editorial; los conmutadores no se condicionan entre sí.
