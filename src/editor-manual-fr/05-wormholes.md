# Trous de ver

Un trou de ver est la plus petite unité de contenu dans Telaris. Tout ce qui se publie en édition est, en fin de compte, un trou de ver : un passage de texte, une photographie, un enregistrement audio, un extrait de film, un PDF, une citation, une seule pensée. Ce chapitre parcourt la création d'un trou de ver, son édition, les champs qui le façonnent, et les choix que le formulaire t'invite à faire.

## Créer un nouveau trou de ver

Depuis la page d'édition, sélectionne la galaxie dans laquelle tu travailles, puis choisis **Nouveau trou de ver**. Une fenêtre s'ouvre :

![Fenêtre Ajouter un nouveau trou de ver : formulaire vide avec Nom, Galaxie, Type, Mots-clés, Description, URL, et onglets de médias visibles](assets/images/editor-manual-fr/05-new-wormhole-modal.png)

Le formulaire a quatre grandes régions, dans l'ordre où tu fais défiler la fenêtre :

1. **Identité** en haut : Nom, Galaxie, Type de trou de ver, Mots-clés.
2. **Bascules de comportement** : Mettre en avant, Afficher les mots-clés.
3. **Corps** : Description, URL.
4. **Médias** : image, vidéo, audio, PDF, et le remplacement d'icône.

Enregistre avec le bouton en bas de la fenêtre ; le nouveau trou de ver apparaît immédiatement dans la liste. Annule ou clique à l'extérieur de la fenêtre pour abandonner.

## Champs d'identité

### Nom

Obligatoire. L'étiquette que lit qui visite dans la scène 3D, dans toute liste, et dans l'URL lors du partage. Choisis un nom qui se lit proprement seul ; il sera cité hors contexte plus souvent que tu ne le crois.

Les noms à l'intérieur d'une galaxie doivent être uniques ; la fenêtre te préviendra si un nom est déjà pris avant l'enregistrement. Entre galaxies, deux trous de ver peuvent partager un nom sans conflit.

### Galaxie

Obligatoire, mais habituellement pré-rempli. Le menu déroulant montre chaque galaxie que tu peux éditer. Si tu es partie d'une galaxie particulière sur la page d'édition, cette galaxie est sélectionnée par défaut ; si tu es partie de *Toutes mes galaxies*, tu choisis ici.

Changer la galaxie dans ce menu déroulant **déplace** le trou de ver vers cette galaxie. Les mots-clés du trou de ver l'accompagnent, mais ses *positions* de mots-clés sur la toile de la galaxie de destination peuvent demander une retouche.

### Type de trou de ver

Un menu déroulant avec deux valeurs :

- **Objet** est la valeur par défaut et la bonne réponse pour presque tout trou de ver. Un Objet porte du contenu (description, médias).
- **Portail** transforme le trou de ver en porte vers une autre galaxie. Choisir Portail révèle un second menu déroulant pour la galaxie cible. Le chapitre 9 couvre les portails.

### Mots-clés

Une saisie par étiquettes. Tape un mot-clé et appuie sur **Entrée** (ou virgule) pour l'ajouter ; clique sur le **×** d'une étiquette pour la retirer. Des suggestions apparaissent à mesure que tu tapes, tirées de :

- Mots-clés déjà utilisés ailleurs dans **cette** galaxie.
- Mots-clés utilisés dans des galaxies qui partagent le préfixe `[crochet]` de ta galaxie.

Choisis les mots-clés en pensant au chemin de qui visite : chaque mot-clé que tu attaches est une porte de ce trou de ver vers chaque autre trou de ver qui partage le même mot. Moins tu en attribues, plus chaque connexion semble délibérée ; plus tu en attribues, plus la toile est dense. Le chapitre 7 couvre la stratégie de mots-clés.

## Bascules de comportement

### Mettre le trou de ver en avant

