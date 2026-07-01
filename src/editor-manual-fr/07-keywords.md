# Mots-clés

Les mots-clés sont de courtes étiquettes que tu attaches aux trous de ver. Ils sont la manière dont Telaris connecte le contenu sans dossiers. Un mot-clé est la différence entre une galaxie qui est une *liste* et une galaxie qui est une *toile* ; tout le reste, dans le quotidien de l'édition, se construit par-dessus.

Ce chapitre couvre l'attribution de mots-clés depuis l'intérieur de la fenêtre de trou de ver, la palette d'étiquettes, et comment travailler sur plusieurs trous de ver à la fois. La **toile** de mots-clés (la surface de dessin relationnelle pour les mots-clés) a son propre chapitre (8).

## Attribuer des mots-clés

Les mots-clés s'attribuent à l'intérieur de la fenêtre de trou de ver, dans le champ **Mots-clés** à côté du nom du trou de ver (voir chapitre 5 pour la fenêtre complète). Le champ est une saisie par étiquettes :

- Tape un mot-clé et appuie sur **Entrée** ou **virgule** pour l'ajouter comme étiquette.
- Clique sur le **×** d'une étiquette pour la retirer.
- Le même mot-clé peut être ajouté dans n'importe quelle casse ; Telaris compare sans tenir compte de la casse, donc *indigène* et *Indigène* sont le même mot-clé.

À mesure que tu tapes, des suggestions apparaissent :

- Les mots-clés déjà utilisés dans **cette galaxie** apparaissent en premier.
- Les mots-clés utilisés dans les **galaxies sœurs** (galaxies qui partagent le préfixe `[crochet]` de ta galaxie courante) apparaissent ensuite.
- Les autres mots-clés récents apparaissent en dernier.

Accepter une suggestion équivaut à taper le mot en entier. Telaris ne t'oblige pas à utiliser les suggestions ; tu peux toujours taper un nouveau mot-clé, auquel cas le nouveau mot-clé rejoint la galaxie.

## Bien choisir les mots-clés

La décision la plus importante au sujet des mots-clés est **d'en utiliser peu**. Un trou de ver étiqueté avec trois mots-clés choisis avec soin est plus lisible qu'un trou de ver étiqueté avec vingt. Chaque mot-clé que tu ajoutes est une connexion vers chaque autre trou de ver qui porte le même mot ; si la connexion n'est pas significative, le chemin de qui visite à travers la galaxie devient plus bruyant.

Quelques règles pratiques :

- **Un mot-clé par qualité que le trou de ver incarne réellement**. *Indigène* sur une plante qui est indigène ; *comestible* sur une qui se mange vraiment. Pas *plante* sur chaque trou de ver d'une galaxie de plantes ; ce mot-clé ne porte aucun signal.
- **Réutilise avant d'inventer.** Quand deux comptes d'édition décrivent la même idée avec des mots différents (*médicinale* et *guérison*), le lien conceptuel s'éteint. Regarde l'autocomplétion ; si un mot proche du tien existe déjà, préfère-le.
- **Évite les mots-clés que tu ne chercherais jamais.** Un mot-clé que personne (qui visite ou qui édite) ne taperait dans une recherche est un mot qui ne fait aucun travail.

Il n'y a pas de file de révision et pas de vocabulaire central. Qui édite décide les mots-clés sur chaque trou de ver ; le système te fait confiance. Le chapitre 13 parle de souveraineté éditoriale en détail.

## La palette d'étiquettes

Chaque mot-clé reçoit une couleur pastel déterministe, choisie par le texte du mot-clé. La couleur est la **même** pour ce mot à travers chaque galaxie sur ton instance : qui visite apprend que *indigène* est l'étiquette verdâtre dans une galaxie, la reconnaîtra instantanément dans une autre.

C'est aussi pourquoi renommer un mot-clé change la couleur : la couleur est attachée au texte, pas à un identifiant interne. Si tu renommes *médicinale* en *guérison*, la couleur de l'étiquette se déplace. (En pratique : renomme rarement ; la fusion est une opération plus propre.)

