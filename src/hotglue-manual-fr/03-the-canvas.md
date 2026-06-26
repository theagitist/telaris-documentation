# La toile

Ce chapitre est le cœur du manuel : comment fonctionne la surface d'édition une fois que tu l'as ouverte.

## Le mode édition

Une page Hotglue a deux états : la vue publiée que voient les personnes qui visitent, et le **mode édition**, où tu peux changer des choses. Tu entres en mode édition par les boutons décrits dans *Entrer*. En mode édition, la page se dote de ses menus et chaque objet devient déplaçable.

![Une page Hotglue ouverte sur la toile d'édition : un bandeau de titre, un sous-titre et deux colonnes de texte, chacune un objet distinct que tu peux déplacer](assets/images/hotglue-manual-fr/03-canvas.png)

## Les deux menus

Presque tout ce que tu fais part de l'un de deux menus, et celui que tu obtiens dépend de la façon dont tu cliques sur l'arrière-plan vide de la page :

- **Clique une fois sur l'arrière-plan** pour ouvrir le **menu NEW** : les outils pour ajouter des choses à la page (téléverser un fichier, ajouter du texte, intégrer une vidéo, dessiner une image). Le raccourci clavier est <kbd>alt</kbd> + <kbd>o</kbd>.

  ![Le menu NEW ouvert sur la toile : de petites icônes pour ajouter un dessin, du texte, un fichier téléversé, une image et une vidéo](assets/images/hotglue-manual-fr/04-new-menu.png)

- **Double-clique sur l'arrière-plan** pour ouvrir le **menu PAGE** : les outils qui touchent la page entière (couleur et image d'arrière-plan, la grille). Le raccourci clavier est <kbd>alt</kbd> + <kbd>p</kbd>.

  ![Le menu PAGE ouvert sur la toile : une grille d'outils pleine page incluant titre, URL de page, page de démarrage, couleur et image d'arrière-plan, et la grille](assets/images/hotglue-manual-fr/05-page-menu.png)

Quand tu **sélectionnes un objet** (en cliquant dessus), un troisième jeu d'outils apparaît : le **menu contextuel** propre à l'objet, un éventail de petites icônes autour de l'objet. Les icônes diffèrent selon le type d'objet (une image a des outils différents d'une boîte de texte), et elles sont couvertes par type dans *Ajouter du contenu*.

## Placer, sélectionner et déplacer

**Ajouter un objet** le place là où tu as cliqué (pour les éléments de menu) ou là où tu l'as déposé (pour le glisser-déposer). Tu peux ensuite le déplacer n'importe où.

**Sélectionner :**

- Clique sur un objet pour le sélectionner.
- Maintiens <kbd>shift</kbd> et clique pour ajouter d'autres objets à la sélection (ou en retirer un).
- Clique sur l'arrière-plan vide pour tout désélectionner.
- <kbd>ctrl</kbd> + <kbd>A</kbd> sélectionne tous les objets, <kbd>ctrl</kbd> + <kbd>D</kbd> n'en sélectionne aucun, <kbd>ctrl</kbd> + <kbd>I</kbd> inverse la sélection, et <kbd>tab</kbd> parcourt les objets un par un.

**Déplacer :**

- Fais glisser un objet sélectionné avec la souris.
- Maintiens <kbd>shift</kbd> en faisant glisser pour verrouiller le mouvement sur un seul axe (purement horizontal ou purement vertical).
- Maintiens <kbd>ctrl</kbd> en faisant glisser pour ignorer la grille d'aimantation et placer l'objet librement.
- Les touches fléchées décalent une sélection d'un pixel à la fois ; <kbd>shift</kbd> + une touche fléchée la déplace d'un pas de grille.

**Redimensionner :** fais glisser la poignée de redimensionnement au coin d'un objet sélectionné. Un petit affichage montre la largeur, la hauteur et la position en direct pendant que tu fais glisser. Maintiens <kbd>ctrl</kbd> pour redimensionner sans la grille.

**Supprimer :** appuie sur <kbd>delete</kbd> avec un objet sélectionné, ou utilise l'icône de suppression propre à l'objet.

## Calques et ordre d'empilement

Quand des objets se chevauchent, tu contrôles lequel se place devant :

- Fais glisser l'icône de premier plan/arrière-plan de l'objet vers la gauche ou la droite pour l'avancer ou le reculer d'un pas à la fois.
- <kbd>shift</kbd> + <kbd>page up</kbd> amène la sélection tout à l'avant ; <kbd>shift</kbd> + <kbd>page down</kbd> l'envoie tout à l'arrière.

## La grille et l'aimantation

Par défaut, les objets s'aimantent à une grille invisible quand tu les déplaces et les redimensionnes, ce qui garde une mise en page nette. Depuis le menu PAGE, tu peux afficher ou masquer la grille, et tu peux changer son espacement en faisant glisser l'outil de grille (l'affichage montre la taille sous la forme NxN). Pour placer un seul objet hors de la grille sans changer la grille elle-même, maintiens <kbd>ctrl</kbd> pendant que tu le fais glisser ou le redimensionnes.

## L'arrière-plan

Depuis le menu PAGE, tu peux :

- **Changer la couleur d'arrière-plan** avec une roue chromatique (ou shift-clique sur la roue pour saisir une valeur exacte).
- **Téléverser une image d'arrière-plan** pour la page.
- Choisir si l'image d'arrière-plan reste **fixe** pendant que la page défile, ou défile avec elle.
- Ajuster quelle partie de l'image d'arrière-plan est visible, en faisant glisser.

## Enregistrement et historique

Il n'y a **pas de bouton Enregistrer**. Chaque action que tu accomplis (déplacer, redimensionner, modifier du texte, changer une couleur) est enregistrée à l'instant où tu la termines.

De ce fait, il n'y a pas non plus d'**annulation** traditionnelle. À la place, Hotglue conserve un historique de la page appelé *révisions*. Ouvre-le avec le bouton **Révisions** dans l'éditeur (ou appuie sur <kbd>ctrl</kbd> + <kbd>z</kbd>, qui te propose de t'y emmener). Dans la vue des révisions, tu peux revenir sur les versions antérieures de la page. Hotglue prend un instantané automatique d'une page environ une fois par heure pendant qu'elle est en cours d'édition, et conserve ces instantanés pendant sept jours.

> [!tip] Travaille par petits mouvements réfléchis
> Comme il n'y a pas d'annulation et que les changements sont immédiats, il vaut la peine de faire les changements un à la fois et de jeter un coup d'œil au résultat. Si quelque chose ne va pas, l'historique des révisions est ton filet de sécurité, pas une touche d'annulation.
