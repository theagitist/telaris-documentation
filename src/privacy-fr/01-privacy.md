# Confidentialité

Telaris est une archive de connaissance décoloniale de niveau recherche. Cet avis s'applique à **www.telaris.ca** (le site que tu lis en ce moment) et au **logiciel Telaris** qui fonctionne sur des instances tenues de manière indépendante. Chaque instance est tenue par une personne indépendante et peut porter ses propres avis de confidentialité supplémentaires qui gouvernent le contenu de cette instance ; cet avis couvre le reste.

## Ce que www.telaris.ca collecte

Le site `www.telaris.ca` est un petit ensemble de pages d'information statiques. Il n'exécute aucun outil d'analyse, ne place aucun traceur publicitaire, n'installe aucun témoin (cookie) et ne collecte aucune information personnelle auprès de qui le visite. Le site est servi via Cloudflare ; les journaux d'accès standards de Cloudflare (adresse IP tronquée, agent utilisateur, URL demandée, statut de la réponse, horodatage) sont conservés pour une courte durée par Cloudflare selon sa propre politique. Au-delà de ces journaux de bordure, le site n'enregistre pas les visites.

Le site renvoie à des documents téléchargeables et à des instances indépendantes de Telaris. Suivre un de ces liens te mène vers un autre site ; cet avis ne gouverne pas ce qui s'y passe.

## Ce qu'une instance de Telaris collecte

Tout site qui exécute le logiciel Telaris peut collecter une petite quantité d'information nécessaire au fonctionnement du logiciel :

- **Comptes d'édition.** Chaque instance tient une liste des personnes autorisées à ajouter du contenu. Pour chaque personne qui édite, elle conserve un nom, une adresse e-mail, une empreinte (hash) du mot de passe, des pronoms facultatifs et des horodatages de connexion, tant que le compte est actif. Voir *Tes informations et ce que tu peux demander en tant que personne qui édite* plus bas.
- **Contenu éditorial.** Les trous de ver, les galaxies, les mots-clés, les descriptions, les fichiers téléversés et les relations entre eux sont conservés par chaque instance. C'est le contenu que voit qui visite. La souveraineté éditoriale est le principe : qui édite décide de ce qui est publié, et rien n'est examiné avant d'être montré.
- **Consentement de la communauté d'origine.** Quand une communauté d'origine contribue du matériel, le consentement de cette communauté gouverne le matériel. Le retrait du consentement est définitif et l'instance le respecte sans négociation.
- **Journaux d'accès du serveur.** Une instance peut conserver des journaux d'accès de courte durée à des fins opérationnelles, comme le débogage et la lutte contre les abus. Quand le logiciel enregistre une adresse IP (par exemple dans son journal d'audit des actions), c'est à qui opère de décider combien de temps la conserver ; le logiciel applique une empreinte aux IP avec une clé du serveur quand il le peut, et ne conserve pas d'IP en clair dans ses propres tables.

## Tes informations et ce que tu peux demander en tant que personne qui édite

Si qui opère te donne un compte d'édition, ce qui suit s'applique à toi.

- **Pourquoi nous gardons tes données : parce que tu as accepté.** La première fois que tu te connectes en tant que personne qui édite, on te demande de vérifier ces documents et de les accepter avant de pouvoir utiliser l'éditeur. Ton acceptation est enregistrée avec la version de chaque document, de sorte qu'une révision ultérieure te la redemande. Tu peux retirer ton consentement à tout moment.
- **Ce qui est conservé à ton sujet :** ton nom, ton adresse e-mail, l'empreinte de ton mot de passe, les pronoms que tu indiques, des horodatages de connexion, le contenu éditorial que tu publies et un journal d'audit des actions administratives que tu réalises (dans lequel ton e-mail n'est conservé que sous forme d'empreinte salée, jamais en clair).
- **Ce que tu peux demander :** tu peux demander à qui opère ton instance de te montrer les données détenues à ton sujet, de les corriger ou de supprimer ton compte et ton contenu. Tu peux retirer ton consentement, ce qui retire ton accès et, si tu le demandes, ton contenu. Qui opère ton instance traite ces demandes ; elles ne se négocient pas, et la suppression est définitive.
- **Conservation :** les données du compte sont conservées tant que le compte est actif et retirées sur demande. Le journal d'audit des actions est conservé pour une durée limitée fixée par qui opère (la valeur par défaut est de 365 jours) à des fins de reddition de comptes, puis purgé.

## Journaux et conservation entre instances

Le logiciel Telaris ne fait aucune promesse générale sur la conservation des journaux, parce que la rotation des journaux vit dans l'infrastructure propre de chaque personne qui opère (son serveur web, son système d'exploitation, son fournisseur de bordure). Ce qui est constant partout, c'est ceci : l'**application** n'enregistre aucune activité de navigation de qui visite. La seule donnée personnelle de visite qui existe est l'adresse IP présente dans les journaux propres du serveur ou de la bordure de qui opère, régie par la conservation que cette personne définit.

Les instances tenues par Polivoxia font tourner leurs journaux de serveur à 14 jours ; c'est une valeur recommandée, pas une promesse qui lie les autres personnes qui opèrent. Chacune fixe sa propre conservation et en est responsable, et nous recommandons une conservation courte ou l'anonymisation des IP comme la posture la plus cohérente avec les valeurs de ce projet.

## Ce que Telaris ne fait pas

- **Pas de publicité.** Pas de traceurs tiers, pas de réseau publicitaire, pas de profilage comportemental.
- **Pas d'entraînement ni d'analyse d'IA sur le corpus.** Le contenu de Telaris n'est pas utilisé pour entraîner ni alimenter des modèles d'IA, en interne comme en externe.
- **Pas d'analyse de contenu par des tiers.** Le contenu n'est pas envoyé à des services externes pour modération ou classification.
- **Pas de vente de données.** Les comptes d'édition, le contenu et les journaux ne sont jamais vendus ni partagés avec des tiers à des fins publicitaires ou commerciales.

## Fédération et contenu entre instances

Quand les instances de Telaris se fédèrent, le contenu qu'une personne qui édite publie explicitement vers une instance partenaire voyage vers cette instance sous des signatures cryptographiques. L'instance réceptrice héberge une copie ; l'instance d'origine garde la souveraineté et peut rétracter le contenu, ce qui retire la copie.

Les comptes d'édition et les adresses e-mail de qui opère **ne** franchissent **pas** les frontières de la fédération. La communication entre personnes qui opèrent passe par un relais qui masque les adresses e-mail des deux côtés.

## Retrait du consentement

Une communauté d'origine, une personne qui édite ou toute personne dont le matériel est hébergé sur une instance de Telaris peut retirer son consentement à tout moment. Qui opère cette instance est responsable de le respecter. Le retrait retire le matériel ; il ne demande pas de négociation ; il est définitif.

## Contact

Pour des questions sur une instance précise, contacte qui l'opère, dont l'adresse figure sur le site de l'instance elle-même. Pour des questions sur www.telaris.ca, sur le logiciel lui-même ou sur cet avis, utilise la page [Contact](https://www.telaris.ca/contact) ; la gouvernance du projet et la personne qui opère et qu'on peut contacter au sujet du traitement des données sont décrites sur la page [Gouvernance](https://www.telaris.ca/governance).

## Version

Version 1.0, en vigueur depuis le 2026-06-04. C'est la première version publiée ; elle remplace le brouillon précédent. Quand cet avis change d'une manière qui touche qui édite, la version est incrémentée et on demande de vérifier la nouvelle version à la prochaine connexion.
