from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import os

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

EVENT_PATH = os.getcwd() + "/plugins/jarvis-calendar/python/event.txt"

def get_intMonth(mois):
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
    return '00'

    
def get_strMonth(mois):
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
    return "janvier"

    
def get_credentials():
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
