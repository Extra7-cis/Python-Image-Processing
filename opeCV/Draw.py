import numpy as np
import cv2

img = cv2.imread('index2.jpeg', cv2.IMREAD_COLOR)


#draw a line on image
cv2.line(img, (0,0), (150,150), (255,255,255), 15)
#draw a rectangle on image
cv2.rectangle(img, (15,25),(200,150),(0,255,0),5)
#draw a Circle on image
cv2.circle(img, (100,63), 55 , (0,0,255), 5)
#set points on image
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#match the points to draw polygon
cv2.polylines(img,[pts],True,(0,255,255),3)
#choos font to type on inage
font = cv2.FONT_HERSHEY_SIMPLEX
#type on image
cv2.putText(img,'Hello World',(0,130),font , 1,(200,255,255),2,cv2.LINE_AA)




cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
