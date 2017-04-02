# -*- coding: utf-8 -*-
from __future__ import print_function
import httplib2
import datetime
import os

from toolsEvent import *

def lookForEvent():
    '''
    reply = ""
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    reply += "Je regarde.\n"
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=50, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
        
    file = open(EVENT_PATH)
    myEvent = file.readlines()
    summary = myEvent[0].capitalize()
    file.close()

    eventFound = False
    for event in events:
        if summary == event['summary'] +'\n' :
            eventFound = True
            debut= event['start'].get('dateTime')

            # Formatage de la date
            if debut[8:10] == now[8:10] :
                date = "aujourd'hui"
            elif int(debut[8:10])-1 == int(now[8:10]) :
                date = "demain"
            else :
                date = "le " + debut[8:10] + " " + get_strMonth(debut[5:7]) + " " + debut[0:4]
            
            # Formatage de l'heure
            heure = debut[11:13] + " heure"
            if debut[14:16] != "00" :
                heure = heure + " " + debut[14:16]

        
            fin = event['end'].get('dateTime')
            location = event['location']
            description = event['description']
            reply = reply + u"L'événement " + summary + u" est prévu pour " + date + u" à " + heure + "\n"
            
    if eventFound == False :
        reply = reply + u"Aucun événement trouvé sous le nom " + summary
    '''
    reply = u"L'option de recherche n'est pas encore opérationnelle."
    file = open(EVENT_PATH, "w")
    file.write(reply)
    file.close()


lookForEvent()
