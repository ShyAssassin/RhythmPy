from cv2 import cv2
import pyautogui

image1 = pyautogui.screenshot(imageFilename='1.png')
image2 = pyautogui.screenshot(imageFilename='.png')
n = 0
while True:
    if image1 == image2:
        print('nothing has changed on screen')
        image1 = pyautogui.screenshot(imageFilename='1.png')
        image2 = pyautogui.screenshot(imageFilename='2.png')
    else:
        print('something on screen has moved')
        n = n + 1
        print(n)
        image1 = pyautogui.screenshot(imageFilename='1.png')
        image2 = pyautogui.screenshot(imageFilename='2.png')
