import numpy as np
from cv2 import cv2
from mss import mss
from PIL import Image
import matplotlib.pyplot as plt
import time
import pyautogui
import json

# this test is used on quaver 

# whole screen
Screen = {'top': 0, 'left': 0, 'width': 500, 'height': 500}
# A
Collum1 = {'top': 0, 'left': 0, 'width': 500, 'height': 500}
# S
Collum2 = {'top': 0, 'left': 0, 'width': 500, 'height': 500}
# K
Collum3 = {'top': 0, 'left': 0, 'width': 500, 'height': 500}
# L
Collum4 = {'top': 0, 'left': 0, 'width': 500, 'height': 500}



sct = mss()
def TestRun(ImShow=True, ConfigFile='', Debug=True):
    count = 0
    while True:
        # captures screen
        ScreenCap = sct.grab(Screen)
        Collum1Cap = sct.grab(Collum1)
        Collum2Cap = sct.grab(Collum2)
        Collum3Cap = sct.grab(Collum3)
        Collum4Cap = sct.grab(Collum4)

        # turns Capture into Numpy array
        ScreenCapArray = np.array(ScreenCap)
        Collum1Array = np.array(Collum1Cap)
        Collum2Array = np.array(Collum2Cap)
        Collum3Array = np.array(Collum3Cap)
        Collum4Array = np.array(Collum4Cap)

        # checks if Imshow is called in run
        if ImShow == True:
            cv2.imshow('screen', ScreenCapArray)
            cv2.imshow('collum1', Collum1Array)
            cv2.imshow('collum2', Collum2Array)
            cv2.imshow('collum3', Collum3Array)
            cv2.imshow('collum4', Collum4Array)
            
            if (cv2.waitKey(1) & 0xFF) == ord('q'):
                cv2.destroyAllWindows()
                exit()

        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            cv2.destroyAllWindows()
            exit()
        ScreenCap = ScreenCapArray
        # gets the RGB colour from the Cords
        (RGB) = ScreenCap[114,232]
        # print(RGB)
        # converts RGB value into a string
        RGBString = str(RGB)
        if Debug == True:
            if RGBString != '[ 68  34  34 255]':
                count = count + 1
                print('something changed')
                print(count)
                # pyautogui.move(0, 10)

if __name__ == '__main__':
    TestRun(ImShow=False, Debug=True)