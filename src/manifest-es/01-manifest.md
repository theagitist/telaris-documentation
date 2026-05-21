# Manifiesto

> [!warning] Borrador
> Este Manifiesto es un borrador, escrito el 2026-05-21. Se refinará a medida que la documentación madure.

Una declaración de qué es Telaris, qué rehúsa, y los principios que lo sostienen. Escrita para cualquiera que se acerque al proyecto desde fuera: una posible operadora, una comunidad de origen que evalúa si contribuir, una estudiante que lee la documentación, una curadora que sopesa si usar el software. El resto de la documentación se apoya en las posiciones que se nombran aquí.

## Qué es Telaris

Un proyecto de archivo de conocimiento decolonial. Relacional, no jerárquico, federado entre pares, hilado por el significado. El contenido vive en **galaxias**: agrupaciones de pequeñas unidades de contenido (un pasaje, una imagen, un sonido, un fragmento de película, un documento) que se conectan a través de **palabras clave** compartidas. No hay carpetas, ni padres, ni migas de pan, ni algoritmo; la estructura es un rizoma que mantienen las personas editoras y que lee la visitante como una escena tridimensional.

Telaris es un proyecto de investigación de posgrado en el Instituto de Género, Raza, Sexualidad y Justicia Social (GRSJ) de la Universidad de British Columbia. Es software de código abierto ejecutado por operadoras independientes en distintos países y comunidades, no una plataforma con un único dueño.

## Decolonial como método, no como metáfora

"Decolonial" nombra una práctica, no una estética. La práctica tiene consecuencias concretas en cómo está diseñado y operado Telaris:

- Rechazo de reducciones categóricas impuestas: no hay vocabulario central, ni ontología obligatoria, ni jefatura editorial.
- Soberanía de los datos para las comunidades de origen: las personas cuyo material está alojado en una instancia de Telaris conservan autoridad sobre él; la retirada del consentimiento es definitiva y se ejecuta sin negociación.
- Soberanía editorial para quienes editan: cada editora decide qué publicar en las galaxias que cuida; no existe una cola de revisión, ni un flujo de aprobación.
- Soberanía operativa para quienes administran instancias: cada operadora ejecuta su instancia bajo sus propias reglas; ninguna autoridad central dicta contenido o acceso.

Son decisiones de método, no consignas. Aparecen en el código (sin función de cola de revisión, sin tabla de vocabulario central, sin anulación del administrador de plataforma) tanto como en la documentación.

## Qué no es Telaris

Un rechazo claro es una posición más clara que un manifiesto largo.

- **No es una plataforma.** No hay un único dueño. No hay catálogo central. No hay publicidad. No hay seguimiento. No se vende ni se comparten datos con fines comerciales.
- **No es un corpus de entrenamiento para IA.** El contenido de Telaris no se usa para entrenar modelos de IA, ni interna ni externamente. El corpus no se envía a proveedores de modelos de lenguaje para moderación, clasificación, resumen, ni ningún otro propósito.
- **No es una jerarquía.** No hay estructura en árbol sobre el contenido. No hay cola de revisión editorial. No hay "mejor contenido" promovido por un algoritmo.
- **No es extractivo.** El contenido aportado por comunidades de origen no se convierte en propiedad de Telaris. Las personas editoras no pierden la autoría al publicar en Telaris. Las operadoras no tienen derechos sobre el contenido editorial más allá de lo que el contrato de cada instancia haga explícito.
- **No es anónimo por defecto.** La atribución viaja con la obra. La autoría de la editora queda registrada; el nombre de la comunidad de origen queda registrado; la licencia (cuando se suministra) queda registrada. El anonimato está disponible cuando una editora o comunidad lo solicita, no por defecto.

## Principios, seis

**1. Soberanía editorial.** Quienes editan deciden qué publicar en las galaxias que cuidan. No hay cola de revisión, ni vocabulario aprobado centralmente, ni palabra clave "incorrecta". El costo es responsabilidad: la decisión de quien edita es de quien edita; el software no la vigila.

**2. Consentimiento de la comunidad de origen.** Cuando una comunidad aporta material, el consentimiento de esa comunidad gobierna el material. La retirada del consentimiento es definitiva. La operadora ejecuta la retirada sin negociación, sin importar la posición editorial que esa operadora pueda tener.

**3. Soberanía operativa.** Cada instancia de Telaris la opera una persona independiente bajo sus propias reglas. No hay autoridad central sobre las operadoras. Las operadoras acuerdan un pequeño conjunto de compromisos de red (identidad criptográfica, honrar las retiradas de federación, atenerse a estos principios) pero por lo demás gobiernan sus instancias de manera independiente.

**4. Federación, no P2P puro.** Las galaxias tienen orígenes autoritativos únicos; las instancias pares las espejan en modo lectura; no hay conflictos de fusión, no hay edición desde cualquier lugar. La federación es bilateral y basada en consentimiento: dos operadoras se federan solo cuando ambas están de acuerdo, y cualquiera puede retirarse en cualquier momento. La terminología rechaza tanto la afirmación deshonesta de "P2P puro" (que Telaris no es) como el patrón de plataforma con una autoridad central (que Telaris rechaza).

**5. Rechazo del patrón de plataforma.** A cada decisión de diseño se le pregunta lo mismo: *¿esto importa el patrón de plataforma que Telaris está construido para rechazar?* Inicio de sesión único, telemetría publicitaria, moderación central, algoritmos conductuales, formatos cerrados, vocabularios cautivos. La respuesta determina si la decisión entra.

**6. Software de código abierto, contenido bajo la licencia de quien edita.** El software de la instancia de Telaris es de código abierto bajo GPL v3; la capa central de coordinación (el Pluriverso, cuando se publique) es AGPL v3. El contenido editorial lleva la licencia que la editora o la comunidad de origen suministre, adjunta a cada pieza de contenido. El software se entrega; el contenido no se anexa al regalo.

## De dónde viene Telaris

El proyecto se llama *Telaris* (del latín *tela*, una red tejida). Se apoya en:

- *Designs for the Pluriverse* y *Pluriversal Politics* de Arturo Escobar.
- *The Darker Side of Western Modernity* de Walter Mignolo.
- *Constructing the Pluriverse* editado por Bernd Reiter.
- *Discurso sobre el colonialismo* de Aimé Césaire.
- Los archivos Mocambos / Baobáxia y la tradición quilombola del archivo digital comunitario.
- *African Fractals* de Ron Eglash, por una comprensión fractal-como-estructura asentada fuera del canon matemático europeo.
- El conocimiento forestal de los pueblos indígenas del Noroeste del Pacífico y la metáfora de la red micorrízica en Suzanne Simard y Robin Wall Kimmerer, por la imagen de intercambio mutuo de la federación.

Son referencias, no autoridades. El proyecto se sitúa en conversación con este cuerpo de trabajo y aporta un pequeño artefacto técnico. La corrección del artefacto frente a la política que reclama es la prueba en torno a la cual está estructurada la documentación.

## Qué es este documento

Una declaración de posición, mantenida corta a propósito. La arquitectura completa, las convenciones editoriales, los manuales de operación y la especificación de federación viven en sus propios documentos. Lea este para saber dónde está Telaris; lea los otros para saber cómo funciona.
