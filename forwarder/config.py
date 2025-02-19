# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    REMOVE_TAG = True

    # REQUIRED
    API_KEY = "6259728425:AAHfgczSRmeyYqxF_nWzVBC3_2YUkiwTiqU"  # API key obtained from BotFather
    OWNER_ID = "5793708681"  # If you dont know, run the bot and do /id in your private chat with the bot

    # FOR AUTOMATICALLY FORWARDING MESSAGES
    FROM_CHATS = [-1001840288438]  # List of chat id's to forward messages from
    TO_CHATS = [-1001607602953]  # List of chat id's to forward messages to

    # FOR WEBHOOKS
    WEBHOOK = False
    IP_ADDRESS = "127.0.0.1"  # Use "0.0.0.0" if using Heroku
    URL = None  # The URL that the bot should listen to for updates
    PORT = 5000  # Port to listen on for webhooks
    CERT_PATH = None  # Path to certificate file

    WORKERS = 4  # Depends on usage, 4 by default


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
