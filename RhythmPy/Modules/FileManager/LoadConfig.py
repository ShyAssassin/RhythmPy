import json


def LoadConfig(self, File):
    ConfigFile = File
    ConfigOpen = open(ConfigFile, "r")
    Config = json.loads(ConfigOpen.read())
    return Config
