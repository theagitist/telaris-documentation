# Galaxies

Une galaxie est un contenant, un point de vue et une position éditoriale tout à la fois. C'est l'unité que qui exploite l'instance te tend en disant « tu peux éditer ici » ; c'est l'unité à laquelle qui visite arrive ; c'est l'unité que tu cadres, nommes et façonnes. Ce chapitre parcourt la création d'une galaxie, sa configuration, et les opérations quotidiennes sur elle.

## Sélectionner une galaxie

Le menu déroulant **Galaxie actuelle** en haut de la page d'édition permet de choisir la galaxie dans laquelle tu travailles. *Toutes mes galaxies* montre les trous de ver de tout ce à quoi tu as accès ; choisir une galaxie particulière filtre tout ce qui suit sur celle-ci.

La première chose que le menu déroulant t'apprend est la forme de tes responsabilités éditoriales : chaque galaxie listée est une galaxie que tu peux éditer. Si la galaxie d'une collègue manque, qui exploite l'instance ne te l'a pas assignée. (Qui visite ton instance voit chaque galaxie publique ; qui édite ne voit que celles dont la personne a la charge.)

L'accès peut être en lecture-écriture ou en lecture seule, réglé par galaxie. Dans une galaxie en lecture-écriture, tu peux ajouter et modifier des trous de ver comme ce manuel le décrit. Dans une galaxie en lecture seule, tu peux tout ouvrir et tout voir, mais les commandes qui permettraient de la modifier ne sont pas disponibles ; cela permet à qui exploite l'instance de partager une galaxie en référence sans céder l'édition. Ta propre galaxie, une que tu as créée, est toujours à toi de modifier.

Quand tu choisis une galaxie particulière, trois nouveaux boutons apparaissent à côté du menu déroulant :

