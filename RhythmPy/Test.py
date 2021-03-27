import cv2
cap = cv2.VideoCapture()
cap.open('udp://127.0.0.1:12/')
print('1')
ret, frame = cap.read()
cv2.imwrite("out.png", frame)
cv2.imsh