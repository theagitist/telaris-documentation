# Introduction

Ce manuel s'adresse à toute personne qui compose une **page Hotglue** : une mise en page visuelle en forme libre où le texte, les images, la vidéo et le son se placent exactement là où tu les déposes, sans grille ni gabarit pour leur dicter leur position. Si une simple boîte de texte te semble trop rigide pour l'aspect que tu veux donner à un contenu, Hotglue est la surface qui t'offre une toile vierge à la place.

## Ce qu'est Hotglue

Hotglue est un éditeur de page visuel. Tu fais glisser des objets sur une page, tu les déplaces et les redimensionnes à la main, et ce que tu arranges est ce que la personne qui visite voit. Il n'y a pas de colonnes à remplir ni de forme fixe : une page peut être aussi large et aussi haute que tu veux, et un objet peut en chevaucher un autre, reposer sur un arrière-plan coloré, ou flotter là où tu le mets.

Deux choses rendent Hotglue différent de la plupart des éditeurs, et il vaut la peine de les connaître dès le départ :

- **Il n'y a pas de bouton Enregistrer.** Chaque déplacement, redimensionnement et modification est enregistré au moment où tu le fais. Tu n'as jamais à penser à enregistrer, et il n'y a pas non plus d'« annuler les modifications ». Si tu veux revenir sur une erreur, Hotglue conserve un historique (voir *révisions* dans *La toile*).
- **Ce que tu modifies est ce qui est publié, immédiatement.** Quand tu changes une page, le changement est en ligne pour les personnes qui visitent aussitôt. Il n'y a pas d'étape de publication distincte ni de cache à vider.

## D'où vient Hotglue

Hotglue n'est pas le nôtre à l'origine. Il a été créé par Danja Vasiliev et Gottfried Haider et est devenu largement connu grâce au service hébergé sur hotglue.me. Il a été conçu comme une réaction délibérée contre les conventions du design web ordinaire : au lieu de gabarits, de colonnes et de hiérarchies bien ordonnées, il offre une toile libre où la mise en page est non linéaire et où le placement t'appartient entièrement. Cet esprit, qui rompt avec les standards habituels du web et invite à une composition créative et imprévue, est exactement la raison pour laquelle Telaris l'utilise.

Le projet original n'est plus développé activement en amont. Son code source reste disponible et ouvert, sous licence GNU General Public License version 3 (GPL-3.0) :

- Projet en amont : <https://hotglue.me> et le code source sur <https://github.com/k0a1a/hotglue2>

## La version Telaris de Hotglue

Ce manuel décrit la **version Telaris de Hotglue**, que nous maintenons et développons activement sous forme de fork. Elle reste open source sous la même licence GPL-3.0, et notre code source est public :

- Fork Telaris : <https://github.com/theagitist/hotglue2>

Comme nous le développons nous-mêmes, le Hotglue intégré à Telaris dispose de plusieurs fonctionnalités absentes de l'original. La plus grande partie de ce que couvre ce manuel est commune au Hotglue classique, mais les éléments suivants ont été ajoutés ou nettement améliorés pour Telaris :

- **La prise en charge des images WebP**, en plus de JPEG, PNG et GIF.
- **Une interface d'édition rafraîchie**, avec un jeu d'icônes moderne et un aspect plus net, aux couleurs de Telaris.
- **Davantage de sources vidéo.** Les intégrations fonctionnent avec YouTube, Vimeo et PeerTube, y compris les vidéos PeerTube hébergées sur n'importe quel serveur fédéré.
- **Un éditeur d'image complet dans la page** (basé sur miniPaint) pour dessiner une nouvelle image ou retoucher une image existante sans quitter la page.
- **Le mode soundboard**, où une page publiée devient jouable : touche les tuiles vidéo pour déclencher des extraits, avec un son auto-hébergé mixé pour que plusieurs puissent retentir en même temps.
- **L'accessibilité sur téléphone et petits écrans.** Les pages publiées s'adaptent automatiquement aux écrans étroits, de sorte qu'une mise en page conçue large reste utilisable sur un téléphone.
- **L'intégration dans Telaris**, avec le contrôle d'accès par personne qui édite, le rattachement de pages aux trous de ver, et la vue de gestion **Contenu hotglue** décrite plus loin dans ce manuel.
- **Une interface localisée.** L'éditeur est disponible en anglais, espagnol, portugais et français : les menus de la toile, les info-bulles et les invites, l'éditeur d'image intégré, ainsi que les contrôles Telaris qui les entourent (la vue Contenu hotglue, la barre d'outils, les boutons et les fenêtres de dialogue) suivent tous la langue dans laquelle tu travailles.

Quand ce manuel mentionne l'un de ces éléments, il décrit spécifiquement la version Telaris. Si tu as déjà utilisé Hotglue ailleurs, voilà les différences auxquelles t'attendre.

## Comment ce manuel est organisé

Les chapitres progressent depuis la façon d'entrer, jusqu'à la toile elle-même, puis chaque type de contenu que tu peux ajouter, et enfin la gestion de tes pages et leur apparence pour les personnes qui visitent.

1. **Entrer.** Atteindre l'éditeur Hotglue dans Telaris, et qui peut modifier quoi.
2. **La toile.** Le mode édition, les deux menus, et comment placer, déplacer, redimensionner et arranger des objets.
3. **Ajouter du contenu.** Images, texte, vidéo web, dessins, son et outils d'objet.
4. **Gérer les pages.** La vue Contenu hotglue : créer, nommer, attribuer et ranger des pages.
5. **L'apparence sur téléphone.** Ce que voit une personne qui visite sur un petit écran, et des conseils pour composer en gardant cela à l'esprit.
6. **Raccourcis clavier.** Tous les raccourcis dans un seul tableau.
7. **Glossaire.** Les éléments nommés, définis brièvement.

## Conventions

- **Les chemins de menu** apparaissent ainsi : <span class="menu-path">menu PAGE &rarr; changer la couleur d'arrière-plan</span>.
- **Les boutons et les info-bulles** apparaissent en gras : **Nouvelle page**, **placer sur la page**, **Trou de ver attribué**.
- **Les raccourcis clavier** utilisent <kbd>alt</kbd> + <kbd>o</kbd>.
- Les *italiques* introduisent un terme la première fois qu'il apparaît.

> [!note] Quand quelque chose ne va pas
> Si une page ne se charge pas, ou si l'éditeur se comporte d'une manière que ce manuel ne décrit pas, contacte la personne qui gère ton instance (la personne qui **opère**). Ce manuel se concentre sur ce que tu peux faire une fois que tout fonctionne comme prévu.
