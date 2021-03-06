# -*- coding: utf-8 -*-
from __future__ import print_function
import httplib2
import os

from toolsEvent import *
from datetime import date

def createEvent():
    " Fonction de création d'événement"
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    
    jetLag = get_jetLag()
    file = open(EVENT_PATH)
    myEvent = file.readlines()
    file.close()
    
    summary = myEvent[0].capitalize()
    location = myEvent[1].capitalize()
    description = myEvent[2].capitalize()
    
    dateTime = myEvent[3].split()
    if dateTime[0] == 'aujourd\'hui' or dateTime[0] == 'aujourd' or dateTime == 'au' or dateTime[0] == 'aujourdhui':
        dateTime = []
        today = date.today()
        dateTime.append(str(today.day))
        dateTime.append(str(today.month))
        dateTime.append(str(today.year))
    elif dateTime[0] == 'demain' :
        dateTime = []
        today = date.today()
        dateTime.append(str(today.day + 1))
        dateTime.append(str(today.month))
        dateTime.append(str(today.year))
    else :
        dateTime[0] = get_numDay(dateTime[0])
        
    h = myEvent[4]
    heure = ""
    i = 0
    while i < len(h) :
        if h[i] == "h" :
            if h[i-1] != " " :
                heure += " " + "h"
            else :
                heure += "h"
        else :
            heure += h[i]
        i += 1

    heure = heure.split()

    if int(heure[0]) < 10 :
       heure[0] = '0' + str(heure[0])
    if len(heure) > 2 :
        heure[2] = get_minute(str(heure[2]))
    else :
        heure.append('00')
        
    startDateTime = dateTime[2] + '-' + get_intMonth(dateTime[1]) + '-' + dateTime[0] + 'T' + heure[0] + ':' + heure[2] + jetLag

    dateTime = myEvent[5].split()
    if dateTime[0] == 'aujourd\'hui' or dateTime[0] == 'aujourd' or dateTime == 'au' or dateTime[0] == 'aujourdhui':
        dateTime = []
        today = date.today()
        dateTime.append(str(today.day))
        dateTime.append(str(today.month))
        dateTime.append(str(today.year))
    elif dateTime[0] == 'demain' :
        dateTime = []
        today = date.today()
        dateTime.append(str(today.day + 1))
        dateTime.append(str(today.month))
        dateTime.append(str(today.year))
    else :
        dateTime[0] = get_numDay(dateTime[0])

    h = myEvent[6]
    heure = ""
    i = 0
    while i < len(h) :
        if h[i] == "h" :
            if h[i-1] != " " :
                heure += " " + "h"
            else :
                heure += "h"
        else :
            heure += h[i]
        i += 1

    heure = heure.split()        
    if int(heure[0]) < 10 :
       heure[0] = '0' + heure[0]
    if len(heure) > 2 :
        heure[2] = get_minute(str(heure[2]))
    else :
        heure.append('00')
        
    endDateTime = dateTime[2] + '-' + get_intMonth(dateTime[1]) + '-' + dateTime[0] + 'T' + heure[0] + ':' + heure[2] + jetLag

    
    event = {
        'summary' : summary,
        'location' : location,
        'description' : description,
        'start' : {
            'dateTime' : startDateTime,
            'timeZone': 'France/(GMT+01:00) Paris',
        },
        'end' : {
            'dateTime' : endDateTime,
            'timeZone': 'France/(GMT+01:00) Paris',
        },
        'recurrence' : [
            'RRULE:FREQ=DAILY;COUNT=1'
        ],
        'reminders' : {
            'useDefault' : False,
            'overrides' : [
                {'method' : 'email', 'minutes' : 24 * 60},
                {'method' : 'popup', 'minutes' : 60},
            ],
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
            

createEvent()
