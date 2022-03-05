import os


class Config:
    API_ID = int(os.environ.get("API_ID", 13554562))  # Change 12345 to your API_ID
    API_HASH = os.environ.get("API_HASH", f018746a92d8e774664bebfb6f28abe5)  # Change None to your API_HASH
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 5287010059:AAG_CKIHbIuo7xwg1Rq6K1QAO30koMqcYOo)  # Change None to your BOT_TOKEN
    OWNER_ID = int(os.environ.get("OWNER_ID", 853523454))  # Change 0 to your OWNER_ID
    OWNER_NAME = os.environ.get("OWNER_NAME", Geralt)  # Change None to your OWNER_NAME

    # For Local Deploys edit above 5 lines.
    # Put your API_ID and OWNER_ID (without comma) and API_HASH,BOT_TOKEN n OWNER_NAME (with commas) below.
    # If got any problem ask in @MysteryBotsChat.
