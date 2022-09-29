#!/usr/bin/python

#Les variables à initialiser 
min = 1
max = 100000

#Boucle qui permettant de ressortir les nombres premiers de 1 à 100 000
for n in range(min,max + 1):

#Si n est uniquement superieure à 1
   if n > 1:
#boucle qui test si il s'agit d'un nombre premier
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
#Affiche le nombre premier
           print(n)
