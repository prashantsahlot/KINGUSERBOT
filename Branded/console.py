import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = int(getenv("API_ID", 24353724))
API_HASH = getenv("API_HASH", 4dfc22b90dc7d9b2f46da5bbfd6cd084)
BOT_TOKEN = getenv("BOT_TOKEN", 7007274501:AAHW5CEqzPmyl3M68PUfzLXKdR5X79xJGiI)
STRING_SESSION = getenv("STRING_SESSION", BQC6kfsAu4aUowiDGJqSDzOlLnVhvrWyw4rFOHHjstWzTG-E6l7Wl-rwdZ8Ti6mEQdnaHtdPT3iGg--JuoZevxY2BLRmsQjzQ6jquCB5NgbTjqLK2a1Bv9Q91nR5mQxAqxiweNM8-Uo1sFMamceJFMn3WU1QAH7trFN8Hk3Qqto3-D4iBv24FibdkovFhcklgLfchq4C7KzfF-IejXawoJZ_FOxESNkpVwtAt8BuoY5fLVa468CQJd1C5v6yUcbp4XM0YP7H29jnHQtIsjPxVOgLHeRQOe9iyO6RdI4DBd7XHH5rEdP1HxtCGSAJdDtiS-o_YqxpcBs8EBMtHVYyxwG-QrjRmgAAAAE6CvCVAA)
MONGO_DB_URL = getenv("MONGO_DB_URL", mongodb+srv://BrandedSupportGroup:BRANDED_WORLD@cluster0.v4odcq9.mongodb.net/?retryWrites=true&w=majority)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", -1001968517603))


# OPTIONAL VARIABLES
SESSION_STRING = getenv("SESSION_STRING", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())



# OTHERS VARIABLES

# PM GUARD VARS
PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**🥀 In the silence of my inbox, your words echo loud and clear......if you are a spamer......Your spammy messages won't hit the right chord, so kindly hit the 'unsend' button, if you could afford.....if facing any problem with the bot just try /reboot.......if the problem continues please drop your group link owner.....we will fix it in under 10 min.....thanks for contacting frozen owner....we value your each and every responce**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 5))



# USERBOT DEFAULT IMAGE
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://te.legra.ph/file/11cfa74175b590014bd16.jpg")



# Don't Edit This Codes From This Line

LOGGER = logging.getLogger("Branded")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

