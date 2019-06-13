import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('pic1.png')

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret,thresh = cv.threshold(img_gray,127,255,0)

img2 = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
contours, hierarchy = img2 if len(img2) == 2 else img2[1:3]

##cv.drawContours(img,contours,-1,(0,255,0),3)
##cv.drawContours(img,contours,1,(0,255,0),3)
cnt=contours[10]
cv.drawContours(img,[cnt],0,(0,255,0),3)

cv.imshow('Contours',img)

cv.waitKey(0)
cv.destroyAllWindows()

