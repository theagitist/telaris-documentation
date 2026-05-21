# Recorridos

Un recorrido es un camino curado a través de una galaxia. La editora elige el inicio, elige el orden, fija un tiempo de permanencia en cada parada, y decide si el recorrido cicla o termina. Las visitantes pueden iniciar el recorrido ellas mismas presionando Play; o el recorrido puede correr por su cuenta cuando la visitante ha estado inactiva; o el recorrido puede empezar en el instante en que la visitante aterriza en la galaxia. Este capítulo recorre cada camino de autoría de un recorrido y las consideraciones prácticas.

Un recorrido es **una configuración de una galaxia**, no un objeto separado. Encender el recorrido configura los agujeros de gusano existentes para ser visitados en un orden elegido; apagarlo deja los agujeros de gusano intactos. Una galaxia puede cargar una configuración de recorrido a la vez; si quieres dos recorridos, publicas una copia de la galaxia con el segundo recorrido.

## Dónde lo haces

Un recorrido vive dentro del modal **Galaxy settings**, en la sección Discovery (el capítulo 4 introduce el modal; el capítulo 10 introduce los conmutadores Discovery).

![Modal de ajustes de galaxia en la sección Discovery](assets/images/editor-manual/12-galaxy-discovery-section.png)

El primer conmutador de la sección Discovery es **Auto-tour**. Encenderlo revela los campos de configuración del recorrido:

- Start mode.
- Node selection.
- Dwell time en cada parada.
- Loop on / off.

Debajo de estos hay un botón **Preview tour**.

## Start mode

Elige cómo empieza el recorrido:

- **Manual**: un pequeño botón **Play** aparece en la esquina inferior derecha de la escena 3D de la visitante. El recorrido empieza cuando la visitante lo presiona. Úsalo cuando el recorrido es un camino *ofrecido*, no uno por defecto.
- **Idle**: el recorrido empieza automáticamente cuando la visitante ha estado inactiva por un número configurable de segundos. El campo del umbral de inactividad aparece debajo de esta opción. Úsalo cuando la galaxia está pensada para encontrarse tanto interactivamente (la visitante explora) como ambientalmente (la galería se despierta cuando nadie la toca).
- **Immediate**: el recorrido empieza en el instante en que la visitante aterriza en la galaxia. La visitante puede detenerlo en cualquier momento con los controles de la escena. Úsalo para galerías cuya experiencia pretendida es el recorrido mismo; el camino de la editora es la lectura canónica.

No hay una respuesta correcta; cada opción calza con una intención editorial distinta. La mayoría de las galaxias de autoría empiezan con **Manual** y se gradúan a **Idle** o **Immediate** a medida que la editora encuentra un camino que merece ser el por defecto.

## Node selection

Elige qué agujeros de gusano visita el recorrido, y en qué orden:

- **All**: cada agujero de gusano en la galaxia, en el orden en que fueron creados. La selección más simple; útil para galaxias cortas donde cada agujero de gusano carga peso igual.
- **Accentuated only**: solo los agujeros de gusano marcados como acentuados. Úsalo cuando quieras que algunos agujeros de gusano estén en el recorrido y otros queden alcanzables pero no en primer plano. La marca Accentuate se fija por agujero de gusano (capítulo 5).
- **Random N**: elige N agujeros de gusano al azar cada sesión. Aparece un campo para N. Úsalo para galerías que deberían sentirse frescas al revisitar; la visitante ve un corte distinto cada vez.
- **Tagged keywords**: visita solo los agujeros de gusano que cargan una de un conjunto elegido de palabras clave. Aparece un selector de palabras clave, similar al campo de entrada de píldoras de palabras clave en un modal de agujero de gusano. Úsalo cuando quieras un recorrido *temático* (solo agujeros de gusano etiquetados con *medicinal*; solo los etiquetados con *native*).

Para recorridos por palabras clave etiquetadas, el orden en que se visitan los agujeros de gusano es el orden en que fueron creados, filtrado al conjunto de palabras clave. No hay un campo de orden manual; si necesitas una secuencia estrictamente autorada, el orden en que crees los agujeros de gusano es el orden que el recorrido respetará.

## Dwell time

Un único número, en segundos, que controla cuánto se detiene el recorrido en cada agujero de gusano antes de pasar al siguiente. La permanencia empieza cuando la ficha del agujero de gusano abre; el siguiente agujero de gusano se selecciona cuando transcurre la permanencia.

