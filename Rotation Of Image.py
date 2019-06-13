import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('hazard10.jpg')

rows = img.shape[0]
cols = img.shape[1]

#Rotaion Matrix

#Center of Rotaion - Center of Images , 90 degrees , Scales =1
M = cv.getRotationMatrix2D(((cols-1)/2.0 , (rows-1)/2.0),45,0.5)##90,1

#Apply Affine Transformation with above Matrix
dst = cv.warpAffine(img,M,(cols,rows))

cv.imshow('original',img)
cv.imshow('Rotation',dst)

cv.waitKey(0)
cv.destroyAllWindows()
