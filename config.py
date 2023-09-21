from os import getenv
import os
from dotenv import load_dotenv

# For Local Deploy
if os.path.exists("Internal"):
    load_dotenv("Internal")

# VARS

get_queue = {}
BOT_TOKEN = 6357692315:AAFRnvdbQmjGSB6mL976V0A475-oWE6x-Lo
API_ID = 13098464
API_HASH = d57f367d43b812aea87fac24d7973356
DURATION_LIMIT_MIN = 100000000000
MONGO_DB_URI = mongodb+srv://monii:monii@cluster0.jdpdmrs.mongodb.net/?retryWrites=true&w=majority
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1318610382").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "6649395836").split()))
LOG_GROUP_ID = -1001836126687
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Bniex")


UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/mukeshmoni/testings"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

if str(getenv("SUPPORT_CHANNEL", "TEAM_VAMPIR")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP", "mirrormusic_support")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))


if str(getenv("STRING_SESSION1", "BQAzQs1VIQIfd8emNUyeCye98IEcgNOgYwYC1ZVE3ST4JeqjBoWvnAZ-6-_jbAm3OOVKy7SeJ6YFmGqUAft0RvmILZF9E4XL58HpmgkxM4ToXC9WwcT5VNZ-sU9bWGlsjYkqnMxgDybLzLUOWUj9UiNCL1izUna4Mq_D-g9WWOIoeHCv4Ubj8RutjkNuO60Pz98CLWUZ6Sp7-SGs7Grcaq4IuM8PrxpBEU-a8YNJIaJNhdY56jQwtlSxKwp_hUkZ-dpkzcOrHIeXodXvdFVYuEpG6mNK3SYfBI-H3hzKvRZqyihdA-W9wTNln-0RuqZobmaNKS4DJBomhaYonHPfgNeAAAAAAYxVunwA"
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
    LOG_SESSION = 1001668749714
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
