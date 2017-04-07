# -*- coding: utf-8 -*-
from __future__ import print_function
import httplib2
import os

from toolsEvent import *

import datetime


def tomorrowEvent():
    " Fonction de recherche des événement pour le lendemain"
    reply = ""

    # Parametrage de l'aplication
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    # Récupération des événements
    i = 0
    evenements = ""
    for event in events:
        debut= event['start'].get('dateTime')
        if debut == None :
            debut = event['start'].get('date')
                
            # Formatage de la date
            if int(debut[8:10])-1 == int(now[8:10]) :
                i += 1
                date = "Demain "
                heure = ""
                
        else :
            # Vérification de la date
            if debut[0:4] == now[0:4] and debut[5:7] == now[5:7] and int(debut[8:10])-1 == int(now[8:10]) :
                i += 1
                date = "Demain "
                # Formatage de l'heure
                heure = u"à " + debut[11:13] + " heure"
                if debut[14:16] != "00" :
                    heure = heure + " " + debut[14:16]

        try :
            summary = event['summary']
        except :
            summary = "Sans titre"

        try :
            location = event['location']
        except :
            location = "Aucun lieu défini"

        try :
            description = event['description']
        except :
            description = "Pas de description"

        if date == "Demain " :
            evenements += date + heure + u", vous avez l'événement : " + summary + ".\n"
            date = ""
            
    if i == 0 :
        reply += u"Vous n'avez pas d'événements de prévus pour demain\n"
    elif i == 1 :
        reply += u"Vous avez 1 événement de prévu pour demain\n" + evenements
    else :
        reply += "Vous avez " + str(i) + u" événements prévus pour demain\n" + evenements
        
    fichier = open(EVENT_PATH, "w")
    fichier.write(reply.encode("utf-8"))
    fichier.close


tomorrowEvent()
