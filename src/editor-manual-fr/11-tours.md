# Visites

Une visite est un chemin curaté à travers une galaxie. L'édition choisit le départ, choisit l'ordre, fixe une durée de pause à chaque arrêt, et décide si la visite revient en boucle ou s'arrête. Qui visite peut lancer la visite en appuyant sur Lecture ; ou la visite peut se lancer toute seule quand qui visite est inactive ; ou la visite peut commencer à l'instant où qui visite arrive sur la galaxie. Ce chapitre parcourt chaque chemin de création d'une visite et les considérations pratiques.

Une visite est **une configuration d'une galaxie**, pas un objet séparé. Activer la visite configure les trous de ver existants pour être parcourus dans un ordre choisi ; la désactiver laisse les trous de ver intouchés. Une galaxie peut porter une seule configuration de visite à la fois ; si tu veux deux visites, tu publies une copie de la galaxie avec la seconde visite.

## Où tu la rédiges

Une visite vit à l'intérieur de la fenêtre **Paramètres de galaxie**, dans la section Découverte (le chapitre 4 présente la fenêtre ; le chapitre 10 présente les bascules de découverte).

![Fenêtre de paramètres de galaxie, à la section Découverte](assets/images/editor-manual-fr/12-galaxy-discovery-section.png)

La première bascule de la section Découverte est **Visite automatique**. La passer en position activée révèle les champs de configuration de la visite :

- Mode de départ.
- Sélection de nœuds.
- Durée de pause à chaque arrêt.
- Boucle activée / désactivée.

En dessous se trouve un bouton **Aperçu de la visite**.

## Mode de départ

Choisis comment la visite commence :

- **Manuel** : un petit bouton **Lecture** apparaît dans le coin inférieur droit de la scène 3D de qui visite. La visite démarre quand qui visite l'appuie. À utiliser quand la visite est un chemin *offert*, pas un chemin par défaut.
- **Inactivité** : la visite démarre automatiquement après que qui visite est restée inactive un nombre de secondes configurable. Le champ de seuil d'inactivité apparaît sous cette option. À utiliser quand la galaxie est censée être abordée à la fois de manière interactive (qui visite explore) et de manière ambiante (la galerie s'éveille quand personne n'y touche).
- **Immédiat** : la visite démarre à l'instant où qui visite arrive sur la galaxie. Qui visite peut arrêter la visite à tout moment avec les commandes en scène. À utiliser pour les galeries dont l'expérience voulue est la visite elle-même ; le chemin de l'édition est la lecture canonique.

Il n'y a pas de bonne réponse ; chaque option correspond à une intention éditoriale différente. La plupart des galaxies rédigées commencent par **Manuel** et passent à **Inactivité** ou **Immédiat** quand l'édition trouve un chemin digne d'être le défaut.

## Sélection de nœuds

Choisis quels trous de ver la visite parcourt, et dans quel ordre :

- **Tous** : chaque trou de ver de la galaxie, dans l'ordre où ils ont été créés. La sélection la plus simple ; utile pour les galaxies courtes où chaque trou de ver porte un poids égal.
- **Mis en avant uniquement** : seulement les trous de ver marqués Mettre en avant. À utiliser quand tu veux que certains trous de ver soient sur la visite et d'autres restent accessibles mais pas mis en avant. Le drapeau Mettre en avant se règle par trou de ver (chapitre 5).
- **N aléatoires** : choisit N trous de ver au hasard à chaque session. Un champ apparaît pour N. À utiliser pour les galeries qui doivent sembler fraîches à chaque retour ; qui visite voit une tranche différente à chaque fois.
- **Mots-clés étiquetés** : ne parcourt que les trous de ver porteurs d'un mot-clé d'un ensemble choisi. Un sélecteur de mots-clés apparaît, semblable à la saisie d'étiquettes de mots-clés sur une fenêtre de trou de ver. À utiliser quand tu veux une visite *thématique* (seulement les trous de ver étiquetés *médicinale* ; seulement ceux étiquetés *indigène*).

Pour les visites par mots-clés étiquetés, l'ordre dans lequel les trous de ver sont parcourus est l'ordre dans lequel ils ont été créés, filtré sur l'ensemble de mots-clés. Il n'y a pas de champ d'ordre manuel ; s'il te faut une séquence strictement rédigée, l'ordre de création des trous de ver est celui que la visite respectera.

## Durée de pause

Un seul nombre, en secondes, qui contrôle combien de temps la visite s'arrête à chaque trou de ver avant d'avancer. La pause démarre quand la fiche d'information du trou de ver s'ouvre ; le trou de ver suivant est sélectionné quand la pause s'écoule.

