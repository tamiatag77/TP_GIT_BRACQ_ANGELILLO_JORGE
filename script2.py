#!/usr/bin/python
#Importe la bibliothèque .os
import os

#Nous permet de définir le chemin ou sera cloner le répertoire
destination_path  = "./clone"
#Correspond à la commande utilisé pour cloner le répertoire
clone_command = "git clone https://github.com/KeligMartin/4-SRC.git"

#Execution de la commande de clonage suivi du chemin de destination du répertoire cloné
clone_with_path = clone_command  +" "+ destination_path
os.system(clone_with_path)
