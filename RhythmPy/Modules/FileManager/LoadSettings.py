import json
import os

try:
    from Paths import AppDataDir, AppDataConfigDir
except ImportError:
    from .Paths import AppDataDir, AppDataConfigDir

# used for loading Config\Settings.json
def LoadSettings():
    """
    Used for Loading application settings
    """
    appdataConfig = AppDataConfigDir
    SettingsFile = appdataConfig + "Settings.json"
    SettingsOpen = open(SettingsFile, "r")
    Settings = json.loads(SettingsOpen.read())
    return Settings
