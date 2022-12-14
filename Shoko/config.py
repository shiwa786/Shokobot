if __name__.endswith("sample_config"):
    import sys

    print(
        "The README is there to be read. Extend this sample config to a config file, don't just rename and change "
        "values here. Doing that WILL backfire on you.\nBot quitting.",
        file=sys.stderr,
    )
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    BOT_TOKEN = "5643681960:AAHwNOqT9DFsxYDvCudTe2IOAkwjA_RghQQ"
    OWNER_ID = (
        "5497627952"  # If you dont know, run the bot and do /id in your private chat with it
    )
    OWNER_USERNAME = "Denvil_xdd"
    TELETHON_HASH =  ' ' 
    TELETHON_ID = 123456

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://sllmmevjuasmdq:e5fb34859df15ca8765804b14fb18ef0a0049444b3c74c06e0caf504e4f6ff7f@ec2-44-209-24-62.compute-1.amazonaws.com:5432/dd3fq8ghhgvkbl"  # needed for any database modules
    REDIS_URI = "redis://ok:Da%4012345@redis-15098.c56.east-us.azure.cloud.redislabs.com:15098"
    MESSAGE_DUMP = -1001747540803  # needed to make sure 'save from' messages persist
    GBAN_DUMP = -1001747540803
    ERROR_DUMP = -1001747540803
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = (
        [1313665327, 1258544708, 1111332827, 1349105330, 680240877, 696086626, 604968079, 840545787, 1353333753, 239508098, 712008424]
    )  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = (
        [1222035687, 1100420431]
    )  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = (
        [1372739207]
    )  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WHITELIST_CHATS = []
    BLACKLIST_CHATS = []
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = None  
    ALLOW_EXCL = False  # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /
    CUSTOM_CMD = ('/', '!')   # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!
    API_OPENWEATHER = None  # OpenWeather API
    SPAMWATCH_API = '2UDxXat2dat_WIfbveq0nIqcw~g2sXVhXsZ5UpNdIWfVCSpECik_g1KsKGhEExl9' # Your SpamWatch token
    
    
class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True


