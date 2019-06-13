import cv2 as cv
import numpy

#Reading The Image
img = cv.imread('hazard10.jpg')
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()

#For Printing Image In Gray scale mode
img1 = cv.imread('hazard10.jpg',0)
cv.imshow('image1',img1)
cv.imwrite('grayhazard.jpg', img1)
