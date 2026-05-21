# Privacidad

> [!warning] Borrador
> Este documento es provisional. Está en curso una versión final del aviso de privacidad que reemplazará a este borrador. Para preguntas entre tanto, escriba a quien mantiene la instancia que está usando.

Telaris es un archivo de conocimiento decolonial de grado investigativo. La postura de privacidad descrita aquí se aplica a **www.telaris.ca** (el sitio que está leyendo) y al **software de Telaris** que se ejecuta en instancias operadas por personas independientes. Cada instancia es operada por una persona independiente y puede llevar avisos de privacidad adicionales propios; esos avisos gobiernan el contenido de la instancia. Este documento cubre el resto.

## Qué recoge www.telaris.ca

El sitio en `www.telaris.ca` es una sola página estática. No ejecuta una herramienta de análisis, no coloca rastreadores publicitarios, no instala cookies, y no recopila información personal de las visitantes. La página se sirve a través de Cloudflare; los registros estándar de acceso de Cloudflare (IP truncada, agente de usuario, URL solicitada, estado de respuesta, marca de tiempo) se conservan por períodos cortos según la política propia de Cloudflare. Más allá de esos registros de acceso, el sitio no registra visitas.

El sitio enlaza a documentos PDF descargables y a instancias independientes de Telaris. Seguir uno de esos enlaces lleva a otra página; este aviso no gobierna lo que sucede ahí.

## Qué pueden recoger las instancias de Telaris

Las instancias individuales (cualquier sitio que ejecute el software de Telaris, incluidas las tres listadas en *Instancias activas* en la página principal) pueden recopilar una pequeña cantidad de información necesaria para que el software funcione:

- **Cuentas de edición.** Cada instancia mantiene una lista de personas autorizadas a añadir contenido. El nombre de la editora, su correo electrónico y un hash de contraseña se almacenan mientras la cuenta esté activa. Quien opera la instancia puede eliminar cuentas de edición a petición.
- **Contenido editorial.** Los agujeros de gusano, galaxias, palabras clave, descripciones, medios subidos, y las relaciones entre todos ellos son almacenados por cada instancia. Esto es el contenido que la visitante ve. La soberanía editorial es el principio: la editora decide qué se publica; nada se revisa antes de mostrarse.
- **Consentimiento de la comunidad de origen.** Cuando una comunidad de origen aporta material a una instancia, el consentimiento de esa comunidad gobierna el material. La retirada del consentimiento es definitiva y la ejecuta quien opera la instancia sin negociación.
- **Registros de acceso del servidor.** Las instancias pueden conservar registros de acceso de corta duración con fines operativos (depuración, mitigación de abusos). Las direcciones IP, cuando se almacenan, se procesan con una clave del servidor (hash); las IP en texto plano no se retienen.

## Qué no hace Telaris

- **Sin publicidad.** Sin rastreadores de terceros, sin red publicitaria, sin perfilado conductual.
- **Sin entrenamiento de IA sobre el corpus.** El contenido de Telaris no se usa para entrenar modelos de IA, ni interna ni externamente.
- **Sin escaneo de contenido por terceros.** El contenido no se envía a servicios externos para moderación o clasificación.
- **Sin venta de datos.** Las cuentas de edición, el contenido y los registros de acceso no se venden ni se comparten con terceros con fines publicitarios o comerciales.

## Federación y contenido entre instancias

Cuando las instancias de Telaris se federan (una característica prevista, aún no activa al momento de este borrador), el contenido que una editora publica explícitamente hacia un socio de federación viaja a la instancia de ese socio bajo firmas criptográficas. La instancia receptora aloja un espejo del contenido; la instancia de origen conserva su soberanía.

Las cuentas de edición y los correos electrónicos de quienes operan **no** cruzan los límites de la federación. La comunicación entre quienes operan está mediada por un relé que oculta las direcciones de correo en ambos lados.

## Retirada del consentimiento

Una comunidad de origen, una editora, o cualquier persona cuyo material esté alojado en una instancia de Telaris puede retirar el consentimiento en cualquier momento. Quien opera la instancia es responsable de honrar la retirada. La retirada elimina el material; no requiere negociación; es definitiva.

## Contacto

Cada instancia de Telaris lista la dirección de contacto de quien la opera en el sitio de la propia instancia. Use ese canal para preguntas de privacidad específicas de una instancia. Para preguntas sobre www.telaris.ca, sobre el software mismo, o sobre este aviso, contacte a quien mantiene el proyecto en la página **/governance** (próximamente).

## Versión

Borrador, 2026-05-21. No reemplaza una versión anterior. Será revisado antes de su publicación definitiva.
