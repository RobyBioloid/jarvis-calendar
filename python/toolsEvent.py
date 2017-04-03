from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from datetime import date

import os

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = '/home/pi/jarvis/plugins/jarvis-calendar/python/client_secret.json'
APPLICATION_NAME = 'Google Calendar API'

EVENT_PATH = os.getcwd() + "/plugins/jarvis-calendar/python/event.txt"
CHECK_PATH = os.getcwd() + "/plugins/jarvis-calendar/python/check.txt"

def get_jetLag() :
    today = date.today()
    startSummerTime = [date(2017, 3, 25), date(2018, 3, 24), date(2019, 3, 30), date(2020, 3, 28),
                   date(2021, 3, 27), date(2022, 3, 26), date(2023, 3, 25), date(2024, 3, 30),
                   date(2025, 3, 29), date(2026, 3, 28), date(2027, 3, 27), date(2028, 3, 25),
                   date(2029, 3, 24), date(2030, 3, 30), date(2031, 3, 29), date(2032, 3, 27)]

    endSummerTime = [date(2017, 10, 28), date(2018, 10, 27), date(2019, 10, 26), date(2020, 10, 24),
                 date(2021, 10, 30), date(2022, 10, 29), date(2023, 10, 28), date(2024, 10, 26),
                 date(2025, 10, 25), date(2026, 10, 24), date(2027, 10, 30), date(2028, 10, 28),
                 date(2029, 10, 27), date(2030, 10, 26), date(2031, 10, 25), date(2032, 10, 30)]
    
    i = 0
    while i < 16 :
        if today > startSummerTime[i] and today < endSummerTime[i] :
            return ':00+02:00'
        else :
            return ':00+01:00'

def get_numDay(jour) :
    jour = unicode(jour, 'utf-8')
    if jour == "un" or jour == "01" or jour == "1" or jour == "1ere" or jour == "1er" or jour =="1e" :
        return "01"
    elif jour == "de" or jour == "deux" or jour == "02" or jour == "2" :
        return "02"
    elif jour == "trois" or jour =="troie" or jour == "bah" or jour == "03" or jour == "3" :
        return "03"
    elif jour == "quatre" or jour == "quatres" or jour == "cat" or jour == "kat" or jour == "04" or jour == "4" :
        return "04"
    elif jour == "cinq" or jour == "ca" or jour == "05" or jour == "5" :
        return "05"
    elif jour == "six" or jour == "scie" or jour == "si" or jour == "06" or jour == "6" :
        return "06"
    elif jour == "sept" or jour == "sete" or jour == "07" or jour == "7" :
        return "07"
    elif jour == "huit" or jour == "oui" or jour == "huitre" or jour == "08" or jour == "8" :
        return "08"
    elif jour == "neuf" or jour == "oeuf" or jour == "09" or jour == "9" :
        return "09"
    elif jour == "dix" or jour == "dis" or jour == "10" :
        return "10"
    elif int(jour) > 10 :
        return str(jour)
    else :
        return "99"



    
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
    return '99'


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
