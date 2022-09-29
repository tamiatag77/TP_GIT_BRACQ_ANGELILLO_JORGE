'''
Script : calcul de l'aire d'un triangle by Alexis Bracq, Jonathan Jorge et Guilian angelillo
Version 1
Date : 29/29/2022


Fonction / Utilité du script

=> Définir une fonction qui attend la base d'un triangle et sa hauteur puis qui retourne son aire.

=> Le script doit ressortir le résultat de cette manière : L'aire d'un triangle de base 10.5 et de hauteur 8.0 est 42.0

'''
#importer le nombbre pi
from math import pi

#fonction
def R(rayon) :
    '''
    retourne l'aire d'un disque
    en connaissant le rayon du disque

Entrée :
    - rayon : rayon du disque

Sortie :
    - le calcul de l'aire du disque
    '''
    return pi*rayon**2

########################################################################
######################   PROGRAMME PRINCIPAL    ########################
#####################   LE SCRIPT DEBUTE ICI     #######################
########################################################################


print ("Début du programme\n\n")

# information sur le rayon
rayon=float(input("Quel est le rayon du disque ? : "))

# appel de la fonction afin de calculer l'aire
Aire = R(rayon)

print ("L'aire d'un disque de rayon",rayon,"est",Aire,"\n")

print("Fin du programme")
