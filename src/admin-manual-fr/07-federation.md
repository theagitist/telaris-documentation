# Fédération et le Pluriverse

Les instances de Telaris peuvent rester seules, ou elles peuvent rejoindre une **fédération** : une famille d'instances indépendantes qui peuvent voir et partager leurs galaxies mutuellement sans qu'aucune ne commande. Ce chapitre couvre le côté de ton instance dans tout cela, et, pour la personne qui exploite le site de coordination, la surface supplémentaire qui vient avec.

La fédération est facultative. Beaucoup d'instances ne l'activent jamais, et un cours ou une archive personnelle en a rarement besoin. Tourne-toi vers ce chapitre quand tu veux que ton instance fasse partie d'un réseau plus large d'instances de Telaris.

## La forme de la chose

Une fédération est coordonnée par un **Pluriverse** : un site central qui tient le répertoire des instances membres et les aide à se trouver et à se faire confiance. Le Pluriverse est un coordinateur, pas un propriétaire ; il ne détient le contenu de personne, et aucune instance ne lui répond pour ses décisions éditoriales. Chaque instance reste souveraine sur ses propres galaxies.

Entre deux instances, le partage fonctionne dans une seule direction à la fois :

- une instance **publie** une galaxie vers un pair à qui elle fait confiance, et
- le pair **s'abonne** et tire un **miroir en lecture seule** de cette galaxie (les galaxies importées du chapitre précédent).

Rien n'est partagé tant qu'une relation de confiance et une décision de publication n'existent pas toutes deux. La fédération est un choix explicite à chaque étape : tu choisis de rejoindre, tu choisis à qui faire confiance, tu choisis quoi publier, et tu peux retirer n'importe quoi de tout cela.

## Rejoindre un Pluriverse

La participation de ton instance se gère depuis l'onglet **Pluriverse** de la console. Rejoindre est un déroulement de demande et d'admission : ton instance postule à un Pluriverse, et qui exploite ce Pluriverse l'admet. Une fois admise, ton instance apparaît dans le répertoire et peut commencer à former de la confiance avec des pairs.

![L'onglet Pluriverse sur une instance pas encore fédérée : le formulaire pour rejoindre le Pluriverse avec l'URL, le nom et le contact d'exploitation de l'instance](assets/images/admin-manual-fr/08-pluriverse.png)

## La liste des pairs

L'onglet Pluriverse montre les pairs que ton instance connaît, chacun avec son état : découvert (connu mais pas encore de confiance), de confiance (une relation de confiance mutuelle existe), ou bloqué. Une action **Rafraîchir** met à jour la liste depuis le Pluriverse maintenant, plutôt que d'attendre le rafraîchissement planifié. Il y a aussi un chemin avancé pour ajouter un pair à la main, pour un pair que tu connais directement, qui te demande de reconfirmer parce qu'ajouter un pair à la main contourne l'introduction du répertoire.

## Établir la confiance

Avant que deux instances puissent partager, elles établissent la **confiance** : une poignée de main où chacune confirme l'identité de l'autre et où toutes deux acceptent d'être pairs. Tu commences ou acceptes une poignée de main depuis la liste des pairs ; quand elle s'achève, l'état du pair devient de confiance des deux côtés. La confiance est mutuelle et symétrique ; elle ne partage, en elle-même, aucun contenu. Elle rend seulement le partage possible.

## Publier tes galaxies

Pour laisser un pair de confiance mettre en miroir une de tes galaxies, tu la lui **publies**. La publication se fait par galaxie et par pair : tu décides, pour chaque pair, lesquelles de tes galaxies il peut tirer. Une galaxie que tu n'as pas publiée est invisible aux pairs, même de confiance.

Publier partage le contenu de la galaxie, y compris ses médias, sous une forme que le pair peut vérifier comme venant de toi sans altération. Tu peux **retirer** une publication plus tard ; le miroir du pair est alors abandonné à son prochain tirage. Publier est une offre permanente, pas un envoi ponctuel : tant qu'elle tient, le miroir du pair suit tes modifications.

## S'abonner aux galaxies d'un pair

L'autre direction : quand un pair de confiance te publie une galaxie, tu peux t'y **abonner** et tirer un miroir en lecture seule. Le miroir apparaît dans ton onglet Galaxies comme une galaxie importée (chapitre précédent), en lecture seule, rafraîchissable. Tu peux te désabonner pour abandonner le miroir. Ce à quoi tu peux t'abonner est ce que tes pairs ont choisi de te publier ; tu ne peux pas tirer une galaxie qui ne t'a pas été publiée.

## Bloquer un pair

Si tu dois couper une relation, **bloque** le pair. Le blocage est l'arrêt fort : il abandonne tous les miroirs que tu as tirés de lui, retire tout ce que tu lui as publié, et arrête tout partage ultérieur dans les deux directions. Le blocage est délibérément uniforme, il ne laisse pas de contenu à moitié partagé, c'est donc la façon propre de terminer une relation qui a mal tourné. Débloquer plus tard ramène le pair à simplement découvert ; cela ne restaure pas le contenu que le blocage a abandonné, qui devrait être republié et retiré à nouveau.

## Pour qui exploite le Pluriverse

Si tu exploites le site de coordination plutôt qu'une seule instance membre, tu as une responsabilité supplémentaire : l'**admission**. De nouvelles instances postulent à ton Pluriverse, et tu décides lesquelles admettre dans le répertoire. L'admission est une étape de vérification ; tu décides qui a sa place dans cette fédération particulière. La surface de la console pour cela te laisse examiner une candidature en attente et l'admettre ou la refuser. Au-delà de l'admission, qui exploite garde le répertoire honnête : retirer une instance devenue silencieuse pour de bon, et répondre si un membre signale un problème avec un pair.

Exploiter un Pluriverse ne te donne aucun pouvoir sur le contenu ou les choix éditoriaux des membres. Cela te donne la liste des invités, pas l'archive.

## Choses qu'il vaut la peine de savoir

- **La fédération est entièrement un choix explicite et réversible.** Tu rejoins par choix, fais confiance par choix, publies par choix, et peux te retirer à chaque niveau. Rien ne se fédère par défaut.
- **Les galaxies importées sont en lecture seule et impermanentes** (chapitre précédent). Traite la galaxie publiée d'un pair comme une vue en direct, pas comme ta copie.
- **Le blocage est uniforme et définitif pour le contenu qu'il abandonne.** C'est le bon outil pour terminer proprement une mauvaise relation ; ce n'est pas une pause. Utilise la confiance et publier/retirer pour des ajustements plus doux.
- **La souveraineté est tout l'enjeu.** Aucune instance, ni le Pluriverse, ne passe outre les décisions éditoriales d'une autre. Le seul pouvoir qu'une source a sur un miroir est de cesser de publier ; le seul pouvoir que tu as sur ce que tu as importé est de cesser de t'abonner.
