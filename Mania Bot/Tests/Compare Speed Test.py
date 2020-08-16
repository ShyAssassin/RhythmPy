import PIL
import PIL
from PIL import Image
import time

Image1 = Image.open(r"gnome.png")
Image2 = Image.open(r"Sunset.png")

n = 0

while True:
    if Image1 != Image2:
        print('not the same')
        n = n+1
        print(n)

time.sleep(10)
