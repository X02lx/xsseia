## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgAXI5Y4MgdoA3wAvhVIIOsFNrqXOLfVsMBFaJEcinTuXwQlCYSpOlxKo0_yyEnmWFOMxcFWCDFuFB9UScHQttEfL9n3EVpyF77BCQCY2XQ2yN-EDCXJdNW4wv2oLdCs64pVjj_iokX0aX95pbqvQmOsSWmySiJJLjy_Ni2KnCUPfX9wSIoi7mmG7exqqSCFY_yr2tOPvrFjf5bKaaq-ZyXkfA05-rEPiE6VZGI3v7tgraad1YRHDYYum7qPk0tpQA2CtZ7ZbGwBZDjPmsVLw93YNlMyPOsLaDq1srALh2u3mFaAj8Fte3IAIiqtIMUDzHdNOZA3bPMRL4zwJnBRKzM5T68V6QA")
BOT_TOKEN = getenv("BOT_TOKEN", "5518255795:AAESEWphEzbr5kQvPhAkgvYwKmKjd1F1pmc")
BOT_NAME = getenv("BOT_NAME", "mocisBot")
API_ID = int(getenv("API_ID", "12446572"))
API_HASH = getenv("API_HASH", "3f0e31008feac76b18b24d4a123868a1")
OWNER_NAME = getenv("OWNER_NAME", "seno")
OWNER_USERNAME = getenv("OWNER_USERNAME", "G9_99")
ALIVE_NAME = getenv("ALIVE_NAME", "seno")
BOT_USERNAME = getenv("BOT_USERNAME", "xdani")
OWNER_ID = getenv("OWNER_ID", "1336874473")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "H69RG")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "xdani")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xdani")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1336874473").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
