import numpy as np
import cv2
image = cv2.imread('cat.jpeg')

image = cv2.resize(image,(800,600))

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY )


cv2.imshow('img',image_gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

histg = cv2.calcHist([image_gray],[0],None,[100],[0,255])
print(histg)

within = []
for i in range(len(histg)):
    x,y = np.split(histg,[i])
    x1 = np.sum(x)/(image.shape[0]*image.shape[1])
    y1 = np.sum(y)/(image.shape[0]*image.shape[1])
    x2 = np.sum([j*t for j,t in enumerate(x)])/np.sum(x)
    y2 = np.sum([j*t for j,t in enumerate(y)])/np.sum(y)
    x3 = np.sum([(j-x2)**2*t for j,t in enumerate(x)])/np.sum(x)
    x3 = np.nan_to_num(x3)
    y3 = np.sum([(j-y2)**2*t for j,t in enumerate(y)])/np.sum(y)
    within.append(x1*x3 + y1*y3)
m = np.argmin(within)
print(m)

(thresh, Bin) = cv2.threshold(image_gray,m,255,cv2.THRESH_BINARY)
cv2.imshow('Binary',Bin)
cv2.waitKey(0)
cv2.destroyAllWindows()
