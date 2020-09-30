import numpy as np
from cv2 import cv2
from mss import mss
from PIL import Image
import matplotlib.pyplot as plt
import time
import json

bounding_box = {'top': 0, 'left': 0, 'width': 500, 'height': 500}

sct = mss()
def Osu4kRun(ImShow=True, ConfigFile=''):
    x = 0
    while True:
        ScreenCap = sct.grab(bounding_box)
        # turns ScreenCap into Numpy array
        ScreenCap2 = np.array(ScreenCap)
        # checks if Imshow is called in run
        if ImShow == True:
            cv2.imshow('screen', ScreenCap2)
            if (cv2.waitKey(1) & 0xFF) == ord('q'):
                cv2.destroyAllWindows()
                exit()

        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            cv2.destroyAllWindows()
            exit()
        ScreenCap = ScreenCap2
        # gets the RGB colour from the Cords
        (RGB) = ScreenCap[114,232]
        # print(RGB)
        # converts RGB value into a string
        RGBString = str(RGB)
        if RGBString != '[ 68  34  34 255]':
            print('something changed')
            # pyautogui.move(0, 10)

        x = x + 1
        print(x)

if __name__ == '__main__':
    Osu4kRun(ImShow=True)