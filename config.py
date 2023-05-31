from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "5096539"))
API_HASH = getenv("API_HASH", "79ead8d0295d53a71e5deeac24eda432")
BOT_TOKEN = getenv("BOT_TOKEN","6182618737:AAG30pcu7jcrQEnNszes4L65Y-x2J7BOtEQ")
BOT_NAME = getenv("BOT_NAME","Python Code Executor")
SESSION_NAME = getenv("SESSION_NAME", "BQBNxFsAvGpfjUQ4i6IkKK-rL4T050f7tLbpGT8NUiribDXYSY5UVgHDucU8G2FajJRrsZE_tfXMOfxDkcxLu5sEVfemv69CFDaAEj2eNip5s0ar4cwfIxT0QBXxmajPXeRebsuwdouqHo3df0if0RAoNsK6Hh7aLfr9bvyjjW00EwX1RtxtOdLvgEV8PbtbuBkxKIToBtkDJvl8KZ36Yz4OaUy3Z8D6PLAahU4kn-JhjZ0ashFCfAocG5KnBye35zSmQ5q3-5LkB80nYbnhrjnIMjHalmysRSKGB_wE91Phw2sBr7ePRciLrRERd8EuoiOX2XYWWOhtsQ12peHvbTpXrhBSUAAAAAFwg0ZxAQ")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ .").split())
