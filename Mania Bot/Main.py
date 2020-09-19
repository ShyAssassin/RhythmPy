import json
import library
import threading
import logging
import os.path
from os import path

def Main():
    # Gets or creates a logger
    logger = logging.getLogger(__name__)

    # set log level  
    logger.setLevel(logging.WARNING)

    # define file handler and set formatter
    LoggingFile = logging.FileHandler('app.log')
    formatter = logging.Formatter('%(name)s || %(asctime)s :: %(levelname)s :: %(message)s')
    LoggingFile.setFormatter(formatter)

    # add file handler to logger
    logger.addHandler(LoggingFile)

    logger.info("Started")
    ###########################################

    # checks if config file exists
    if path.exists('Config.json') == False:
        print('Config file is missing')
        logger.warning('Config file missing, creating now')
        open("Config.json", "w+") 
       # writes defualt Config to file
       
    else:
        logger.info('started')

    game = input()


if __name__ == "__main__":
    Main()