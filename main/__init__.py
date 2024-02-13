#Github.com/Vasusen-code

from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys
from os import environ
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.ALERT)

# variables
API_ID = config("API_ID", "9544521", cast=int)
API_HASH = config("API_HASH", "5cf32e97dc94510e46524f2286c95116")
BOT_TOKEN = config("BOT_TOKEN", "")
SESSION = config("SESSION", "")
FORCESUB = config("FORCESUB", "bot_logv4")
AUTH = config("AUTH", "1358657527", cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
