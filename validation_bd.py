#!/usr/bin/python
# -*- encoding: utf-8 -*-
special_char_string = u"äöüáèéôà" # Ajout de caractères spéciaux
from collections import Counter
from collections import defaultdict

try:
	BD =  open('formulaire_AESMUL.csv', 'r') # Réponses du vote
except IOError:
	print "Problemes avec le fichier : formulaire_AESMUL.csv"
	exit(0)

try:
	couriels_et_clef =  open('noms_et_clefs.csv', 'r') # Liste des courriels ulaval
except IOError:
	print "Problemes avec le fichier : noms_et_clefs_test.csv"
	exit(0)

Liste_clefs_valide = [] # base de données des clefs valides

# Création de la base de données des clefs valides
while True:
	line = couriels_et_clef.readline() # Obtention d'un courriel et d'une clef
	if line == '\n': # Si la dernière ligne du fichier est un espace
		break
	if not line: # Fin du fichier
		break
	infos = line.split(",") # Séparare dans une liste : [courriel,uuid]
	Liste_clefs_valide = Liste_clefs_valide + [str(infos[1][:-1])]
couriels_et_clef.close() # Fermer le fichier

uuid_vote = [] # Liste des uuid dans BD (formulaire_AESMUL.csv)
oui =0 # Compteur oui
non =0 # Compteur non
neutre =0 # Compteur neutre

# Lecture de la BD
BD.readline() # Sauter la ligne 1
while True:
	line = BD.readline() # Obtention d'un courriel et d'une clef
	if line == '\n': # Si la dernière ligne du fichier est un espace
		break
	if not line: # Fin du fichier
		break
	infos_BD = line.split(",") # Séparare dans une liste : [temps,reponse,uuid]

	if str(infos_BD[2].strip('\n')) in Liste_clefs_valide and str(infos_BD[2].strip('\n')) not in uuid_vote: # Si clef valide
		# Compteur
		if infos_BD[1] == 'Oui':
			oui += 1
		elif infos_BD[1] == 'Non':
			non += 1
		elif infos_BD[1] == 'Abstention':
			neutre += 1
		else:
			print ('Erreur BD :' + infos_BD[1])

	else: #Clef invalide
		print('Clef invalide :' + infos_BD[2].strip('\n'))

	uuid_vote = uuid_vote + [infos_BD[2].strip('\n')] # Ajouter des uuid déjà lus
BD.close() # Fermer le fichier

#Doublon (O(n))
D = defaultdict(list)
for i,item in enumerate(uuid_vote):
    D[item].append(i)
D = {k:v for k,v in D.items() if len(v)>1}

#print(D)

#print(uuid_vote)
#print(Liste_clefs_valide)
print("Oui: ", oui, "Non: ", non, "Abstention: ", neutre)
