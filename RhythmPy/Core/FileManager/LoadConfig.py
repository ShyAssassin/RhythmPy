import json


def LoadConfig(File):
    """Used for loading a config file as json"""
    ConfigFile = File
    ConfigOpen = open(ConfigFile, "r")
    Config = json.loads(ConfigOpen.read())
    return Config
