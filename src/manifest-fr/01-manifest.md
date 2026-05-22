# Manifeste

> [!warning] Brouillon
> Ce Manifeste est un brouillon, rédigé le 2026-05-22. Il sera affiné à mesure que la documentation gagnera en maturité.

Une déclaration de ce qu'est Telaris, de ce qu'il refuse, et des principes qui le tiennent ensemble. Écrite pour toute personne qui aborde le projet depuis l'extérieur : une éventuelle responsable d'instance, une communauté source qui envisage de contribuer, une étudiante qui lit la documentation, une équipe de conservation qui évalue l'usage du logiciel. Le reste de la documentation s'appuie sur les positions nommées ici.

## Ce que Telaris est

Un projet d'archive de connaissance décoloniale. Relationnel, non hiérarchique, fédéré entre pairs, tissé par le sens. Le contenu vit dans des **galaxies** : des amas de petites unités de contenu (un passage, une image, un son, un extrait de film, un document) qui se connectent à travers des **mots-clés** partagés. Pas de dossiers, pas de parents, pas de fil d'Ariane, pas d'algorithme ; la structure est un rhizome entretenu par qui édite et lu par qui visite comme une scène tridimensionnelle.

Telaris est un projet de recherche de cycle supérieur à l'Institut de genre, race, sexualité et justice sociale (GRSJ) de l'Université de la Colombie-Britannique. C'est un logiciel libre exécuté par des instances indépendantes à travers plusieurs pays et communautés, et non une plateforme tenue par un seul propriétaire.

## Décolonial comme méthode, pas comme métaphore

« Décolonial » nomme une pratique, pas une esthétique. La pratique a des conséquences concrètes dans la manière dont Telaris est conçu et exploité :

- Refus des réductions catégorielles imposées : pas de vocabulaire central, pas d'ontologie obligatoire, pas de direction éditoriale.
- Souveraineté des données pour les communautés sources : les personnes dont le matériel est hébergé sur une instance de Telaris conservent leur autorité sur celui-ci ; le retrait du consentement est définitif et exécuté sans négociation.
- Souveraineté éditoriale pour qui édite : chaque compte d'édition décide quoi publier dans les galaxies qu'il prend en charge ; il n'y a ni file d'attente de révision, ni flux d'approbation.
- Souveraineté pour qui exploite une instance : chaque instance fonctionne sous ses propres règles ; aucune autorité centrale ne dicte le contenu ou l'accès.

