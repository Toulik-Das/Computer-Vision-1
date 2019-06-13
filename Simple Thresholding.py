import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('gradient.png',0)
cv.imshow('OriginalImage',img)

ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

##Change the image in the following statement after each thresholding
##cv.imshow('Threshold Image',thresh1)

titles = ['Original','Binary','Binary_INV','Trunc','Tozeo','Tozero_INV']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()



cv.waitKey(0)
cv.destroyAllWindows()  
