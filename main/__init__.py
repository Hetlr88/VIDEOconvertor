from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", 29452145, cast=int)
API_HASH = config("API_HASH", "5a2784e571fe5043852d32396a34a13b")
BOT_TOKEN = config("BOT_TOKEN", "7445547849:AAHfX4_8TQ57cg71Q_l9ABoa6RfgfPWHgsE")
BOT_UN = config("BOT_UN", "YouTube_downloader_S1BOT")
AUTH_USERS = config("AUTH_USERS", 6169288210, cast=int)
LOG_CHANNEL = config("LOG_CHANNEL","series0x1")
LOG_ID = config("LOG_ID",-1002248610571, cast=int )
FORCESUB = config("FORCESUB", -1002248610571, cast=int)
FORCESUB_UN = config("FORCESUB_UN", "series0x1")
ACCESS_CHANNEL = config("ACCESS_CHANNEL", -1002243837012, cast=int)
MONGODB_URI = config("MONGODB_URI", "mongodb+srv://KannadaMagaa:KannadaMagaa@kannadamagaaclone.kweqbmy.mongodb.net/?retryWrites=true&w=majority")

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
