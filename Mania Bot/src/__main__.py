import json
import os.path
from os import path
# IDK why the hell the import does not work sometimes 
# this is a hippy solution
try:
    from .Logger import logger
    from .ProcessCheck import IsProcessRunning
except:
    from Logger import logger
    from ProcessCheck import IsProcessRunning

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


class Functions:

    def __init__(self):
        logger.info(msg='started')

    # If Config File exists
    def ConfigExists(self):
        if path.exists('Config.json') == False:
            print('Config file is missing, creating now...')
            logger.warning('Config file missing, creating now')
            # writes config to file
            with open('Config.json', 'w+') as json_file:
                json.dump(Defualt_Config, json_file, indent=4)
                logger.info('defualt config writen to file')
        else:
            pass

    # checks if process is running
    def Process(self):
        if(IsProcessRunning('Osu')):
            Game = 'Osu'
            return Game
        elif(IsProcessRunning('Quaver')):
            Game = 'Qauver'
            return Game
        else:
            print(' cant find the running Process\n Please select it manually\n Osu or Quaver ')
            GameInput = input()
            if GameInput in ('Osu', 'OSU', 'osu'):
                Game = 'Osu'
                return Game
            elif GameInput in ('Quaver', 'QUAVER' 'quaver'):
                Game = 'Quaver'
                return Game
            else:
                logger.critical('what the actual fuck')

class Main():

    def Run(self):
        Functions().Process()
        Functions().ConfigExists()

    
if __name__ == "__main__":
    Main().Run()