import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
CHANNEL_ID = os.getenv("CHANNEL_ID")
TARGET_CHANNEL_ID = os.getenv("TARGET_CHANNEL_ID")
TURN_ON_KEYWORD = os.getenv("TURN_ON", "").casefold()
TURN_OFF_KEYWORD = os.getenv("TURN_OFF", "").casefold()

if not all([API_ID, API_HASH, CHANNEL_ID, TARGET_CHANNEL_ID]):
    raise ValueError(
        "Необходимо указать API_ID, API_HASH, CHANNEL_ID, TARGET_CHANNEL_ID в .env файле"
    )
