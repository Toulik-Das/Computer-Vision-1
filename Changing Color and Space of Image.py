import cv2 as cv
import numpy as np

img=cv.imread('hazard10.jpg')
cv.imshow('BGR',img)
print('Shape of the Image')
print(img.shape)
print('The size of the Image')
print(img.size)

##img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
##cv.imshow('GRAY',img_gray)
##print('The shape of the gray Image')
##print(img_gray.shape)
##print('The size of the gray IMage')
##print(img_gray.size)

img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV', img_hsv)
print('Shape of HSV')
print(img_hsv.shape)
print('The size of the hsv imager')
print(img_hsv.size)

cv.waitKey(0)
cv.destroyAllWindows()
