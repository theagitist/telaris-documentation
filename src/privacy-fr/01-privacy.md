# Confidentialité

> [!warning] Brouillon
> Ce document est provisoire. Une version finalisée de l'avis de confidentialité est en cours et remplacera ce brouillon. Pour toute question entre-temps, écris à la personne qui maintient l'instance que tu utilises.

Telaris est une archive de connaissance décoloniale de niveau recherche. La posture de confidentialité décrite ici s'applique à **www.telaris.ca** (le site que tu lis en ce moment) et au **logiciel Telaris** qui fonctionne sur des instances tenues de manière indépendante. Chaque instance est tenue par une personne indépendante et peut porter ses propres avis de confidentialité supplémentaires ; ces avis gouvernent le contenu de l'instance. Ce document couvre le reste.

## Ce que www.telaris.ca collecte

Le site `www.telaris.ca` est une simple page statique. Il n'exécute pas d'outil d'analyse, ne place pas de traceurs publicitaires, n'installe pas de témoins (cookies), et ne collecte aucune information personnelle auprès de qui visite. La page est servie via Cloudflare ; les journaux d'accès standards de Cloudflare (adresse IP tronquée, agent utilisateur, URL demandée, statut de la réponse, horodatage) sont conservés pour une courte durée par Cloudflare selon sa propre politique. Au-delà de ces journaux d'accès, le site n'enregistre pas les visites.

Le site renvoie à des documents PDF téléchargeables et à des instances indépendantes de Telaris. Suivre un de ces liens mène à une autre page ; cet avis ne gouverne pas ce qui s'y passe.

## Ce que les instances de Telaris peuvent collecter

Les instances individuelles (tout site qui exécute le logiciel Telaris, y compris les trois listées sous *Instances actives* sur la page d'accueil) peuvent collecter une petite quantité d'information nécessaire au fonctionnement du logiciel :

- **Comptes d'édition.** Chaque instance maintient une liste de personnes autorisées à ajouter du contenu. Le nom du compte d'édition, son courriel et un hachage de mot de passe sont stockés tant que le compte reste actif. Qui exploite l'instance peut supprimer des comptes d'édition sur demande.
- **Contenu éditorial.** Les trous de ver, les galaxies, les mots-clés, les descriptions, les médias téléversés, et les relations entre eux sont stockés par chaque instance. C'est le contenu que voit qui visite. La souveraineté éditoriale est le principe : qui édite décide ce qui se publie ; rien n'est révisé avant d'être montré.
- **Consentement de la communauté source.** Quand une communauté source contribue du matériel à une instance, le consentement de cette communauté gouverne le matériel. Le retrait du consentement est définitif et est exécuté par qui exploite l'instance sans négociation.
- **Journaux d'accès au niveau serveur.** Les instances peuvent conserver des journaux d'accès à courte rétention à des fins opérationnelles (débogage, atténuation des abus). Les adresses IP, lorsqu'elles sont stockées, sont hachées avec une clé côté serveur ; les IP en clair ne sont pas conservées.

## Ce que Telaris ne fait pas

- **Pas de publicité.** Pas de traceurs tiers, pas de réseau publicitaire, pas de profilage comportemental.
- **Pas d'entraînement d'IA sur le corpus.** Le contenu de Telaris n'est pas utilisé pour entraîner des modèles d'IA, ni à l'interne ni à l'externe.
- **Pas d'analyse de contenu par des tiers.** Le contenu n'est pas envoyé à des services externes pour modération ou classification.
- **Pas de vente de données.** Les comptes d'édition, le contenu et les journaux d'accès ne sont pas vendus ni partagés avec des tiers à des fins publicitaires ou commerciales.

## Fédération et contenu entre instances

Quand des instances de Telaris se fédèrent (une fonctionnalité prévue, pas encore active au moment de ce brouillon), le contenu qu'une personne qui édite publie explicitement vers un partenaire de fédération voyage vers l'instance de ce partenaire sous des signatures cryptographiques. L'instance réceptrice héberge un miroir du contenu ; l'instance d'origine conserve sa souveraineté.

Les comptes d'édition et les courriels d'exploitation **ne** traversent **pas** les frontières de la fédération. La communication entre instances passe par un relais qui masque les adresses de courriel des deux côtés.

## Retrait du consentement

Une communauté source, une personne qui édite, ou toute personne dont le matériel est hébergé sur une instance de Telaris peut retirer son consentement à tout moment. Qui exploite l'instance est responsable d'honorer le retrait. Le retrait supprime le matériel ; il n'exige aucune négociation ; il est définitif.

## Contact

Chaque instance de Telaris liste l'adresse de contact de qui l'exploite sur le site de l'instance elle-même. Utilise ce canal pour les questions de confidentialité propres à une instance. Pour les questions concernant www.telaris.ca, le logiciel lui-même, ou cet avis, contacte la personne qui maintient le projet, nommée sur la page **/governance** (à venir).

## Version

Brouillon, 2026-05-22. Ne remplace aucune version antérieure. À réviser avant toute publication publique.
