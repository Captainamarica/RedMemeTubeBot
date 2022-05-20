import os

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

class var:
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # from @botfather
    API_ID = int(os.getenv("API_ID"))  # from https://my.telegram.org/apps
    API_HASH = os.getenv("API_HASH")  # from https://my.telegram.org/apps
    START_MESSAGE = os.getenv("START_MESSAGE", None)  # Not Mandatory
    OWNER_ID = os.getenv("OWNER_ID", None)
    REDIS_URI = os.getenv("REDIS_URI", None)
    REDIS_PASS = os.getenv("REDIS_PASS", None)
    FSUB = os.getenv("FSUB", None)
    START_STICKER_ID = os.getenv("START_STICKER_ID", None)
    ADMIN_GROUP_ID = os.getenv("ADMIN_GROUP_ID", None)
    MAIN_CHAN_ID = os.getenv("MAIN_CHAN_ID", None)
