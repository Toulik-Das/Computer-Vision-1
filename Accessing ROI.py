import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('hazard10.jpg')
cv.imshow('Image',img)

###Use matplotlib to find pixel of the ball
##
##img_RGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
##
##plt.axis('off')
##plt.imshow(img_RGB)
##plt.show()

ball = img[235:295,465:530]

##convert the Ball region into White

##ball = ([255,255,255])
##img[235:295,465:530] = ball

##Replicate the ball to display an Additional ball

img[235:295,555:620] =ball

cv.imshow('ROI',img)


cv.waitKey(0)
cv.destroyAllWindows()
