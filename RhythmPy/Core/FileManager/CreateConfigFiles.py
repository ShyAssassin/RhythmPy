from os import path
import json
import sys
from .Paths import AppDataDir, AppDataConfigDir
from .FmLogger import Logger
from .DefualtConfigs import (
    Defualt_Config_Osu4K,
    Defualt_Config_Quaver4K,
    Defualt_Settings,
)


# Creates Config Files
def CreateConfigFiles():
    """Creates Defualt configs for Osu Qauver and settings"""
    logger = Logger()
    logger = logger.StartLogger(name=__name__)
    # writes settings
    if path.exists(AppDataDir() + "Settings.json") == False:
        try:
            with open(AppDataDir() + "Settings.json", "w+") as json_file:
                json.dump(Defualt_Settings, json_file, indent=4)
                logger.info("created Settings.json")
        except Exception:
            logger.exception("Failed to create Settings.json\n")
            sys.exit()

    # writes defualt Osu config
    if path.exists(AppDataConfigDir() + "Osu4K.json") == False:
        try:
            with open(AppDataConfigDir() + "Osu4K.json", "w+") as json_file:
                json.dump(Defualt_Config_Osu4K, json_file, indent=4)
                logger.info("created Osu4K.json")
        except Exception:
            logger.exception("Failded to create Osu4K.json\n")
            sys.exit()

    # writes defualt quaver config
    if path.exists(AppDataConfigDir() + "Quaver4K.json") == False:
        try:
            with open(AppDataConfigDir() + "Quaver4K.json", "w+") as json_file:
                json.dump(Defualt_Config_Quaver4K, json_file, indent=4)
                logger.info("created Quaver4K.json")
        except Exception:
            logger.exception("Failed to create Quaver4K.json")
            sys.exit()