![Page d'édition avec une galaxie sélectionnée : boutons Voir, Paramètres, Toile](assets/images/editor-manual-fr/03-editor-home-single-galaxy.png)

- **Voir** ouvre la galaxie en mode visite, dans un nouvel onglet. Utilise-le chaque fois que tu veux vérifier comment un changement se lit depuis le siège de qui visite.
- **Paramètres** ouvre la configuration de la galaxie. Une grande partie de ce chapitre porte sur ce qui se trouve dans cette fenêtre.
- **Toile** ouvre la toile de mots-clés, la surface de dessin relationnelle couverte au chapitre 8.

## Créer une galaxie

Le fait de pouvoir créer une nouvelle galaxie dépend de la configuration de qui exploite l'instance ; certaines instances laissent qui édite créer librement, d'autres réservent la création à l'administration. Si tu as la permission, le bouton de nouvelle galaxie se trouve dans la même rangée que le sélecteur ; sinon, demande à qui exploite l'instance et la personne en mettra une en place pour toi.

Quand une nouvelle galaxie est créée, elle arrive vide : zéro trou de ver, aucun mot-clé, thème par défaut. L'étape suivante est de remplir ses paramètres.

## Paramètres de galaxie

Ouvre le bouton **Paramètres** à côté du sélecteur. Une fenêtre s'ouvre :

![Fenêtre Modifier la galaxie : Nom, Devise, Thème visuel, Étiquettes, actions groupées, et bascules de découverte](assets/images/editor-manual-fr/04-galaxy-settings-modal.png)

La fenêtre est l'endroit central où tu façonnes ce qu'est une galaxie et comment elle se comporte. Les champs, dans l'ordre :

**Nom** (obligatoire). Le nom que voit qui visite dans le sélecteur de galaxie et en haut de la scène. Les noms de galaxie ne sont pas uniques à travers le réseau, mais deux galaxies portant le même nom sur la même instance sont confondantes ; choisis quelque chose de lisible et distinct. Tu peux changer le nom d'une galaxie à tout moment.

**Devise** (facultative, courte). Une description d'une ligne affichée à côté ou sous le nom de la galaxie dans l'interface pour qui visite. La devise n'apparaît pas dans la scène 3D ; son public principal est le sélecteur et le listing public.

**Thème visuel**. Un menu déroulant qui choisit l'apparence de la scène 3D : *Cosmique* (étoiles, planètes, fusées) est la valeur par défaut et la plus courante ; les autres thèmes sont *Simple*, *Abstrait*, *Rectangles*, *Rayures*, et *Tech*. Choisis celui dont le vocabulaire correspond à ton contenu. Le thème peut être changé à tout moment ; le changement s'applique immédiatement pour qui visite, mais ne modifie pas ce que tu as composé, seulement la manière dont c'est rendu.

**Étiquettes** (facultatives). De courtes étiquettes qui regroupent cette galaxie avec d'autres. Deux galaxies qui partagent une étiquette forment une *union de galaxies* : qui visite et suit l'étiquette voit les trous de ver des deux à la fois, chacun gardant le style visuel de sa galaxie source. Utilise les étiquettes quand plusieurs galaxies sont des sœurs dans un arrangement plus large. La saisie Étiquettes propose une autocomplétion à partir des étiquettes utilisées dans tes autres galaxies et des étiquettes partagées par les galaxies préfixées du même `[crochet]`.

**Actions groupées sur les trous de ver**. Deux boutons qui appliquent un seul paramètre à tous les trous de ver de cette galaxie à la fois.

- **Utiliser les images comme icônes (tous les trous de ver)** règle chaque trou de ver porteur d'image pour qu'il rende son image comme nœud 3D au lieu de l'icône par défaut du thème. Utile quand tu as une galaxie de photographies et veux que les photos *soient* la scène.
- **Tout rétablir aux icônes du thème** défait l'action précédente : chaque trou de ver revient à l'icône du thème, qu'il ait ou non une image.

Ces actions agissent en lot ; les trous de ver individuels peuvent encore être basculés un par un ensuite (chapitre 5).

**Bascules de découverte**. Un ensemble d'interrupteurs en bas de la fenêtre qui contrôlent l'expérience de qui visite. Ils sont désactivés par défaut ; active chacun quand tu veux la fonctionnalité correspondante. Chaque bascule est couverte au chapitre 10 (Vues pour qui visite) où la fonctionnalité qu'elle contrôle est aussi montrée.

Enregistre la fenêtre avec **Mettre à jour la galaxie** ; ferme sans changement via **Annuler** ou en cliquant à l'extérieur de la fenêtre. Les changements s'appliquent immédiatement pour qui visite.

## Cadre éditorial

Le cadre d'une galaxie est le court paragraphe qui l'ouvre pour qui visite. C'est la réponse à la question *qu'est-ce que cette galaxie ?* avant que qui visite n'ait rencontré aucun trou de ver. Deux endroits où l'écrire :

1. Le champ **Devise** dans la fenêtre de galaxie, pour le résumé d'une ligne qui apparaît à côté du nom de la galaxie.
2. (Sur certaines instances) un trou de ver de cadrage dédié à l'intérieur de la galaxie, souvent le premier que voit qui visite à l'entrée. Si ton instance utilise ce modèle, qui l'exploite te le fera savoir.

Les deux sont des choix éditoriaux, pas techniques. Écris le cadre dans ta propre voix ; la galaxie est à toi de présenter.

## Partager des trous de ver entre galaxies par les étiquettes

Si tu as une galaxie dont le contenu fait partie d'une constellation de travail plus large (une exposition à plusieurs salles ; une revue à plusieurs numéros ; une série de collections apparentées), le champ **Étiquettes** est la manière de le dire. Ajoute la même étiquette à chaque galaxie qui va ensemble ; l'union devient accessible à qui visite à `/tag/<segment-d-etiquette>` (qui exploite l'instance peut partager le lien).

Les étiquettes ne créent ni ne modifient des trous de ver. Elles sont purement un arrangement de visionnage : dans la vue d'union, qui visite voit ensemble les trous de ver de chaque galaxie étiquetée, mais chaque trou de ver reste dans sa galaxie d'origine. Édite une galaxie, les autres restent inchangées.

## Retirer une galaxie

Il n'y a pas de bouton « supprimer la galaxie » pour l'édition dans la configuration typique d'une instance ; si tu as vraiment besoin de retirer une galaxie, demande à qui exploite l'instance et la personne l'organisera. La raison de cette friction est éditoriale : une galaxie qui a été liée depuis l'extérieur (par une visite, par un portail, par une union d'étiquettes, par le favori de qui visite) ne disparaît pas simplement ; le lien devient sombre. Qui exploite peut décider comment gérer le lien sombre.

Le modèle le plus courant n'est pas de supprimer une galaxie mais de la rendre invisible pour qui visite tout en la gardant côté édition, pour que la décision éditoriale puisse être renversée plus tard.

## Choses qu'il vaut la peine de savoir

- **Tu ne peux pas déplacer une galaxie.** Une fois qu'une galaxie a un segment d'URL (la partie `/<court-nom>` de l'URL), ce segment est permanent. Renommer la galaxie change le nom affiché mais pas le segment. Si un changement de segment est critique, qui exploite l'instance peut en organiser un, mais l'URL change pour toute personne avec l'ancien lien.
- **Le sélecteur de galaxie regroupe les galaxies de même préfixe `[crochet]`.** Si ton instance utilise les préfixes entre crochets (`[mocambos] Galaxie A`, `[mocambos] Galaxie B`), le sélecteur les regroupe visuellement. Les crochets sont une convention, pas une fonctionnalité ; utilise-les quand le regroupement aide qui édite à trouver des galaxies apparentées.
- **Une galaxie avec zéro trou de ver est permise.** Les nouvelles galaxies commencent vides et restent modifiables. Il n'y a pas d'exigence de nombre minimum de trous de ver avant d'enregistrer.
- **Le thème visuel ne change que l'apparence de la scène.** Passer de Cosmique à Tech ne change pas ce qui est dans la galaxie ; cela change la manière dont les trous de ver sont *dessinés*. Essaie un thème ; s'il ne convient pas, reviens au précédent.
