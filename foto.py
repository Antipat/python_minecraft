import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

time.sleep(3)
while True:
    _, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.imwrite('obrab.jpg', frame)
    time.sleep(1)
    break

b = cv2.resize(frame  , (60 , 50))
cv2.imwrite('obrab11.jpg', b)
