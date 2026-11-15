# La toile de mots-clés

La toile de mots-clés est l'endroit où tu rédiges la carte conceptuelle d'une galaxie. Les trous de ver te donnent des objets ; les mots-clés te donnent des manières d'étiqueter ces objets ; la toile est l'endroit où tu dessines, à la main, les relations **entre les mots-clés eux-mêmes**. Deux étiquettes se penchent l'une vers l'autre parce que l'édition a décidé qu'elles allaient ensemble. Deux étiquettes ont une ligne tracée entre elles parce que l'édition a décidé de dire *ces deux idées sont liées, et voici pourquoi*.

Ce chapitre parcourt la surface, ses outils de dessin, et la discipline éditoriale du bon usage.

## Ouvrir la toile

Sélectionne la galaxie sur laquelle tu veux travailler depuis la page d'édition. Quand une galaxie particulière est sélectionnée, trois boutons apparaissent à côté du sélecteur de galaxie ; le troisième est **Toile**. Sélectionne-le. La toile s'ouvre dans un nouvel onglet.

> [!warning] Ordinateur de bureau uniquement
> La toile est une surface réservée à l'ordinateur de bureau. Sur un téléphone ou une tablette, les interactions d'étiquettes et de lignes ne se comportent pas bien ; le bouton Toile est caché dans ces contextes. S'il te faut travailler l'arrangement de mots-clés d'une galaxie depuis un petit écran, la liste de trous de ver et le champ de mots-clés à l'intérieur de chaque fenêtre de trou de ver fonctionnent encore ; la toile non.

## Ce que tu vois

La toile s'ouvre en pleine fenêtre, sur une scène sombre, avec les mots-clés de la galaxie disposés comme des étiquettes pastel sur une grille de points :

![Toile de mots-clés : étiquettes pastel avec des lignes de relation tracées entre elles, sur un fond sombre quadrillé de points](assets/images/editor-manual-fr/10-keyword-canvas.png)

Chaque étiquette est un mot-clé. La couleur de l'étiquette correspond à la couleur utilisée ailleurs dans l'application : *indigène* est le même verdâtre ici que sur une ligne de trou de ver. Les étiquettes dérivent légèrement quand la toile est au repos (une douce simulation physique les garde vivantes) ; faire glisser une étiquette l'épingle à sa place à partir de là.

Les lignes entre étiquettes sont des **relations** que l'édition a tracées. Chaque ligne a deux extrémités (les étiquettes qu'elle connecte), une note facultative (une phrase qui explique la connexion), et un enregistrement de qui l'a tracée et quand.

La barre du haut porte :
- **Retour** : te ramène à la page d'édition pour cette galaxie.
- Le nom de la galaxie.
- **?** : ouvre une petite superposition d'aide qui liste chaque interaction clavier et souris de la toile.
- **Prête** (ou **Enregistrement…**) : un petit indicateur d'état qui confirme que la toile a enregistré ton dernier changement.

## Tracer une relation

Deux manières de tracer une ligne entre deux étiquettes :

