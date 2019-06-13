import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('pic1.png')

img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

ret,thresh = cv.threshold(img_gray,127,255,0)

img2 = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
contours, hierarchy = img2 if len(img2) == 2 else img2[1:3]


cnt = contours[6]
cv.drawContours(img,[cnt],0,(0,255,0),3)


M=cv.moments(cnt)
cx=int(M['m10']/M['m00'])
cy=int(M['m01']/M['m00'])
print('Centroid of the Face is',(cx,cy))


area=cv.contourArea(cnt)
print('Area of The Face',area)

##parimeter = cv.arcLength(cnt,True)
##print('Perimeter of the Face is',parimeter)

(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv.circle(img,center,radius,(255,0,0),2)


cv.imshow('Contours',img)

cv.waitKey(0)
cv.destroyAllWindows()