Désactivée par défaut. Quand elle est activée, ce trou de ver s'affiche plus grand et plus saillant dans la scène 3D. Utilise avec parcimonie : si tu mets tout en avant, rien n'est en avant. Le drapeau de mise en avant est aussi le marqueur que la fonctionnalité de visite automatique peut utiliser pour choisir ses arrêts (chapitre 11).

### Afficher les mots-clés

Désactivée par défaut. Quand elle est activée, qui visite voit les mots-clés de ce trou de ver imprimés à côté de lui dans la scène 3D, avant de l'ouvrir. Utile pour les trous de ver dont le rôle dans la galaxie se comprend mieux à travers ses étiquettes (un document de référence ; un repère de navigation ; une définition).

## Corps

### Description

Le texte que lit qui visite quand il ouvre le trou de ver. Il n'y a pas de limite de longueur ; les trous de ver d'une ligne et les essais longs sont également pris en charge. Le champ accepte un formatage markdown de base : paragraphes (une ligne vide), `**gras**`, `*italique*`, `[lien](https://...)`, listes, et `code` en ligne. Les titres et les médias intégrés ne sont pas rendus à l'intérieur de la description ; s'il te faut une coupure de type titre, laisse une ligne vide et commence un nouveau paragraphe.

Écris les descriptions dans ta propre voix. Telaris n'édite pas ce que tu écris ; la plateforme cadre le contenu, le contenu est à toi.

### URL

Facultatif. Si tu remplis ce champ, le trou de ver devient cliquable comme un lien sortant : quand qui visite ouvre la fiche d'information du trou de ver, un bouton *Ouvrir le lien* apparaît qui ouvre l'URL dans un nouvel onglet.

Utilise-le pour des références qui font autorité (un article, une page de livre, une archive sonore, un site communautaire). Laisse-le vide quand le trou de ver se suffit à lui-même.

## Médias

Un trou de ver peut porter un **visuel principal** plus une piste **audio** facultative et un **remplacement d'icône** facultatif. Le visuel principal est ce que voit qui visite en haut de la fiche d'information à l'ouverture du trou de ver ; l'audio joue en arrière-plan ; le remplacement d'icône change la façon dont le trou de ver apparaît dans la scène 3D.

La fenêtre organise le visuel principal comme un ensemble d'onglets : **Image**, **Vidéo (MP4)**, **PDF**. En choisir un puis enregistrer efface les autres ; un seul visuel principal à la fois. Le chapitre 6 couvre chaque onglet en détail.

Le champ audio est indépendant du visuel principal ; un trou de ver avec une image et un fichier audio joue l'audio pendant que l'image est visible. Du code à intégrer (par exemple un iframe Spotify ou Vimeo) est pris en charge comme alternative à image / vidéo / PDF quand le visuel est hébergé à l'extérieur.

## Éditer un trou de ver existant

Pour éditer un trou de ver, clique n'importe où sur sa ligne dans la liste, ou ouvre le menu d'actions de sa ligne et choisis **Modifier** :

![Fenêtre Modifier le trou de ver pour Fraise de plage : nom rempli, étiquettes de mots-clés, description, onglets de médias](assets/images/editor-manual-fr/06-edit-wormhole-modal.png)

La fenêtre est la même que le formulaire de création, avec les valeurs existantes pré-remplies. L'identifiant du trou de ver apparaît dans le coin supérieur droit (ici, `#279`) ; l'édition a rarement besoin de se référer aux identifiants, mais le nombre est utile quand tu signales un problème à qui exploite ton instance.

L'enregistrement applique le changement immédiatement. Qui visite la galaxie verra ta mise à jour au prochain chargement de page.

## Dupliquer, voir, supprimer

Le menu d'actions sur chaque ligne de trou de ver offre ces opérations :

