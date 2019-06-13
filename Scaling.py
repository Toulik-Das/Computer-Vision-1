import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('hazard10.jpg')

##Zooming an Image
##res = cv.resize(img, (400,300),0,0,interpolation = cv.INTER_LINEAR)
##res=cv.resize(img,None,fx=2,fy=2,interpolation =  cv.INTER_CUBIC)
res=cv.resize(img,None,fx=0.5,fy=0.5,interpolation =  cv.INTER_AREA)

cv.imshow('Original',img)
cv.imshow('Scaled',res)

cv.waitKey(0)
cv.destroyAllWindows()

print('Shape of Original Image:')
print(img.shape)
print('Shape of Resized Image:')
print(res.shape)
