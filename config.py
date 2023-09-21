from os import getenv
import os
from dotenv import load_dotenv

# For Local Deploy
if os.path.exists("Internal"):
    load_dotenv("Internal")

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN", "6357692315:AAHZnwh4gYzMmS7Cp7oV3n6ECosvMRzPggg")
API_ID =  "9181844"
API_HASH = "996a3e7194a4f07576fda5c20bb1138b"
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

if str(getenv("SUPPORT_CHANNEL", "bot_testing_groups")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP", "bot_testing_groups")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))


if str(getenv("STRING_SESSION1", "BQBEAli_yvsxp3OpmyQ9Pf6KcahS-fOwwON-uoXzarv2xW8bJtevc-QBdfmL08oa0uVFAns8cURI60d-fXyvH8kFluoT7xt8bj3ht7waMB_cF8lSfcUGPWLyDuHP30zlkNyhKkBqhDTAtBeAie_1V0WAkkLqePtfzcL_RahAV4z5Qmg7W3XyN-eicf0SIA_hJbLYF5cQ2YKmLSCTpHZMWURugxTiknwZsfzKvADHp2vD_83w_Am-CugOJsOcdQDuvK_u_uRpZEy12j6gkxy37qjs0kyqin2vTbGUfHmoFZrhHbn3fGCwoPUJC4m-FCy-w8bRnTf50b4NNOqREs3lzJ3fAAAAATY1YRQA ")).strip() == "":
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
