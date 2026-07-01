# Vues pour qui visite

Le travail de l'édition est lu par qui visite. Presque chaque choix éditorial que tu fais finit par apparaître côté visite, soit directement (la description, les médias, les mots-clés), soit indirectement (les relations tracées sur la toile de mots-clés, la manière dont les trous de ver sont étiquetés). Ce chapitre est ta carte de ce que voit qui visite, et des interrupteurs côté édition qui le façonnent.

La vue de visite s'atteint en suivant n'importe quelle URL de visite de ton instance : typiquement le segment de galaxie, parfois sans segment du tout (qui exploite ton instance peut confirmer le chemin d'entrée).

![Scène 3D pour qui visite la galaxie de démonstration Plantes côtières](assets/images/editor-manual-fr/13-visitor-scene.png)

## La scène 3D

La vue par défaut pour qui visite est une scène tridimensionnelle où chaque trou de ver est un petit objet qui flotte dans l'espace contre le fond du thème choisi de la galaxie. La souris de qui visite fait pivoter la vue ; le défilement ou le pincement zoome ; cliquer sur un trou de ver ouvre sa fiche d'information.

Ce que tu choisis en édition et qui apparaît ici :

- **Le thème de la galaxie** (chapitre 4) contrôle l'apparence : quelles icônes rendent les trous de ver, à quoi ressemble le fond, à quoi se sent l'éclairage.
- **La bascule Utiliser comme icône** sur chaque trou de ver (chapitre 5) décide si ce trou de ver se rend comme son image (quand elle est activée) ou comme l'icône par défaut du thème (quand elle est désactivée).
- **Le drapeau Mettre en avant** sur un trou de ver le rend plus grand et plus saillant dans la scène.
- **Le drapeau Afficher les mots-clés** imprime les mots-clés du trou de ver comme étiquettes flottantes à côté de l'icône.

Ces quatre choix interagissent : une galaxie de trous de ver mis en avant, à icônes-images, qui affichent leurs mots-clés est une scène chargée ; une galaxie de trous de ver à icône de thème, sobres, est une scène calme. Il n'y a pas de « bon » mode ; choisis le registre visuel qui correspond au registre éditorial du contenu.

## La fiche d'information

Qui visite et clique un trou de ver voit sa **fiche d'information** s'ouvrir au-dessus de la scène. La fiche contient, dans l'ordre :

- Le **nom** du trou de ver en haut.
- Le **visuel principal** (image, vidéo ou PDF) sous le nom, dimensionné à la fiche.
- La **description** en paragraphe de corps.
- Le **lecteur audio** si un audio est attaché.
- Le **code à intégrer** s'il a été fourni.
- Une rangée d'**étiquettes de mots-clés** en bas de la fiche, chacune cliquable.
- Le bouton **Ouvrir le lien** si le trou de ver porte une URL.

Quand qui visite clique une étiquette de mot-clé sur la fiche d'information, la scène atténue les trous de ver qui ne portent pas ce mot-clé. La fiche se ferme. C'est une des principales manières dont qui visite navigue par étiquettes plutôt que par nom.

## Les bascules de découverte

La fenêtre de paramètres de galaxie porte une section Découverte (le chapitre 4 a présenté la fenêtre ; voici ce que chaque bascule fait côté visite) :

![Fenêtre de paramètres de galaxie, descendue jusqu'aux bascules de découverte](assets/images/editor-manual-fr/12-galaxy-discovery-section.png)

Chaque bascule est désactivée par défaut. Active-en une quand tu veux la fonctionnalité correspondante.

### Visite automatique

Une visite qui se déroule toute seule à travers la galaxie. Quand elle est activée, des options supplémentaires apparaissent :

- **Mode de démarrage** (manuel, inactivité, immédiat) :
  - **Manuel** : qui visite doit appuyer sur un bouton Lecture pour lancer la visite.
  - **Inactivité** : la visite démarre automatiquement après que qui visite n'a pas interagi avec la scène pendant un certain nombre de secondes (configurable).
  - **Immédiat** : la visite démarre dès que qui visite arrive sur la galaxie.
- **Sélection de nœuds** (tous, mis en avant, N aléatoires, mots-clés étiquetés) :
  - **Tous** : la visite parcourt chaque trou de ver de la galaxie dans l'ordre.
  - **Mis en avant uniquement** : ne parcourt que les trous de ver marqués Mettre en avant.
  - **N aléatoires** : choisit N trous de ver au hasard à chaque session ; le nombre est configurable.
  - **Mots-clés étiquetés** : ne parcourt que les trous de ver porteurs d'un mot-clé d'un ensemble choisi. La liste de mots-clés se règle dans un sous-champ qui apparaît quand cette option est sélectionnée.
- **Durée de pause** en secondes à chaque arrêt, avant que la visite n'avance au suivant.
- **Boucle** : quand elle est activée, la visite revient au début après le dernier arrêt ; quand elle est désactivée, elle s'arrête tranquillement.

Un bouton **Aperçu de la visite** apparaît à côté des champs de visite automatique ; le sélectionner ouvre la vue de visite dans un nouvel onglet avec la visite en cours, pour que tu puisses vérifier la cadence sans enregistrer la configuration.

Le chapitre 11 parcourt les visites plus en profondeur.

### Projecteur en veille

Quand il est activé, la scène met doucement un trou de ver différent en lumière toutes les N secondes pendant que qui visite est inactive. Contrairement à la visite automatique, il ne déplace pas la caméra et n'ouvre pas de fiche d'information ; il fait simplement avancer un trou de ver, doucement, comme un musée qui change l'éclairage de la salle.

Deux réglages :

- **Seuil d'inactivité** en secondes avant que le projecteur ne commence.
- **Sélection** (tous, mis en avant uniquement).

Le projecteur en veille convient bien aux galaxies à sensation ambiante (un cycle de poèmes ; une séquence de photographies) ; il donne à la pièce quelque chose à faire quand qui visite a cessé de cliquer.

### Étiquettes de mots-clés

Quand elle est activée, la scène peint une bande d'étiquettes pastel en bas de l'écran de qui visite, une étiquette par mot-clé le plus utilisé dans la galaxie. Qui visite peut cliquer une étiquette pour atténuer chaque trou de ver qui ne la porte pas.

À utiliser quand la galaxie a un vocabulaire de mots-clés fort que qui visite parcourrait naturellement ; à désactiver quand les mots-clés sont trop fins ou trop nombreux pour que les étiquettes soient utiles.

### Trous de ver liés

Quand elle est activée, une fiche d'information s'ouvre avec jusqu'à cinq étiquettes de trous de ver **liés** en bas : d'autres trous de ver (dans cette galaxie ou dans des galaxies sœurs) qui partagent au moins un mot-clé avec celui ouvert. Qui visite peut cliquer une étiquette pour sauter directement au trou de ver lié.

C'est la principale manière dont qui visite voyage latéralement à travers un réseau sans ouvrir de portail. Active-la quand tu veux que qui visite découvre la toile ; désactive-la quand tu veux que qui visite reste concentrée sur un trou de ver à la fois.

### Vue 2D

Quand elle est activée, une petite bascule **3D / 2D** apparaît en haut de l'écran de qui visite. Passer en 2D rabat la scène sur une carte plate d'étiquettes de trous de ver : chaque étiquette est l'icône du trou de ver plus son nom. La vue 2D se charge plus vite et est plus facile à parcourir ; qui visite la préfère parfois pour trouver un trou de ver précis rapidement.

La carte 2D peut être **zoomée et déplacée** (défile ou pince pour zoomer, fais glisser pour déplacer), et un contrôle **Fit** ramène tous les trous de ver dans la vue d'un seul coup, pour que rien ne reste empilé hors de l'écran, peu importe le nombre de trous de ver que contient la galaxie. Quand plus d'une galaxie est en vue (une union de galaxies, chapitre 12), la liste de galaxies à côté de la carte atténue les galaxies que tu ne pointes pas, et chaque étiquette de trou de ver porte le nom de sa galaxie en préfixe pour que tu puisses distinguer des trous de ver aux noms identiques.

Le choix de qui visite entre 3D et 2D persiste dans son navigateur (tu n'as pas à choisir à nouveau).

## Pieds de provenance et attribution

Quand la provenance éditoriale d'un trou de ver porte une attribution (`Attribution de l'image`, crédit de communauté source, ou mention de miroir fédéré), la fiche d'information le montre comme une petite ligne de pied sous la description.

Il n'y a pas de bascule globale pour masquer les pieds de provenance ; si ton travail crédite une photographe ou une communauté source, ce crédit apparaît chaque fois que le trou de ver est ouvert. L'attribution d'autrice et le consentement de la communauté source sont des préoccupations éditoriales de premier ordre ; le chapitre 13 couvre la discipline éditoriale autour d'elles.

## Choses qu'il vaut la peine de savoir

- **Qui visite voit ce que tu as publié, pas ton brouillon.** Il n'y a pas de mode « aperçu » séparé de la vue publiée ; dès que tu enregistres un trou de ver ou un paramètre de galaxie, le prochain chargement de page côté visite reflète le changement. Pour prévisualiser un changement sans affecter qui visite, il faudrait faire le changement dans une galaxie qui n'est pas encore publique.
- **La scène 3D fonctionne dans le navigateur de qui visite.** Les appareils plus anciens ou les ordinateurs peu puissants peuvent peiner avec des galaxies très denses. La bascule vers la vue 2D est le remède standard.
- **L'audio à lecture automatique peut être bloqué par le navigateur de qui visite.** La plupart des navigateurs n'autorisent pas l'audio à démarrer sans une interaction de qui visite. Si tu actives la lecture automatique (chapitre 6) et que qui visite signale l'absence de son, c'est la cause la plus probable ; le premier clic de qui visite sur la page débloque généralement l'audio. Une galaxie dotée d'un paysage sonore affiche un petit contrôle **son activé/désactivé** dans la scène ; la première fois que qui visite l'active, le paysage sonore démarre (la même règle de geste du navigateur s'applique).
- **Les bascules de découverte sont indépendantes les unes des autres.** Visite automatique et projecteur en veille peuvent être activés en même temps (le projecteur prend le relais si la visite se termine ou n'est pas lancée). Choisis les combinaisons qui correspondent à ton intention éditoriale ; les bascules ne se conditionnent pas mutuellement.
