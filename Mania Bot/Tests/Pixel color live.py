import numpy as np
from cv2 import cv2
from mss import mss
from PIL import Image
import matplotlib.pyplot as plt
import time
import pyautogui

bounding_box = {'top': 0, 'left': 0, 'width': 500, 'height': 500}

sct = mss()
while True:
    ScreenCap = sct.grab(bounding_box)
    # turns ScreenCap into Numpy array
    ScreenCap2 = np.array(ScreenCap)
    cv2.imshow('screen', ScreenCap2)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
    ScreenCap = ScreenCap2
    # gets the RGB colour from the Cords
    (RGB) = ScreenCap[114,232]
    # print("Pixel at (50, 50) - Red: {}, Green: {}, Blue: {}".format(r,g,b))
    RGBString = str(RGB)
    if RGBString != '[ 68  34  34 255]':
        print('something changed')


# while True:
#     ScreenCap()
#     (b, g, r) = ScreenCap[114,232]
#     print("Pixel at (50, 50) - Red: {}, Green: {}, Blue: {}".format(r,g,b))
#     plt.imshow(cv2.cvtColor(ScreenCap, cv2.COLOR_BGR2RGB))
#     plt.show()

