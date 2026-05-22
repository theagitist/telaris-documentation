# Dépannage

Les situations quotidiennes qu'une personne qui édite rencontre, ce qu'il faut essayer, et quand demander à qui exploite ton instance. Ce chapitre est organisé par symptôme, pas par cause ; cherche ce que *tu* vois, pas ce qui se passe *techniquement*.

## Je n'arrive pas à me connecter

**Ce que tu vois** : le formulaire de connexion refuse tes identifiants, ou tu arrives à la page de connexion alors que tu t'attendais à être déjà connectée.

**Ce qu'il faut essayer**, dans l'ordre :

1. Confirme que l'adresse de courriel et le mot de passe sont corrects. Les deux sont sensibles à la casse.
2. Utilise le lien **Mot de passe oublié ?** sous le bouton Se connecter. Un courriel avec un lien de réinitialisation arrive en moins d'une minute.
3. Vérifie que tu es sur l'adresse de ton instance. Si qui exploite gère plusieurs instances, ta connexion est limitée à une seule.

**Quand demander à qui exploite** : si le lien de réinitialisation de mot de passe n'arrive pas (vérifie d'abord les courriers indésirables), si ton courriel de réinitialisation rebondit, ou si tu es sûre que ton mot de passe est correct et que le formulaire continue de refuser.

## Un trou de ver que j'ai créé a disparu

**Ce que tu vois** : un trou de ver que tu as rédigé n'est plus dans la liste de trous de ver.

**Ce qu'il faut essayer** :

1. Confirme que le menu déroulant **Galaxie courante** est sur la bonne galaxie (ou réglé sur *Toutes mes galaxies*). Le trou de ver peut être dans une galaxie différente de ce que tu attends, surtout si tu as utilisé le menu déroulant Galaxie à l'intérieur de la fenêtre de trou de ver.
2. Utilise le champ de recherche sur la page d'édition. Cherche le nom du trou de ver ; s'il existe dans n'importe quelle galaxie que tu peux éditer, la recherche le trouve.
3. Vérifie le filtre **Touchés aujourd'hui** ; si tu l'as cliqué par accident, seules les éditions du jour s'affichent.

**Quand demander à qui exploite** : si la recherche sur Toutes mes galaxies ne renvoie rien et que tu es certaine d'avoir enregistré le trou de ver. Le trou de ver a peut-être été supprimé (par toi, ou par un autre compte d'édition) ; qui exploite peut peut-être restaurer depuis un instantané.

## Je ne peux pas éditer un trou de ver ; la fenêtre s'ouvre en mode visualisation

**Ce que tu vois** : cliquer une ligne de trou de ver ouvre une fiche d'information ou un aperçu en lecture seule, pas la fenêtre de modification.

**Ce que tu pourrais voir** :

- Le trou de ver est dans une galaxie à laquelle tu as **accès en lecture** mais pas en édition (certaines instances laissent l'édition voir toutes les galaxies mais n'en éditer que certaines). Le trou de ver est éditable par un autre compte d'édition.
- Le trou de ver a été **importé** d'une source externe (une archive sœur, une communauté via un pont). Les trous de ver importés sont en lecture seule par conception ; les changements doivent se faire à la source.

**Quand demander à qui exploite** : si le trou de ver a été rédigé sur cette instance et que tu devrais avoir des droits d'édition mais que la fenêtre s'ouvre encore en lecture seule.

## Un téléversement échoue

**Ce que tu vois** : le sélecteur de fichier accepte le fichier, le téléversement commence, puis une erreur apparaît ou la fenêtre se ferme sans que le fichier soit attaché.

**Ce qu'il faut essayer** :

1. Vérifie la taille du fichier. Les PDF sont couramment plafonnés à 25 Mo (qui exploite ton instance peut avoir réglé une autre limite) ; les images et vidéos peuvent avoir leurs propres limites.
2. Vérifie le type de fichier. Telaris prend en charge JPG et PNG (et la plupart des autres formats courants) pour les images ; MP4 pour la vidéo ; MP3, OGG et WAV pour l'audio ; PDF pour les documents. Les fichiers d'autres types sont rejetés au moment du téléversement.
3. Essaie un fichier plus petit ou un format différent. Si l'original est trop gros, compresse ou transcode avant de téléverser.

**Quand demander à qui exploite** : si les téléversements échouent systématiquement pour des fichiers dans les limites annoncées, ou s'il te faut faire augmenter la limite.

## L'étiquette d'un mot-clé est au mauvais endroit sur la toile

**Ce que tu vois** : une étiquette sur la toile de mots-clés chevauche une autre étiquette, se trouve hors de la zone visible, ou flotte dans une position qui ne correspond pas à l'endroit où tu te rappelles l'avoir placée.

**Ce qu'il faut essayer** :

1. Fais glisser l'étiquette là où tu la veux ; la nouvelle position s'enregistre automatiquement.
2. Si beaucoup d'étiquettes sont mal disposées, utilise l'option **Réinitialiser toutes les positions d'étiquettes** dans la superposition d'aide de la toile (le **?** en haut de la toile).
3. Rafraîchis la page ; la toile récupère la disposition la plus récente.

**Quand demander à qui exploite** : rarement. La toile est indulgente ; presque tout problème se résout en faisant glisser.

## Un changement que j'ai fait n'apparaît pas dans la vue de qui visite

**Ce que tu vois** : tu as enregistré un changement dans l'édition, mais qui visite (ou toi dans un autre onglet) ne le voit pas.

**Ce qu'il faut essayer** :

