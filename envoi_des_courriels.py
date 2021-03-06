#!/usr/bin/python
# -*- encoding: utf-8 -*-
special_char_string = u"äöüáèéôà" # Ajout de caractères spéciaux

import smtplib
import email.utils
from email.mime.text import MIMEText

# Prompt the user for connection info
# to_email = 'sim_123_@hotmail.com'
servername = 'smtp.gmail.com:587'
username = 'simonpierreroy@gmail.com'
password = '46rt46rt'

try:
	couriels_et_clef =  open('noms_et_clefs_PARTIEL2.csv', 'r') # Liste des courriels ulaval
except IOError:
	print "Problemes avec le fichier : noms_et_clefs_test.csv"
	exit(0)

#Envoi des courriels
while True:
	line = couriels_et_clef.readline() # Obtention d'un courriel et d'une clef
	if line == '\n': # Si la dernière ligne du fichier est un espace
		break
	if not line: # Fin du fichier
		break
	infos = line.split(",") # Séparare dans une liste : [courriel,uuid]

	to_email = infos[0] # Destinataire
	contenu = """
Bonjour,
	
	
Suite à l'assemblée spéciale du 27 mars 2015, la proposition suivante a été
proposée et acceptée :


- Je, Rosalie Bentz-Moffet, propose que L'AESMUL adopte un mandat de grève
le 2 avril 2015 afin de permettre à ses membres de se rendre à la 
manifestation nationale.

- Je, Benoît Pouliot, propose que la question référendaire soit :

     « Que L'AESMUL adopte un mandat de grève le 2 avril 2015 afin de 
     permettre à ses membres de se rendre à la manifestation nationale. »

- Je, Gabriel St-Pierre, propose un vote électronique. Le  courriel sera 
envoyé dimanche matin (29 mars 2015) et le vote se terminera le 30 mars 
2015 à 23h. 

Veuillez utiliser le lien suivant pour voter : http://bit.ly/1H1RuV3.
Voici votre identifiant unique : """ + infos[1] + """
       
    
David Landry
Scrutateur de l'AESMUL
scrutateuraesmul@gmail.com
"""

	# Create the message
	msg = MIMEText(contenu) # Message
	msg.set_unixfrom('author')
	msg['To'] = email.utils.formataddr((infos[0], to_email)) # À
	msg['From'] = email.utils.formataddr(('David Landry', 'scrutateuraesmul@gmail.com')) # De
	msg['Subject'] = 'AESMUL - Vote de grève' # Sujet

	server = smtplib.SMTP(servername)
	try:
		# Messages for connection and all messages sent to and received from the server.
	    server.set_debuglevel(True) 

	    # identify ourselves, prompting server for supported features
	    server.ehlo()

	    # If we can encrypt this session, do it
	    if server.has_extn('STARTTLS'):
	        server.starttls()
	        server.ehlo() # re-identify ourselves over TLS connection

	    server.login(username, password) # Connexion au serveur
	    server.sendmail('scrutateuraesmul@gmail.com', [to_email], msg.as_string()) # Envoi du message
	finally:
	    server.quit()
	    
couriels_et_clef.close() # Fermer le fichier
