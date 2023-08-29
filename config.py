from os import getenv
import os
from dotenv import load_dotenv

# For Local Deploy
if os.path.exists("Internal"):
    load_dotenv("Internal")

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN", "6370320656:AAGJ4Qd0QmhxxJbPboPsX3xZs4PkOXYQ9CI")
API_ID = 9181844
API_HASH = getenv("API_HASH","996a3e7194a4f07576fda5c20bb1138b")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9000"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://mongodb1:mongodb1@cluster0.fhk9lze.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5444362033").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5444362033").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001836126687"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Bniex")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Sandy8752/SweetyMusicBot"
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


if str(getenv("STRING_SESSION1", "BQCaBZC2GkfQQf3m3UVBzffAG3HeXDoYC75CM7ZeiDd3jyAHIRyVQUO4syJfgeqPwkFcEgil54Z6JRC7moGG79DqP2KWABS-JRseQEsN-CHpZCxt1wCYasri9H18wOVAIe0Rh7WK-VTjn6uqkakgLCdVkGtoj25BVbyJA4HrkehDek9GSVYgm1IFx_4yUltdBJzyzcJT62k4evaBV2rlenTHF9pL4AUteyeOYFJF6gnn8YUWlzJSbcsGAnNKjgiT813RBY9-KHIZN_HVtZ21fVjtUmMJ9mR7zD6HesTwE4B_N4-Z916bFAjCLSgJxM6EigNyGOPly7hHTBbS0LDRigFIAAAAAVuZk5cA")).strip() == "":
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
