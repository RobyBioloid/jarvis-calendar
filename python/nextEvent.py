# -*- coding: utf-8 -*-
from __future__ import print_function
import httplib2
import os
from toolsEvent import *

import datetime

def nextEvent():
    "Fonction qui retourne le prochain événement" 
    reply = ""
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=1, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        reply += u"Vous n'avez aucun événements de prévus.\n"
    elif len(events) == 1:
        reply += u"Votre prochain événement de prévu est :\n"
    else:      
        reply += 'Vos ' + str(len(events)) + u" prochains événements de prévus sont :\n"
        
    for event in events:
        debut= event['start'].get('dateTime')
        if debut == None :
            debut = event['start'].get('date')
                
            # Formatage de la date
            if int(debut[8:10]) == int(now[8:10]) :
                date = "Aujourd'hui "
            elif debut[0:4] == now[0:4] and debut[5:7] == now[5:7] and int(debut[8:10])-1 == int(now[8:10]) :
                date = "Demain "
            else :
                date = "Le " + str(debut[8:10]) + " " + str(get_strMonth(debut[5:7])) + " " + str(debut[0:4]) + " "
            heure = ""
                
        else :
            # Formatage de la date
            if debut[8:10] == now[8:10] :
                date = "Aujourd'hui "
            elif debut[0:4] == now[0:4] and debut[5:7] == now[5:7] and int(debut[8:10])-1 == int(now[8:10]) :
                date = "Demain "
            else :
                date = "Le " + debut[8:10] + " " + get_strMonth(debut[5:7]) + " " + debut[0:4] + " "
            
            # Formatage de l'heure
            heure = u"à " + debut[11:13] + " heure"
            if debut[14:16] != "00" :
                heure = heure + " " + debut[14:16]

        try :
            fin = event['end'].get('dateTime')
        except :
            fin = date
            
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

        reply += date + heure + ", " + summary + ".\n"
        
    
    file = open(EVENT_PATH, "w")
    file.write(reply.encode("utf-8"))
    file.close()



nextEvent()
