from os import path
import json
import sys
import os
import traceback

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
class FileManager:
    def __init__(self):
        # starts logger
        logger = Logger()
        self.logger = logger.StartLogger(name=__name__)
        self.appdata = str(os.path.expandvars("%appdata%//RhythmPy//"))
        self.appdataConfig = str(os.path.expandvars("%appdata%//RhythmPy//Config//"))

    # Creates Config Folder
    def CreateConfigFolder(self):
        if path.exists(self.appdata + 'Config') == False:
            self.logger.warning('Config Folder missing, creating now')
            try:
                os.mkdir(self.appdata + 'Config')
                self.logger.info('Created config dir')
            except Exception:
                self.logger.exception('could not create Config dir\n')
                CloseGlobal(master=None, running=None)

    # Creates Config Files
    def CreateConfigFiles(self):
        # writes settings
        if path.exists(self.appdataConfig + "Settings.json") == False:
            try:
                with open(self.appdataConfig + "Settings.json", "w+") as json_file:
                    json.dump(Defualt_Settings, json_file, indent=4)
                    self.logger.info('created Settings.json')
            except Exception:
                self.logger.exception('Failed to create Settings.json\n')
                CloseGlobal(master=None, running=None)

        # writes defualt Osu config
        if path.exists(self.appdataConfig + "Osu4K.json") == False:
            try:
                with open(self.appdataConfig + "Osu4K.json", "w+") as json_file:
                    json.dump(Defualt_Config_Osu4K, json_file, indent=4)
                    self.logger.info('created Osu4K.json')
            except Exception:
                self.logger.exception('Failded to create Osu4K.jso\n')
                CloseGlobal(master=None, running=None)

        # writes defualt quaver config
        if path.exists(self.appdataConfig + "Quaver4K.json") == False:
            try:
                with open(self.appdataConfig + "Quaver4K.json", "w+") as json_file:
                    json.dump(Defualt_Config_Quaver4K, json_file, indent=4)
                    self.logger.info('created Quaver4K.json')
            except Exception:
                self.logger.exception('Failed to create Quaver4K.json')
                CloseGlobal(master=None, running=None)

    # used for loading Config\Settings.json
    def LoadSettings(self):
        self.SettingsFile = self.appdataConfig + "Settings.json"
        self.SettingsOpen = open(self.SettingsFile, "r")
        self.Settings = json.loads(self.SettingsOpen.read())
        return self.Settings

    def LoadConfig(self, File):
        ConfigFile = File
        ConfigOpen = open(ConfigFile, "r")
        Config = json.loads(ConfigOpen.read())
        return Config
