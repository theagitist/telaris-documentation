# Contrôle d'accès de l'édition

Avoir un compte d'édition est une chose ; pouvoir éditer une galaxie donnée en est une autre. Telaris sépare les deux, pour que tu puisses décider non seulement *qui* édite, mais *ce que* chaque compte d'édition peut toucher. Ce chapitre couvre les deux mécanismes : l'interrupteur de modification qui peut être désactivé à plusieurs niveaux, et l'accès par siège qui limite un compte d'édition à des galaxies précises.

## L'interrupteur de modification (une cascade)

La modification peut être activée ou désactivée à quatre niveaux, du plus large au plus étroit :

- l'**instance entière**,
- un **amas** de galaxies,
- une seule **galaxie**,
- un seul **compte**.

L'interrupteur cascade : désactiver la modification à un niveau plus large la désactive pour tout ce qui est à l'intérieur, à moins qu'un niveau plus étroit ne la réactive. Désactiver la modification pour l'instance arrête toute l'édition ; la désactiver pour un amas arrête la modification dans les galaxies de cet amas ; et ainsi de suite. La modification est **activée par défaut** à chaque niveau, donc une instance neuve se comporte comme tu t'y attends et tu ne touches ces interrupteurs que lorsque tu veux arrêter quelque chose.

**L'administration est exemptée.** La cascade ne verrouille jamais l'administration hors de la modification ; elle gouverne l'édition. C'est délibéré, pour que tu ne puisses pas désactiver par accident ta propre capacité à réparer les choses.

### Quand l'utiliser

- **Un cours ou un projet s'est terminé.** Désactive la modification pour l'instance (ou pour cet amas) pour figer le contenu tout en gardant chaque compte et tout ce qu'ils ont fait. C'est exactement ce que fait une instance de démonstration une fois son cours terminé : les comptes et le contenu restent, mais rien de nouveau ne peut être édité.
- **Une galaxie est en révision ou en cours de transfert.** Désactive la modification pour cette seule galaxie pendant qu'elle se stabilise, sans affecter le reste de l'instance.
- **Un compte d'édition devrait faire une pause.** Désactive la modification pour un seul compte sans toucher à personne d'autre.

L'interrupteur **Autoriser la modification** dans *Paramètres globaux* est le bout au niveau de l'instance de cette cascade ; les niveaux amas, galaxie et compte s'atteignent là où ces choses se gèrent.

## Accès par siège : lecture seule et lecture et écriture

La modification étant *activée* ne veut toujours pas dire qu'un compte d'édition peut éditer *tout*. L'édition travaille sur les galaxies où elle a un **siège**, et chaque siège est soit :

- **lecture et écriture**, le compte d'édition peut changer le contenu de la galaxie, soit
- **lecture seule**, le compte d'édition peut voir la galaxie dans sa vue d'édition mais ne peut pas la changer.

Un compte d'édition a toujours lecture et écriture sur les galaxies qu'il a créées. Les sièges sur d'autres galaxies s'accordent : toi (ou les valeurs par défaut de l'inscription autonome) donnes à un compte d'édition un siège sur une galaxie, au niveau que tu choisis. Un siège en lecture seule est la façon de laisser quelqu'un étudier ou consulter une galaxie, ou l'utiliser comme modèle, sans pouvoir la modifier. La lecture seule est aussi la façon dont le contenu importé se comporte pour tout le monde : le contenu en miroir depuis une autre instance est en lecture seule pour ton édition, parce que l'autorité qui le régit vit à sa source (voir *Galaxies et amas*).

Les deux mécanismes se combinent. Un compte d'édition ne peut changer une galaxie que lorsque la modification est activée pour lui tout le long de la cascade **et** qu'il détient un siège en lecture et écriture sur cette galaxie. S'il manque l'un ou l'autre, la galaxie s'ouvre pour lui en état de visualisation plutôt que d'édition.

## Choses qu'il vaut la peine de savoir

- **Désactivé par défaut n'est rien ; les interrupteurs sont un retrait.** Tu n'as jamais à activer la modification. Tu la désactives quand tu veux arrêter quelque chose, et la réactives quand tu as fini.
- **Figer n'est pas supprimer.** Désactiver la modification garde chaque compte et tout ce qui a été rédigé ; cela empêche seulement de nouveaux changements. C'est la façon sûre de terminer un projet sans le jeter.
- **La lecture seule est un choix de premier ordre, pas un moindre.** Une grande partie de la valeur d'une archive partagée est de pouvoir montrer une galaxie à des collaborations qui ne devraient pas la changer. Accorde des sièges en lecture seule librement.
