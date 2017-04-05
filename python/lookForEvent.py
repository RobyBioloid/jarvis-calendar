# -*- coding: utf-8 -*-
from __future__ import print_function
import httplib2
import datetime
import os

from toolsEvent import *

def lookForEvent():
    reply = u"Je regarde\n"
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=100, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
        
    file = open(EVENT_PATH)
    myEvent = file.readline() + "\n"
    file.close()

    myEventSplit = myEvent.split()
    
    myEventCopy = "" 
    copy = False
    i = 0
    while i < len(myEventSplit) :
        if copy == True :
            myEventCopy += myEventSplit[i] + " "
        else :
            if myEventSplit[i] == "événement" or myEventSplit[i] == "évènement" or myEventSplit[i] == "l'événement" or myEventSplit[i] == "l'évènement" :
                copy = True
        i += 1

    myEventCopy = myEventCopy[0:len(myEventCopy)-1]
    summary = myEventCopy.lower()
    summary = unicode(summary, 'utf-8')
    eventFound = False
    for event in events:
        try :
            summ = event['summary'].lower()
        except :
            summ = "Sans titre"

        print("summ = " + summ)
        print("summary = " + summary)
        if summary == summ :
            eventFound = True
            
            debut = event['start'].get('dateTime')
            if debut == None :
                debut = event['start'].get('date')
                
                # Formatage de la date
                if debut[8:10] == now[8:10] :
                    date = "aujourd'hui"
                elif int(debut[8:10])-1 == int(now[8:10]) :
                    date = "demain"
                else :
                    date = "le " + str(debut[8:10]) + " " + str(get_strMonth(debut[5:7])) + " " + str(debut[0:4])
                heure = ""
                
            else :
                # Formatage de la date
                if debut[8:10] == now[8:10] :
                    date = "aujourd'hui"
                elif int(debut[8:10])-1 == int(now[8:10]) :
                    date = "demain"
                else :
                    date = "le " + str(debut[8:10]) + " " + str(get_strMonth(debut[5:7])) + " " + str(debut[0:4])
            
                # Formatage de l'heure
                heure = u" à " + debut[11:13] + " heure"
                if debut[14:16] != "00" :
                    heure = heure + " " + debut[14:16]

            try :
                fin = event['end'].get('dateTime')
            except :
                fin = date
            try :
                location = event['location']
            except :
                location = "Sans lieu"
            try :
                description = event['description']
            except :
                description = "Pas de description"
                
            reply = reply + u"L'événement " + summary + u" est prévu pour " + date + heure + "\n"
            break
            
    if eventFound == False :
        reply = reply + u"Aucun événement trouvé sous le nom " + summary + "\n"

    file = open(EVENT_PATH, "w")
    file.write(reply.encode('utf-8'))
    file.close()


lookForEvent()
