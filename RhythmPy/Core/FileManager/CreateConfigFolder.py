from os import path
import sys
import os
from .Paths import AppDataConfigDir
from .FmLogger import Logger


# Creates Config Folder!
def CreateConfigFolder():
    """Creates folder that holds configs in (%appdata%//RhythmPy//Config//) or (~//RhythmPy//Config//)"""
    logger = Logger()
    logger = logger.StartLogger(name=__name__)
    if path.exists(AppDataConfigDir()) == False:
        logger.warning("Config Folder missing, creating now")
        try:
            os.mkdir(AppDataConfigDir())
            logger.info("Created config dir")
        except Exception as e:
            print(e)
            logger.exception("could not create Config dir\n")
            sys.exit()
