from os import path
import sys
import os
from .Paths import PluginsDir
from .FmLogger import Logger


# Creates Config Folder
def CreatePluginFolder():
    """Creates folder that will hold Plugins in (%appdata%//RhythmPy//Plugins//) or (~//RhythmPy//Plugins//)"""
    logger = Logger()
    logger = logger.StartLogger(name=__name__)
    if path.exists(str(PluginsDir())) == False:
        logger.warning("Plugins Folder missing, creating now")
        try:
            os.mkdir(str(PluginsDir()))
            logger.info("Created Plugins dir")
        except Exception as e:
            print(e)
            logger.exception("could not create Plugins dir\n")
            sys.exit()
