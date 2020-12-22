from os import path
import logging
import json
import webbrowser
import sys

try:
    from .Logger import Logger
except ImportError:
    from Logger import Logger

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk
    from Tkinter import messagebox

try:
    from .Logger import Logger
except ImportError:
    from Logger import Logger

class FirstRun:
    def __init__(self):
        logger = Logger()
        self.logger = logger.StartLogger(name=__name__)

        self.ConfigFile = r"Config\Settings.json"
        self.ConfigOpen = open(self.ConfigFile, "r")
        self.Config = json.loads(self.ConfigOpen.read())

    def Notify(self):
        wins = tk.Tk()
        wins.withdraw()
        messagebox.showwarning('READ THE DOCS!', "Please take some time to read the setup guide before complaining")
        wins.destroy()
        

    def Warn(self):
        winss = tk.Tk()
        winss.withdraw()
        messagebox.showwarning('Warning', "First Run is missing from config\nPlease update your config file")
        winss.destroy()

    # reads Value
    def ReadValue(self):
        Value = self.Config["FirstRun"]        
        if Value == True or Value == 'True' or Value == 'true':
            return True
        else:
            return False

    def Run(self):
        try:
            if self.ReadValue():
                self.logger.info('First time running!')
                # changes the values so it can later be dumped into file
                self.Config["FirstRun"] = "False"
                with open(self.ConfigFile, "w") as file:
                    json.dump(self.Config, file, indent=4)
                self.Notify()
                webbrowser.open_new('https://github.com/assassinsorrow/RhythmPy/blob/master/README.md')
            else:
                self.logger.info('has been run before carrying on')
        except:
            self.logger.warning('FirstRun is missing from config user may be using a old config')
            self.Warn()


if __name__ == "__main__":
    FirstRun().Run()


