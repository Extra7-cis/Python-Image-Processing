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

    kernal = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask , kernal , iterations = 1)
    dialation = cv2.dilate(mask , kernal , iterations = 1)
    #opening : remove false positive(noise in the backgroung)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
    #closing : remove false negative(noise in the focusing area)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

    # it is the difference between input image and Opening of the image
    #cv2.imshow('Tophate',tophate)
    #it is the difference between the closing of the closing of the input image and input image
    #cv2.imshow('Blackhat',blackhat)


    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dialation',dialation)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cv2.release()
