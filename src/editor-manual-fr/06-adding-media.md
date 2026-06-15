# Ajouter des médias

Le corps d'un trou de ver est la description ; ses **médias** sont tout ce que qui visite rencontre visuellement ou sonorement à côté du corps : une image, un extrait de film, un enregistrement sonore, un document PDF, un lecteur intégré venant d'un autre site. Ce chapitre parcourt chaque type, dans l'ordre où la fenêtre les présente.

Un trou de ver porte au plus **un visuel principal** à la fois. Image, Vidéo et PDF sont trois onglets dans la fenêtre qui partagent un même emplacement sous-jacent ; en choisir un et enregistrer efface les autres. Le quatrième type de média, **audio**, est indépendant du visuel principal : un trou de ver avec une image *et* une piste audio joue l'audio pendant que l'image reste à l'écran.

La section des médias a elle-même deux onglets de premier niveau : **Classique** et **Hotglue**. Tout ce qui est décrit plus haut (image, vidéo, PDF, audio, code d'intégration) se trouve sous **Classique**, l'option par défaut. **Hotglue** est une autre façon de construire les médias d'un trou de ver : au lieu d'une seule image ou d'une seule vidéo, tu composes une page libre, en plaçant texte et images où tu veux sur une toile ouverte. Les deux sont des alternatives ; l'onglet ouvert au moment d'enregistrer est ce que voit qui visite. Hotglue est traité à la fin de ce chapitre.

## L'onglet Image

L'onglet par défaut, et le choix de média le plus courant. Utilise-le pour les photographies, les illustrations, les scans, les diagrammes, tout ce qui est immobile.

![Onglet Image dans la fenêtre Nouveau trou de ver : champ URL et sélecteur de fichier, plus la bascule Utiliser comme icône](assets/images/editor-manual-fr/05-new-wormhole-modal.png)

Deux manières d'attacher une image :

- **URL de l'image** : colle l'adresse d'une image hébergée ailleurs sur le web. À utiliser quand le foyer de l'image est quelque part de stable (une archive de musée, un site communautaire, un CDN sous ton contrôle). L'URL doit pointer vers l'image elle-même, pas vers une page qui contient l'image.
- **Sélecteur de fichier** : choisis **Choisir un fichier** et téléverse une image depuis ton ordinateur. Telaris garde le fichier téléversé sur ton instance et le sert à qui visite.

Dans les deux cas, l'image devient le visuel principal de qui visite à l'ouverture du trou de ver.

**Utiliser comme icône du trou de ver** est une bascule sous les champs d'image. Quand elle est activée, l'image remplace l'icône 3D par défaut du thème : qui visite voit l'image *comme* le trou de ver dans la scène 3D, pas seulement à l'intérieur de la fiche d'information. Utile quand l'image est l'identité du trou de ver (un portrait, une couverture, un logo). Quand elle est désactivée, la scène 3D montre l'icône par défaut du thème et l'image n'apparaît que dans la fiche d'information ouverte.

**Attribution de l'image** est un petit champ libre qui voyage avec l'image. Utilise-le pour le crédit photographique, l'archive source, une note de licence, tout ce qui s'attacherait à l'image si elle paraissait dans un livre imprimé. Qui visite voit cette mention à côté de l'image dans la fiche d'information.

## L'onglet Vidéo

À utiliser pour les extraits de film, les entretiens enregistrés, les animations, tout ce qui bouge. Telaris prend en charge le MP4 uniquement à ce stade ; les autres formats (WebM, MOV, AVI) doivent être transcodés d'abord ou hébergés sur un service vidéo et intégrés (voir Code à intégrer ci-dessous).

![Onglet Vidéo dans la fenêtre Nouveau trou de ver : URL vidéo / sélecteur de fichier pour un MP4](assets/images/editor-manual-fr/07-media-video-tab.png)

Mêmes deux chemins que pour l'image : colle une URL vers un MP4 hébergé ailleurs, ou téléverse un fichier. Une fois le trou de ver enregistré, la fiche d'information de qui visite montre un lecteur vidéo avec les contrôles standards (lecture, pause, défilement, volume, plein écran).

**La taille importe.** Les fichiers vidéo sont typiquement bien plus gros que les images ; la limite de téléversement d'une instance peut t'arrêter bien avant que ta patience s'épuise. Si le téléversement échoue, demande à qui exploite l'instance la limite en vigueur, ou héberge la vidéo à l'extérieur et utilise le champ URL.

Si ta vidéo vit sur un service de diffusion en continu (Vimeo, YouTube, archive.org), le champ Code à intégrer plus bas est le bon outil, pas l'onglet Vidéo.

## L'onglet PDF

Pour les documents : articles, guides de terrain, photocopies, rapports, partitions, manuscrits.

![Onglet PDF dans la fenêtre Nouveau trou de ver : URL PDF / sélecteur de fichier](assets/images/editor-manual-fr/08-media-pdf-tab.png)

Mêmes deux chemins. Une fois enregistré, la fiche d'information de qui visite intègre un lecteur PDF dans la page : la personne peut faire défiler le document, le chercher, copier le texte, et le télécharger (les commandes standards du lecteur PDF).

Les téléversements PDF ont une taille maximale fixée par qui exploite l'instance (couramment 25 Mo). Si ton fichier est plus gros, scinde-le, héberge-le à l'extérieur et lie-le avec le champ URL, ou demande à qui exploite d'augmenter la limite.

## Audio

Le champ Audio apparaît sous les onglets de visuel principal. Il est indépendant du choix image / vidéo / PDF ; un trou de ver peut combiner audio et un visuel principal de n'importe quelle façon.

- **URL / fichier audio** : colle une URL vers un fichier audio ou téléverses-en un. MP3 est le choix le plus sûr ; de nombreux navigateurs prennent aussi en charge OGG et WAV.

Quand l'audio est attaché, deux bascules contrôlent la lecture :

- **Lecture automatique** : quand elle est activée, l'audio démarre dès que qui visite ouvre la fiche d'information du trou de ver. Désactivée, qui visite voit un bouton de lecture et démarre l'audio elle-même. La lecture automatique convient généralement aux pistes courtes, ambiantes ou atmosphériques ; désactivée convient à la parole, à la musique, à tout ce qui demande de l'attention.
- **Boucle** : quand elle est activée, l'audio repart du début à chaque fin. À utiliser pour les boucles ambiantes, les nappes, les paysages sonores ; à désactiver pour tout audio avec un arc narratif.

L'audio joue en arrière-plan de la fiche d'information ; qui visite peut le mettre en pause ou le faire défiler à tout moment avec les commandes audio standards.

## Code à intégrer

Le quatrième chemin de média, pour du contenu hébergé sur un autre service qui fournit déjà un fragment d'intégration : un iframe Vimeo, un lecteur Spotify, une piste SoundCloud, un lecteur archive.org, une scène 3D SketchFab.

Trouve le champ **Code à intégrer** (sous les onglets de visuel principal) et colle le fragment exactement comme l'hôte te le donne. Telaris ne transforme ni n'assainit le code à intégrer ; ce que tu colles est ce que qui visite obtient. Teste le trou de ver ensuite en l'ouvrant en vue de visite ; si l'intégration est cassée, le champ est l'endroit à corriger.

Le code à intégrer et le visuel principal ne s'excluent pas mutuellement (l'intégration apparaît séparément dans la fiche d'information), mais pour la clarté il vaut généralement mieux choisir l'un ou l'autre.

## Le remplacement d'icône

Sous les champs de médias, une **URL / fichier d'icône** apparaît. Ceci règle l'apparence du trou de ver dans la scène 3D, *séparément* du visuel principal. À utiliser quand :

- Tu veux une icône 3D personnalisée (un petit graphisme qui représente le trou de ver à l'échelle de la scène), distincte de la plus grande image que voit qui visite à l'intérieur de la fiche d'information.
- La bascule Utiliser comme icône de l'onglet Image ne suffit pas parce que tu as une Image *et* que tu veux que l'icône de scène soit autre chose.

La plupart des comptes d'édition n'en ont pas besoin ; les icônes par défaut du thème couvrent la plupart des cas. Quand tu en as besoin, fournis une petite image carrée (PNG ou SVG) et Telaris l'utilise dans la scène 3D.

## Stockage et ce qui voyage avec un trou de ver

Les médias téléversés sont stockés sur ton instance. Les téléversements de chaque trou de ver vivent sous un dossier identifié par l'identifiant du trou de ver ; restaurer un instantané ramène les téléversements avec lui, supprimer un trou de ver retire ses téléversements.

Les médias liés par URL restent chez leur hôte d'origine ; si l'hôte supprime le fichier, le média du trou de ver s'éteint. L'édition avec des références externes précieuses devrait songer à téléverser le fichier plutôt qu'à le lier, pour que l'archive survive à l'hôte d'origine.

## Composer une page avec Hotglue

Parfois une seule image ou une seule vidéo ne suffit pas. Tu veux une petite composition : un titre, un paragraphe, deux photographies côte à côte, une légende en dessous, un lien vers l'extérieur. **Hotglue** est le mode de média pour cela. Au lieu de remplir un emplacement fixe, tu composes une page libre où chaque élément peut être placé, dimensionné et disposé à la main, et cette page devient les médias du trou de ver.

Dans la fenêtre de modification du trou de ver, ouvre la section **Médias** et choisis l'onglet **Hotglue**, puis choisis **Modifier le contenu hotglue**. Un éditeur presque en plein écran s'ouvre par-dessus la page. C'est une toile ouverte : il n'y a ni lignes ni colonnes auxquelles s'ajuster. Tu ajoutes un bloc de texte ou une image, puis tu le glisses où tu veux, tu le redimensionnes et tu superposes les éléments les uns sur les autres.

![La fenêtre de modification du trou de ver avec l'onglet de média Hotglue actif : une courte ligne d'aide et le bouton Modifier le contenu hotglue](assets/images/editor-manual-fr/14-media-hotglue-tab.png)

Les gestes de base :

- **Ajouter du texte.** Double-clique sur une zone vide de la toile pour créer un bloc de texte, puis écris. Clique en dehors pour terminer. Glisse le bloc pour le repositionner ; glisse son bord pour le redimensionner.
- **Ajouter une image.** Glisse un fichier image depuis ton ordinateur sur la toile, ou utilise la barre d'outils pour en choisir une. L'image est enregistrée avec la page. Glisse-la et redimensionne-la comme n'importe quel autre élément.
- **Disposer librement.** Les éléments peuvent se trouver n'importe où et se chevaucher. Il n'y a pas de grille ; la disposition que tu construis est celle que voit qui visite.
- **La page s'enregistre pendant que tu travailles.** Il n'y a pas de bouton d'enregistrement séparé dans la toile ; tes changements sont conservés au fur et à mesure. Quand tu as terminé, ferme l'éditeur.

De retour dans la fenêtre du trou de ver, laisse l'onglet **Hotglue** sélectionné et enregistre le trou de ver. Dès lors, ouvrir ce trou de ver montre ta page composée à la place de l'image ou de la vidéo classiques. Qui visite voit la page exactement comme tu l'as disposée, sans pouvoir la modifier.

Quelques points à garder en tête :

- **Tu ne modifies que les pages des galaxies où tu as un siège.** La modification avec Hotglue suit la même règle d'accès que le reste du trou de ver : tu peux composer des pages sur tes propres galaxies, et non sur des galaxies auxquelles on ne t'a pas donné accès.
- **Une page Hotglue est une seule surface composée.** Contrairement au reste de Telaris, elle ne se traduit pas d'elle-même selon la langue de qui visite ; le texte que tu places est le texte que tout le monde voit. Si ton public est multilingue, écris la page en conséquence.
- **La disposition libre est le mode de média le plus expressif et le moins indulgent.** Le placement absolu apparaît exactement comme tu l'as fixé, ce qui veut aussi dire qu'il ne se réajuste pas pour les petits écrans ni pour les technologies d'assistance comme le fait le texte ordinaire. Utilise-le là où la composition compte ; appuie-toi sur les onglets classiques Image ou PDF pour les documents simples.
- **Classique et Hotglue sont des alternatives, pas un empilement.** Un trou de ver montre l'un ou l'autre, selon l'onglet ouvert au moment d'enregistrer. Revenir à Classique n'efface pas la page Hotglue ; cela cesse seulement de l'afficher, donc tu peux y revenir plus tard en resélectionnant l'onglet Hotglue.

## Choses qu'il vaut la peine de savoir

- **Passer d'un onglet de visuel principal à l'autre efface le champ où tu étais.** Une invite de sécurité avant l'enregistrement t'avertit. Si tu changes d'avis, reviens à l'onglet précédent avant d'enregistrer.
- **Un audio en boucle peut surprendre à la première visite.** Si tu livres une boucle audio, écoute la frontière (le moment où la boucle redémarre) ; la couture est ce que qui visite remarquera.
- **Une image en haute résolution est plus utile qu'en basse.** Telaris réduit automatiquement les images pour la scène 3D ; téléverser à pleine qualité signifie une fiche d'information plus nette, et signifie que les futurs changements de format n'exigeront pas un retéléversement.
- **Le texte d'un PDF est cherchable dans le lecteur en page**, mais seulement si le PDF lui-même a une couche de texte. Les documents scannés sans OCR sont des images plates dans une enveloppe PDF ; la recherche ne trouvera rien.
- **Les fichiers vidéo ne diffusent pas par tronçons** : à l'ouverture du trou de ver, le fichier entier se télécharge. Garde les vidéos courtes et bien compressées.
- **Les intégrations externes peuvent se casser avec le temps.** Les services changent leur format d'intégration, abandonnent des lecteurs, ou retirent du contenu. Un trou de ver qui dépend d'une intégration est un trou de ver dont la demi-vie est plus courte que celui dont le média vit sur ton instance.
