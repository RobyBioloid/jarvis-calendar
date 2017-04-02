# -*- coding: utf-8 -*-
from toolsEvent import *

def check():
    reply = "" 
    file = open(EVENT_PATH)
    myEvent = file.readlines()
    file.close()
    
    summary = myEvent[0].decode('utf8')
    location = myEvent[1].decode('utf-8')
    description = myEvent[2].decode('utf-8')
    jour_debut = myEvent[3].decode('utf-8')
    heure_debut = myEvent[4].decode('utf-8')
    jour_fin = myEvent[5].decode('utf-8')
    heure_fin = myEvent[6].decode('utf-8')

    
    reply += u"Confirmez vous l'ajout de l'événement. Titre : " + summary
    reply += ", lieu : " + location
    reply += ", description : " + description
    reply += u", avec comme date de début : " + jour_debut
    reply += u", à " + heure_debut
    reply += ", avec comme date de fin : " + jour_fin
    reply += u", à " + heure_fin + "."

    file = open(CHECK_PATH, 'w')
    file.write(reply.encode('utf-8'))
    file.close()

check()
