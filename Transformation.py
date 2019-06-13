import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('hazard10.jpg')

rows =img.shape[0]
cols=img.shape[1]

##Transformation matrix for translation

##Transformation 100px in x-direction
M = np.float32([[1,0,100],[0,1,50]])

##Apply Affinite Transformation with the the above matrix
dst = cv.warpAffine(img,M,(cols,rows))

cv.imshow('Original',img)
cv.imshow('Translated',dst)

cv.waitKey(0)
cv.destroyAllWindows()
