# Necessary imports
from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
# For Google Colab we use the cv2_imshow() function

# Loading our image with a cv2.imread() function
img=cv2.imread(r"Mania Bot\Tests\atsisiusti_2.png",cv2.IMREAD_COLOR)
# img=cv2.imread("Cybertruck.jpg",1)

# Loading our image with a cv2.imread() function
gray=cv2.imread(r"Mania Bot\Tests\atsisiusti_2.png",cv2.IMREAD_GRAYSCALE)
# gray=cv2.imread("Cybertruck.jpg",

# For Google Colab we use the cv2_imshow() function
# but we can use cv2.imshow() if we are programming on our computer 

# We can show the image using the matplotlib library. 
# OpenCV loads the color images in reverse order: 
# so it reads (R,G,B) like (B,G,R)
# So, we need to flip color order back to (R,G,B)


plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# Y goes before X
(b, g, r) = img[114,232]
print("Pixel at (50, 50) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

dimensions = img.shape
print(dimensions)
plt.title('Original')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()


# while True:
#      # We can show the image using the matplotlib library. 
#     # OpenCV loads the color images in reverse order: 
#     # so it reads (R,G,B) like (B,G,R)
#     # So, we need to flip color order back to (R,G,B)
#     plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#     # We can use comand plt.axis("off") to delete axis
#     # from our image
#     plt.title('Original')
#     cv2.imshow("1",img)
#     cv2.imshow("2",gray)
#     # If we want to get the dimensions of the image we use img.shape
#     # It will tell us the number of rows, columns, and channels 
#     # If an image is a grayscale, img.shape returns 
#     #the number of rows and columns
#     dimensions = gray.shape
#     print(dimensions)
#     dimensions = img.shape
#     print(dimensions)
#     if cv2.waitKey(30) & 0xFF == ord('q'):
#         break