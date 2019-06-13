import cv2 as cv
import numpy


img = cv.imread('hazard10.jpg')
cv.imshow('image',img)
img1 = cv.imread('hazard10.jpg',0)
cv.imshow('image1',img1)

key = cv.waitKey(0)

if key == 27:
 cv.destroyAllWindows()
if key == ord('s'):
 cv.imwrite('grayhazard1.jpg',img1)
 cv.destroyAllWindows()
