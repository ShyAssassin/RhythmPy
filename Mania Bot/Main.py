import json
import library
import threading
import logging

##########################################
#                                       #       
#                 Logging               #
#                                       #
#########################################

# Gets or creates a logger
logger = logging.getLogger(__name__)

# set log level  
logger.setLevel(logging.INFO)

# define file handler and set formatter
LoggingFile = logging.FileHandler('app.log')
formatter = logging.Formatter('%(name)s || %(asctime)s :: %(levelname)s :: %(message)s')
LoggingFile.setFormatter(formatter)

# add file handler to logger
logger.addHandler(LoggingFile)

logger.info('Main started')
###########################################


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
        