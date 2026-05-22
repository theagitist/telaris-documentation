# Portails

Un portail est un type particulier de trou de ver. Au lieu de porter son propre contenu, il porte une destination : une autre galaxie. Qui visite et ouvre un portail le traverse. La scène se dissout, une nouvelle galaxie se charge, le portail se referme derrière. Les portails sont la manière dont l'édition construit des ponts intentionnels entre galaxies.

Ce chapitre couvre quand utiliser un portail plutôt qu'un mot-clé partagé, comment en créer un, et le petit ensemble de conventions éditoriales qui gardent un réseau de portails lisible.

## Quand le portail est le bon outil

Telaris t'offre déjà deux manières de connecter du contenu entre galaxies :

1. **Mots-clés partagés** : un trou de ver dans la galaxie A et un trou de ver dans la galaxie B tous deux étiquetés *intertidal* forment une connexion *passive*. Qui visite et suit *intertidal* dans l'une ou l'autre arrive sur une vue qui montre les deux.
2. **Étiquettes de galaxie** : la galaxie A et la galaxie B partageant l'étiquette *côte* créent une union ; qui visite et suit `/tag/coast` voit les trous de ver des deux galaxies ensemble.

Un portail est un troisième type de connexion, et beaucoup plus *actif* : l'édition dit en effet *depuis ce trou de ver, va là maintenant*. C'est le bon outil quand :

- La connexion est **directionnelle et délibérée**. Un mot-clé partagé est un réseau ; un portail est une flèche.
- La galaxie de destination est une **continuation de la conversation**, pas seulement un sujet apparenté. Qui lit devrait quitter sa galaxie courante et arriver dans une autre, pas naviguer les deux à la fois.
- Tu veux que le portail lui-même **apparaisse dans la scène 3D** comme un objet navigable. Un portail se rend comme un nœud 3D distinct ; qui visite peut le reconnaître et cliquer dessus délibérément.

Si rien de tout cela n'est vrai, un mot-clé ou une étiquette de galaxie est généralement un meilleur choix.

## Créer un portail

Un portail est un trou de ver dont le Type de trou de ver est réglé sur **Portail**. Depuis la fenêtre Nouveau trou de ver :

![Fenêtre Nouveau trou de ver avec Type de trou de ver réglé sur Portail : un champ Galaxie cible apparaît](assets/images/editor-manual-fr/11-portal-type-selector.png)

Étapes :

1. Ouvre **Nouveau trou de ver** depuis la page d'édition (ou ouvre la fenêtre de modification d'un trou de ver existant et change son type).
2. Règle **Type de trou de ver** sur **Portail**. Un champ **Galaxie cible** apparaît, avec un menu déroulant qui liste chaque galaxie à laquelle tu as accès.
3. Choisis la galaxie de destination dans le menu déroulant. Le bouton à côté, **Créer une nouvelle galaxie**, est un raccourci pour le cas où la destination n'existe pas encore ; le sélectionner te laisse rédiger la destination dans la foulée. La plupart du temps, tu choisis une galaxie existante.
4. **Nomme** le portail de manière lisible. Un portail est un trou de ver, donc le nom apparaît dans les listes et dans la scène 3D ; choisis un nom qui signale le voyage, pas seulement la destination. *Vers les cuvettes de marée* se lit mieux que *Cuvettes de marée*.
5. Ajoute une **Description** si tu veux qu'un court paragraphe apparaisse quand qui visite ouvre la fiche d'information du portail. La description est montrée brièvement avant le départ vers la galaxie de destination ; traite-la comme une phrase de seuil.
6. Facultatif : attribue quelques **mots-clés**. Les portails peuvent porter des mots-clés comme n'importe quel autre trou de ver ; cela aide le portail à apparaître dans la découverte par mots-clés.
7. Enregistre.

Le portail apparaît désormais dans la liste de trous de ver avec une étiquette **Portail** dans la colonne Type, et comme un nœud distinguable dans la scène 3D.

