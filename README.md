# TP Git

Le but de ce TP est d'utiliser Git pour collaborer à plusieurs avec différents scripts


# Contexte

1er Script : Il permet d'afficher la liste des nombres premiers entre 1 et 1 000 000 
2ème Script : Il permet de cloner le repository suivant : https://github.com/KeligMartin/4-SRC.git
3ème Script : Il permet de retourner grâce à une fonction l'aire d'un disque en connaissant le rayon du disque 


## Prérequis

- Avoir Python3 (apt install python3)

## Memo Script 1
Aucune blibliothèque nécessaire à télécharger.
Il retournera l'ensemble des nombres premiers lors de son execution.


## Memo Script 2
Aucune blibliothèque nécessaire à télécharger.
Le script 2 créera un dossier "clone" dans le répertoire courant.
Ensuite, il clonera le repository https://github.com/KeligMartin/4-SRC.git dans ce dossier.

# Memo Script 3
Aucune blibliothèque nécessaire à télécharger.
Le script 3 demandera le rayon du disque. Celui-ci retournera l'aire du disque.

## WorkFlow

Nous avons choisi le workflow : Feature branch + merge request , pour les raisons suivantes :

	- Nous pouvons valider chaque étape depuis github afin de vérifier les commit des membres du groupe 
	- La feature branch permet de créer diverses branches pour chaque étape du projet notamment avec une branche hotfix
	- La branche basic flow n'était pas adapté car nous sommes 3 personnes sur ce projet
	- Un visuel ergonomique pour tous les membres du groupe sur github
	- Ceci va améliorer la sécurité générale du projet
