# Galaxies et amas

Les onglets **Galaxies** et **Amas** sont la vue de l'administration sur tout le contenu de l'instance. L'édition ne voit que ses propres galaxies ; toi, tu vois chaque galaxie, y compris celles importées d'ailleurs, et tu peux les regrouper en amas. Ce chapitre couvre les deux onglets.

## L'onglet Galaxies

![L'onglet Galaxies : un tableau de chaque galaxie de l'instance avec son amas, son propriétaire, et si elle est importée](assets/images/admin-manual-fr/05-galaxies-list.png)

L'onglet Galaxies liste chaque galaxie de l'instance, peu importe qui l'a faite. Pour chaque galaxie, tu peux voir à quel amas elle appartient (le cas échéant), à qui elle appartient, et si elle est **importée** d'une autre instance. D'ici, tu peux atteindre les paramètres d'une galaxie de la même façon que le ferait son édition, et tu peux déplacer une galaxie dans ou hors d'un amas.

La rédaction quotidienne d'une galaxie (son thème, ses trous de ver, ses mots-clés) est un travail d'édition et vit dans le Manuel d'édition. Ce qui t'est propre en tant qu'administration, c'est la vue de toute l'instance : tout voir d'un coup, et les deux préoccupations ci-dessous, le contenu importé et les amas.

## Galaxies importées (en lecture seule)

Si ton instance s'abonne à une galaxie publiée par une autre instance (voir *Fédération et le Pluriverse*), cette galaxie apparaît ici comme **importée**. Une galaxie importée est un miroir : son contenu est copié sur ton instance pour que qui visite puisse le voir, mais l'autorité qui la régit reste avec l'instance qui l'a publiée.

- Les galaxies importées sont en **lecture seule** pour tout le monde sur ton instance, l'édition comme l'administration. Tu ne peux pas changer leur contenu, parce que le changement doit se faire à la source.
- Une action **Rafraîchir** tire la dernière version d'une galaxie importée depuis sa source, pour que ton miroir rattrape les modifications faites en amont. La fédération rafraîchit aussi les miroirs selon un calendrier ; Rafraîchir est le bouton « maintenant » manuel.
- Si la source cesse de te publier la galaxie, ou si tu cesses de t'y abonner, le miroir est abandonné. Le contenu importé n'a jamais été à toi pour le garder ; il n'est présent que tant que dure l'abonnement.

Le chapitre sur la fédération couvre l'abonnement, la publication et le blocage en détail. Ici, il suffit de savoir que les galaxies importées apparaissent dans cette liste, sont en lecture seule, et peuvent être rafraîchies.

## L'onglet Amas

Un **amas** regroupe des galaxies. Les amas sont la façon dont une famille de galaxies apparentées est présentée ensemble et la façon dont certains paramètres de l'instance sont limités à un sous-ensemble de galaxies plutôt qu'à toute l'instance.

![L'onglet Amas : une liste d'amas de galaxies, chacun avec les galaxies qu'il contient](assets/images/admin-manual-fr/06-clusters-list.png)

Depuis l'onglet Amas, tu peux créer un amas, le nommer, et y mettre des galaxies. Une galaxie appartient à au plus un amas à la fois. Les amas comptent pour l'administration pour deux raisons :

- Ils sont un niveau dans la **cascade de modification** (voir *Contrôle d'accès de l'édition*) : tu peux désactiver la modification pour tout un amas d'un coup.
- Ils sont une portée pour la **correspondance des mots-clés**, ci-dessous.

L'inscription autonome peut aussi placer automatiquement la galaxie personnelle de chaque nouveau compte d'édition dans un amas propre à l'instance, pour que toutes les galaxies personnelles d'un appel ouvert se tiennent ensemble plutôt que de se disperser dans la liste.

## Correspondance des mots-clés (exacte et floue)

Telaris trace des connexions entre les trous de ver qui partagent un mot-clé. Par défaut, la correspondance est **exacte** : deux trous de ver ne se connectent que lorsqu'ils portent exactement le même mot. Tu peux assouplir cela en une correspondance **floue**, pour que des orthographes proches se connectent aussi : un pluriel et son singulier, une petite faute de frappe, une variante mineure.

La correspondance floue est une bascule, et elle peut être fixée à deux portées :

- pour l'**instance entière** (l'interrupteur se trouve dans l'onglet Paramètres globaux, voir *Paramètres globaux*), pour que chaque galaxie utilise la correspondance floue, ou
- pour un **amas** (dans les paramètres propres de cet amas), pour que seules les galaxies de cet amas le fassent.

Elle est **désactivée par défaut** ; les connexions restent exactes jusqu'à ce que tu l'actives. Un garde-fou empêche la correspondance floue de trop connecter sur des mots courts très courants, pour que l'activer n'inonde pas le réseau de liens erronés, mais c'est tout de même un changement que ton édition verra (de nouvelles lignes de relation apparaissant entre des mots-clés proches à travers les galaxies). Active-la quand le vocabulaire de ton contenu dérive dans l'orthographe et que tu veux que ces variantes se connectent ; laisse-la désactivée quand tes mots-clés sont contrôlés et que tu veux que seules les correspondances exactes tracent une ligne.

## Choses qu'il vaut la peine de savoir

- **Tu vois tout ; l'édition voit le sien.** L'onglet Galaxies est le seul endroit avec toute l'instance en vue. Utilise-le pour auditer ce qui existe, à qui cela appartient, et ce qui est venu de l'extérieur.
- **Importé n'est pas à toi.** Les galaxies importées en lecture seule sont une courtoisie d'une autre instance, présentes tant que dure l'abonnement. Ne les traite pas comme une sauvegarde ni comme ton contenu.
- **La correspondance floue est un choix éditorial par instance ou par amas**, pas par trou de ver. Si l'édition demande pourquoi des mots-clés d'orthographe proche se connectent (ou non), cette bascule est la réponse.
