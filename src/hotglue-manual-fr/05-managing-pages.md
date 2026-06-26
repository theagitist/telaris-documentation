# Gérer les pages

La vue **Contenu hotglue** est l'endroit où tu suis tes pages Hotglue : les créer, les nommer, les rattacher à des trous de ver, et faire le rangement. Ce chapitre la parcourt.

## La liste

La vue montre un tableau des pages Hotglue que tu peux atteindre, avec un décompte dans le titre. Les colonnes sont :

- une case à cocher pour sélectionner la ligne,
- **Titre**,
- **Trou de ver attribué** (le trou de ver dans lequel cette page est affichée, ou vide s'il n'y en a pas),
- **Mises à jour**,
- **Actions**.

![La liste Contenu hotglue avec trois pages : une attribuée à un trou de ver, une sans attribution, et une deuxième page attribuée, chacune avec une date de mise à jour et un menu d'actions](assets/images/hotglue-manual-fr/02-hotglue-content-list.png)

Clique sur le titre d'une page pour l'ouvrir dans la superposition d'édition.

## Créer et nommer une page

Clique sur **Nouvelle page** pour en créer une. Elle s'ouvre aussitôt dans l'éditeur, sans titre et sans attribution, prête à composer.

Pour renommer une page, ouvre-la et modifie le champ **Nom de la page** en haut de la superposition. Le nouveau nom s'enregistre tout seul quand tu cliques ailleurs ; une petite note d'état le confirme.

## Attribuer une page à un trou de ver

Une page Hotglue n'apparaît aux personnes qui visitent qu'une fois rattachée à un trou de ver. Dans la superposition d'édition, utilise le contrôle **Trou de ver attribué** :

- C'est une liste avec recherche. Commence à taper le nom d'un trou de ver pour la réduire. Chaque option s'affiche sous la forme du nom du trou de ver suivi de sa galaxie, pour que tu puisses distinguer des trous de ver aux noms semblables.
- Choisis un trou de ver pour y attribuer la page. Choisis **Aucune attribution** pour détacher la page de nouveau (le trou de ver revient alors à son média classique ; la page elle-même n'est pas supprimée).

Si le trou de ver que tu choisis affiche déjà une autre page Hotglue, Hotglue demande d'abord : « Remplacer ? Ce trou de ver affiche déjà une page hotglue. La page qu'il affiche maintenant ne sera plus attribuée (elle n'est pas supprimée). » Ainsi tu ne perds jamais une page en réattribuant un trou de ver ; la page déplacée se retrouve simplement sans attribution.

> [!note] Tu as besoin d'un accès en modification à la galaxie cible
> Attribuer ou détacher une page nécessite un siège en lecture-écriture sur la galaxie du trou de ver. Un siège en lecture seule te laisse voir les pages mais pas changer ce à quoi elles sont rattachées.

## Dupliquer une page

L'action **Dupliquer** dans le menu d'une ligne crée une copie d'une page (son titre gagne un suffixe « (copie) »). La copie est toujours créée **sans attribution**, donc la duplication ne perturbe jamais le trou de ver de l'original. Juste après la duplication, Hotglue propose d'attribuer la nouvelle copie quelque part.

## Consulter une page

Le menu d'actions d'une ligne donne trois façons de regarder une page :

- **Voir dans le navigateur** ouvre la page Hotglue nue dans un nouvel onglet, exactement comme la verrait une personne qui visite, et copie son adresse dans ton presse-papiers. Cela fonctionne pour n'importe quelle page, attribuée ou non.
- **Voir dans le trou de ver** ouvre un aperçu de la page à l'intérieur de son trou de ver, dans la même fenêtre. Disponible uniquement pour les pages attribuées.
- **Voir dans la galaxie** ouvre le visualiseur de galaxie tridimensionnel en direct, centré sur le trou de ver, dans une nouvelle fenêtre. Disponible uniquement pour les pages attribuées.

## Consulter des versions antérieures

Pendant qu'une page est ouverte dans l'éditeur, le bouton **Révisions** ouvre son historique, pour que tu puisses revenir sur les versions antérieures et récupérer après un changement que tu ne voulais pas garder. Voir *Enregistrement et historique* dans *La toile* pour le fonctionnement de l'historique.

## Rechercher et filtrer

- La boîte **Rechercher** filtre la liste à mesure que tu tapes, en cherchant dans le titre de la page, le nom du trou de ver et le nom de la galaxie.
- Le sélecteur de galaxie de l'en-tête de l'éditeur sert aussi de filtre : choisis une galaxie pour n'afficher que les pages Hotglue dont les trous de ver s'y trouvent, ou laisse-le sur toutes les galaxies pour tout voir.

## Travailler en lot

Coche les cases (ou la case tout-sélectionner dans l'en-tête) pour agir sur plusieurs pages à la fois. Une barre apparaît, indiquant combien sont sélectionnées, avec :

- **Effacer la sélection**,
- **Désattribuer la sélection** (détacher les pages choisies de leurs trous de ver),
- **Supprimer la sélection**.

## Supprimer une page

Supprime une seule page depuis le menu d'actions de sa ligne, ou plusieurs à la fois avec **Supprimer la sélection**. Dans les deux cas, Hotglue confirme d'abord, car la suppression est définitive : « Supprimer cette page hotglue ? Cela retire son contenu définitivement. Si elle est attribuée à un trou de ver, ce trou revient aux médias classiques. » Supprimer une page retire son contenu pour de bon ; tout trou de ver auquel elle était rattachée revient simplement à l'affichage du média classique.
