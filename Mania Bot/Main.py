import json
import src
import os.path
from os import path
import src
from src import logger

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

    def Process(self):
    # checks if game is running
        if(src.ProcessCheck.ProcessRunning('')):
            Game = 'Osu'
        elif(src.ProcessCheck.ProcessRunning('')):
            Game = 'Qauver'
        else:
            print('cant find the running Process\n Please select it manualy\n Osu or Quaver')
            if input == 'Osu':
                Game = 'Osu'
            else:
                Game == 'Quaver'
        return Game


class ui:

    def SettingsUI(self):
        pass


class Main():

    def Run(self):
        pass

    
if __name__ == "__main__":
    Main = Main()
    Main.Run()

