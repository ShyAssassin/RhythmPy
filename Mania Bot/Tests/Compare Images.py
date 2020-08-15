import PIL
from PIL import Image
import time
Image1 = Image.open(r"gnome.png")
Image2 = Image.open(r"Sunset.png")

print('is Image1 equal to image2?')
if Image1 == Image2:
    print('something went wrong')
else:
    print('images are not the same')


print('is Image1 equal to Image1')
if Image1 == Image1:
    print('images are the same')
else:
    print('something went wrong')
time.sleep(10)
