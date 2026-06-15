# Privacidad

Telaris es un archivo de conocimiento decolonial de grado investigativo. Este aviso se aplica a **www.telaris.ca** (el sitio que estás leyendo) y al **software de Telaris** que se ejecuta en instancias operadas por personas independientes. Cada instancia es operada por una persona independiente y puede llevar avisos de privacidad adicionales propios que gobiernan el contenido de esa instancia; este aviso cubre el resto.

## Qué recoge www.telaris.ca

El sitio en `www.telaris.ca` es un pequeño conjunto de páginas informativas estáticas. No ejecuta ninguna herramienta de análisis, no coloca rastreadores publicitarios, no instala cookies y no recopila información personal de quien lo visita. El sitio se sirve a través de Cloudflare; los registros estándar de acceso de Cloudflare (IP truncada, agente de usuario, URL solicitada, estado de respuesta, marca de tiempo) se conservan por poco tiempo según la política propia de Cloudflare. Más allá de esos registros de borde, el sitio no registra visitas.

El sitio enlaza a documentos descargables y a instancias independientes de Telaris. Seguir uno de esos enlaces te lleva a otro sitio; este aviso no gobierna lo que sucede ahí.

## Qué recoge una instancia de Telaris

Cualquier sitio que ejecute el software de Telaris puede recopilar una pequeña cantidad de información necesaria para que el software funcione:

- **Cuentas de edición.** Cada instancia mantiene una lista de quienes están autorizados para agregar contenido. De cada persona editora guarda un nombre, un correo electrónico, pronombres opcionales y marcas de tiempo de inicio de sesión, mientras la cuenta esté activa. Una cuenta también puede tener un hash de contraseña, pero la contraseña es opcional: en su lugar, una persona editora puede iniciar sesión mediante un enlace de un solo uso que se le envía por correo cada vez, en cuyo caso no se guarda ninguna contraseña. Consulta *Tu información y lo que puedes solicitar como persona editora* más abajo.
- **Registro autónomo (solo si quien opera lo activa).** Algunas personas operadoras abren su instancia al registro autónomo de personas editoras. Cuando está activado, cualquiera puede solicitar una cuenta de edición indicando un nombre y un correo electrónico; el correo se confirma mediante un enlace de un solo uso antes de que la cuenta pueda usarse. Una solicitud que nunca se confirma se elimina automáticamente tras un período breve. El registro autónomo está desactivado salvo que quien opera decida activarlo; en la mayoría de las instancias las cuentas de edición las sigue creando quien opera.
- **Contenido editorial.** Los agujeros de gusano, las galaxias, las palabras clave, las descripciones, los archivos subidos y las relaciones entre ellos se guardan en cada instancia. Es el contenido que ve quien visita. La soberanía editorial es el principio: quien edita decide qué se publica, y nada se revisa antes de mostrarse.
- **Consentimiento de la comunidad de origen.** Cuando una comunidad de origen aporta material, el consentimiento de esa comunidad gobierna el material. La retirada del consentimiento es definitiva y la instancia la acata sin negociación.
- **Registros de acceso del servidor.** Una instancia puede conservar registros de acceso de corta duración con fines operativos, como depuración y mitigación de abuso. Cuando el software registra una dirección IP (por ejemplo en su registro de auditoría de acciones), corresponde a quien opera decidir cuánto tiempo conservarla; el software aplica un hash a las IP con una clave del servidor cuando puede, y no conserva IP en texto claro en sus propias tablas.

## Tu información y lo que puedes solicitar como persona editora

Si tienes una cuenta de edición en una instancia, ya sea que quien opera te la haya creado o que te hayas registrado por tu cuenta, lo siguiente te aplica.

