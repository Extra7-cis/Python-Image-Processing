import numpy as np
import cv2

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('arrow.png')

#add logo to the image
rows,cols,channels = img2.shape
#find the region of image
roi = img1[0:rows,0:cols]
#create mask to the logo and convert it
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#if the pixel value is apove 220 it will be coverted to 255(white) else its converted to black
ret, mask = cv2.threshold(img2gray, 220,255, cv2.THRESH_BINARY_INV)
#define the part there is no mask
mask_inv = cv2.bitwise_not(mask)
#define the black area for img1
img1_bg = cv2.bitwise_and(roi, roi , mask=mask_inv)
#define the black area for img2
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)
#add image1 in the back ground of image2
dst = cv2.add(img1_bg, img2_fg)
#did not understand that !!!!!!!!!!!!!!!!!!!!!!!
img1[0:rows,0:cols] = dst

cv2.imshow('res',img1)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('dst',dst)



cv2.waitKey(0)
cv2.destroyAllWindows()
