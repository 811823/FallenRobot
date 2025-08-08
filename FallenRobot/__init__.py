import logging
import os
import sys
import time

from dotenv import load_dotenv
load_dotenv()

import telegram.ext as tg
from pyrogram import Client, errors
from telethon import TelegramClient

StartTime = time.time()

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger("telethon").setLevel(logging.ERROR)
logging.getLogger("pymongo").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)

# 统一优先从环境变量读取，未设置时回退到config.py
from FallenRobot.config import Development as Config

def get_env(key, default=None, cast_type=str):
    value = os.environ.get(key)
    if value is not None:
        try:
            return cast_type(value)
        except Exception:
            return value
    return getattr(Config, key, default)

API_ID = get_env("API_ID", None, int)
API_HASH = get_env("API_HASH", None, str)
ALLOW_CHATS = get_env("ALLOW_CHATS", True, lambda x: x.lower() == 'true')
ALLOW_EXCL = get_env("ALLOW_EXCL", True, lambda x: x.lower() == 'true')
CASH_API_KEY = get_env("CASH_API_KEY", "", str)
DB_URI = get_env("DATABASE_URL", "", str)
DEL_CMDS = get_env("DEL_CMDS", True, lambda x: x.lower() == 'true')
EVENT_LOGS = get_env("EVENT_LOGS", (), str)
INFOPIC = get_env("INFOPIC", True, lambda x: x.lower() == 'true')
LOAD = get_env("LOAD", [], lambda x: x.split() if x else [])
MONGO_DB_URI = get_env("MONGO_DB_URI", "", str)
NO_LOAD = get_env("NO_LOAD", [], lambda x: x.split() if x else [])
START_IMG = get_env("START_IMG", "https://telegra.ph/file/40eb1ed850cdea274693e.jpg", str)
STRICT_GBAN = get_env("STRICT_GBAN", True, lambda x: x.lower() == 'true')
SUPPORT_CHAT = get_env("SUPPORT_CHAT", "DevilsHeavenMF", str)
TEMP_DOWNLOAD_DIRECTORY = get_env("TEMP_DOWNLOAD_DIRECTORY", "./", str)
TOKEN = get_env("TOKEN", None, str)
TIME_API_KEY = get_env("TIME_API_KEY", "", str)
WORKERS = get_env("WORKERS", 8, int)

try:
    OWNER_ID = get_env("OWNER_ID", None, int)
except Exception:
    raise Exception("Your OWNER_ID env variable is not a valid integer.")

try:
    BL_CHATS = set(int(x) for x in get_env("BL_CHATS", "", str).split())
except Exception:
    raise Exception("Your blacklisted chats list does not contain valid integers.")

try:
    DRAGONS = set(int(x) for x in get_env("DRAGONS", "", str).split())
    DEV_USERS = set(int(x) for x in get_env("DEV_USERS", "", str).split())
except Exception:
    raise Exception("Your sudo or dev users list does not contain valid integers.")

try:
    DEMONS = set(int(x) for x in get_env("DEMONS", "", str).split())
except Exception:
    raise Exception("Your support users list does not contain valid integers.")

try:
    TIGERS = set(int(x) for x in get_env("TIGERS", "", str).split())
except Exception:
    raise Exception("Your tiger users list does not contain valid integers.")

try:
    WOLVES = set(int(x) for x in get_env("WOLVES", "", str).split())
except Exception:
    raise Exception("Your whitelisted users list does not contain valid integers.")


DRAGONS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(1356469075)


updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient("Fallen", API_ID, API_HASH)

pbot = Client("FallenRobot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
dispatcher = updater.dispatcher

print("[INFO]: Getting Bot Info...")
BOT_ID = dispatcher.bot.id
BOT_NAME = dispatcher.bot.first_name
BOT_USERNAME = dispatcher.bot.username

DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)

# Load at end to ensure all prev variables have been set
from FallenRobot.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler
