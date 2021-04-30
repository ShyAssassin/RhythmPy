from Core import FileManager
from Core.Bot.Mania4k import Mania4k
from Core.Bot.Mania7k import Mania7k


class Bot:
    def Start(Running, ConfigFile):
        global Mode
        Config = FileManager.LoadConfig(ConfigFile)
        # starts Bot based on Mode found in config
        if Config["Mode"] in ["4k"]:
            Mode = Mania4k()
        elif Config["Mode"] in ["7k"]:
            Mode = Mania7k()
        # starts Bot
        Mode.Start(Config=ConfigFile, Running=Running)

    def Stop():
        Mode.Stop()
