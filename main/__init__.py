#Join @dev_gagan

from telethon.errors import FloodWaitError
from datetime import datetime as dt, timedelta
import asyncio
import sys
from pyrogram import Client
import asyncio
import uvloop
from pyrogram.errors import FloodWait
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from decouple import config
import logging, time
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

uvloop.install()
MDB = "mongodb+srv://ggn:ggn@ggn.upuljx5.mongodb.net/?retryWrites=true&w=majority&appName=ggn"
API_ID = "21266744" #config("API_ID", default=None, cast=int)
API_HASH = "41028624362faeb4515884b4fe67a9b9" #config("API_HASH", default=None)
BOT_TOKEN = "7310794519:AAFFiZVUnMVQn2frTDKk61rzyiJHPAYDXoA" #config("BOT_TOKEN", default=None)
SESSION = "BQFEgTgAuKzuY_nfSFx-2fw1zLa83dr78jcwjInzzrJuxHytgqjAKVkr2tykenkv_VIWQWW-FqqjU8ip7S2QNywX8ZmvtWbzIrfxrbwAal6oj06ayR5nm1-OQA4StOv5tTOYI28vn8QCjZLajVaaPxNMQixgfzQNcnCqsVrspxta9Dw1S5uzjU1DDRHHo5Gz0adEU4p9QjBcYR5W_vzQQe_3V7s45mSrsG_HWKSUjFXg1UP3iWFBvJKQlNQoFphG8xYaSGLU6rcPk65g7oQ-rP8dqII6T6QM1CNyTDw9suXniuxdAnrjq2zJgux0NHq_dBuZmpjr_BLKBhj3qFcYRSNICsOEoQAAAABjoCK0AA" #config("SESSION", default=None)
FORCESUB = "samrabotss" #config("FORCESUB", default=None)
AUTH = "6756781098" #config("AUTH", default=None)
MONGODB = config("MONGODB", default=MDB)
OWN = 6756781098 # edit this
GROUP = -1002240648361 # edit this
OWNER_ID = int(config("OWNER_ID", default=OWN))
LOG_GROUP = int(config("LOG_GROUP", default=GROUP))

SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks.")
    sys.exit(1)

Bot = Client(
    "ggnbot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    sys.exit(1)
