# Travail multigalaxies

Parfois une idée vit à travers plus d'une galaxie : un sujet de recherche qui couvre deux collections ; une exposition à plusieurs salles ; une série de numéros apparentés. Telaris est construit pour que le trou de ver reste dans sa galaxie d'origine et que la *combinaison* soit un arrangement de visionnage, pas un arrangement structurel. Ce chapitre parcourt les trois manières dont tu peux composer des galaxies, et quand chacune est le bon choix.

## Les trois chemins de composition

Telaris offre trois manières de mettre plusieurs galaxies dans une seule vue :

1. **Étiquettes de galaxie** (chapitre 4) : deux galaxies qui partagent une étiquette forment une *union de galaxies*. Qui visite arrive à l'union via `/tag/<segment-d-etiquette>` et voit ensemble les trous de ver de chaque galaxie étiquetée, chacun gardant le style visuel de sa galaxie source.
2. **Regroupement par préfixe entre crochets** : les galaxies dont les noms commencent par le même préfixe `[crochet]` s'unissent automatiquement à `/[crochet]`. Un repli naturel face aux étiquettes de galaxie ; le préfixe est aussi le signal visuel pour qui édite en parcourant le sélecteur.
3. **Listes explicites de galaxies** : passer une liste séparée par des virgules dans l'URL `?galaxies=segment1,segment2` produit une union ponctuelle. Utile pour partager une combinaison curatée sans changer les galaxies sous-jacentes.

Le choix entre les trois dépend de **la durabilité de la combinaison** :

- *Durable* : étiquettes de galaxie. La connexion est éditoriale et persiste à travers les sessions.
- *Conventionnel* : préfixe entre crochets. Utile quand les galaxies sont sœurs par convention de nommage, pas seulement par étiquette.
- *Ponctuel* : liste explicite. Utile pour un courriel ou un lien qui guide qui lit à travers une combinaison particulière, une seule fois.

## Partager des trous de ver sans dupliquer

Le premier instinct dans beaucoup de systèmes d'archive est de copier un trou de ver dans une seconde galaxie quand une idée appartient aux deux endroits. Telaris est construit contre cet instinct : copier crée deux trous de ver à entretenir, deux endroits à mettre à jour quand la source change, deux endroits d'où retirer quand la communauté source retire son consentement.

Le chemin voulu est : laisser le trou de ver dans son unique galaxie d'origine et laisser des **mots-clés partagés** le connecter aux autres. Qui visite et suit *intertidal* dans la galaxie A atteint les trous de ver étiquetés *intertidal* dans la galaxie B ; le contenu du trou de ver vit en un seul endroit ; la connexion est calculée à partir du mot-clé.

Quand cela ne suffit pas, les options de l'édition sont, dans l'ordre du moins au plus invasif :

1. **Ajouter une étiquette de galaxie** aux deux galaxies qui partagent le thème. Qui visite et suit l'étiquette voit l'union.
2. **Placer un portail** (chapitre 9) d'une galaxie à l'autre. Le portail est un trou de ver, mais c'est un petit trou de ver, délibéré ; il ne duplique aucun contenu.
3. **Dupliquer le trou de ver** (menu d'actions du chapitre 5). Seulement quand le contenu du trou de ver a vraiment besoin de vivre dans deux endroits (par exemple, une galaxie est amorcée avec du matériel d'une autre, avec la décision éditoriale de relever plutôt que de relier). Le duplicata est indépendant à partir de là ; les deux copies doivent être entretenues.

Les deux premiers sont presque toujours préférables au troisième.

## L'expérience d'une union pour qui visite

Qui visite et arrive à une union d'étiquettes de galaxie (par exemple `/tag/coast`) voit :

- Une scène composée des trous de ver de chaque galaxie portant l'étiquette.
- **Thèmes d'origine par trou de ver** : chaque trou de ver se rend avec le thème de sa galaxie source, pas avec un thème unifié unique. C'est intentionnel ; qui visite voit l'union comme la *rencontre des galaxies*, pas comme un aplatissement.
- Une bande ou un sélecteur de galaxies en haut qui montre les galaxies constitutives, avec la possibilité de basculer dans une seule.
- Les mêmes fonctionnalités de découverte que toute galaxie (étiquettes de mots-clés, trous de ver liés, etc.), en puisant désormais dans l'union.

La barre d'URL de qui visite reste à `/tag/<étiquette>` pendant qu'elle est dans l'union ; cliquer sur un trou de ver ouvre sa fiche d'information sans quitter l'union.

## Quand ajouter une étiquette de galaxie

Une étiquette est éditoriale. Les deux questions à se poser :