Un défaut utile est cinq à huit secondes ; c'est assez long pour que qui visite lise une description courte et regarde l'image, assez court pour garder de l'élan sur une longue visite. Les trous de ver avec audio attaché méritent souvent une pause plus longue pour que l'audio se résolve avant que la visite n'avance ; le chapitre 6 couvre la sémantique de boucle audio.

La pause est globale à la visite ; l'édition ne peut pas (encore) régler une pause différente par trou de ver.

## Boucle

Une seule bascule :

- **Activée** : après le dernier trou de ver, la visite revient au premier et continue. À utiliser pour les installations de galerie ambiantes où qui visite peut entrer en plein cycle.
- **Désactivée** : la visite s'arrête tranquillement après le dernier trou de ver ; la scène revient en mode interactif et qui visite peut explorer librement. À utiliser pour les visites narratives avec un début et une fin.

## Prévisualiser une visite

Sous les champs de configuration de visite, un bouton **Aperçu de la visite** apparaît. Le sélectionner ouvre la vue de visite dans un nouvel onglet avec la visite en cours, indépendamment de l'enregistrement de la configuration. C'est la bonne manière de vérifier le minutage, l'ordre et la pause avant de publier les changements pour qui visite.

L'aperçu reflète ce que tu as saisi dans la fenêtre, pas ce qui est actuellement enregistré. Si tu décides que l'aperçu n'est pas bon, change les champs et sélectionne Aperçu à nouveau ; le nouvel onglet se met à jour.

## Visites et Mettre en avant

Le drapeau Mettre en avant sur un trou de ver (chapitre 5) chevauche la sélection de visite mais n'est pas la même chose. Les trous de ver mis en avant sont *visuellement plus grands* dans la scène 3D indépendamment du fait qu'une visite les parcourt ou non. L'option de sélection de nœuds **Mis en avant uniquement** pour la visite est une façon d'utiliser le drapeau, mais tu peux aussi Mettre en avant des trous de ver qui ne sont pas dans la visite, et avoir une visite qui inclut des trous de ver qui ne sont pas mis en avant.

Le modèle le plus lisible :

- Utilise Mettre en avant pour les trous de ver qui doivent ressortir visuellement en tout temps.
- Utilise la visite pour spécifier le *chemin narratif*, qui peut ou non recouvrir l'emphase visuelle.

## Visites et toile de mots-clés

Une visite étiquetée par mot-clé (sélection de nœuds réglée sur *mots-clés étiquetés*) offre à l'édition un chemin à travers la galaxie qui suit le vocabulaire de mots-clés que la toile rédige. Les deux surfaces travaillent ensemble : choisis d'abord sur la toile les mots-clés que la visite suivra, trace les relations entre eux, puis choisis la visite pour suivre ce chemin thématique côté visite.

La connexion est éditoriale plutôt que structurelle ; Telaris ne demande pas que la toile soit peuplée avant la configuration d'une visite, mais la visite qui en résulte semble souvent plus délibérée quand le vocabulaire de mots-clés a été travaillé.

## Choses qu'il vaut la peine de savoir

- **La visite automatique ne fait pas pause pour l'audio.** Si un trou de ver a une piste audio de 30 secondes et que la pause est de 8 secondes, la visite avance à 8 secondes pendant que l'audio continue en arrière-plan. Pour laisser l'audio se terminer, allonge la pause.
- **Qui visite peut toujours arrêter la visite.** Une commande Arrêter ou Pause apparaît pendant une visite en cours ; qui visite peut aussi cliquer n'importe où en dehors de la fiche d'information pour interrompre. Les visites doivent sembler offertes, pas imposées.
- **Les visites en N aléatoires changent à chaque session.** Qui revient à la page ne voit pas les mêmes N trous de ver ; la sélection aléatoire est relancée. Utile pour la sensation ambiante ; surprenant si tu attendais une séquence stable.
- **Les visites par mots-clés étiquetés suivent l'union des mots-clés choisis.** Une visite réglée sur les mots-clés *indigène* et *comestible* parcourt chaque trou de ver étiqueté avec **soit** *indigène* **soit** *comestible* (ou les deux) ; elle n'exige pas les deux.
- **Les visites sont limitées à la galaxie courante.** Une visite ne peut pas parcourir des trous de ver dans une autre galaxie ; pour des chemins entre galaxies, utilise les portails (chapitre 9).
- **La vue 2D (chapitre 10) interagit avec les visites avec grâce.** Qui visite en mode 2D voit la visite comme une séquence d'étiquettes mises en valeur, pas comme un mouvement de caméra. La pause s'applique encore ; le visuel est juste plus plat.
