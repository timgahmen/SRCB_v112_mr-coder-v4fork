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
BOT_TOKEN = config("BOT_TOKEN", "5650815754:AAGcjI8LjK4wvqu5gC3NCVEyhoSJ8norfWE")
SESSION = config("SESSION", "BQCRo0kAF6YmG0auj6F4a70OWx9ygCmR7dnU92UtzcG4_Igc9Ah4Jvw0-sRzH0E8LgACTamTii-8iO_R7rkdqC8RHHhwu_3wAJzlQ_YFIYkJZu_mZziST3U3BFRq_1iF-XtrAiRzhRMxyo4URYWLA8WNUb9x5YieQuwKfOIlhJg6HQh5MkYXjFOZ_XsflNFY0u99IqO2yu0ik2jM4CwTnNrh7sIRC4QQBLPm55PImoCCbWTvh4wq4e0Ok9a1tIXf8eF_YCYfUQOyWhZJ_cPO_T83JCMbz-F4q1RUlg5WurOufgiZjhTAfeMWN-YqqASL7v022WnTM8pv2o79aK4ewH1aY_2WdwAAAABQ-3f3AA")
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
