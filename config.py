from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "5096539"))
API_HASH = getenv("API_HASH", "79ead8d0295d53a71e5deeac24eda432")
BOT_TOKEN = getenv("BOT_TOKEN","6182618737:AAG30pcu7jcrQEnNszes4L65Y-x2J7BOtEQ")
BOT_NAME = getenv("BOT_NAME","Python Code Executor")
SESSION_NAME = getenv("SESSION_NAME", "")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ .").split())
