# Inscription autonome des comptes d'édition

Au-delà de la création de comptes à la main, une instance peut laisser les gens **s'inscrire eux-mêmes** pour obtenir un compte d'édition. C'est désactivé par défaut. Quand tu l'actives, qui visite peut demander un compte d'édition via un formulaire, confirmer son courriel, et commencer à éditer, sans que tu crées le compte d'abord. Ce chapitre couvre quand l'utiliser et chaque interrupteur qui la gouverne.

L'inscription autonome se configure depuis la console d'administration (les réglages d'auto-inscription ; sur la plupart des instances, ils se trouvent avec les autres contrôles de comptes). Toute la fonctionnalité est une seule décision avec plusieurs cadrans : *des inconnus devraient-ils pouvoir obtenir un compte d'édition ici, et sous quelles limites ?*

## Quand l'utiliser

Active-la pour un appel ouvert : une archive communautaire qui invite des contributions, un cours où les personnes étudiantes s'inscrivent elles-mêmes, un projet public qui veut une faible barrière pour aider. Laisse-la désactivée pour une instance fermée où chaque compte d'édition devrait être quelqu'un que tu as ajouté délibérément. Tu peux l'activer un temps (la durée d'un cours, la période d'un appel) et la désactiver ensuite ; les comptes existants ne sont pas affectés quand tu le fais.

## L'activer

Le contrôle d'auto-inscription a un interrupteur principal. Tant qu'il est désactivé, le formulaire d'inscription est fermé : qui l'atteint voit un avis indiquant que l'inscription n'est pas ouverte, et le lien d'inscription est masqué sur la page de connexion. Tant qu'il est activé, le formulaire est ouvert et le lien apparaît.

L'activer révèle les limites ci-dessous. Fixe-les avant d'annoncer l'appel, pas après.

## Les limites

- **Plafond.** Un nombre maximum de comptes d'édition auto-inscrits. Une fois le plafond atteint, le formulaire se ferme de lui-même et le lien d'inscription disparaît jusqu'à ce que tu relèves le plafond ou retires des comptes. Utilise-le pour empêcher un appel ouvert de t'échapper. Le plafond compte les comptes d'édition auto-inscrits, pas les comptes que tu as créés toi-même.
- **Liste de domaines de courriel autorisés.** Une liste facultative de domaines de courriel qui peuvent s'inscrire (par exemple, le domaine d'une université pour un cours). Quand elle est fixée, seules les adresses de ces domaines peuvent achever l'inscription ; tout le monde d'autre est renvoyé. Laisse-la vide pour autoriser n'importe quelle adresse.
- **Nommage de la galaxie personnelle.** Quand quelqu'un s'inscrit, Telaris peut créer une **galaxie personnelle** dans laquelle cette personne travaillera. Tu choisis comment elle est nommée : d'après le nom complet de la personne, ou d'après son prénom seulement. Le prénom seul est la valeur par défaut qui préserve la confidentialité, parce qu'un nom de galaxie est public ; un nom complet dans un titre de galaxie est visible pour qui visite. Choisis les noms complets seulement quand cette exposition est acceptable dans ton contexte.
- **Accès par défaut.** Les nouveaux comptes d'édition auto-inscrits peuvent recevoir des sièges sur des galaxies de démonstration, en lecture seule ou en lecture et écriture, pour qu'ils arrivent avec quelque chose à regarder ou sur quoi travailler. *Contrôle d'accès de l'édition* explique les sièges.

## Comment un compte d'édition auto-inscrit se connecte

Un compte d'édition auto-inscrit n'a **aucun mot de passe**. Il se connecte chaque fois par le lien de courriel : saisir l'adresse, recevoir un lien à usage unique, le suivre. C'est pourquoi le courriel doit être configuré pour que l'inscription fonctionne du tout ; si l'instance ne peut pas envoyer de courriel, personne ne peut confirmer une inscription ni se connecter ensuite. Le chapitre *Paramètres globaux* couvre le courriel.

Parce que l'inscription dépend entièrement du courriel, le déroulement est : la personne soumet le formulaire, Telaris lui écrit pour confirmer que l'adresse est bien la sienne, et ce n'est qu'après qu'elle suit cette confirmation qu'elle est un compte d'édition réel. Une inscription non confirmée n'est pas encore un compte et est nettoyée automatiquement si elle n'est jamais confirmée.

## Vérification

Un compte d'édition auto-inscrit peut éditer dès qu'il confirme son courriel ; tu n'as pas à l'approuver d'abord. La **vérification** est une étape séparée et facultative qui dit « je reconnais cette personne ». Quand tu vérifies un compte :

- la personne peut fixer un mot de passe, elle n'est donc plus limitée aux liens de courriel, et
- Telaris lui dit qu'elle a été vérifiée.

La vérification ne conditionne **pas** l'édition. Un compte d'édition auto-inscrit non vérifié est déjà un compte d'édition à part entière ; la vérification est une marque de reconnaissance et une commodité (le mot de passe), pas une permission. Les comptes non vérifiés sont mis en évidence dans la liste des comptes pour que tu voies au premier coup d'œil qui a rejoint mais n'a pas encore été reconnu.

## Garder cela en sûreté

- **Un plafond est ta soupape de sûreté.** Un formulaire ouvert sans plafond peut être inondé. Fixe un plafond que tu es à l'aise de modérer, et relève-le délibérément.
- **La liste autorisée cadre l'appel.** Pour un cours ou une organisation, une liste de domaines de courriel autorisés transforme « n'importe qui » en « n'importe qui d'ici », ce qui est habituellement ce que tu voulais vraiment dire.
- **Les prénoms par défaut.** À moins d'avoir une raison contraire, garde le nommage de la galaxie personnelle sur les prénoms, pour que le nom complet de personne ne devienne un titre de galaxie public sans son accord.
- **Désactive-la quand l'appel se termine.** Une inscription laissée ouverte indéfiniment est une invitation permanente que tu as peut-être oubliée. Ferme-la quand la raison de l'ouvrir est passée ; les comptes déjà faits restent.
