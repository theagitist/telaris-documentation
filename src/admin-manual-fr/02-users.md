# Comptes

L'onglet **Comptes** est l'endroit où vit chaque compte de l'instance. Ce chapitre couvre les comptes que tu crées toi-même ; le chapitre suivant couvre les comptes que les gens créent pour eux-mêmes par l'inscription autonome, qui partage la même liste.

![L'onglet Comptes : un tableau de comptes avec le nom, le courriel, le rôle, et des actions par ligne](assets/images/admin-manual-fr/02-users-list.png)

## La liste des comptes

La liste montre chaque compte : administration et édition ensemble. Pour chaque compte, tu vois son nom, son adresse de courriel, son rôle, et, le cas échéant, s'il a été vérifié (le chapitre suivant explique la vérification). Un décompte dans le titre t'indique combien de comptes existent.

Chaque compte a un menu d'actions par ligne pour le modifier et le retirer, décrit ci-dessous.

## Rôles

Telaris a deux rôles :

- **Édition.** Peut se connecter et rédiger du contenu, dans les limites de l'accès qui lui a été accordé (voir *Contrôle d'accès de l'édition*). Ne peut pas atteindre la console d'administration.
- **Administration.** Peut faire tout ce que l'édition peut faire, et peut atteindre la console d'administration. Attribue ce rôle avec parcimonie ; chaque compte d'administration peut changer les paramètres, lire chaque compte, et retirer du contenu.

Le rôle d'un compte est fixé à sa création et peut être changé en modifiant le compte.

## Créer un compte

Sélectionne **Créer un nouveau compte**. Un formulaire demande le nom du nouveau compte, son adresse de courriel, son rôle, et, facultativement, un mot de passe.

- **Nom** est la façon dont la personne est affichée, et ce d'après quoi les galaxies propres à un compte d'édition sont nommées si tu utilises les conventions de nommage du chapitre suivant.
- **Courriel** est l'identité du compte et l'adresse à laquelle Telaris écrit (liens de connexion, notifications). Elle doit être unique sur l'instance.
- **Rôle** est édition ou administration, comme ci-dessus.
- **Mot de passe** est facultatif. Si tu en fixes un, la personne peut se connecter avec. Si tu le laisses vide, le compte se connecte par le lien de courriel sans mot de passe décrit ci-dessous. Beaucoup de comptes d'administration le laissent vide et laissent les gens utiliser des liens de courriel, pour qu'il n'y ait aucun mot de passe à gérer ou à fuir.

Enregistre, et le compte apparaît aussitôt dans la liste.

## Connexion sans mot de passe

Les comptes Telaris n'ont pas besoin de mot de passe. Un compte sans mot de passe se connecte en demandant un lien de courriel : la personne saisit son courriel sur la page de connexion, Telaris lui envoie un lien à usage unique, et le suivre la connecte. C'est le même mécanisme qu'utilise un compte d'édition auto-inscrit.

Pour que cela fonctionne, l'instance doit pouvoir envoyer du courriel. Si le courriel n'est pas configuré, les liens de courriel ne peuvent pas être livrés et les comptes sans mot de passe ne peuvent pas se connecter. Le chapitre *Paramètres globaux* couvre la configuration du courriel et l'avertissement que la console montre quand ce n'est pas en place.

## Modifier un compte

Ouvre le menu d'actions d'une ligne et choisis **Modifier** pour changer le nom, le courriel, le rôle, le mot de passe ou l'état de vérification d'un compte. Les changements s'enregistrent en une seule opération ; si tu changes plusieurs champs à la fois, ils prennent tous effet ensemble.

Changer le courriel d'un compte change l'adresse à laquelle Telaris écrit et l'identité avec laquelle la personne se connecte. Changer le rôle d'édition à administration accorde l'accès à la console immédiatement ; le changer dans l'autre sens le retire.

## Importation en lot

Quand tu as besoin de créer beaucoup de comptes à la fois (une classe, une cohorte, un groupe de travail), utilise l'**importation en lot**. Elle prend une liste de comptes, typiquement sous forme de CSV avec une colonne par champ (nom, courriel, rôle), et les crée en une seule passe. Les comptes dont le courriel existe déjà sont signalés plutôt que dupliqués, donc relancer une importation est sans danger.

L'importation en lot est le bon outil pour intégrer un groupe connu. Pour un groupe que tu ne connais pas d'avance (un appel ouvert à contributions), l'inscription autonome, au chapitre suivant, convient mieux.

## Retirer un compte

Choisis **Supprimer** dans le menu d'actions d'une ligne. Telaris confirme d'abord, parce que retirer un compte est permanent.

Si le compte possède une **galaxie personnelle** (une galaxie créée pour ce compte d'édition, selon les conventions de nommage du chapitre suivant), Telaris demande quoi en faire : retirer la galaxie avec le compte, ou garder la galaxie et son contenu en place. Supprimer le compte ne supprime jamais silencieusement du contenu ; on te demande toujours. Garde la galaxie quand le contenu doit survivre à l'accès de la personne ; retire-la quand le compte et sa galaxie n'étaient qu'un ensemble jetable (un compte de test, une démonstration de cours).

## Choses qu'il vaut la peine de savoir

- **Il n'y a aucun moyen de voir un mot de passe.** Les mots de passe sont stockés de sorte que même toi ne peux pas les relire. Si quelqu'un oublie le sien, soit efface-le (pour qu'il utilise des liens de courriel), soit fixe-en un nouveau ; tu ne peux pas récupérer l'ancien.
- **L'administration peut voir chaque compte et chaque galaxie.** La confidentialité qui limite l'édition à son propre travail ne s'applique pas à toi. Traite la liste, et le contenu derrière elle, avec la discrétion qu'implique cet accès.
- **Supprimer le dernier compte d'administration te verrouillerait dehors.** Telaris ne laissera pas l'instance sans administration ; garde au moins un compte d'administration auquel tu peux te connecter avant d'en retirer d'autres.
