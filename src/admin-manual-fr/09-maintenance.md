# Maintenance et diagnostics

Ce chapitre rassemble les broutilles opérationnelles : les onglets **Clés d'API** et **Informations PHP**, la façon dont l'instance garde à jour sa propre structure de base de données, et l'endroit où vivent les quelques réglages au niveau des fichiers. Tu visiteras ceux-ci rarement, ce qui est précisément pourquoi il est utile de savoir ce qu'ils sont avant d'en avoir besoin.

## Clés d'API

La façade propre de l'instance lit le contenu à travers une API interne, et cette API est protégée par une clé. L'onglet **Clés d'API** est l'endroit où ces clés se gèrent : tu peux voir les clés qui existent et en générer une nouvelle.

Pour une instance mise en place normalement, une clé par défaut existe déjà et tout fonctionne ; tu n'as jamais besoin de cet onglet. Il compte dans deux situations :

- **Une instance provisionnée à la main sans clé.** Si une instance a été mise en place à la main plutôt que par la configuration normale, elle peut n'avoir aucune clé par défaut, et la scène pour qui visite ou les vues d'administration échouent à charger le contenu (une erreur « échec du chargement »). Générer une clé ici corrige cela.
- **Faire tourner une clé.** Si une clé doit être remplacée, génères-en une nouvelle ici.

À moins de dépanner l'une de ces situations, laisse cet onglet tranquille.

## Informations PHP

L'onglet **Informations PHP** rapporte l'environnement serveur sur lequel l'instance tourne : la version de PHP, quelles extensions importantes sont présentes, et la liste complète des extensions chargées. C'est un diagnostic en lecture seule. Son but est de répondre, rapidement, « ce serveur a-t-il ce dont Telaris a besoin ? » quand quelque chose se comporte étrangement, sans que tu te connectes au serveur lui-même. Si tu signales un jour un problème à qui gère le serveur, la version et les informations d'extensions ici sont ce qu'on te demandera.

## Comment la structure de la base de données reste à jour

Telaris gère sa propre structure de base de données. Quand l'instance exécute une version du code plus récente que celle pour laquelle la base de données a été préparée en dernier, elle met la structure à jour toute seule, en ajoutant ce dont la nouvelle version a besoin, la première fois que c'est nécessaire. Il n'y a pas d'étape séparée « lancer les migrations » que tu aies à accomplir après un déploiement ; l'instance s'en charge.

C'est pourquoi déployer une mise à jour n'est, dans le cas normal, que mettre le nouveau code en place ; l'instance fait le reste à la prochaine requête. La **bannière d'incohérence de schéma** (voir *Sauvegardes et instantanés*) est l'exception, le signal que cette mise à jour automatique ne s'est pas achevée, et le reste de ce chapitre couvre ce qu'elle signifie.

## Les quelques réglages au niveau des fichiers

Presque tout ce que l'administration règle vit dans la console et la base de données, ce qui est là où tu devrais le régler. Un petit nombre de valeurs fondatrices, principalement la connexion à la base de données qu'utilise l'instance, vivent dans un fichier de configuration sur le serveur plutôt que dans la console, parce que l'instance en a besoin avant de pouvoir atteindre sa propre base de données pour lire quoi que ce soit d'autre. Tu ne toucheras normalement pas à ce fichier ; il est fixé une fois quand l'instance est installée. Les réglages que tu *changes* au quotidien, le courriel, l'adresse de l'instance, la langue par défaut, l'interrupteur d'édition, sont tous dans *Paramètres globaux*, dans la console, précisément pour que tu n'aies pas à modifier des fichiers pour conduire l'instance.

Si tu n'as pas installé l'instance toi-même et que quelque chose à ce niveau semble anormal (l'instance ne peut pas atteindre sa base de données, ou les liens de courriel pointent vers la mauvaise adresse), c'est le moment d'impliquer qui a mis le serveur en place, ou de consulter la référence d'installation propre au dépôt de code.

## Choses qu'il vaut la peine de savoir

- **La plupart de ces onglets sont « en cas de », pas « au quotidien ».** Clés d'API et Informations PHP sont des surfaces de dépannage ; une instance en bonne santé a rarement besoin de l'une ou de l'autre.
- **Déployer, c'est mettre le nouveau code en place ; l'instance met sa propre structure à jour.** Tu ne lances pas les migrations à la main.
- **La console est l'endroit pour les réglages, pas les fichiers.** Si tu te surprends à vouloir modifier un fichier pour changer le comportement de l'instance, vérifie d'abord *Paramètres globaux* ; le réglage y est probablement.
