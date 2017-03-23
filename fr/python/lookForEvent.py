# -*- coding: utf-8 -*-
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

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
    if mois == "01":
        return "janvier"
    elif mois == "02":
        return "fevrier"
    elif mois == "03":
        return "mars"
    elif mois == "04":
        return "avril"
    elif mois == "05":
        return "mai"
    elif mois == "06":
        return "juin"
    elif mois == "07":
        return "juillet"
    elif mois == "08":
        return "aout"
    elif mois == "09":
        return "septembre"
    elif mois == "10":
        return "octobre"
    elif mois == "11":
        return "novembre"
    elif mois == "12":
        return "decembre"
    return ""

    
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
    reply = ""
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    reply += "Je regarde.\n"
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=50, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
        
    file = open('/home/pi/jarvis/plugins/jarvis-calendar/fr/evenement.txt')
    myEvent = file.readlines()
    summary = myEvent[0].capitalize()
    file.close()

    eventFound = False
    for event in events:
        if summary == event['summary'] :
            eventFound = True
            debut= event['start'].get('dateTime')

            # Formatage de la date
            if debut[8:10] == now[8:10] :
                date = "aujourd'hui"
            elif int(debut[8:10])-1 == int(now[8:10]) :
                date = "demain"
            else :
                date = "le " + debut[8:10] + " " + get_mois(debut[5:7]) + " " + debut[0:4]
            
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
        
    file = open("/home/pi/jarvis/plugins/jarvis-calendar/fr/evenement.txt", "w")
    file.write(reply.encode("utf-8"))
    file.close


if __name__ == '__main__':
    main()