1. **Clic-clic** : clique le point d'ancrage d'une étiquette (un petit cercle qui apparaît sur l'étiquette quand tu la survoles), puis clique le point d'ancrage d'une autre étiquette. Une ligne s'enclenche.
2. **Glisser** : appuie sur le point d'ancrage d'une étiquette et fais glisser vers l'autre ; relâche. Même résultat.

Quand la ligne apparaît, une petite saisie en ligne te laisse taper une note facultative. Entrée enregistre la note ; Échap laisse la ligne sans note. La note est visible quand qui visite (ou une autre personne qui édite) survole la ligne plus tard.

La ligne **adhère aux bords des étiquettes** à mesure que tu déplaces les étiquettes. Fais glisser l'étiquette *indigène* à travers la toile ; la ligne vers *tolérante au sel* suit. Pas de routage manuel de ligne ; la géométrie se charge d'elle-même.

## Déplacer et arranger les étiquettes

- **Fais glisser** une étiquette pour la repositionner. La nouvelle position est enregistrée automatiquement.
- La toile se souvient de la position **par compte d'édition** : chaque compte d'édition a sa propre vue de la toile. Deux personnes qui travaillent sur la même galaxie ne se disputent pas les positions des étiquettes ; chacune voit son propre arrangement, et la vue de qui visite utilise l'arrangement le plus récent ou un agencement fusionné (consulte qui exploite ton instance pour le réglage en vigueur).
- Les étiquettes que tu n'as pas déplacées flottent dans une dérive douce, en se déposant lentement dans une disposition influencée par leurs lignes de relation (les étiquettes connectées par une ligne sont doucement attirées l'une vers l'autre). La dérive s'arrête dès que tu fais glisser une étiquette ; à partir de ce moment, l'étiquette est épinglée.

C'est le petit secret de la toile : la disposition que tu vois est en partie l'œuvre de la simulation et en partie les choix éditoriaux que tu as faits. Deux galaxies dont l'édition n'a tracé aucune relation ressemblent à de la poussière sur la grille de points ; deux galaxies dont l'édition en a tracé beaucoup ressemblent à des constellations.

## Modifier ou supprimer une relation

Survole une ligne ; un petit menu contextuel apparaît avec deux options :

- **Modifier la note** : change la note en ligne attachée à la ligne.
- **Supprimer** : retire la relation entièrement.

Les suppressions sont permanentes au niveau de la ligne (pas d'annulation dans la toile), mais les extrémités d'étiquettes restent sur la toile. Tu peux retracer une relation entre les deux mêmes étiquettes plus tard ; la nouvelle ligne est un nouvel enregistrement dans la mémoire sous-jacente, pas la restauration de l'ancien.

## Renommer et fusionner des mots-clés

Clic droit (ou appui long sur écran tactile) sur une étiquette pour ouvrir ses options :

- **Renommer** : change le mot. Le renommage s'applique à chaque trou de ver qui porte le mot-clé à travers chaque galaxie de l'instance, parce que les mots-clés sont globaux par texte. La couleur de l'étiquette se déplace pour correspondre au nouveau texte (les couleurs sont déterministes par le mot).
- **Fusionner dans…** : sélectionne une autre étiquette sur la toile pour y fusionner ce mot-clé. Après la fusion, chaque trou de ver qui portait le mot-clé source porte désormais le mot-clé cible. L'étiquette source disparaît.
- **Supprimer** : retire le mot-clé de chaque trou de ver qui le portait sur l'instance.

Ce sont des outils tranchants. La fusion est la plus douce des trois (pas de perte de données ; juste un changement d'étiquette), puis le renommage (aussi pas de perte de données ; le mot change mais les connexions restent), puis la suppression (le mot-clé disparaît ; les trous de ver survivent sans lui). Opère un jour calme si une galaxie a plusieurs personnes qui éditent.

## Réinitialisation en lot

La toile expose deux opérations de réinitialisation en lot par la superposition d'aide **?** :

- **Réinitialiser toutes les positions d'étiquettes** dans cette galaxie : chaque étiquette revient à une position par défaut uniforme. À utiliser quand la disposition a accumulé du désordre et que tu veux repartir.
- **Réinitialiser toutes les relations** dans cette galaxie : supprime chaque ligne de relation dans cette galaxie. Les étiquettes restent. À utiliser quand tu veux redessiner la carte conceptuelle de zéro.

Les deux sont limitées à la **galaxie courante** ; elles ne touchent pas les autres galaxies.

## Quand utiliser la toile (et quand non)

La toile est la plus utile quand :

- Les mots-clés d'une galaxie portent une structure qui vaut la peine d'être montrée (certains sont frères, certains sont opposés, certains sont propres à une sous-région du contenu).
- Un point éditorial vit **entre** mots-clés plutôt qu'à l'intérieur d'un seul. *Indigène* seul n'est qu'une étiquette ; *indigène* tracé près de *tolérante au sel* avec une note (« la plupart des indigènes ici tolèrent le sel ») est une observation.
- Tu veux une surface de travail pour penser. La toile est un carnet de croquis pour le vocabulaire de la galaxie autant qu'un artefact public.

La toile est **moins utile** pour :

- Les toutes petites galaxies (moins de dix trous de ver ; le nombre d'étiquettes est généralement trop petit pour qu'une disposition soit intéressante).
- Les galaxies dont les mots-clés sont surtout des noms propres ou propres à un seul trou de ver ; la toile sert aux relations *entre* concepts, et les concepts isolés n'ont rien à relier.

Si une galaxie ne donne jamais envie d'ouvrir la toile, c'est très bien. La toile est offerte, pas requise.

## Choses qu'il vaut la peine de savoir

- **La toile enregistre chaque changement automatiquement.** Il n'y a pas de bouton Enregistrer. L'indicateur **Enregistrement…** / **Prête** en haut à droite reflète l'état de persistance.
- **Pas d'annulation à l'intérieur de la surface de toile.** Un mauvais geste se corrige par un autre geste ; une suppression accidentelle, en redessinant la ligne. Si quelque chose tourne mal, demande à qui exploite ton instance au sujet d'un instantané.
- **Qui visite ne voit pas les étiquettes directement.** La toile est une surface d'édition ; ce que voit qui visite dans la scène 3D est influencé par l'arrangement de mots-clés (quels trous de ver partagent des mots-clés ; quelles étiquettes ont des relations), mais qui visite ne regarde pas la grille d'étiquettes elle-même.
- **Les notes de ligne sont remontées à qui visite seulement au survol** dans le panneau des trous de ver liés (le chapitre 10 a le détail côté visite). La note fait partie de l'artefact public ; écris-la pour qui lira plus tard, pas pour toi-même.

## Tracer des chemins entre trous de ver (l'Éditeur de carte)

La toile trace des lignes entre *mots-clés*. L'**Éditeur de carte** trace des lignes entre *trous de ver* : des chemins que tu dessines à la main, comme on esquisse une promenade dans un lieu. Sers-t'en quand l'ordre du voyage compte, par exemple un labyrinthe dont les étudiantes et étudiants écrivent les salles, mais dont le chemin est fixé d'avance.

### Ouvrir l'Éditeur de carte

Choisis une galaxie depuis la page d'édition. À côté de **Toile** se trouve un bouton **Carte** ; clique dessus et l'Éditeur de carte s'ouvre dans un nouvel onglet. Comme la toile, il ne fonctionne que sur ordinateur.

Tous les trous de ver de la galaxie apparaissent sur la carte. Ceux qui sont estompés n'ont pas encore de place : **fais glisser** un trou de ver pour le poser où tu veux. Les positions s'enregistrent toutes seules.

### Tracer un chemin

1. Survole un trou de ver ; de petits points d'ancrage apparaissent sur son bord.
2. Clique sur un point d'ancrage du trou de ver où le chemin **commence**, puis sur un point du trou de ver où il **finit**. (Tu peux aussi glisser d'un point à l'autre.)
3. Écris une note facultative et enregistre-la, ou passe. La note apparaît au survol du chemin.

Appuie sur **Échap** pendant le tracé pour annuler. Maintiens **Espace** et fais glisser pour te déplacer ; utilise la molette pour zoomer.

### Sens

Un nouveau chemin est **à sens unique** : il va du premier trou de ver sur lequel tu as cliqué au second. Pour le changer, clique sur le chemin et choisis **Changer de sens**. Chaque clic passe à l'option suivante : un sens, le sens inverse ou double sens. Clique de nouveau sur le chemin et choisis **Modifier la note** ou **Supprimer** pour changer sa note ou l'enlever. Seule la personne qui a tracé le chemin, ou une personne administratrice, peut le modifier.

### Parcours

Un parcours est une suite nommée de trous de ver à suivre étape par étape. Dans le panneau **Parcours**, clique sur **Nouveau parcours**, puis sur les trous de ver dans l'ordre (clique de nouveau sur le dernier pour l'annuler), puis sur **Enregistrer le parcours** et donne-lui un nom. Les parcours se suivent dans la vue 2D.

### Ce que voient les visiteurs et visiteuses

- **En 3D** (sur la page propre de la galaxie), les chemins apparaissent comme des lignes fines et sinueuses entre les trous de ver. Les chemins à sens unique portent une lente ondulation de lumière qui coule vers la destination ; ceux à double sens restent immobiles et plus pâles. Survoler un trou de ver allume ses chemins.
- **En 2D** (quand la vue 2D de la galaxie est activée, chapitre 10), la carte montre ta disposition, tes chemins avec le même sens qui coule, et les parcours.
- **Sur la fiche d'un trou de ver**, une liste **Mène à** montre où vont ses chemins. Un clic sur un nom mène au trou de ver suivant, en 2D et en 3D.
- Dès qu'une galaxie a au moins un chemin tracé, les lignes automatiques de mots-clés y sont masquées, pour ne montrer que le trajet que tu as dessiné. Supprime tous les chemins pour les faire revenir.
