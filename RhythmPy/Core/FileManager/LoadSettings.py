import json
from .Paths import AppDataDir


# used for loading Config\Settings.json
def LoadSettings():
    """Used for Loading application settings"""
    appdataConfig = AppDataDir()
    SettingsFile = appdataConfig + "Settings.json"
    SettingsOpen = open(SettingsFile, "r")
    Settings = json.loads(SettingsOpen.read())
    return Settings
