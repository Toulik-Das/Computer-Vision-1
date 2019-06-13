import cv2 as cv
import numpy


img = cv.imread('hazard10.jpg')
cv.imshow('image',img)
print('The Shape of the Image is')
print(img.shape)
print('The Size Of the Image')
print(img.size)
print('The dtype of the Pixel Value in Th Image')
print(img.dtype)

px = img[100,100]
print('The Value of the Pixel at 100*100 is')
print(px)

blue = img[100,100,0]
print('The value of blue color in pixel at 100*100 is')
print(blue)

img[100,100] = [255,255,255]
cv.imshow('Image1',img)

cv.waitKey(0)
cv.destroyAllWindows()
