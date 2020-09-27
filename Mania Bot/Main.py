import json
import Bot
import threading
import logging
import os.path
from os import path
import multiprocessing

def Main():
    # Gets or creates a logger
    logger = logging.getLogger(__name__)

    # set log level  
    logger.setLevel(logging.DEBUG)

    # define file handler and set formatter
    LoggingFile = logging.FileHandler('app.log')
    formatter = logging.Formatter('%(name)s || %(asctime)s :: %(levelname)s :: %(message)s')
    LoggingFile.setFormatter(formatter)

    # add file handler to logger
    logger.addHandler(LoggingFile)

    ###########################################

    # checks if config file exists
    if path.exists('Config.json') == False:
        print('Config file is missing, creating now')
        logger.warning('Config file missing, creating now')
        open("Config.json", "w+")
       # writes defualt Config to file

        logger.info('defualt config writen to file') 

    else:
        logger.info('started')

    game = input("Osu or Quaver")

    if game in ("osu", "OSU", "Osu"):
        if input('4K or 7k') in ("4k", "4K"):
            Bot.Osu4kRun()
        else:
            Bot.Osu7kRun()


if __name__ == "__main__":
    Main()