1. Rafraîchis l'onglet de visite. Telaris ne pousse pas les mises à jour en direct ; le changement apparaît au prochain chargement de page.
2. Vérifie que tu as enregistré avec **Enregistrer**, et que tu n'as pas fermé la fenêtre avec **Annuler** ou en cliquant à l'extérieur.
3. Vérifie que tu regardes la même galaxie. L'onglet de visite peut être sur une galaxie différente de celle que tu as éditée.

**Quand demander à qui exploite** : si tu as enregistré et rafraîchi et que le changement n'est toujours pas visible après une minute. Les caches périphériques peuvent prendre un bref moment à s'invalider ; si cela persiste, c'est du territoire de qui exploite.

## Un bouton est grisé

**Ce que tu vois** : un bouton sur la page d'édition ou dans une fenêtre est visible mais pas cliquable.

**Ce que tu pourrais voir** :

- Le bouton est **conditionnel à quelque chose que tu n'as pas encore fait**. Par exemple, le bouton Paramètres à côté du sélecteur de galaxie ne s'active que quand une galaxie particulière est sélectionnée (pas *Toutes mes galaxies*).
- Le bouton est **filtré par ton rôle**. Si tu es en édition et que l'action est réservée à l'administration, le bouton peut apparaître mais rester désactivé.

**Quand demander à qui exploite** : si tu crois que tu devrais avoir accès à l'action et que le bouton reste désactivé. Ton rôle peut avoir besoin d'être ajusté.

## Ma session a expiré au milieu d'une édition

**Ce que tu vois** : un enregistrement échoue avec un message « non authentifiée » ou « veuillez vous connecter » ; l'édition te ramène à la page de connexion.

**Ce qu'il faut essayer** :

1. Reconnecte-toi. Ta session expire périodiquement ; c'est normal.
2. Si tu éditais un trou de ver quand la session a expiré et que le changement n'a pas été enregistré, tu as peut-être perdu le travail depuis le dernier enregistrement. Le texte dans la fenêtre est parfois récupérable par le comportement de restauration de formulaire du navigateur ; sinon, le trou de ver revient à son dernier état enregistré.

**Quand demander à qui exploite** : si les sessions expirent anormalement vite. La session par défaut dure 30 jours avec renouvellement par activité ; si tu es éjectée en quelques minutes, quelque chose ne va pas.

## Un message envoyé à un autre compte d'édition semble perdu

**Ce que tu vois** : tu as envoyé un message dans l'application à un autre compte d'édition (ou à qui exploite une instance) et le destinataire n'a pas répondu, ou tu ne trouves pas le message envoyé.

**Ce que tu pourrais voir** :

- Le destinataire n'a pas encore ouvert sa boîte de réception.
- La surface de messagerie dans l'application peut vivre dans une section de l'interface d'administration à laquelle tu n'as pas accès. La plupart des communications entre comptes d'édition se gèrent mieux en dehors de Telaris (courriel, Signal, ce que qui exploite et ton équipe ont convenu d'utiliser).

**Quand demander à qui exploite** : si la messagerie dans l'application est le canal canonique sur ton instance et qu'un message que tu as envoyé par ce biais n'arrive pas au destinataire.

## Un trou de ver s'ouvre sur une fiche d'information vide

**Ce que tu vois** : cliquer un trou de ver ouvre la fiche d'information mais sans description, sans média, sans mots-clés.

**Ce qu'il faut essayer** :

1. Vérifie que le trou de ver que tu as ouvert est celui pour lequel tu voulais rédiger du contenu. Les trous de ver vides sont permis ; ils n'ont juste pas de corps.
2. Ouvre le trou de ver dans l'édition et confirme que le champ Description a le texte attendu.
3. Si la description apparaît dans l'édition mais pas dans la vue de qui visite, rafraîchis les deux onglets du navigateur.

**Quand demander à qui exploite** : si le trou de ver a du contenu dans l'édition mais est vide dans la vue de qui visite après rafraîchissement.

## La scène 3D est lente ou saccadée

**Ce que tu vois** : la scène 3D de visite met longtemps à se charger, s'anime de manière saccadée, ou se fige brièvement.

**Ce que tu pourrais voir** :

- Une galaxie dense sur un appareil plus ancien. La scène 3D fonctionne dans le navigateur de qui visite ; les galaxies très denses sont exigeantes sur du matériel peu puissant.
- Une galaxie avec beaucoup de trous de ver à icône-image (chaque image se rend dans la scène comme une texture).

**Ce qu'il faut essayer** :

- Suggère à qui visite de basculer en **vue 2D** (chapitre 10) si elle est activée sur la galaxie.
- Pour les galaxies que tu rédiges, considère si tous les drapeaux d'image-comme-icône sont nécessaires ; une galaxie avec douze trous de ver à icône-image est plus rapide qu'une avec cinquante.

**Quand demander à qui exploite** : si la lenteur est universelle (chaque personne qui visite la voit) et pas propre à un appareil.

## Je ne sais pas qui exploite cette instance

**Ce que tu vois** : ce manuel n'arrête pas de te dire de « demander à qui exploite ». Si tu ne sais pas qui c'est, il te faut le savoir.

**Ce qu'il faut essayer** :

- Vérifie l'adresse de ton instance. Beaucoup d'instances ont une page de contact à `/contact` ou une page de gouvernance à `/governance` qui nomme qui exploite.
- Regarde le courriel original qui t'a invitée à éditer. L'expéditeur est le plus souvent qui exploite.
- À défaut, la prochaine personne qui édite ou qui visite avec qui tu parles de Telaris en saura probablement quelque chose.

Si tu ne peux pas identifier qui exploite du tout, c'est en soi une sorte de problème qui mérite d'être résolu ; une instance sans personne joignable est une instance qui dérive.
