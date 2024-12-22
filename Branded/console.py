import os
import time
import logging
from logging.handlers import RotatingFileHandler

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
API_ID = os.getenv("API_ID", "0")  # Default to "0" if not provided
API_HASH = os.getenv("API_HASH", "")
STRING_SESSION = os.getenv("SESSION_STRING", "")  # Alias for compatibility
COMMAND_PREFIXES = list(os.getenv("COMMAND_PREFIXES", ". !").split())

# Optional PM Guard variables
PM_GUARD = bool(os.getenv("PM_GUARD", True))
PM_GUARD_TEXT = os.getenv("PM_GUARD_TEXT", "Default PM Guard Text")
PM_GUARD_LIMIT = int(os.getenv("PM_GUARD_LIMIT", 5))

# Userbot default image
USERBOT_PICTURE = os.getenv("USERBOT_PICTURE", "https://telegra.ph/file/8c81173143a4923516c18.jpg")

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
COMMAND_HANDLERS.append('.')