- **Por qué guardamos tus datos: porque lo aceptaste.** Antes de poder usar el editor, se te pide revisar estos documentos y aceptarlos: en tu primer inicio de sesión si quien opera creó tu cuenta, o al registrarte si te uniste por tu cuenta. Tu aceptación se registra junto con la versión de cada documento, de modo que una revisión posterior te lo vuelve a pedir. Puedes retirar tu consentimiento en cualquier momento.
- **Qué se guarda sobre ti:** tu nombre, tu correo electrónico, los pronombres que indiques, marcas de tiempo de inicio de sesión, el contenido editorial que publicas y un registro de auditoría de las acciones administrativas que realizas (en el que tu correo se guarda solo como un hash con sal, nunca en claro). Si usas contraseña, se guarda su hash; si en su lugar inicias sesión mediante enlaces por correo, no se guarda ninguna contraseña. Los tokens de acceso de un solo uso y de corta duración (para los enlaces por correo que te inician sesión, confirman un registro o te permiten establecer una contraseña) se guardan solo como hashes, y solo hasta que se usan o caducan.
- **Lo que puedes solicitar:** puedes pedir a quien opera tu instancia que te muestre los datos que tiene sobre ti, que los corrija o que elimine tu cuenta y tu contenido. Puedes retirar el consentimiento, lo que elimina tu acceso y, si lo pides, tu contenido. Quien opera tu instancia atiende estas solicitudes; no se negocian, y la eliminación es definitiva.
- **Conservación:** los datos de la cuenta se conservan mientras la cuenta esté activa y se eliminan cuando lo pides. El registro de auditoría de acciones se conserva por un período limitado que fija quien opera (el valor predeterminado es 365 días) por razones de rendición de cuentas, y luego se depura.

## Registros y conservación entre instancias

El software de Telaris no hace ninguna promesa general sobre la conservación de registros, porque la rotación de registros vive en la infraestructura propia de cada persona operadora (su servidor web, su sistema operativo, su proveedor de borde). Lo que es constante en todas partes es esto: la **aplicación** no registra la actividad de navegación de quien visita. El único dato personal de visita que existe es la dirección IP que queda en los registros propios del servidor o del borde de quien opera, regida por la conservación que esa persona defina.

Las instancias operadas por Polivoxia rotan sus registros de servidor a los 14 días; es un valor recomendado, no una promesa que obligue a otras personas operadoras. Cada quien fija su propia conservación y es responsable de ella, y recomendamos una conservación corta o la anonimización de IP como la postura más coherente con los valores de este proyecto.

## Lo que Telaris no hace

- **Sin publicidad.** Sin rastreadores de terceros, sin red publicitaria, sin perfilado de comportamiento.
- **Sin entrenamiento ni análisis de IA sobre el corpus.** El contenido de Telaris no se usa para entrenar ni alimentar modelos de IA, ni interna ni externamente.
- **Sin escaneo de contenido por terceros.** El contenido no se envía a servicios externos para moderación o clasificación.
- **Sin venta de datos.** Las cuentas de edición, el contenido y los registros nunca se venden ni se comparten con terceros con fines publicitarios o comerciales.

## Federación y contenido entre instancias

Cuando las instancias de Telaris se federan, el contenido que una persona editora publica explícitamente hacia una instancia asociada viaja a esa instancia bajo firmas criptográficas. La instancia receptora aloja una réplica; la instancia de origen conserva la soberanía y puede retractar el contenido, lo que elimina la réplica.

Las cuentas de edición y los correos de quienes operan **no** cruzan los límites de la federación. La comunicación entre personas operadoras pasa por un relé que oculta los correos en ambos lados.

## Retirada del consentimiento

Una comunidad de origen, una persona editora o cualquier persona cuyo material esté alojado en una instancia de Telaris puede retirar su consentimiento en cualquier momento. Quien opera esa instancia es responsable de acatarlo. La retirada elimina el material; no requiere negociación; es definitiva.

## Contacto

Para preguntas sobre una instancia concreta, contacta a quien la opera, cuya dirección figura en el sitio de la propia instancia. Para preguntas sobre www.telaris.ca, sobre el software mismo o sobre este aviso, usa la página de [Contacto](https://www.telaris.ca/contact); la gobernanza del proyecto y la persona operadora a quien contactar sobre cómo se tratan los datos se describen en la página de [Gobernanza](https://www.telaris.ca/governance).

## Versión

Versión 1.0, vigente desde el 2026-06-04. Es la primera versión publicada; reemplaza el borrador anterior. Cuando este aviso cambie de una forma que afecte a quienes editan, la versión se incrementa y se pide revisar la nueva versión en el siguiente inicio de sesión.
