from os import path
import logging
import json
import webbrowser
import sys
try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk
    from Tkinter import messagebox

class FirstRun:
    def __init__(self):
        # gets logger
        self.logger = logging.getLogger(__name__)
        # sets logger level
        self.logger.setLevel(logging.DEBUG)
        # define file handler and set formatter
        self.LoggingFile = logging.FileHandler('app.log')
        self.Formatter = logging.Formatter('%(name)s, %(lineno)d || %(asctime)s :: %(levelname)s :: %(message)s')
        self.LoggingFile.setFormatter(self.Formatter)
        # add file handler to logger
        self.logger.addHandler(self.LoggingFile)

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
                self.logger.info('First time running')
                print('Firstime Running!')
                # changes the values so it can later be dumped into file
                self.Config["FirstRun"] = "False"
                with open(self.ConfigFile, "w") as file:
                    json.dump(self.Config, file, indent=4)
                self.Notify()
                webbrowser.open_new('https://github.com/assassinsorrow/RhythmPy/blob/master/README.md')
            else:
                print('has been run before carrying on')
        except:
            print('FirstRun is missing from config user may be using a old config')
            self.logger.warning('FirstRun is missing from config user may be using a old config')
            self.Warn()


if __name__ == "__main__":
    FirstRun().Run()