Ce sont des choix de méthode, pas des slogans. Ils apparaissent dans le code (pas de fonctionnalité de file de révision, pas de table de vocabulaire central, pas de droit d'annulation pour une administration de plateforme) tout autant que dans la documentation.

## Localisation, jusqu'au bout

Un modèle courant en logiciel consiste à localiser les chaînes visibles et à laisser les identifiants, les codes d'erreur, les clés d'état et autres jetons en anglais. Telaris refuse ce modèle. La logique implicite selon laquelle « les identifiants anglais sont neutres ; ce qui se traduit, c'est l'anglais visible » présuppose que le sens vit en anglais ; qu'au moment où un système cesse d'être anglais, il doit devenir abstrait ou aléatoire. C'est le même modèle colonial à une couche plus silencieuse.

En pratique : tout jeton qu'une personne qui utilise ou qui exploite peut rencontrer hors du code source est invariant par langue. Les codes d'erreur de l'API prennent la forme `<statut-http>.<sous-code-à-3-chiffres>` (RFC 9457 Problem Details), p. ex., `404.001`. Ils portent leur sens par la position, et non par une abréviation anglaise. Le même principe s'étend aux clés d'état, aux catégories de journal et à tout identifiant futur qui sort du code source pour atteindre une surface visible. Quand une traduction manque pour une langue donnée, ce qui s'affiche est le code lui-même, et non la chaîne d'origine en anglais : le pire cas visible est l'identifiant documenté, et non un anglais par défaut non déclaré.

Les identifiants du code source (noms de variables, noms de fonctions, chemins de fichiers, clés internes de configuration) restent en anglais : ils vivent dans le contexte de développement et sont lus quotidiennement. La ligne se trace selon que le jeton atteint ou non quelqu'un en dehors du code.

## Ce que Telaris n'est pas

Un refus clair est une position plus claire qu'un long manifeste.

- **Pas une plateforme.** Pas de propriétaire unique. Pas de catalogue central. Pas de publicité. Pas de pistage. Aucune donnée vendue ou partagée à des fins commerciales.
- **Pas un corpus d'entraînement pour l'IA.** Le contenu de Telaris n'est pas utilisé pour entraîner des modèles d'IA, ni à l'interne ni à l'externe. Le corpus n'est pas envoyé à des fournisseuses de modèles de langage pour modération, classification, résumé, ni aucun autre usage.
- **Pas une hiérarchie.** Pas de structure arborescente sur le contenu. Pas de file de révision éditoriale. Pas de « meilleur contenu » poussé par un algorithme.
- **Pas extractif.** Le contenu apporté par les communautés sources ne devient pas la propriété de Telaris. Qui édite ne perd pas son autorité d'autrice en publiant sur Telaris. L'exploitation d'une instance ne détient aucun droit sur le contenu éditorial au-delà de ce que le contrat de chaque instance rend explicite.
- **Pas anonyme par défaut.** L'attribution voyage avec l'œuvre. La signature de qui édite est consignée ; le nom de la communauté source est consigné ; la licence (lorsqu'elle est fournie) est consignée. L'anonymat est disponible lorsqu'une personne qui édite ou une communauté le demande, pas par défaut.

## Principes, au nombre de six

**1. Souveraineté éditoriale.** Qui édite décide quoi publier dans les galaxies qu'il prend en charge. Pas de file de révision, pas de vocabulaire approuvé centralement, pas de mot-clé « erroné ». Le coût est la responsabilité : la décision de qui édite lui appartient ; le logiciel ne la surveille pas.

**2. Consentement de la communauté source.** Quand une communauté contribue à du matériel, le consentement de cette communauté gouverne le matériel. Le retrait du consentement est définitif. Le retrait est exécuté par l'instance sans négociation, indépendamment de toute position éditoriale qu'elle pourrait tenir.

**3. Souveraineté de l'instance.** Chaque instance de Telaris est tenue par une personne indépendante sous ses propres règles. Pas d'autorité centrale au-dessus de l'exploitation des instances. Les instances s'accordent sur un petit ensemble d'engagements de réseau (identité cryptographique, honorer les retraits de fédération, se tenir à ces principes), mais gouvernent par ailleurs leurs instances de manière indépendante.

**4. Fédération, et non P2P pur.** Les galaxies ont une origine autoritative unique ; les pairs les reflètent en lecture seule ; pas de conflits de fusion, pas d'édition depuis n'importe où. La fédération est bilatérale et fondée sur le consentement : deux instances se fédèrent uniquement quand toutes les deux acceptent, et l'une ou l'autre peut se retirer à tout moment. Le vocabulaire refuse à la fois la prétention malhonnête du « P2P pur » (ce que Telaris n'est pas) et le modèle de plateforme à autorité centrale (ce que Telaris refuse).

**5. Refus du modèle de plateforme.** Chaque choix de conception est interrogé par cette même question : *est-ce que cela importe le modèle de plateforme que Telaris est construit pour refuser ?* Authentification unique, télémétrie publicitaire, modération centrale, algorithmes comportementaux, formats verrouillés, vocabulaires captifs. La réponse détermine si le choix entre.

**6. Logiciel libre, contenu sous la licence de qui édite.** Le logiciel de l'instance Telaris est libre sous GPL v3 ; la couche centrale de coordination (le Pluriverse, lorsqu'il sera publié) sera sous AGPL v3. Le contenu éditorial porte la licence que la personne qui édite ou la communauté source fournit, attachée à chaque pièce de contenu. Le logiciel se donne ; le contenu n'est pas annexé au don.

## D'où vient Telaris

Le projet s'appelle *Telaris* (du latin *tela*, une toile tissée). Il s'appuie sur :

- *Designs for the Pluriverse* et *Pluriversal Politics* d'Arturo Escobar.
- *The Darker Side of Western Modernity* de Walter Mignolo.
- *Constructing the Pluriverse* dirigé par Bernd Reiter.
- *Discours sur le colonialisme* d'Aimé Césaire.
- Les archives Mocambos / Baobáxia et la tradition quilombola de l'archive numérique communautaire.
- *African Fractals* de Ron Eglash, pour une compréhension du fractal comme structure ancrée hors du canon mathématique européen.
- Le savoir forestier des peuples autochtones du Nord-Ouest du Pacifique et la métaphore du réseau mycorhizien chez Suzanne Simard et Robin Wall Kimmerer, pour l'image d'échange mutuel de la fédération.

Ce sont des références, non des autorités. Le projet se situe en conversation avec ce corps de travail et y apporte un petit artefact technique. La justesse de l'artefact face à la politique qu'il revendique est l'épreuve autour de laquelle la documentation est structurée.

## Ce qu'est ce document

Une déclaration de position, tenue courte exprès. L'architecture complète, les conventions éditoriales, les manuels d'exploitation et la spécification de la fédération vivent dans leurs propres documents. Lis celui-ci pour savoir où Telaris se tient ; lis les autres pour savoir comment il fonctionne.
