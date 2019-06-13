import cv2 as cv
import numpy as np
import pytesseract as pyt
from tkinter.filedialog import askopenfilename

filename = askopenfilename()

image = cv.imread(filename)
image_work = np.copy(image)

#Find Countor of the Image
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

smooth = cv.GaussianBlur(gray,(5,5),0)

thresh = cv.Canny(smooth ,100,300)

image_contour = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
contours, hierarchy = image_contour if len(image_contour) == 2 else image_contour[1:3]

if(len(contours)!=0):
    areas = [cv.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt = contours[max_index]

epsilon = 0.05*cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt,epsilon,True)

cv.drawContours(image_work , [approx],-1,(255,0,0),3)

cv.imshow('image',image_work)
cv.waitKey(1000)
#Find Perspective Transform Matrix

src = np.float32([approx[0,0],approx[1,0],approx[2,0].approx[3,0]])
dst = np.float32([500,300],[500,0],[0,0],[0,300])

M= cv.getPerspectiveTransform(src,dst)
warped = cv.warpPerspective(image,M,(500,300))

cv.imshow('Warped',warped)
cv.waitKey(1000)

##pre-process Image for Text Extraction

res = cv.resize(warped,None,fx=8,fy=8,interpolation = cv.INTER_CUBIC)

gray_warped = cv.cvtColor(res,cv.COLOR_BGR2GRAY)
ret,thresh_warped = cv.threshold(gray_warped,150,255,cv.THRESH_BINARY_INV)

#cv.imshow('Threshold',thresh)

#cv.waitKey(0)
cv.destroyAllWindows()

##text=pyt.image_to_tstring(thresh_warped)
##print(text)
