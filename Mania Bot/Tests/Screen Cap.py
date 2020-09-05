import numpy as np
from cv2 import cv2
from mss import mss
from PIL import Image
import matplotlib.pyplot as plt

bounding_box = {'top': 0, 'left': 0, 'width': 1920, 'height': 1000}

sct = mss()
y = 0
while True:
    sct_img = sct.grab(bounding_box)
    sct_img2 = sct.grab(bounding_box)
    cv2.imshow('screen', np.array(sct_img))
    print(y)
    y = y + 1
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break