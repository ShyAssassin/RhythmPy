try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import json
import logging
import shutil


# updates config with latest valuse when there is a update
class UpdateConfig:
    def __init__(self, DefualtConfig):
        # gets logger
        self.logger = logging.getLogger(__name__)
        # sets logger level
        self.logger.setLevel(logging.DEBUG)
        # define file handler and set formatter
        self.LoggingFile = logging.FileHandler("app.log")
        self.Formatter = logging.Formatter(
            "%(name)s, %(lineno)d || %(asctime)s :: %(levelname)s :: %(message)s"
        )
        self.LoggingFile.setFormatter(self.Formatter)
        # add file handler to logger
        self.logger.addHandler(self.LoggingFile)
        # takes in defualt config so we can check for missing keys
        self.DefualtConfig = DefualtConfig

    # creates a copy of the Config as `Config_Old`
    def CreateCopy(self):
        shutil.copyfile("Config.json", "Config_Old.json")
        print("created copy of config saved as Config_Old")
        self.logger.info("created copy of Config saved as Config_Old")

    def Run(self):
        self.CreateCopy()
