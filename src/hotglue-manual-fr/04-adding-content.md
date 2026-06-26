# Ajouter du contenu

Ce chapitre couvre chaque type d'objet que tu peux poser sur une page, et les outils que chacun offre une fois sur la toile. Tu ajoutes la plupart d'entre eux depuis le **menu NEW** (clique une fois sur l'arrière-plan vide). Les outils propres à chaque objet apparaissent sous forme de petites icônes autour de lui quand tu le sélectionnes.

## Images

**Pour ajouter une image,** utilise l'outil de téléversement dans le menu NEW, ou fais simplement glisser un fichier image depuis ton ordinateur et dépose-le n'importe où sur la page. Hotglue accepte JPEG, PNG, GIF et WebP. Si tu déposes une image très grande, Hotglue la réduit automatiquement à une taille raisonnable pour la page (les GIF animés sont laissés à leur taille d'origine).

Quand une image est sélectionnée, ses outils te permettent de :

- **Activer ou désactiver la mosaïque d'image**, pour que l'image se répète et remplisse sa boîte comme un motif.
- **Réinitialiser la taille de l'image** à ses dimensions naturelles. Maintiens <kbd>shift</kbd> ou <kbd>ctrl</kbd> en le faisant pour conserver le rapport d'aspect.
- **Ajuster la sélection de l'image** en faisant glisser, pour n'en montrer qu'une partie.
- **Télécharger le fichier original**.
- **Modifier cette image dans l'éditeur de dessin** (voir *Dessins* ci-dessous).

## Texte

**Pour ajouter du texte,** choisis « ajouter un nouvel objet texte » dans le menu NEW. Une boîte de texte apparaît. Clique sur une boîte de texte sélectionnée pour en modifier les mots directement ; appuie sur <kbd>esc</kbd> pour arrêter la modification.

Les outils d'une boîte de texte te permettent de la façonner en détail :

- **Couleur d'arrière-plan** de la boîte, ou **rendre l'arrière-plan transparent**.
- **Taille de police** : fais glisser l'outil pour la changer, clique pour réinitialiser.
- **Couleur de police**.
- **Police de caractères** : clique pour faire défiler les polices disponibles.
- **Style de police** : faire défiler normal, gras et italique.
- **Hauteur de ligne**, **espacement des lettres** et **espacement des mots**.
- **Alignement du texte** : à gauche, centré, à droite, puis justifié.
- **Marge intérieure** dans la boîte.

Les boîtes de texte comprennent aussi quelques macros qui se remplissent automatiquement, comme `$BASEURL$` et `$PAGE$`. Saisis-les dans une boîte de texte et elles sont remplacées quand la page est affichée.

## Vidéo web

**Pour intégrer une vidéo,** choisis « intégrer une vidéo youtube, vimeo ou peertube » dans le menu NEW et colle l'adresse de la vidéo quand on te le demande. Hotglue reconnaît les liens YouTube, Vimeo et PeerTube (y compris les vidéos PeerTube sur n'importe quel hôte fédéré) et crée le bon lecteur intégré pour chacun.

Quand l'objet vidéo est sélectionné, ses outils te permettent de :

- **Activer ou désactiver la lecture automatique** de la vidéo (le changement prend effet après le rechargement de la page publiée).
- **Activer ou désactiver la lecture en boucle** de la vidéo (également après un rechargement).

En mode édition, une petite bande « faire glisser ici » se place par-dessus le lecteur pour que tu puisses déplacer l'objet sans que la vidéo ne capte tes clics.

## Dessins

Hotglue inclut un éditeur d'image complet dans la page (miniPaint) pour créer ou retoucher une image sans quitter la toile. Il y a deux façons d'y entrer :

- Depuis le menu NEW, choisis **dessiner une image nouvelle** pour commencer sur une toile vierge.
- Avec une image sélectionnée, choisis **modifier cette image dans l'éditeur de dessin** pour ouvrir cette image afin de la modifier.

L'éditeur de dessin s'ouvre dans une fenêtre avec les outils de peinture habituels. Quand tu as terminé, clique sur **placer sur la page** pour redéposer le résultat sur ta page Hotglue (il aplatit tes calques en une seule image), ou sur **annuler** pour l'abandonner. Si tu modifiais une image existante, la nouvelle version prend sa place.

## Son (le soundboard)

Le **soundboard** transforme une page en quelque chose que l'on peut jouer. C'est un réglage par page que tu actives depuis le menu PAGE : « activer ou désactiver le mode soundboard ». Quand il est activé, la page publiée traite tes tuiles vidéo comme des déclencheurs, et toucher une tuile lance son extrait.

Ce qui en fait un soundboard plutôt que simplement plusieurs vidéos, c'est le mixage audio :

- **Les extraits vidéo auto-hébergés** que tu as téléversés se lisent à travers un même moteur audio partagé, de sorte que plusieurs extraits peuvent retentir en même temps et se superposer. Cela fonctionne sur téléphone comme sur ordinateur.
- **Les vidéos intégrées** (YouTube, PeerTube, Vimeo) se lisent à travers les contrôles de leur propre lecteur intégré. Plusieurs peuvent se lire en parallèle ; c'est fiable sur ordinateur et plus limité sur téléphone.

Le changement prend effet après le rechargement de la page publiée. Le mode soundboard est désactivé tant que tu ne l'actives pas, donc une page ordinaire avec des vidéos se comporte normalement.

## Outils d'objet (n'importe quel objet)

Au-delà des outils par type ci-dessus, chaque objet partage un jeu commun :

- **Cloner** l'objet.
- **Changer la transparence** en faisant glisser.
- **Transformer l'objet en lien** : pointe-le vers une adresse web, une autre page ou une ancre, avec le choix facultatif de l'ouvrir dans un nouvel onglet.
- **Obtenir le nom de cet objet**, pour pouvoir y faire un lien depuis ailleurs.
- **Faire apparaître cet objet sur toutes les pages** (pratique pour un logo ou un pied de page).
- **Verrouiller** l'objet pour qu'il ne puisse pas être déplacé ou redimensionné par accident ; clique de nouveau pour déverrouiller.
- **Retourner** l'objet.
- **Supprimer** l'objet.

> [!note] Pas de code personnalisé
> La version Telaris de Hotglue laisse intentionnellement de côté les modules qui te permettraient de coller du HTML ou des scripts arbitraires. Tout ce que tu ajoutes est l'un des types de contenu ci-dessus. C'est un choix de sécurité, pas un oubli.
