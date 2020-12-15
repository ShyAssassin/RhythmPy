import logging
import sys

class Logger:
    def StartLogger(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        # define file handler and set formatter
        self.LoggingFile = logging.FileHandler('app.log')
        self.Formatter = logging.Formatter('%(name)s, %(lineno)d || %(asctime)s :: %(levelname)s :: %(message)s')
        self.LoggingFile.setFormatter(self.Formatter)
        # add file handler to logger
        self.consoleHandler = logging.StreamHandler(sys.stdout)
        self.consoleHandler.setFormatter(self.LoggingFile)
        # i have sat here for the last hour trying to figure out what this does
        # i have not a single god damn clue but without it the logger wont output to sdout
        self.logger.addHandler(self.consoleHandler)
        self.logger.addHandler(self.LoggingFile)
        return self.logger