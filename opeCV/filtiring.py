import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    # _ is mean its a value that is return from a function put we dont care about it
    _, frame = cap.read()
    #convert to HSV Color
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_white = np.array([150,10,10])
    upper_white = np.array([180,255,150])

    mask = cv2.inRange(hsv, lower_white , upper_white)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    kernal = np.ones((15,15), np.float32)/225
    smoothed = cv2.filter2D(res, -1, kernal)
    blur = cv2.GaussianBlur(res, (15,15), 0)
    median = cv2.medianBlur(res , 15)
    bilateral = cv2.bilateralFilter(res , 15, 75, 75)


    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    cv2.imshow('mask',mask)
    cv2.imshow('smoothed',smoothed)
    cv2.imshow('blur',blur)
    cv2.imshow('median',median)
    cv2.imshow('bilateral',bilateral)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cv2.release()




