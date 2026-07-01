# Control de acceso de edición

Tener una cuenta de edición es una cosa; poder editar una galaxia dada es otra. Telaris separa las dos, así que puedes decidir no solo *quién* edita sino *qué* puede tocar cada persona editora. Este capítulo cubre los dos mecanismos: el interruptor de edición que puede apagarse en varios niveles, y el acceso por asiento que acota a una persona editora a galaxias específicas.

## El interruptor de edición (una cascada)

La edición puede encenderse o apagarse en cuatro niveles, del más amplio al más estrecho:

- la **instancia entera**,
- un **cúmulo** de galaxias,
- una sola **galaxia**,
- una sola **cuenta**.

El interruptor cae en cascada: apagar la edición en un nivel más amplio la apaga para todo lo que hay dentro, salvo que algo más estrecho la vuelva a encender. Apagar la edición para la instancia detiene a todas las editoras; apagarla para un cúmulo detiene la edición en las galaxias de ese cúmulo; y así sucesivamente. La edición está **encendida por defecto** en cada nivel, así que una instancia recién creada se comporta como esperarías y solo recurres a estos interruptores cuando quieres detener algo.

**La administración está exenta.** La cascada nunca deja a la administración sin poder editar; gobierna a la edición. Esto es deliberado, para que no puedas apagar por accidente tu propia capacidad de arreglar cosas.

### Cuándo lo usarías

- **Un curso o proyecto ha terminado.** Apaga la edición para la instancia (o para ese cúmulo) para congelar el contenido conservando cada cuenta y todo lo que hicieron. Esto es exactamente lo que hace una instancia de demostración una vez que su curso ha terminado: las cuentas y el contenido se quedan, pero no puede editarse nada nuevo.
- **Una galaxia se está revisando o traspasando.** Apaga la edición para esa sola galaxia mientras se asienta, sin afectar al resto de la instancia.
- **Una editora debe pausar.** Apaga la edición para una sola cuenta sin tocar a nadie más.

El interruptor **Permitir edición** en *Ajustes globales* es el extremo a nivel de instancia de esta cascada; los niveles de cúmulo, galaxia y cuenta se alcanzan donde se gestionan esas cosas.

## Acceso por asiento: solo lectura y lectura y escritura

Que la edición esté *encendida* sigue sin significar que una persona editora pueda editar *todo*. Quien edita trabaja en las galaxias en las que tiene un **asiento**, y cada asiento es de:

- **lectura y escritura**, quien edita puede cambiar el contenido de la galaxia, o
- **solo lectura**, quien edita puede ver la galaxia en su vista de edición pero no puede cambiarla.

Quien edita siempre tiene lectura y escritura en las galaxias que creó. Los asientos en otras galaxias se conceden: tú (o los valores por defecto del auto-registro) le das a una persona editora un asiento en una galaxia, al nivel que elijas. Un asiento de solo lectura es como dejas que alguien estudie o consulte una galaxia, o la use como modelo, sin poder alterarla. Solo lectura es también como se comporta el contenido importado para todo el mundo: el contenido replicado de otra instancia es de solo lectura para tus editoras, porque la autoridad sobre él vive en su fuente (consulta *Galaxias y cúmulos*).

Los dos mecanismos se combinan. Una persona editora puede cambiar una galaxia solo cuando la edición está encendida para ella todo el camino hacia arriba en la cascada **y** tiene un asiento de lectura y escritura en esa galaxia. Si falta cualquiera de los dos, la galaxia se le abre en estado de visor en vez de estado de edición.

## Cosas que vale la pena saber

- **Apagado por defecto no es nada; los interruptores son de exclusión.** Nunca tienes que encender la edición. La apagas cuando quieres detener algo, y la vuelves a encender cuando terminas.
- **Congelar no es eliminar.** Apagar la edición conserva cada cuenta y todo lo creado; solo impide cambios nuevos. Es la forma segura de terminar un proyecto sin descartarlo.
- **Solo lectura es una elección de primera clase, no una menor.** Buena parte del valor de un archivo compartido es poder mostrar una galaxia a colaboradoras que no deberían cambiarla. Concede asientos de solo lectura con generosidad.
