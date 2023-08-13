# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID'))
    API_HASH = str(getenv('API_HASH'))
    BOT_TOKEN = str(getenv('BOT_TOKEN'))
    name = str(getenv('name', 'tomen'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '5'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL'))
    PORT = int(getenv('PORT', 80))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split())  
    NO_PORT = bool(getenv('NO_PORT', 80))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME'))
    if 'KOYEB' in environ:
        ON_KOYEB = True
        APP_NAME = str(environ.get('APP_NAME'))
    else:
        ON_KOYEB = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_KOYEB or getenv('FQDN') else APP_NAME+'.koyeb.app'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
