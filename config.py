from os import getenv
import os
from dotenv import load_dotenv

# For Local Deploy
if os.path.exists("Internal"):
    load_dotenv("Internal")

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN", "6357692315:AAHZnwh4gYzMmS7Cp7oV3n6ECosvMRzPggg")
API_ID =  "15883181"
API_HASH = "093e1723084f836d8399bdbdd9ef536f"
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "90000"))
MONGO_DB_URI = "MONGO_DB_URI", "mongodb+srv://moniabi:moniabi@cluster0.oikiuo4.mongodb.net/?retryWrites=true&w=majority"
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5444362033").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "6649395836").split()))
LOG_GROUP_ID = "-1001668749714"
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "testing bot")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "e30bcc5c-4ce0-4e24-b341-d75dbce9d35c")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "moni")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/mukeshmoni/testing"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

if str(getenv("SUPPORT_CHANNEL", "Sad_shayari_lovers")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP", "bot_testing_groups")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))


if str(getenv("STRING_SESSION1", "BQDMM2QANeTRB7nHOa7amMW4xk0pM3jRKEBTB1eybXY96c3gNEvYdC8WvrCGbv1XHav8v6cHSNoM-o3wXl1xaNLQP440CkG3HAtTwbD7kG74oTZ4YWvt-LLUpgxsS58V2Kgl7mt-zJAtY-Rtmm2KPjbADHxqN7DVYfAw7o8_38eULFh2A2b-oLKkZO3LZYzCSGr7pWHxpsCQP7YW9Ecrp4ISqhEkSvyp1K-yiiKB8C4Wjj5i2hbBWkwDTBLTw3i_b-pY9yngveHkxUQaB9QSkzkrBXrnBmn3mPZ4BtYn8LRflfg49fmgxosuxi54VgL-YqHb11IdnKQ0AmfxG50wu_BV-692lAAAAAGMVbp8AA")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
