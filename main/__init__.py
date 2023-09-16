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
SESSION = config("SESSION", "BQCRo0kAvVz88rmThedZ0D2Y8CGeOx-Kt5XC2mLlg6VnKQhCAKD13spqe4-YNCXz0G-0_cfKL3sCps8XIvN9dkJR4QZX4-oEcq4rQAz21dUe-WqiFf7scFfvVYavOnzf37vIxYRTJtfV10Espco5kgnbRoe45zW65WuVeCacQYGKmV3LpCbBOAlrxZQFTxQZOoTl3MaorbZ-yofycfG9Lc4mqw8HZ8VH6kKw-6iVd6Q8QcTlnSOnl4JI6BJoWkvfrvcpomd3wN6Yu5nfds9pGO5qSEolmfbKuo6s70KTt1SsYl2wzqy3JNWbkeBXYQBrQqZ4GAD-JeA50SpmQGUj0in8-bHMSwAAAABQ-3f3AA")
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
