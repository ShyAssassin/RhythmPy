import numpy as np
from cv2 import cv2
from mss import mss
from PIL import Image
import matplotlib.pyplot as plt
import time
import DirectInput
import json
import logging
import os
import threading

# this test is used on quaver 

# A
Collum1 = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
# S
Collum2 = {'top': 0, 'left': 0, 'width': 500, 'height': 500}
# K
Collum3 = {'top': 0, 'left': 0, 'width': 500, 'height': 500}
# L
Collum4 = {'top': 0, 'left': 0, 'width': 500, 'height': 500}

'''
TODO:
make json Config settings
add multiprocessing / threading
find a way to check if you are running osu or quiver at start up
detect 4k or 7k
global stop / start button
user interface with TKinter
executable for mac / windows
'''

def TestRun(ImShow=True, ConfigFile='', Debug=True, Logging=True):
    sct = mss()
    count = 0
    last_time = time.time()
    
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
    LoggingFile = logging.FileHandler('app.log')
    formatter = logging.Formatter('%(name)s || %(asctime)s :: %(levelname)s :: %(message)s')
    LoggingFile.setFormatter(formatter)

    # add file handler to logger
    logger.addHandler(LoggingFile)

    logger.info('started')
    ###########################################

    ##########################################
    #                                       #       
    #             JSON Settings             #
    #                                       #
    #########################################

    # runs the important stuff
    while True:
        # captures screen
        ScreenCap = sct.grab(Collum1)

        # turns Capture into Numpy array
        ScreenCapArray = np.array(ScreenCap)

        # checks if Imshow is called in run 
        if ImShow == True:
            # shows screen capture
            cv2.imshow('collum1', ScreenCapArray)
            
            if (cv2.waitKey(1) & 0xFF) == ord('q'):
                logger.info('ImShow has been closed')
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
        (BGR) = ScreenCapArray[904,781]
        Collum1BGR = BGR
        # S                   y   x
        (BGR) = ScreenCapArray[114,232]
        Collum2BGR = BGR
        # # K                 y   x
        (BGR) = ScreenCapArray[114,232]
        Collum3BGR = BGR
        # # L                 y   x
        (BGR) = ScreenCapArray[114,232]
        Collum4BGR = BGR

        # converts RGB value into a string
        Collum1BGR = str(Collum1BGR)
        Collum2BGR = str(Collum2BGR)
        Collum3BGR = str(Collum3BGR)
        Collum4BGR = str(Collum4BGR)
        ########################################


        # print(Collum1BGR)

        if Collum1BGR == '[244 244 244 255]' or Collum1BGR == '[243 243 243 255]' or Collum1BGR == '[242 242 242 255]':
            # print('block')
            DirectInput.keyDown('a')
            DirectInput.keyUp('a')
            
        # this needs to be at the bottom
        if Debug == True:
            print('FPS {}'.format(1 / (time.time()-last_time)))
            last_time = time.time()
            

if __name__ == '__main__':
    # we are using threading until i can figuire out how to share memory between mutiple processes
   TestRun(Debug=True, ImShow=False, Logging=True)
