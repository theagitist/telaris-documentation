# Gestionar páginas

La vista **Contenido hotglue** es donde llevas el control de tus páginas de Hotglue: crearlas, nombrarlas, adjuntarlas a agujeros de gusano y ordenarlas. Este capítulo la recorre.

## La lista

La vista muestra una tabla de las páginas de Hotglue a las que puedes llegar, con un recuento en el encabezado. Las columnas son:

- una casilla para seleccionar la fila,
- **Título**,
- **Agujero de gusano asignado** (el agujero de gusano en el que se muestra esta página, o en blanco si no hay ninguno),
- **Actualizado**,
- **Acciones**.

![La lista de Contenido hotglue con tres páginas: una asignada a un agujero de gusano, una sin asignar y una segunda página asignada, cada una con una fecha de Actualizado y un menú de acciones](assets/images/hotglue-manual-es/02-hotglue-content-list.png)

Haz clic en el título de una página para abrirla en la superposición del editor. Haz clic en el encabezado de la columna **Título**, **Agujero de gusano asignado** o **Actualizado** para ordenar por esa columna; haz clic de nuevo para invertir el orden. Una pequeña flecha marca la columna por la que ordenaste.

## Crear y nombrar una página

Haz clic en **Nueva página** para crear una. Se abre de inmediato en el editor como una página sin título y sin asignar, lista para componer.

Para renombrar una página, ábrela y edita el campo **Nombre de la página** en la parte superior de la superposición. El nombre nuevo se guarda por sí solo cuando haces clic fuera; una pequeña nota de estado lo confirma.

## Asignar una página a un agujero de gusano

Una página de Hotglue solo aparece para quien visita una vez que está adjunta a un agujero de gusano. Dentro de la superposición del editor, usa el control **Agujero de gusano asignado**:

- Es una lista con búsqueda. Empieza a escribir el nombre de un agujero de gusano para acotarla. Cada opción se muestra como el nombre del agujero de gusano seguido de su galaxia, para que puedas distinguir agujeros de gusano con nombres parecidos.
- Elige un agujero de gusano para asignarle la página. Elige **Sin asignar** para desadjuntar la página de nuevo (el agujero de gusano vuelve entonces a sus medios clásicos; la página en sí no se elimina).

Si el agujero de gusano que eliges ya muestra una página de Hotglue distinta, Hotglue pregunta primero: "¿Reemplazar? Este agujero de gusano ya muestra una página hotglue. La página que muestra ahora quedará sin asignar (no se elimina)." Así que nunca pierdes una página al reasignar un agujero de gusano; la página desplazada simplemente queda sin asignar.

> [!note] Necesitas acceso de edición a la galaxia de destino
> Asignar o desadjuntar una página requiere un asiento de lectura y escritura en la galaxia del agujero de gusano. Un asiento de solo lectura te deja ver las páginas pero no cambiar a qué están adjuntas.

## Duplicar una página

La acción **Duplicar** en el menú de una fila hace una copia de una página (su título gana un sufijo "(copia)"). La copia se crea siempre **sin asignar**, así que duplicar nunca altera el agujero de gusano del original. Justo después de duplicar, Hotglue se ofrece a asignar la nueva copia a algún sitio.

## Ver una página

El menú de acciones de una fila ofrece tres formas de mirar una página:

- **Ver en el navegador** abre la página de Hotglue desnuda en una pestaña nueva, exactamente como la vería quien visita, y copia su dirección a tu portapapeles. Esto funciona para cualquier página, asignada o no.
- **Copiar URL directa** copia esa misma dirección a tu portapapeles sin abrir una pestaña. Úsala cuando solo quieres el enlace para pegarlo en algún sitio.
- **Ver en el agujero de gusano** abre una vista previa de la página dentro de su agujero de gusano, en la misma ventana. Disponible solo para páginas asignadas.
- **Ver en la galaxia** abre el visor tridimensional de la galaxia en vivo enfocado en el agujero de gusano, en una ventana nueva. Disponible solo para páginas asignadas.

## Revisar versiones anteriores

Mientras una página está abierta en el editor, el botón **Revisiones** abre su historial, para que puedas mirar atrás entre las versiones anteriores y recuperarte de un cambio que no querías conservar. Consulta *Guardado e historial* en *El lienzo* para ver cómo funciona el historial.

## Buscar y filtrar

- El cuadro **Buscar** filtra la lista a medida que escribes, coincidiendo con el título de la página, el nombre del agujero de gusano y el nombre de la galaxia.
- El selector de galaxia del encabezado del editor también sirve de filtro: elige una galaxia para mostrar solo las páginas de Hotglue cuyos agujeros de gusano viven allí, o déjalo en todas las galaxias para verlo todo.
- **Las páginas sin asignar se muestran bajo cualquier filtro de galaxia.** Una página que no está adjunta a ningún agujero de gusano no tiene galaxia propia, así que se mantiene visible sea cual sea la galaxia a la que filtres. Una página que acabas de crear no va a "desaparecer" porque hayas cambiado el selector de galaxia; simplemente está sin asignar hasta que la adjuntes.

## Trabajar en bloque

Marca las casillas (o la casilla de seleccionar todo del encabezado) para actuar sobre varias páginas a la vez. Aparece una barra que muestra cuántas están seleccionadas, con:

- **Limpiar selección**,
- **Desasignar seleccionadas** (desadjuntar las páginas elegidas de sus agujeros de gusano),
- **Eliminar seleccionadas**.

## Eliminar una página

Elimina una sola página desde el menú de acciones de su fila, o varias a la vez con **Eliminar seleccionadas**. En cualquier caso Hotglue confirma primero, porque la eliminación es permanente: "¿Eliminar esta página hotglue? Se borrará su contenido de forma permanente. Si está asignada a un agujero de gusano, ese agujero vuelve a los medios clásicos." Eliminar una página borra su contenido para siempre; cualquier agujero de gusano al que estuviera adjunta simplemente vuelve a mostrar los medios clásicos.
