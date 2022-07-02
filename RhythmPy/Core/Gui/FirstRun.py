import json
import webbrowser
from Core.FileManager import AppDataDir
from Core.Logger import Logger
import tkinter as tk
from tkinter import messagebox


class FirstRun:
    def __init__(self):
        logger = Logger()
        self.logger = logger.StartLogger(name=__name__)
        self.appdataConfig = AppDataDir()
        self.ConfigFile = self.appdataConfig + "Settings.json"
        self.ConfigOpen = open(self.ConfigFile, "r")
        self.Config = json.loads(self.ConfigOpen.read())

    def Notify(self):
        # we need to create a window to show a messagebox
        window = tk.Tk()
        window.withdraw()
        messagebox.showwarning(
            "READ THE DOCS!",
            "Please take some time to read the setup guide before complaining!",
        )
        window.destroy()

    def Run(self):
        try:
            if self.Config["FirstRun"] in [True, "True", "true"]:
                self.logger.info("First time running!")
                # changes the values so it can later be dumped into file
                self.Config["FirstRun"] = "False"
                with open(self.ConfigFile, "w") as file:
                    json.dump(self.Config, file, indent=4)
                self.Notify()
                webbrowser.open_new(
                    "https://github.com/assassinsorrow/RhythmPy/blob/master/README.md"
                )
        except Exception:
            self.logger.warning("FirstRun is missing. Config file might be corrupted")
