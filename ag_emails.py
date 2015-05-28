#!/usr/bin/python
# -*- encoding: utf-8 -*-
special_char_string = u"äöüáèéàô" # Ajout de caractères spéciaux

import uuid # Permet de générer un identifiant universel unique

print("C'est parti !!!")

noms_et_clefs = open('noms_et_clefs.csv', 'w') # Créer la liste des courriels avec les uuid

try:
	couriels =  open('courriels_etudiants.csv', 'r') # Courriels ulaval
except IOError:
	print "Problemes avec le fichier : courriels_etudiants.csv"
	exit(0)

while True:
    line = couriels.readline() # Lecture d'une adresse courriel
    if not line: # Fin du ficher
        break # Arrêt de la boule si fin fichier
    clefs = str(uuid.uuid4()) # Convertis les uuid en séquence de caractères 
    email = line.strip('\n') # Retier le \n de la séquence email
    value = email  + ',' + clefs +  '\n' 
    noms_et_clefs.write(value) # Écris les courriels et les clefs dans un fichier

# Fermeture du fichier des noms et courriels   
#noms_et_clefs.write('\n')
noms_et_clefs.close()
# Fermeture du fichier des couriels ulaval
couriels.close()