## Modifier les mots-clés sur un trou de ver existant

Ouvre la fenêtre Modifier du trou de ver (chapitre 5). Le champ Mots-clés montre les étiquettes existantes. Ajoute des étiquettes comme ci-dessus ; retire avec le × ; enregistre. Les changements s'appliquent au prochain chargement de page de qui visite.

## Agir sur plusieurs trous de ver à la fois

Pour trouver et agir sur chaque trou de ver porteur d'un mot-clé donné, tape le mot-clé dans le champ de recherche de la page d'édition. La liste se réduit aux trous de ver correspondants, et tu peux ouvrir le menu d'actions de chacun pour le modifier, le déplacer (en changeant sa galaxie dans la fenêtre Modifier), ou le supprimer. Chercher d'abord, puis agir trou de ver par trou de ver, te garde devant exactement ce que tu es sur le point de changer, plutôt que de déclencher une seule action balayante contre un décompte que tu ne peux pas voir.

## Alias (synonymes par galaxie)

Le modèle de mots-clés de Telaris traite l'usage du même mot dans deux galaxies comme le **même mot-clé**. Il n'y a pas de mécanisme d'alias par galaxie dans la v1 du déploiement ; si tu veux que *médicinale* dans une galaxie soit traité comme le même mot-clé que *guérison* dans une autre, la solution pratique est de **renommer l'un pour qu'il corresponde à l'autre** afin que les deux galaxies convergent vers un seul mot.

Si l'intention éditoriale est précisément l'inverse (un mot qui signifie des choses différentes dans deux galaxies et qui ne devrait pas les connecter), utilise des mots différents dans chacune. La précision conceptuelle est plus utile que l'astuce syntaxique ici.

## Nombre de mots-clés dans la vue de qui visite

Quand la fonctionnalité de découverte **Étiquettes de mots-clés** de la galaxie est activée (le chapitre 4 couvre la bascule ; le chapitre 10 couvre l'expérience résultante de qui visite), qui visite voit une rangée d'étiquettes en bas de la scène 3D montrant les mots-clés les plus utilisés. Cliquer une étiquette atténue chaque trou de ver qui *ne* porte *pas* ce mot-clé.

C'est un filtre doux (il ne retire pas les trous de ver de la scène, il les atténue), et c'est une des principales manières dont qui visite navigue une galaxie sans instructions. Les mots-clés que tu choisis sont la navigation : des mots-clés clairs donnent une scène claire.

## Choses qu'il vaut la peine de savoir

- **Un trou de ver sans mots-clés est permis mais silencieux.** Qui visite peut encore l'atteindre par la recherche par nom ou en cliquant en 3D ; la personne ne l'atteindra pas par la couche d'étiquettes de mots-clés. Utilise zéro mot-clé quand le rôle du trou de ver est purement solitaire.
- **Les noms de mots-clés sont cherchés dans le champ de recherche de la page d'édition** aux côtés des noms et descriptions de trous de ver. Chercher un mot-clé est la manière la plus rapide d'auditer quels trous de ver le portent.
- **Renommer un mot-clé le met à jour partout sur l'instance.** Renommer *médicinale* le renomme dans chaque galaxie qui utilise le mot. Il n'y a pas de renommage par galaxie.
- **Supprimer un mot-clé le retire de chaque trou de ver qui le porte.** Les trous de ver survivent ; l'étiquette du mot-clé disparaît d'eux. Supprimer un mot-clé (via la toile de mots-clés, chapitre 8) retire le mot ; supprimer un trou de ver (via le menu d'actions de sa ligne, chapitre 5) retire le contenu. Ce sont des opérations différentes.
- **Il n'y a pas de nombre maximum de mots-clés par trou de ver**, mais la lisibilité pratique suggère que trois à sept suffisent. Au-delà de dix, la bande d'étiquettes sur la fiche d'information commence à passer à la ligne de façon disgracieuse.