Un valor útil por defecto es de cinco a ocho segundos; esto es lo suficientemente largo para que una visitante lea una descripción corta y mire la imagen, lo suficientemente corto para mantener impulso a lo largo de un recorrido largo. Los agujeros de gusano con audio adjunto a menudo merecen una permanencia más larga para que el audio se resuelva antes de que el recorrido pase; el capítulo 6 cubre la semántica del bucle de audio.

La permanencia es global al recorrido; la editora (por ahora) no puede fijar una permanencia distinta por agujero de gusano.

## Loop

Un único conmutador:

- **On**: tras el último agujero de gusano, el recorrido regresa al primero y continúa. Úsalo para instalaciones ambientales de galería donde la visitante puede entrar a mitad de ciclo.
- **Off**: el recorrido termina en silencio tras el último agujero de gusano; la escena vuelve al modo interactivo y la visitante puede explorar libremente. Úsalo para recorridos narrativos con un principio y un final.

## Previsualizar un recorrido

Debajo de los campos de configuración del recorrido aparece un botón **Preview tour**. Seleccionarlo abre la vista de visitante en una pestaña nueva con el recorrido corriendo, sin importar si has guardado la configuración. Esta es la forma correcta de comprobar timing, orden, y permanencia antes de publicar cambios a las visitantes.

La vista previa refleja lo que has introducido en el modal, no lo que está guardado actualmente. Si decides que la vista previa está mal, cambia los campos y selecciona Preview de nuevo; la pestaña nueva se actualiza.

## Recorridos y Accentuate

La marca Accentuate en un agujero de gusano (capítulo 5) se solapa con la selección de recorrido pero no es lo mismo. Los agujeros de gusano acentuados son *visualmente más grandes* en la escena 3D sin importar si un recorrido los visita. La opción **Accentuated only** de selección de nodos para el recorrido es una forma de usar la marca, pero también puedes acentuar agujeros de gusano que no están en el recorrido y tener un recorrido que incluya agujeros de gusano que no están acentuados.

El patrón que lee más limpio:

- Usa Accentuate para agujeros de gusano que deberían destacar visualmente todo el tiempo.
- Usa el recorrido para especificar el *camino narrativo*, que puede o no solaparse con el énfasis visual.

## Recorridos y el lienzo de palabras clave

Un recorrido por palabras clave etiquetadas (selección de nodos fijada a *tagged keywords*) le da a la editora un camino por la galaxia que sigue el vocabulario de palabras clave que el lienzo escribe. Las dos superficies trabajan juntas: elige primero en el lienzo las palabras clave que el recorrido seguirá, dibuja las relaciones entre ellas, luego configura el recorrido para seguir ese camino temático del lado visitante.

La conexión es editorial más que estructural; Telaris no requiere que el lienzo esté poblado antes de configurar un recorrido, pero el recorrido resultante suele sentirse más deliberado cuando el vocabulario de palabras clave ha sido trabajado.

## Cosas que vale la pena saber

- **Auto-tour no pausa por el audio.** Si un agujero de gusano tiene una pista de audio de 30 segundos y la permanencia es de 8 segundos, el recorrido pasa a los 8 segundos mientras el audio sigue sonando de fondo. Para dejar que el audio se complete, alarga la permanencia.
- **La visitante siempre puede detener el recorrido.** Un control Stop o Pause aparece durante un recorrido en curso; la visitante también puede hacer clic en cualquier lugar fuera de la ficha para interrumpirlo. Los recorridos deben sentirse ofrecidos, no forzados.
- **Los recorridos Random-N cambian en cada sesión.** Una visitante que vuelve a la página no ve los mismos N agujeros de gusano; la selección al azar se vuelve a tirar. Útil para sensación ambiental; sorprendente si esperabas una secuencia estable.
- **Los recorridos por palabras clave etiquetadas siguen la unión de las palabras clave elegidas.** Un recorrido fijado a las palabras clave *native* y *edible* visita cada agujero de gusano etiquetado con **cualquiera** de *native* o *edible* (o ambas); no requiere ambas.
- **Los recorridos están acotados a la galaxia actual.** Un recorrido no puede visitar agujeros de gusano de otra galaxia; para caminos entre galaxias, usa portales (capítulo 9).
- **La vista 2D (capítulo 10) interactúa con los recorridos con gracia.** Una visitante en modo 2D ve el recorrido como una secuencia de píldoras resaltadas, no como movimiento de cámara. La permanencia sigue aplicándose; el visual es solo más plano.
