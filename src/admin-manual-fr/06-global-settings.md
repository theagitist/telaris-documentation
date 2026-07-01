# Paramètres globaux

L'onglet **Paramètres globaux** contient les interrupteurs à l'échelle de l'instance : comment l'instance se nomme, quelle galaxie accueille qui visite, quelle taille un téléversement peut atteindre, comment les mots-clés correspondent, comment elle envoie du courriel, à quelle adresse elle répond, quelle langue elle utilise par défaut, et si l'édition est activée du tout. Ces paramètres sont stockés dans la base de données propre de l'instance, donc tu les changes ici dans la console plutôt qu'en modifiant des fichiers sur le serveur.

![L'onglet Paramètres globaux : le nom de l'instance, la galaxie par défaut, la limite de téléversement, l'interrupteur de correspondance approximative, et (plus bas) les réglages de courriel et du site](assets/images/admin-manual-fr/07-global-settings.png)

## Les bases de l'instance

Le haut de l'onglet réunit les faits simples sur l'instance :

- **Nom.** Le nom public de l'instance. Il s'affiche du côté visiteur et devient l'étiquette de l'instance dans le répertoire du Pluriverse si tu demandes à publier (chapitre 7). Laissé vide, il prend par défaut la première partie du nom d'hôte.
- **Galaxie par défaut.** Quelle galaxie voit qui visite à la racine du site, avant d'en choisir une. Choisis la galaxie qui doit être la porte d'entrée.
- **Taille maximale du PDF (Mo).** Le plus gros PDF qu'un trou de ver peut porter, en mégaoctets (25 par défaut). Qui édite et téléverse un fichier plus gros est averti que le fichier dépasse la limite. Augmente-la si ton contenu en a besoin et si ton serveur a la place.
- **Correspondance approximative des mots-clés.** L'interrupteur à l'échelle de l'instance pour la correspondance assouplie décrite dans *Galaxies et amas* : quand il est activé, les graphies proches se connectent entre galaxies, pas seulement les mots identiques. Désactivé par défaut. Un amas peut remplacer ce réglage dans ses propres paramètres.


## Réglages de courriel

Presque tout ce que Telaris envoie par courriel, liens de connexion, confirmations d'inscription, notifications, dépend de la capacité de l'instance à envoyer du courriel. Le formulaire des réglages de courriel est l'endroit où tu configures cela :

- **Hôte SMTP** et **port** de ton relais de courriel.
- **Nom d'utilisateur** et **mot de passe** du relais.
- **Chiffrement** (typiquement TLS).
- **Adresse d'expéditeur** et **nom d'expéditeur** que voient les destinataires.

Deux aides accompagnent le formulaire :

- Un bouton **Envoyer un courriel de test** envoie un message de test à une adresse que tu indiques, pour que tu puisses confirmer que les réglages fonctionnent avant de compter dessus.
- Un **avertissement de non-configuration**. Tant que le courriel n'est pas en place, la console montre un avertissement, et les endroits qui dépendent du courriel (les réglages d'inscription autonome, entre autres) le répètent, parce qu'activer une fonctionnalité qui a besoin de courriel pendant que le courriel est cassé ne produit que des échecs silencieux.

Si le courriel n'est pas configuré, les comptes sans mot de passe ne peuvent pas se connecter et l'inscription autonome ne peut pas fonctionner, parce que les deux reposent sur des liens envoyés par courriel. Configure le courriel avant d'activer l'un ou l'autre.

> [!important] Le mot de passe du courriel est le seul secret ici
> Le mot de passe SMTP est la seule valeur sensible dans ces réglages. Telaris le traite à part : il n'est jamais inclus dans aucune sauvegarde, aucun instantané, ni aucune exportation de fédération. Cela veut dire qu'il est sûr de partager une sauvegarde, mais aussi que restaurer une instance ailleurs n'emportera pas le mot de passe ; tu le ressaisis après une restauration. Le chapitre *Sauvegardes et instantanés* y revient.

## Réglages du site

Ceux-ci renseignent l'instance sur elle-même :

- **Nom d'hôte de l'instance** et **URL de base** : l'adresse à laquelle l'instance est atteinte. Telaris s'en sert pour construire les liens qu'elle met dans les courriels, pour qu'ils pointent au bon endroit, quelle que soit la façon dont une requête donnée est arrivée. Fixe-les à ta véritable adresse publique.
- **Langue par défaut** : la langue que voit qui visite avant tout choix qui lui est propre, parmi l'anglais, l'espagnol, le portugais ou le français. Fixe-la à la langue de ton public.

Fixer ici le nom d'hôte et l'URL de base veut dire que tu n'as pas à modifier des fichiers de configuration à la main pour rendre les liens de courriel corrects ; la console est la source de vérité pour eux.

## Les interrupteurs de l'instance

Un interrupteur ici décide d'une fonctionnalité entière de l'instance :

- **Autoriser la modification.** Le bout au niveau de l'instance de la cascade de modification (voir *Contrôle d'accès de l'édition*). Désactive-le pour figer toute la modification sur l'instance d'un coup, par exemple quand un projet s'est terminé, tout en gardant chaque compte et tout ce qui a été rédigé. Activé par défaut.

## Choses qu'il vaut la peine de savoir

- **Ces réglages vivent dans la base de données, pas dans un fichier.** Les changer ici prend effet sans toucher au serveur. Ils l'emportent aussi sur les valeurs de repli inscrites dans le fichier de configuration de l'instance, donc la console est là où tu devrais les changer.
- **Teste le courriel après tout changement.** Le bouton Envoyer un courriel de test existe pour que tu ne découvres jamais un relais cassé par le biais d'un compte d'édition qui n'a pas pu se connecter. Utilise-le chaque fois que tu touches aux réglages de courriel.
- **L'adresse d'expéditeur devrait être une adresse réelle et autorisée à envoyer, à ton domaine.** Les relais et les destinataires rejettent de plus en plus le courriel dont l'adresse d'expéditeur n'est pas autorisée à envoyer ; fixe-la à quelque chose que ton relais a le droit d'envoyer.
