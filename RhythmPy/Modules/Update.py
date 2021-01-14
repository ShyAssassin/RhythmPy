import logging
import requests
import json
from .Logger import logger


def UpdateCheck(ConfigDir=r""):

    # it will be jank but i am going to load version values from the config.json file
    # using a random repo for now NEEDS TO BE CHANGED BEFORE REALESE
    response = requests.get(
        "https://api.github.com/repos/v2ray/v2ray-core/releases/latest"
    )
    print(response.json()["name"])

    config = json.load(ConfigDir)

    config = config["Version"]
    if response > config:
        Update = True
    else:
        Update = False

    if Update is None:
        logger.error("Cant connect to github")
    elif Update == True:
        print("update found, would you like to download it? \n Y or N")

        if input == "yes" or "y" or "Y" or "Yes":
            print("downloading update now")
        else:
            pass
    else:
        pass


if __name__ == "__main__":
    UpdateCheck()
