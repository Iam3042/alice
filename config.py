import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 22736752
API_HASH = "274dcb8d3faf32bc3390886f18642df5"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7678366178:AAEFPBH8kAiUyMrNbaLi1P0oYLv9HPiu8oc"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://himanshukumar30426@cluster0.gggbet1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002564548018

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7846862619

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/SnarkSanctum"
SUPPORT_GROUP = "https://t.me/SnarkSanctum"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQFa73AAjet9rLGCyudz3zKtoS-CeOItDJhqAeHLbruDHFqCIyxOtelmGyUha0HFfEhG0EVc7h-xzPbadUxzDPHtYca0zvyArYgPM99_6cSeRu8m25kSZB9ifXVkWlaytn70ZbtVZxNS4zfgPsQAd5GHw1oJZbEpCX9HalyBCjj6FHbJ_npx0qjfego3_d4qCZjC0fopO2AD7LAYYoYNA3hoJyZU2aKyGB6VZwNjUE99e-Nbq0SsgjPhfd6BeoLmMNTIOUepxeGaz7M7VAzfJ8_Z1ccc57AIomD_PdQpRDo15dO-0BQbCcpVNM7Nrn9HKieTWA6bZBrkKdgmBtjTkK7Ahi8QSAAAAAHTtZ8bAASzXg5KEP4hVuifwXM47KCOzcppKryW3rajlIW0bxCjI3pHQAUsJTxQZbCLnkWOzvx6mckdU2--eibmVq_5LauQVIBBZlB3KRQAAAAGpg2YNAA"
STRING2 = getenv("BQFa73AAjet9rLGCyudz3zKtoS-CeOItDJhqAeHLbruDHFqCIyxOtelmGyUha0HFfEhG0EVc7h-xzPbadUxzDPHtYca0zvyArYgPM99_6cSeRu8m25kSZB9ifXVkWlaytn70ZbtVZxNS4zfgPsQAd5GHw1oJZbEpCX9HalyBCjj6FHbJ_npx0qjfego3_d4qCZjC0fopO2AD7LAYYoYNA3hoJyZU2aKyGB6VZwNjUE99e-Nbq0SsgjPhfd6BeoLmMNTIOUepxeGaz7M7VAzfJ8_Z1ccc57AIomD_PdQpRDo15dO-0BQbCcpVNM7Nrn9HKieTWA6bZBrkKdgmBtjTkK7Ahi8QSAAAAAHTtZ8bAA", None)
STRING3 = getenv("BQFa73AAjet9rLGCyudz3zKtoS-CeOItDJhqAeHLbruDHFqCIyxOtelmGyUha0HFfEhG0EVc7h-xzPbadUxzDPHtYca0zvyArYgPM99_6cSeRu8m25kSZB9ifXVkWlaytn70ZbtVZxNS4zfgPsQAd5GHw1oJZbEpCX9HalyBCjj6FHbJ_npx0qjfego3_d4qCZjC0fopO2AD7LAYYoYNA3hoJyZU2aKyGB6VZwNjUE99e-Nbq0SsgjPhfd6BeoLmMNTIOUepxeGaz7M7VAzfJ8_Z1ccc57AIomD_PdQpRDo15dO-0BQbCcpVNM7Nrn9HKieTWA6bZBrkKdgmBtjTkK7Ahi8QSAAAAAHTtZ8bAA", None)
STRING4 = getenv("BQFa73AAjet9rLGCyudz3zKtoS-CeOItDJhqAeHLbruDHFqCIyxOtelmGyUha0HFfEhG0EVc7h-xzPbadUxzDPHtYca0zvyArYgPM99_6cSeRu8m25kSZB9ifXVkWlaytn70ZbtVZxNS4zfgPsQAd5GHw1oJZbEpCX9HalyBCjj6FHbJ_npx0qjfego3_d4qCZjC0fopO2AD7LAYYoYNA3hoJyZU2aKyGB6VZwNjUE99e-Nbq0SsgjPhfd6BeoLmMNTIOUepxeGaz7M7VAzfJ8_Z1ccc57AIomD_PdQpRDo15dO-0BQbCcpVNM7Nrn9HKieTWA6bZBrkKdgmBtjTkK7Ahi8QSAAAAAHTtZ8bAA", None)
STRING5 = getenv("BQFa73AAjet9rLGCyudz3zKtoS-CeOItDJhqAeHLbruDHFqCIyxOtelmGyUha0HFfEhG0EVc7h-xzPbadUxzDPHtYca0zvyArYgPM99_6cSeRu8m25kSZB9ifXVkWlaytn70ZbtVZxNS4zfgPsQAd5GHw1oJZbEpCX9HalyBCjj6FHbJ_npx0qjfego3_d4qCZjC0fopO2AD7LAYYoYNA3hoJyZU2aKyGB6VZwNjUE99e-Nbq0SsgjPhfd6BeoLmMNTIOUepxeGaz7M7VAzfJ8_Z1ccc57AIomD_PdQpRDo15dO-0BQbCcpVNM7Nrn9HKieTWA6bZBrkKdgmBtjTkK7Ahi8QSAAAAAHTtZ8bAA", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/958070df4bff4ccc1e624-8071717ec7f1efb828.jpg"

PING_IMG_URL = "https://graph.org/file/958070df4bff4ccc1e624-8071717ec7f1efb828.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/958070df4bff4ccc1e624-8071717ec7f1efb828.jpg"
STATS_IMG_URL = "https://graph.org/file/958070df4bff4ccc1e624-8071717ec7f1efb828.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/958070df4bff4ccc1e624-8071717ec7f1efb828.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/958070df4bff4ccc1e624-8071717ec7f1efb828.jpg"
STREAM_IMG_URL = "https://graph.org/file/958070df4bff4ccc1e624-8071717ec7f1efb828.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/958070df4bff4ccc1e624-8071717ec7f1efb828.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/b1ecc259bc1145717053f-71be50868489f04316.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/958070df4bff4ccc1e624-8071717ec7f1efb828.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/958070df4bff4ccc1e624-8071717ec7f1efb828.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/958070df4bff4ccc1e624-8071717ec7f1efb828.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
