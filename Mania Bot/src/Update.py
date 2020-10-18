import logging
import requests
import json

def UpdateCheck(ConfigDir=r''):
    ##########################################
    #                                       #       
    #                 Logging               #
    #                                       #
    #########################################

    # Gets or creates a logger
    logger = logging.getLogger(__name__)

    # set log level+
    
    logger.setLevel(logging.DEBUG)

    # define file handler and set formatter
    LoggingFile = logging.FileHandler('app.log')
    formatter = logging.Formatter('%(name)s || %(asctime)s :: %(levelname)s :: %(message)s')
    LoggingFile.setFormatter(formatter)

    # add file handler to logger
    logger.addHandler(LoggingFile)

    ###########################################

    # it will be jank but i am going to load version values from the config.json file
    # using a random repo for now NEEDS TO BE CHANGED BEFORE REALESE 
    response = requests.get("https://api.github.com/repos/v2ray/v2ray-core/releases/latest")
    print(response.json()["name"])

    config = json.load(ConfigDir)

    config = config['Version']
    if response > config:
        Update = True
    else:
        Update = False

    if Update is None:
        logger.error('Cant connect to github')
    elif Update == True:
        print('update found, would you like to download it? \n Y or N')

        if input == 'yes' or 'y' or 'Y' or 'Yes':
            print('downloading update now')
        else:
            pass  
    else:
        pass

if __name__ == "__main__":        
    UpdateCheck()