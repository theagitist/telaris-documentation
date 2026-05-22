# Comment entrer

Telaris est un site web. Pour utiliser l'édition, tu ouvres ton instance dans un navigateur, tu te connectes, et tu commences à travailler. C'est tout le flux de connexion ; le reste de ce chapitre parcourt ce que tu vois, dans l'ordre.

## Ce dont tu as besoin

Trois choses, toutes fournies par qui exploite ton instance :

- **L'adresse de ton instance de Telaris** : un lien web, quelque chose comme `https://ton-instance.exemple`. Mets-le en favori.
- **Ton courriel d'édition** : l'adresse sous laquelle qui exploite l'instance a créé ton compte.
- **Ton mot de passe** : choisi par toi ou envoyé par qui exploite l'instance. Si ton compte a été créé pour toi, on te demandera probablement de définir un nouveau mot de passe à la première connexion.

S'il te manque l'un de ces trois éléments, demande à qui exploite ton instance.

## La page de connexion

Ouvre l'adresse de ton instance dans un navigateur moderne. Si tu n'es pas déjà connectée, tu arrives automatiquement sur la page de connexion. Si tu avais enregistré un favori vers une autre partie de l'instance, le navigateur fera un détour par la page de connexion d'abord puis te ramènera là où tu allais.

![Formulaire de connexion](assets/images/editor-manual-fr/01-login-form.png)

Deux champs : **Courriel** et **Mot de passe**. Saisis tes identifiants et sélectionne **Se connecter**.

Si tu oublies ton mot de passe, il y a un lien **Mot de passe oublié ?** sous le bouton Se connecter. Le lien demande ton courriel ; un courriel avec un lien de réinitialisation arrive dans ta boîte de réception en moins d'une minute. Les liens de réinitialisation expirent au bout d'un court délai ; si le lien ne fonctionne plus, redemande-en un.

## Une fois connectée

Tu arrives sur la page **Modifier les trous de ver**. C'est la page d'accueil d'édition, le point de départ de chaque session de travail. Les sections suivantes de ce manuel partent toutes d'ici.

![Page d'édition : sélecteur de galaxie en haut à droite, liste de trous de ver en dessous, recherche à droite](assets/images/editor-manual-fr/02-editor-home.png)

La page se présente en deux cartes :

**Carte du haut : qui tu es, où tu es.**

- Le titre de la page, **Modifier les trous de ver**, se trouve en haut à gauche.
- Sous le titre, une petite ligne te salue par ton nom et confirme ton rôle : *Bienvenue, Ton Nom (édition)*. Le rôle détermine ce que tu peux faire ; si tu vois quelque chose que ce manuel décrit mais que tu n'y accèdes pas, ton rôle n'inclut pas cette surface, et qui exploite ton instance peut l'ajuster.
- À droite du titre, **Galaxie courante** est un menu déroulant qui sélectionne la galaxie dans laquelle tu édites en ce moment. *Toutes mes galaxies* est la valeur par défaut et montre les trous de ver de chaque galaxie à laquelle tu as accès. Choisir une galaxie particulière filtre tout ce qui se trouve en dessous sur cette galaxie.
- À côté du menu déroulant, le bouton **Voir** ouvre ta galaxie courante dans la vue pour qui visite (la scène 3D). C'est la même vue que voit qui lit ; il est utile d'y basculer de temps à autre pour vérifier que les changements que tu fais se lisent comme tu l'attends.
- Le bouton **Déconnexion** tout à droite met fin à ta session. Telaris garde ta session active à travers les redémarrages du navigateur tant que tu ne te déconnectes pas explicitement.

**Carte du bas : tes trous de ver.**

- **Trous de ver (N)** en haut à gauche t'indique combien de trous de ver se trouvent dans la vue de galaxie courante. *N* est un nombre ; quand tu choisis *Toutes mes galaxies*, il compte à travers toutes les galaxies.
- **Nouveau trou de ver** ouvre le formulaire pour créer un nouveau trou de ver. Le chapitre 5 le couvre en détail.
- **Touchés aujourd'hui** restreint la liste aux trous de ver que tu as édités depuis minuit. Utile pour reprendre là où tu en étais.
- **Action groupée par mot-clé** ouvre une fenêtre pour des opérations en lot sur plusieurs trous de ver à la fois (supprimer tous les trous de ver portant un mot-clé donné, les déplacer tous vers une autre galaxie). Le chapitre 7 couvre cette surface.
- **?** ouvre un petit panneau qui liste tous les raccourcis clavier que l'édition prend en charge. En mémoriser ne serait-ce que deux ou trois te fera gagner du temps ; les plus utiles sont `n` (nouveau trou de ver), `/` (mettre le focus sur la recherche), et `g` (ouvrir les paramètres de galaxie).
- **Recherche** filtre la liste des trous de ver à mesure que tu tapes. Elle parcourt les noms de trous de ver, les descriptions, les noms de galaxies et les mots-clés ; un seul champ, quatre colonnes.

La liste de trous de ver elle-même montre : nom, type, galaxie, mots-clés, un drapeau de mise en avant, date de création, date de mise à jour, et un menu d'actions. Les chapitres suivants expliquent chaque colonne.

## Se déconnecter

Le bouton **Déconnexion** en haut à droite met fin à ta session et te ramène à la page de connexion. Telaris ne te déconnecte pas automatiquement ; si tu partages un ordinateur, déconnecte-toi à la fin de ta session.

## Choses qu'il vaut la peine de savoir

- **Plusieurs onglets, c'est sans danger.** Tu peux ouvrir l'édition dans plusieurs onglets sans la perturber. Chaque onglet garde sa propre sélection de *Galaxie courante*.
- **Ta session persiste à travers les redémarrages du navigateur** jusqu'à ce que tu te déconnectes explicitement ou que qui exploite l'instance invalide les sessions pendant une maintenance. Si tu te retrouves soudain à la page de connexion, c'est la raison la plus probable ; reconnecte-toi et continue.
- **L'expérience mobile couvre la lecture et l'édition légère.** Certaines surfaces (notamment la *toile de mots-clés*, couverte au chapitre 8) sont réservées à l'ordinateur de bureau. Le manuel signale chaque surface au fil de l'eau.
- **Si une page ne se charge pas** : rafraîchis le navigateur. Si elle échoue encore, c'est le moment d'écrire à qui exploite ton instance.
