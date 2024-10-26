import os
import time
import logging
from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

# Load environment variables from .env file if it exists
if os.path.exists("Internal"):
    load_dotenv("Internal")

# Configure logging
logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler("logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10),
        logging.StreamHandler(),
    ],
)

# Set logging levels for various libraries
logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)

# Environment variables
API_ID = int(getenv("API_ID", 29568441))
API_HASH = getenv("API_HASH", "b32ec0fb66d22da6f77d355fbace4f2a")
BOT_TOKEN = getenv("BOT_TOKEN", "8091193581:AAFDkfuXJ7mplRdrcxX7Td_022cfWRmzysU")
STRING_SESSION = getenv("STRING_SESSION", "BQHDLbkAJ8FiB01GNFdNmk0Awyx2TJoIdbEKPgjdoWUois9-Yh46SeWu5eXUYg_VASDdHD7G35891ZLiBx3nJKXGg454k2v4pRiuqweTEVHFpigjM8j0LqKv20LKLwypuROVISwO9KU5DAR1ERy9V1HyC75Q30TsOM8hUUSOveJD25IMdoSJx9NkHKi1fZxtMxXQ7P9-H8RWOa3Okob2yYafCEcnfLKXtE8lMwEeQiWwaoqnb5F2ZMEqQx9IViZHK69wkvSbs2_9St4LWNmHgCBeitCPjeSPE5T7BLTK3VqtDpoN9-gwcfltAhL_WaVc6fKay28z4vHuIIdAi0pR7kSP0irr9wAAAAGhyyf_AA")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://BrandedSupportGroup:BRANDED_WORLD@cluster0.v4odcq9.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", -1002488370988))

# Optional variables
SESSION_STRING = getenv("SESSION_STRING", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())

# PM Guard variables
PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "нєу 𝐹𝓇𝑜𝓏𝑒𝓃 𝒪𝒻𝒻𝒾𝒸𝒾𝒶𝓁, 🥀\n\n๏ ᴛʜɪs ɪs 🇫ʀᴏᴢᴇɴ ❄️ ᴍᴜsɪᴄ !\n\n➻ ᴀ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɡʀᴀᴍ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.\n\nSᴜᴘᴘᴏʀᴛᴇᴅ Pʟᴀᴛғᴏʀᴍs : ʏᴏᴜᴛᴜʙᴇ, sᴘᴏᴛɪғʀʏ, ʀᴇssᴏ, ᴀᴘᴘʟᴇ ᴍᴜsɪᴄ ᴀɴᴅ sᴏᴜɴᴅᴄʟᴏᴜᴅ.\n──────────────────\n๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 5))

# Userbot default image
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://telegra.ph/file/8c81173143a4923516c18.jpg")

# Don't Edit This Code From This Line
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
