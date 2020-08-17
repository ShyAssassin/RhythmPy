# import numpy as np
# from cv2 import cv2
# from mss import mss
# from PIL import Image

# bounding_box = {'top': 0, 'left': 0, 'width': 1920, 'height': 1000}

# sct = mss()

# while True:
#     sct_img = sct.grab(bounding_box)
#     sct_img2 = sct.grab(bounding_box)
#     cv2.imshow('screen', np.array(sct_img))

#     if (cv2.waitKey(1) & 0xFF) == ord('q'):
#         cv2.destroyAllWindows()
#         break
#     if sct_img == sct_img2:
#       print('test')

import numpy as np
from cv2 import cv2

# Capture video from file
cap=cv2.VideoCapture(r'Mania Bot\Tests\video0 (1).mp4')
cap2 = cv2.VideoCapture(r'Mania Bot\Tests\video0 (1).mp4')

old_frame = None

while True:

    ret, frame = cap.read()

    if ret == True:
        ret, frame = cap2.read()
        cv2.imshow('BaseVideo',frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if old_frame is not None:
            diff_frame = gray - old_frame
            diff_frame -= diff_frame.min()
            disp_frame = np.uint8(255.0*diff_frame/float(diff_frame.max()))
            cv2.imshow('diff_frame',disp_frame)
        old_frame = gray

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    else:
        print('ERROR!')
        break

cap.release()
cv2.destroyAllWindows()