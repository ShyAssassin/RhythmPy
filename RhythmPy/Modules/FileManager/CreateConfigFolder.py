from os import path
import sys
import os

try:
    from Paths import AppDataDir, AppDataConfigDir
    from Logger import Logger
except ImportError:
    from .Paths import AppDataDir, AppDataConfigDir
    from .Logger import Logger

# Creates Config Folder
def CreateConfigFolder():
    logger = Logger()
    logger = logger.StartLogger(name=__name__)
    if path.exists(AppDataConfigDir) == False:
        logger.warning("Config Folder missing, creating now")
        try:
            os.mkdir(AppDataConfigDir)
            logger.info("Created config dir")
        except Exception as e:
            print(e)
            logger.exception("could not create Config dir\n")
            sys.exit()
