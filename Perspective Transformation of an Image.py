import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('Perspective_Transformation.png')

pts1=np.float32([[123,353],[701,349],[592,40],[232,33]])
pts2=np.float32([[50,50],[775,50],[775,250],[50,250]])

M = cv.getPerspectiveTransform(pts1,pts2)

#Use Affinite Transform inj Above Matrix
dst= cv.warpPerspective(img,M,(800,300))

##Transform  image to RGB color Space
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
dst=cv.cvtColor(dst,cv.COLOR_BGR2RGB)

plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Input')

plt.subplot(1,2,2)
plt.imshow(dst)
plt.title('Output')

plt.show()
