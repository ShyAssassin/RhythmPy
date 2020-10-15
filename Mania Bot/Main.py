import json
import src
import logging
import os.path
from os import path

Defualt_Config = {
    "Version": "",
    "Osu4K":{
        "Window Name": "",
        "Collum1Pos": "",
        "Collum2Pos": "",
        "Collum3Pos": "",
        "Collum4Pos": ""
    },
    "Quaver4K":{
        "Window Name": "", 
        "Collum1Pos": "",
        "Collum2Pos": "",
        "Collum3Pos": "",
        "Collum4Pos": ""
    }
}

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

        with open('Config.json', 'w+') as json_file:
            json.dump(Defualt_Config, json_file, indent=4)
        logger.info('defualt config writen to file') 

    else:
        logger.info('started')

    game = input("Osu or Quaver")

    if game in ("osu", "OSU", "Osu"):
        if input('4K or 7k') in ("4k", "4K"):
            pass
        else:
            pass


if __name__ == "__main__":
    Main()

