#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", "9544521", cast=int)
API_HASH = config("API_HASH", "5cf32e97dc94510e46524f2286c95116")
BOT_TOKEN = config("BOT_TOKEN", "5874353588:AAGBko69Fge6yzneLl8QgAGA0tLKHZ5Jl-0")
SESSION = config("SESSION", "BQCRo0kAH_5IzI38xba_qoHDrcOTTIrE_RtybVAWFXIJkOSJUSlv05GbnF6TyGHf4--guSp9VjUZahg3K4up5053qngYtdV0pnOVEqHSrg5GILoI3C0OAeZdQPeECNmm3BFZ2-yqwzZkItOU6y5ZCP3wr3t2JWYTEJMMbD7o4ms_eP6z6hwWipOApVKiXWodkjG6m5mkSELtxUSh7TSvAFZZOo2l3QVRo2yL7iW9Z4aTqDvItYhKXgaP5Ld0AkOSfVeh9i3jrEdonEFbW0Il76a5E051zHYoDNYj6Vs1KVwru91rbCDRW5IFjCZI2YP6g2bpqgBltBHB-bmRzUO5RvOlsgiiqAAAAABQ-3f3AA")
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