## Ce que vit qui visite

Qui visite et clique un portail dans la scène 3D voit :

- La fiche d'information du portail s'ouvre, comme pour tout autre trou de ver.
- La fiche montre le nom du portail, la description, et (selon les paramètres de l'instance) un bouton d'appel à l'action **Voyager** ou nommé de façon similaire.
- Activer l'appel à l'action ferme la galaxie courante et charge la destination.
- Dans la galaxie de destination, qui visite arrive à l'entrée de la galaxie (la position de départ par défaut), pas à un trou de ver particulier.

Qui visite peut utiliser le bouton Retour du navigateur pour revenir à la galaxie d'origine. Telaris **ne** place **pas** automatiquement de portail de retour dans la galaxie de destination ; si tu veux que le voyage soit aller-retour, tu dois placer un portail correspondant à la main.

## Portails aller-retour

Quand tu places un portail de A vers B, considère si tu veux aussi un portail de B vers A. Les deux sont indépendants : chacun est un trou de ver dans sa propre galaxie. Il n'y a pas de concept de « portails liés ».

La décision est éditoriale :

- **Oui, place un portail de retour** quand les deux galaxies sont partenaires à parts égales dans une conversation ; qui arrive en B devrait être invitée à revenir vers A aussi naturellement qu'elle a été invitée de A à B.
- **Non, laisse le retour implicite** quand le chemin naturel de qui visite est à sens unique (A est la galaxie de cadrage ; B est la réponse ; qui visite revient par le navigateur, si elle revient).

Si tu places un portail de retour, nomme-le pour la destination qu'il atteint, pas pour « revenir ». *Vers les plantes côtières* se lit mieux que *Retour* ou *Revenir*.

## Portails et toile de mots-clés

Les étiquettes de mots-clés d'un portail apparaissent sur la toile de mots-clés comme celles de n'importe quel autre trou de ver. Un portail étiqueté *intertidal* contribue à la toile de connexions *intertidal*. Parfois l'édition étiquette les portails avec un mot-clé spécifique comme *portail* pour pouvoir les filtrer hors de la découverte par mots-clés (qui visite peut ne pas vouloir des sauts trop riches en portails) ; dans notre galaxie de démonstration, le trou de ver portail porte l'étiquette *portail* précisément pour cette raison.

## Choses qu'il vaut la peine de savoir

- **Un portail ne peut cibler qu'une seule galaxie à la fois.** Si tu veux un « centre » qui s'éclate vers plusieurs galaxies, la réponse est plusieurs portails, pas un. Tu peux placer plusieurs portails dans une seule galaxie, chacun pointant ailleurs.
- **Le menu déroulant de cible liste seulement les galaxies que tu peux éditer.** Si la galaxie vers laquelle tu veux faire un portail est sur une autre instance, c'est du territoire de fédération et le domaine de qui exploite l'instance ; la surface d'édition ne rédige pas de portails entre instances.
- **Un portail peut être reciblé** en l'éditant et en choisissant une galaxie différente dans le champ Galaxie cible. Qui visite avait mis le portail en favori continuera d'arriver sur la galaxie désormais sélectionnée. Prévois cela quand tu changes de destination après publication.
- **Un portail qui cible sa propre galaxie** est techniquement permis mais fonctionnellement inutile : qui visite revient là où elle était. L'interface d'édition ne t'arrêtera pas, mais le résultat est nul.
- **Supprimer un portail retire le trou de ver entièrement.** La galaxie de destination n'est pas affectée ; seule la connexion disparaît. Les propres portails de la destination (s'il y en a) fonctionnent encore.
- **Les portails ne portent pas de médias.** Ils ont un nom, une description et des mots-clés, plus la galaxie cible. Les champs image, vidéo, audio et PDF sont encore dans la fenêtre mais devraient rester vides pour les portails ; si tu les remplis, ils sont simplement ignorés par l'expérience de visite du portail.
