from os import path
import json
import sys
import os

try:
    from .Logger import Logger
except ImportError:
    from Logger import Logger

try:
    from .CloseGlobal import CloseGlobal
except ImportError:
    from CloseGlobal import CloseGlobal

# needs to be updated when new key is used
Defualt_Config_Osu4K = {
    "Collums": "4",
    "Window Name": "",
    "Collum1Pos": "",
    "Collum2Pos": "",
    "Collum3Pos": "",
    "Collum4Pos": ""
}

Defualt_Config_Quaver4K = {
    "Collums": "4",
    "Window Name": "",
    "Collum1Pos": "",
    "Collum2Pos": "",
    "Collum3Pos": "",
    "Collum4Pos": ""
}

Defualt_Settings = {
    "Version": "1",
    "Debug": "False",
    "FirstRun": "True",
    "MultiConfig": "False",
    "FindRunningProcess": "True",
    "WindowDrag": "True"
}

# creates defualt config files
class Config:
    def __init__(self):
        # starts logger
        logger = Logger()
        self.logger = logger.StartLogger(name=__name__)

    # Creates Config Folder
    def CreateConfigFolder(self):
        if path.exists('Config') == False:
            self.logger.warning('Config Folder missing, creating now')
            try:
                os.mkdir('Config')
                self.logger.info('Created config dir')
            except:
                self.logger.critical('could not create Config dir')
                CloseGlobal(master=None)

    # Creates Config Files
    def CreateConfigFiles(self):
        # writes settings
        if path.exists(r"Config\Settings.json"):
            pass
        else:
            with open(r"Config\Settings.json", "w+") as json_file:
                json.dump(Defualt_Settings, json_file, indent=4)
                self.logger.info('created Settings.json')

        # writes defualt Osu config
        if path.exists(r"Config\Osu4K.json"):
            pass
        else:
            with open(r"Config\Osu4K.json", "w+") as json_file:
                json.dump(Defualt_Config_Osu4K, json_file, indent=4)
                self.logger.info('created Osu4K.json')

        # writes defualt quaver config
        if path.exists(r"Config\Quaver4K.json"):
            pass
        else:
            with open(r"Config\Quaver4K.json", "w+") as json_file:
                json.dump(Defualt_Config_Quaver4K, json_file, indent=4)
                self.logger.info('created Quaver4K.json')

    # used for loading Config\Settings.json
    def LoadSettings(self):
        self.SettingsFile = r"Config\Settings.json"
        self.SettingsOpen = open(self.SettingsFile, "r")
        self.Settings = json.loads(self.SettingsOpen.read())
        return self.Settings

    def LoadConfig(self, File):
        ConfigFile = File
        ConfigOpen = open(ConfigFile, "r")
        Config = json.loads(ConfigOpen.read())
        return Config