- **La relation entre ces galaxies est-elle de longue durée ?** Une étiquette persiste ; si la relation est ponctuelle, une URL explicite est plus propre.
- **La relation est-elle symétrique ?** Une étiquette est symétrique (chaque galaxie qui porte l'étiquette est également membre). Si la relation est directionnelle (la galaxie A est l'introduction à la galaxie B), un portail est plus honnête.

Exemples qui justifient une étiquette :
- Une série de collections de recherche apparentées.
- Une exposition à plusieurs salles.
- Un regroupement régional (galaxies qui décrivent toutes du contenu d'un même paysage, géographie ou communauté).

Exemples qui ne la justifient pas :
- « Vieilles galaxies que je veux regrouper pour un lien unique » (utilise `?galaxies=...`).
- « Galaxies qui partagent quelques mots-clés » (utilise directement les mots-clés).

## Quand utiliser le regroupement par préfixe entre crochets

Telaris reconnaît les noms de galaxies qui commencent par le même `[crochet]` comme une famille. Une galaxie nommée `[demo] Plantes côtières` et une autre nommée `[demo] Cuvettes de marée` partagent le préfixe `[demo]` ; qui visite et suit `/[demo]` voit les deux en union.

Le préfixe entre crochets est le plus utile quand :

- Tu as plusieurs comptes d'édition qui travaillent sur des galaxies apparentées, et le préfixe leur signale que les galaxies sont sœurs.
- Les galaxies forment une famille que tu veux aussi voir comme une famille dans le sélecteur d'édition (le sélecteur regroupe les galaxies par préfixe entre crochets).
- Tu veux le comportement d'union sans rédiger explicitement une étiquette sur chaque galaxie.

Le préfixe entre crochets et une étiquette de galaxie explicite ne s'excluent pas mutuellement ; les deux s'appliquent si les deux sont présents.

## Quand utiliser une liste explicite de galaxies

Parfois tu veux une union ponctuelle pour un moment particulier : un courriel à une équipe de conservation qui montre une combinaison particulière ; un lien pédagogique qui mène une classe à travers trois galaxies côte à côte ; une exposition temporaire qui ne justifie pas une étiquette de longue durée.

La forme URL est `?galaxies=segment1,segment2,segment3` ajoutée à l'adresse de ton instance. Le résultat est identique à une union d'étiquettes, mais la combinaison n'existe que comme l'URL elle-même.

C'est le bon outil pour la curation ponctuelle. Il sert aussi de vérification rapide : si une combinaison particulière de galaxies se lit bien en URL explicite, tu as une candidate pour une étiquette permanente.

## Multigalaxies entre instances

Et les galaxies qui vivent sur **d'autres** instances de Telaris ? Cela appartient au domaine de qui exploite : le contenu entre instances arrive sur ta surface d'édition via la fédération ou via les imports de ponts que qui exploite configure. Depuis le siège de l'édition, les galaxies fédérées et issues de ponts se comportent comme des galaxies locales (une galaxie est une galaxie est une galaxie), mais l'édition ne peut pas rédiger d'union entre instances ; seule qui exploite peut mettre en place la fédération qui les rend possibles.

## Choses qu'il vaut la peine de savoir

- **Un trou de ver appartient à une seule galaxie à la fois.** Multigalaxies est un concept de *visionnage*, pas un concept structurel. La galaxie d'origine du trou de ver est sa source unique de vérité.
- **Qui visite, dans une vue d'union, ne peut pas dire au premier coup d'œil quelle galaxie a rédigé un trou de ver donné** au-delà du thème visuel de l'icône du trou de ver. La fiche d'information montre la galaxie source dans le pied ; le thème de l'icône est l'indicateur instantané.
- **Une galaxie dans une union ne perd pas son individualité.** Qui visite peut entrer dans une seule galaxie depuis la vue d'union ; l'union est une couche de visionnage, pas une fusion.
- **Les mots-clés sont globaux par texte** (chapitre 7). Les mots-clés sur un trou de ver dans la galaxie A sont les mêmes mots-clés que les mêmes mots sur un trou de ver dans la galaxie B. Une vue d'union consolide la bande d'étiquettes de mots-clés à travers toutes les galaxies constitutives ; cliquer un mot-clé dans l'union filtre l'union.
- **La toile de mots-clés reste par galaxie** (chapitre 8). Il n'y a pas de « toile d'union » ; chaque galaxie tient son propre arrangement de mots-clés. Les mots-clés eux-mêmes sont partagés (renommer ou fusionner s'applique partout), mais la disposition d'étiquettes et les relations tracées sont limitées à chaque galaxie.