- **Voir** ouvre un aperçu en lecture seule de la fiche d'information du trou de ver comme qui visite la verra. Utilise-le chaque fois que tu veux vérifier un changement avant de considérer le travail comme terminé.
- **Modifier** ouvre la fenêtre ci-dessus.
- **Dupliquer** crée une copie du trou de ver, avec le même contenu, dans la même galaxie, nommée « Nom d'origine (Copie) ». Le nouveau trou de ver reçoit une nouvelle position dans la scène 3D ; tout le reste est repris. Utile quand tu veux un quasi-doublon comme point de départ.
- **Créer un modèle** enregistre la forme du trou de ver comme un modèle réutilisable à partir duquel tu pourras estamper de nouveaux trous de ver plus tard. La section Modèles ci-dessous le couvre entièrement.
- **Supprimer** retire le trou de ver. Une fenêtre de confirmation apparaît d'abord ; les suppressions sont permanentes (qui exploite l'instance peut parfois restaurer depuis un instantané, mais la réponse devrait être : ne supprime que si tu en es sûre).

Dupliquer et Créer un modèle répondent à deux besoins différents : Dupliquer te donne un trou de ver de plus tout de suite, dans cette galaxie ; Créer un modèle te donne un moule que tu peux réutiliser à travers les galaxies et à travers les sessions.

## Trier la liste de trous de ver

Clique sur n'importe quel en-tête de colonne dans la liste de trous de ver pour trier selon cette colonne ; clique de nouveau pour inverser l'ordre. Trie par nom pour trouver un trou de ver par ordre alphabétique, ou par la colonne de dernière modification pour remonter ton travail le plus récent en haut. Le tri est une simple commodité d'affichage ; il ne change rien aux trous de ver eux-mêmes ni à la façon dont ils apparaissent à qui visite.

## Modèles

Un modèle est un point de départ réutilisable pour de nouveaux trous de ver. Si tu te retrouves à créer trou de ver après trou de ver avec la même forme (le même type, la même poignée de mots-clés, le même thème de description, le même genre de média intégré), tu peux saisir cette forme une fois et estamper de nouveaux trous de ver à partir d'elle, au lieu de remplir les mêmes champs à la main à chaque fois.

Les modèles sont **privés à toi**. Les modèles que tu crées sont les tiens seulement ; un autre compte d'édition sur la même instance ne les voit pas, et tu ne vois pas les siens. (L'administration peut voir chaque modèle, de la même façon qu'elle peut voir chaque galaxie.)

### Créer un modèle à partir d'un trou de ver

Tu ne construis pas un modèle à partir d'un formulaire vide. Tu le construis à partir d'un trou de ver que tu aimes déjà. Ouvre le menu d'actions de la ligne du trou de ver et choisis **Créer un modèle** :

![Le menu d'actions d'une ligne de trou de ver ouvert, montrant Voir, Modifier, Dupliquer, Créer un modèle et Supprimer](assets/images/editor-manual-fr/15-create-template-action.png)

Telaris saisit une copie de la structure et du contenu de ce trou de ver : son type, ses mots-clés, sa description, son URL, ses bascules de comportement et ses réglages de médias. Si le trou de ver porte du contenu Hotglue, le modèle copie aussi ce contenu, de sorte qu'un trou de ver créé à partir du modèle s'ouvre sur sa propre copie privée de la même page en forme libre. Le trou de ver d'origine n'est pas touché ; le modèle est une chose séparée et autonome dès l'instant où il est fait. Modifier ou supprimer le trou de ver plus tard ne change pas le modèle, et réciproquement.

Le nouveau modèle prend le nom du trou de ver. Tu peux le renommer plus tard depuis l'onglet Modèles.

### Baser un nouveau trou de ver sur un modèle

À côté de **Nouveau trou de ver** sur la page d'édition se trouve un petit menu déroulant. Sa valeur par défaut est **Aucun modèle**, qui te donne le formulaire vide ordinaire. Choisis plutôt un modèle dans le menu déroulant, et le prochain trou de ver que tu crées s'ouvre avec les champs de ce modèle déjà remplis :

