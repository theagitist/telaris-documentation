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

Le menu d'actions sur chaque ligne de trou de ver offre quatre opérations :

- **Voir** ouvre un aperçu en lecture seule de la fiche d'information du trou de ver comme qui visite la verra. Utilise-le chaque fois que tu veux vérifier un changement avant de considérer le travail comme terminé.
- **Modifier** ouvre la fenêtre ci-dessus.
- **Dupliquer** crée une copie du trou de ver, avec le même contenu, dans la même galaxie, nommée « Nom d'origine (Copie) ». Le nouveau trou de ver reçoit une nouvelle position dans la scène 3D ; tout le reste est repris. Utile quand tu veux un quasi-doublon comme point de départ.
- **Supprimer** retire le trou de ver. Une fenêtre de confirmation apparaît d'abord ; les suppressions sont permanentes (qui exploite l'instance peut parfois restaurer depuis un instantané, mais la réponse devrait être : ne supprime que si tu en es sûre).

## Choses qu'il vaut la peine de savoir

- **Enregistre avant de changer de galaxie dans le menu déroulant** si tu es au milieu d'une édition ; le changement peut fermer la fenêtre sans enregistrer.
- **La position dans la scène 3D est automatique.** Chaque trou de ver reçoit une position attribuée par le système à la création. Tu n'as pas besoin de choisir où le trou de ver se place dans l'espace ; la disposition est générée. Pour relancer la position d'un trou de ver au hasard, duplique-le et supprime l'original (le duplicata reçoit une nouvelle position).
- **Les mots-clés se comparent sans tenir compte de la casse.** « Indigène » et « indigène » sont le même mot-clé ; l'étiquette utilisera la casse utilisée en premier dans la galaxie.
- **Un trou de ver sans description est permis mais silencieux.** Qui visite et l'ouvre ne voit que le nom. Utilise ce modèle quand le rôle du trou de ver est purement visuel (une carte postale en image seule) ou quand il sert de repère de navigation.
- **Les étiquettes de mots-clés d'un trou de ver sont colorées de façon déterministe** par le texte du mot-clé. Le même mot-clé reçoit toujours le même pastel à travers chaque galaxie sur ton instance ; c'est intentionnel, pour que qui visite reconnaisse *indigène* par la couleur autant que par l'orthographe.
- **Les trous de ver importés sont en lecture seule.** Si ton instance importe du contenu d'une source externe (une archive sœur, une communauté en amont), ces trous de ver apparaissent dans ta liste d'édition mais ne peuvent pas être édités ; la fenêtre de modification s'ouvre en état de visualisation. Le changement doit se faire à la source.
