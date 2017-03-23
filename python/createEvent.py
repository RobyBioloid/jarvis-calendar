# -*- coding: utf-8 -*-
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from datetime import date

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_mois(mois):
    if mois == "janvier" or mois == '01' or mois == '1':
        return "01"
    elif mois == "fevrier" or mois == '02' or mois == '2':
        return "02"
    elif mois == "mars" or mois == '03' or mois == '3':
        return "03"
    elif mois == "avril" or mois == '04' or mois == '4':
        return "04"
    elif mois == "mai" or mois == '05' or mois == '5':
        return "05"
    elif mois == "juin" or mois == '06' or mois == '6':
        return "06"
    elif mois == "juillet" or mois == '07' or mois == '7':
        return "07"
    elif mois == "aout" or mois == '08' or mois == '8':
        return "08"
    elif mois == "septembre" or mois == '09' or mois == '9':
        return "09"
    elif mois == "octobre" or mois == '10':
        return "10"
    elif mois == "novembre" or mois == '11':
        return "11"
    elif mois == "decembre" or mois == '12' :
        return "12"
    return '01'


def get_minute(minute) :
    if minute == 'cinq' or minute == '5' or minute == '05':
        return '05'
    elif minute == 'dix' or minute == '10' :
        return '10'
    elif minute == 'quinze' or minute == '15' :
        return '15'
    elif minute == 'vingt' or minute == '20' :
        return '20'
    elif minute == 'vingt-cinq' or minute == '25' :
        return '25'
    elif minute == 'trente' or minute == '30' :
        return '30'
    elif minute == 'tentre-cinq' or minute == '35' :
        return '35'
    elif minute == 'quarante' or minute == '40' :
        return '40'
    elif minute == 'quarante-cinq' or minute == '45' :
        return '45'
    elif minute == 'cinquante' or minute == '50' :
        return '50'
    elif minute == 'cinquante-cinq' or minute == '55' :
        return '55'


    
def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
        
    credential_path = os.path.join(credential_dir, 'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
            
        print('Storing credentials to ' + credential_path)
        
    return credentials

def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    file = open('/home/pi/jarvis/plugins/jarvis-calendar/fr/evenement.txt')
    myEvent = file.readlines()
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
        
    heure = myEvent[4].split()
    if int(heure[0]) < 10 :
       heure[0] = '0' + heure[0]
    if len(heure) > 2 :
        heure[2] = get_minute(str(heure[2]))
    else :
        heure.append('00')
        
    startDateTime = dateTime[2] + '-' + get_mois(dateTime[1]) + '-' + dateTime[0] + 'T' + heure[0] + ':' + heure[2] + ':00+01:00'

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
        
    heure = myEvent[6].split()
    if int(heure[0]) < 10 :
       heure[0] = '0' + heure[0]
    if len(heure) > 2 :
        heure[2] = get_minute(str(heure[2]))
    else :
        heure.append('00')
        
    endDateTime = dateTime[2] + '-' + get_mois(dateTime[1]) + '-' + dateTime[0] + 'T' + heure[0] + ':' + heure[2] + ':00+01:00'

    
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
            

if __name__ == '__main__':
    main()
