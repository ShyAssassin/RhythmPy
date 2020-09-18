import json
import library
import threading
import logging
import os.path
from os import path

##########################################
#                                       #       
#                 Logging               #
#                                       #
#########################################

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

###########################################

# checks if config file exists
if path.exists('Config.json') == False:
    print('Config file is missing')
    logger.warning('Config file missing, creating now')
    ConfigCreate  = open("Config.json", "w+") 
else:
    logger.info('Main started')


Game = input('osu or Quaver \n')
if Game == 'osu':
    Mode = input('4k or 7k \n')
    if Mode in ('4k', '4K', '4'):
        # runs 4k
        print('4k has been selected \n')
        
    else:
        # runs 7k
        print('7k has been selected \n')\
        
elif Game == 'quaver':
    Mode = input('4k or 7k \n')
    if Mode in ('4k', '4K', '4'):
        # runs 4k
        print('4k has been selected \n')
        
    else:
       # runs 7k 
       print('7k has been selected \n')
        