![La barre d'outils de la page d'édition : le bouton Nouveau trou de ver à côté d'un menu déroulant affichant Aucun modèle, avec une liste de modèles enregistrés](assets/images/editor-manual-fr/16-template-selector.png)

La fenêtre qui s'ouvre est la fenêtre Nouveau trou de ver ordinaire, pré-remplie. Tout reste modifiable : change le nom (tu voudras presque toujours le faire, puisque le nom du modèle n'est qu'un espace réservé), ajuste les mots-clés, réécris la description. Rien n'est verrouillé. Le modèle décide seulement où le formulaire commence, pas où il finit. Si le modèle incluait du contenu Hotglue, le nouveau trou de ver reçoit sa propre copie privée de ce contenu, que tu modifies ensuite indépendamment.

Choisir un modèle est un choix par création. Le menu déroulant ne reste pas « armé » ; après que tu as créé un trou de ver à partir d'un modèle, il revient à **Aucun modèle** pour que ton prochain trou de ver soit vide à moins que tu ne choisisses de nouveau un modèle.

### Gérer tes modèles

La page d'édition a trois onglets en haut : **Trous de ver**, **Modèles** et **Contenu hotglue**. L'onglet Modèles liste chaque modèle que tu possèdes :

![L'onglet Modèles : un tableau de modèles avec les colonnes Nom et Hotglue, une boîte de recherche, et des actions Renommer et Supprimer par ligne](assets/images/editor-manual-fr/17-templates-tab.png)

La liste a deux colonnes : le **Nom** du modèle, et une colonne **Hotglue** qui marque les modèles porteurs de contenu Hotglue. Une boîte de recherche filtre la liste par nom. Clique sur un en-tête de colonne pour trier.

Les actions de chaque modèle sont :

- **Renommer** change le nom du modèle. C'est purement une étiquette pour ton propre usage ; cela ne touche aucun trou de ver déjà créé à partir du modèle.
- **Supprimer** retire le modèle. Les trous de ver que tu as déjà créés à partir de lui ne sont pas affectés ; ce sont désormais des trous de ver ordinaires, sans lien vivant vers le modèle. Supprimer un modèle est irréversible.

Dans cette première version, renommer et supprimer sont les seules modifications. Pour changer ce qu'un modèle contient, crée un nouveau modèle à partir d'un trou de ver qui a la forme voulue, et supprime l'ancien.

## Choses qu'il vaut la peine de savoir

- **Enregistre avant de changer de galaxie dans le menu déroulant** si tu es au milieu d'une édition ; le changement peut fermer la fenêtre sans enregistrer.
- **La position dans la scène 3D est automatique.** Chaque trou de ver reçoit une position attribuée par le système à la création. Tu n'as pas besoin de choisir où le trou de ver se place dans l'espace ; la disposition est générée. Pour relancer la position d'un trou de ver au hasard, duplique-le et supprime l'original (le duplicata reçoit une nouvelle position).
- **Les mots-clés se comparent sans tenir compte de la casse.** « Indigène » et « indigène » sont le même mot-clé ; l'étiquette utilisera la casse utilisée en premier dans la galaxie.
- **Un trou de ver sans description est permis mais silencieux.** Qui visite et l'ouvre ne voit que le nom. Utilise ce modèle quand le rôle du trou de ver est purement visuel (une carte postale en image seule) ou quand il sert de repère de navigation.
- **Les étiquettes de mots-clés d'un trou de ver sont colorées de façon déterministe** par le texte du mot-clé. Le même mot-clé reçoit toujours le même pastel à travers chaque galaxie sur ton instance ; c'est intentionnel, pour que qui visite reconnaisse *indigène* par la couleur autant que par l'orthographe.
- **Les trous de ver importés sont en lecture seule.** Si ton instance importe du contenu d'une source externe (une archive sœur, une communauté en amont), ces trous de ver apparaissent dans ta liste d'édition mais ne peuvent pas être édités ; la fenêtre de modification s'ouvre en état de visualisation. Le changement doit se faire à la source.
