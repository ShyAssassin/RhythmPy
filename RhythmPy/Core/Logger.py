import logging
import sys
import os
from os import path
from datetime import date
from .FileManager import Paths


class Logger:
    def CreateLogFolder(self):
        if path.exists(Paths.AppDataLogsDir()) == False:
            os.mkdir(Paths.AppDataLogsDir())

    def StartLogger(self, name):
        self.appdatapath = Paths.AppDataLogsDir()

        # gets current date
        self.CurrentDate = str(date.today())
        self.LogFile = str(self.appdatapath + self.CurrentDate + ".log")

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # define file handler and set formatter
        self.LoggingFile = logging.FileHandler(self.LogFile)
        self.Formatter = logging.Formatter(
            "%(name)s, %(funcName)s(), %(lineno)d, || %(asctime)s :: %(levelname)s :: %(message)s"
        )
        self.LoggingFile.setFormatter(self.Formatter)
        # add file handler to logger
        self.consoleHandler = logging.StreamHandler(sys.stdout)
        self.consoleHandler.setFormatter(self.LoggingFile)
        # i have sat here for the last hour trying to figure out what this does
        # i have not a single god damn clue but without it the logger wont output to sdout
        self.logger.addHandler(self.consoleHandler)
        self.logger.addHandler(self.LoggingFile)
        return self.logger

    def GetCurrentLogFile(self):
        return self.LogFile
