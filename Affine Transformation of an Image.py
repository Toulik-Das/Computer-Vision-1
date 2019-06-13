import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('chessboard.png')

rows = img.shape[0]
cols = img.shape[1]

##Points from first Image
pts1 = np.float32([[100,100],[100,200],[200,100]])
pts2 = np.float32([[150,50],[50,150],[200,200]])

M=cv.getAffineTransform(pts1,pts2)
print(M)

#Apply Affine Transformation to above matrix
dst = cv.warpAffine(img,M,(cols,rows))

##3 points joined by lines on Source Image
cv.line(img,(pts1[0,0],pts1[0,1]),(pts1[1,0],pts1[1,1]),(255,0,0),2)
cv.line(img,(pts1[1,0],pts1[1,1]),(pts1[2,0],pts1[2,1]),(0,255,0),2)

##Transformed points on Destination Image
cv.line(dst,(pts2[0,0],pts2[0,1]),(pts2[1,0],pts2[1,1]),(255,0,0),2)
cv.line(dst,(pts2[1,0],pts2[1,1]),(pts2[2,0],pts2[2,1]),(0,255,0),2)

plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Input')

plt.show()
