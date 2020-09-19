import numpy as np
from cv2 import cv2
from mss import mss
from PIL import Image
import matplotlib.pyplot as plt
import time
import pyautogui
import json
import logging
import os

# this test is used on quaver 

# A
Collum1 = {'top': 0, 'left': 0, 'width': 500, 'height': 500}
# S
Collum2 = {'top': 0, 'left': 0, 'width': 500, 'height': 500}
# K
Collum3 = {'top': 0, 'left': 0, 'width': 500, 'height': 500}
# L
Collum4 = {'top': 0, 'left': 0, 'width': 500, 'height': 500}

sct = mss()
def TestRun(ImShow=True, ConfigFile='', Debug=True, Logging=True):
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

    logger.info('Bot started')
    ###########################################

    while True:
        # captures screen
        Collum1Cap = sct.grab(Collum1)
        Collum2Cap = sct.grab(Collum2)
        Collum3Cap = sct.grab(Collum3)
        Collum4Cap = sct.grab(Collum4)

        # turns Capture into Numpy array
        Collum1Array = np.array(Collum1Cap)
        Collum2Array = np.array(Collum2Cap)
        Collum3Array = np.array(Collum3Cap)
        Collum4Array = np.array(Collum4Cap)

        # checks if Imshow is called in run 
        if ImShow == True:
            # shows screen capture
            cv2.imshow('collum1', Collum1Array)
            cv2.imshow('collum2', Collum2Array)
            cv2.imshow('collum3', Collum3Array)
            cv2.imshow('collum4', Collum4Array)
            
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
        (BGR) = Collum1Array[114,232]
        Collum1BGR = BGR
        # S                   y   x
        (BGR) = Collum2Array[114,232]
        Collum2BGR = BGR
        # K                   y   x
        (BGR) = Collum3Array[114,232]
        Collum3BGR = BGR
        # L                   y   x
        (BGR) = Collum4Array[114,232]
        Collum4BGR = BGR

        # converts RGB value into a string
        Collum1BGR = str(Collum1BGR)
        Collum2BGR = str(Collum2BGR)
        Collum3BGR = str(Collum3BGR)
        Collum4BGR = str(Collum4BGR)
        ########################################

        if Debug == True:
            print('Loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            

if __name__ == '__main__':
    TestRun(ImShow=True, Debug=True, Logging=True)