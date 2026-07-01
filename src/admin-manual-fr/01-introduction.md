# Introduction

Ce manuel s'adresse à la personne qui exploite une instance de Telaris : l'administration. L'administration n'est pas la même chose que l'édition. L'édition rédige des galaxies, des trous de ver et des connexions à l'intérieur de l'archive ; l'administration décide qui peut éditer, comment l'instance se comporte, si et comment elle se connecte à d'autres instances, et comment ses données sont protégées. Si ton travail quotidien est de rédiger du contenu, le Manuel d'édition est ton livre ; celui-ci est pour les surfaces que l'édition ne voit jamais.

## Trois rôles

Il est utile de garder trois rôles distincts, parce que ce manuel, le Manuel d'édition, et le quotidien de la conduite d'un réseau Telaris s'adressent chacun à un rôle différent.

- **Édition.** Quelqu'un qui a un compte d'édition sur ton instance. Cette personne se connecte, rédige du contenu, et ne voit que la surface d'édition. Le Manuel d'édition est écrit pour elle.
- **Administration (toi).** Quelqu'un qui a un compte d'administration sur ton instance. Tu atteins la **Console d'administration** et tu gères les comptes, les galaxies, les paramètres, les sauvegardes, et la participation de ton instance au réseau plus large. Ce manuel est écrit pour toi.
- **Qui exploite le Pluriverse.** La personne qui tient le site de coordination central (le Pluriverse) à travers lequel une famille d'instances se fédère. Une grande partie de ce travail passe par la même console d'administration que tu connais déjà ; les parties propres à la conduite du Pluriverse sont rassemblées dans le chapitre sur la fédération. Sur un petit réseau, l'administration et qui exploite le Pluriverse sont souvent la même personne.

Un même compte peut, bien sûr, être à la fois d'édition et d'administration. La distinction porte sur les *surfaces*, pas sur les personnes : la console d'administration est un endroit séparé de la page d'édition, atteint séparément, et ce manuel est ton guide vers elle.

## Atteindre la Console d'administration

La Console d'administration vit au chemin `/admin` de ton instance (par exemple, `https://ton-instance.exemple.org/admin`). Tu dois être connectée avec un compte qui a le rôle d'administration ; un compte d'édition ordinaire qui ouvre `/admin` est renvoyé.

En haut de la console se trouve une rangée d'onglets. Chacun est un chapitre de ce manuel :

- **Galaxies** et **Amas** : la vue de l'administration sur tout le contenu de l'instance, y compris le contenu importé d'ailleurs. Couverts dans *Galaxies et amas*.
- **Comptes** : chaque compte de l'instance, et les outils pour les créer, les modifier, les vérifier et les retirer. Couvert dans *Comptes* et *Inscription autonome des comptes d'édition*.
- **Sauvegarde** et **Instantanés** : faire et restaurer des copies de toute l'instance. Couverts dans *Sauvegardes et instantanés*.
- **Paramètres globaux** : le courriel, l'adresse propre de l'instance, la langue par défaut, et l'interrupteur à l'échelle de l'instance pour l'édition. Couverts dans *Paramètres globaux*.
- **Pluriverse** : la participation de ton instance à une fédération d'instances. Couvert dans *Fédération et le Pluriverse*.
- **Clés d'API** et **Informations PHP** : broutilles opérationnelles et diagnostics. Couverts dans *Maintenance et diagnostics*.

## Ce que ce manuel suppose

Il suppose que l'instance est déjà installée et en marche, et que tu peux te connecter en tant qu'administration. Il ne couvre pas l'installation de Telaris sur un serveur à partir de rien ; c'est une affaire de la méthode de déploiement que tu as choisie (un dépôt direct, une image de conteneur, ou une instance hébergée provisionnée pour toi), et le README du dépôt de code en est la référence. Ce que ce manuel couvre, c'est tout ce que tu fais *après* que l'instance est en marche : la conduire bien, la garder en sûreté, et décider à quel point elle est ouverte.

## Une note sur la langue et les termes

La console, comme le reste de Telaris, est entièrement traduite. Les écrans montrés ici sont en anglais ; ta console peut être en espagnol, en portugais ou en français, et les étiquettes diffèrent en conséquence. Quand ce manuel nomme un contrôle, il nomme l'étiquette française ; retrouve le même contrôle dans ta propre langue par sa position, qui est la même dans chaque langue.

Telaris garde aussi une séparation délibérée entre les mots que lisent qui visite et qui édite et les mots qu'utilise le code. Tu verras *galaxie*, *trou de ver* et *portail* dans l'interface ; les données sous-jacentes les appellent *constellation*, *nœud* et *portail*. Ce manuel utilise les mots de l'interface partout. Le glossaire à la fin rassemble les termes que l'administration rencontre.
