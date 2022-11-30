import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "21648470"))
    API_HASH = os.environ.get("API_HASH", "d2489056db8f2bd3bf0ad5ab863367bc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5801929271:AAEFz9ChB9z5cqb2N0mHSiGqm8BSm5uoKcw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBu54Wm_FZNXEuUZjn5aJGQooTlgf6Q1iDRdNdNqdxHcZRqWSwllEkzyjH0R2hWGNj8klCnIdcWsSRYbDv518UTCSi28aJ_8v4xvWPg2ZV_cwj99qzPxcPLEKw3DkQ1vBpQLqy_aBXcvdt0Jp-iUebZF5hOyiShaUEuMIom5CXVC4foNPJLgFlto9w4WE_4GKAN0SjbFjIPd7FDU914fKEDWzItU96qeZnpfOzSmhwDozfg-EtkY2Xw404l6HOKo3q_yr1Nbz0b6wueWa2UTaqc3n0rVU--ve4FhzP4C5BsQE1SGDInIQfLoO5KQdcm0_dDygds-Sf6EiT7ea8SCBdC2A=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "jusvc_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5435883609")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
