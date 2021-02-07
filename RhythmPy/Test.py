import json
import logging
import os
import threading
import time

from cv2 import cv2

# more retarded imports
try:
    from .Modules import GameInput
    from .Modules import Windowcapture
except:
    from Modules import GameInput
    from Modules import Windowcapture

# this test is used on quaver

# A
Collum1 = {"top": 0, "left": 0, "width": 1920, "height": 1080}
# S
Collum2 = {"top": 0, "left": 0, "width": 500, "height": 500}
# K
Collum3 = {"top": 0, "left": 0, "width": 500, "height": 500}
# L
Collum4 = {"top": 0, "left": 0, "width": 500, "height": 500}

"""
TODO:
make json Config settings
add multiprocessing / threading
find a way to check if you are running osu or quiver at start up
detect 4k or 7k
global stop / start button
user interface with TKinter
executable for mac / windows
"""


def TestRun(ImShow=True, ConfigFile="", Debug=True, Logging=True):
    last_time = float(time.time())

    ##########################################
    #                                       #
    #                 Logging               #
    #                                       #
    #########################################

    # Gets or creates a logger
    logger = logging.getLogger(__name__)

    # set log level
    if Debug == True:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)

    # define file handler and set formatter
    LoggingFile = logging.FileHandler("app.log")
    formatter = logging.Formatter(
        "%(name)s || %(asctime)s :: %(levelname)s :: %(message)s"
    )
    LoggingFile.setFormatter(formatter)

    # add file handler to logger
    logger.addHandler(LoggingFile)

    logger.info("Started")
    ###########################################

    ##########################################
    #                                       #
    #             JSON Settings             #
    #                                       #
    #########################################

    # runs the important stuff
    Wincap = Windowcapture.WindowCapture(None)
    Wincap.start()
    last_time = float(time.time())
    while True:
        # skips first frame to prevent stuff from breaking
        if Wincap.screenshot is None:
            continue
        # captures screen
        ScreenCap = Wincap.screenshot

        # checks if Imshow is called in run
        if ImShow == True:
            cv2.imshow("screen", ScreenCap)

        if (cv2.waitKey(1) & 0xFF) == ord("q"):
            logger.info("ImShow has been closed")
            Wincap.stop()
            cv2.destroyAllWindows()
            exit()

        ##########################################
        #                                       #
        #       image is in BGR Not RGB         #
        #         and Y goes before X           #
        #                                       #
        #########################################

        # gets the BGR colour from the Cords in the brackets
        # A                   y   x
        (BGR) = ScreenCap[904, 781]
        Collum1BGR = BGR
        # S                   y   x
        (BGR) = ScreenCap[114, 232]
        Collum2BGR = BGR
        # # K                 y   x
        (BGR) = ScreenCap[114, 232]
        Collum3BGR = BGR
        # # L                 y   x
        (BGR) = ScreenCap[114, 232]
        Collum4BGR = BGR

        # converts RGB value into a string
        Collum1BGR = str(Collum1BGR)
        Collum2BGR = str(Collum2BGR)
        Collum3BGR = str(Collum3BGR)
        Collum4BGR = str(Collum4BGR)
        #######################################

        print(Collum2BGR)

        if (
            Collum1BGR == "[244 244 244 255]"
            or Collum1BGR == "[243 243 243 255]"
            or Collum1BGR == "[242 242 242 255]"
        ):
            print("block")

        # this needs to be at the bottom
        if Debug == True:
            try:
                time_taken = float(time.time()) - last_time
                # raises an error if diveded by one sometimes...
                fps = 1 / time_taken
                print("FPS {}".format(round(fps)))
                last_time = float(time.time())
            except:
                logger.error("FPS does not like being devided by one")
                Wincap.stop()
                cv2.destroyAllWindows()
                exit()


if __name__ == "__main__":
    TestRun(Debug=False, ImShow=True, Logging=True)
