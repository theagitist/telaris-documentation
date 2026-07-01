# Sauvegardes et instantanés

Une instance, c'est du contenu, et le contenu devrait être récupérable. Telaris te donne deux outils apparentés : des **sauvegardes** que tu télécharges et gardes, et des **instantanés** que l'instance prend et stocke pour toi, sur un calendrier si tu veux. Ce chapitre couvre les deux, et comment restaurer.

## Sauvegardes (l'onglet Sauvegarde)

![L'onglet Sauvegarde : un panneau Télécharger une sauvegarde et un panneau Restaurer à partir d'une sauvegarde](assets/images/admin-manual-fr/09-backup.png)

L'onglet **Sauvegarde** a deux moitiés :

- **Télécharger une sauvegarde** produit un seul fichier capturant le contenu de l'instance, que ton navigateur télécharge. Garde-le dans un endroit sûr et hors du serveur. C'est la copie que tu prends avant quoi que ce soit de risqué, et la copie que tu utiliserais pour déplacer une instance ou récupérer d'un serveur perdu.
- **Restaurer à partir d'une sauvegarde** prend un fichier de sauvegarde et le recharge dans l'instance, en remplaçant le contenu actuel. Restaurer est destructeur pour ce qui est là maintenant, donc Telaris confirme d'abord. Restaure sur une instance neuve ou destinée à être écrasée ; ne restaure pas par-dessus du contenu que tu veux encore.

Une sauvegarde est portable : tu peux la restaurer sur une autre instance pour cloner ou migrer. Rappelle-toi, d'après *Paramètres globaux*, que le mot de passe du courriel n'est jamais dans une sauvegarde ; après avoir restauré, ressaisis les réglages de courriel pour que l'instance restaurée puisse envoyer.

## Instantanés (l'onglet Instantanés)

Là où une sauvegarde est un fichier dont tu prends soin, un **instantané** est une copie que l'instance garde pour toi. L'onglet Instantanés a trois parties :

- **Créer un instantané maintenant** prend un instantané à la demande. Fais-le avant un changement en masse ou toute modification dont tu n'es pas sûre, pour qu'il y ait un point récent où revenir.
- **Planificateur d'instantanés** prend des instantanés automatiquement à un intervalle que tu fixes, et en garde un nombre glissant, pour qu'il y ait toujours un instantané récent sans que tu penses à en faire un. Active-le pour toute instance dont le contenu compte.
- **Instantanés disponibles** liste les instantanés en réserve, du plus récent au plus ancien, chacun restaurable sur place.

Les instantanés sont le filet de sécurité du quotidien : bon marché, fréquents, et à portée de main. Les sauvegardes sont l'assurance hors site : moins nombreuses, délibérées, et gardées à l'écart du serveur. Utilise les deux, les instantanés pour « annuler », les sauvegardes téléchargées pour « le serveur a disparu ».

## Restaurer

Restaurer, à partir d'une sauvegarde téléchargée ou d'un instantané stocké, remplace le contenu actuel par le contenu enregistré. Parce que cela écrase, traite-le comme un acte réfléchi :

1. Assure-toi que tu restaures la version que tu veux. Les instantanés sont horodatés ; vérifie l'heure.
2. Comprends que les modifications faites depuis ce point auront disparu après la restauration.
3. Au moindre doute, télécharge d'abord une sauvegarde de l'état *actuel*, pour que même l'état que tu es sur le point d'écraser soit récupérable.

Quand une restauration s'achève, la console le confirme. Reconnecte-toi si la session a été affectée, et vérifie une galaxie au hasard pour confirmer que le contenu est bien ce que tu attendais.

## La bannière d'incohérence de schéma

Telaris garde la structure de sa base de données au pas avec le code en marche, automatiquement ; quand tu déploies une nouvelle version, l'instance met sa propre structure à jour toute seule. Si le code et la structure de la base de données ne s'accordent jamais d'une façon que l'instance ne peut pas réconcilier silencieusement, la console montre une **bannière d'incohérence de schéma**. C'est un signal qu'un déploiement ne s'est pas terminé proprement, pas un état de routine. Si tu la vois, la réponse sûre est de t'assurer que l'instance exécute la version voulue du code et de la laisser achever sa mise à jour de structure ; si elle persiste, c'est le moment de regarder le déploiement ou de demander à qui gère le serveur. Ne restaure pas une sauvegarde pour « réparer » une bannière de schéma ; restaurer du contenu ne change pas l'incohérence code-contre-structure.

## Choses qu'il vaut la peine de savoir

- **Sauvegarde avant tout ce qui est irréversible.** Un changement en masse, une restauration, une grosse suppression : prends d'abord un instantané ou télécharge une sauvegarde. Cela coûte des secondes et sauve le jour où tu en as besoin.
- **Garde au moins une sauvegarde hors du serveur.** Un instantané stocké sur le même serveur n'aide en rien si c'est le serveur que tu perds. Télécharge une sauvegarde périodiquement et garde-la ailleurs.
- **Le mot de passe du courriel n'est ni dans les sauvegardes ni dans les instantanés.** Après avoir restauré ou cloné, ressaisis les réglages de courriel (*Paramètres globaux*).
- **Teste une restauration avant d'en dépendre.** Si la récupération compte, prouve qu'une sauvegarde se restaure proprement sur une instance de rechange une fois, plutôt que de découvrir un problème pendant une vraie récupération.
