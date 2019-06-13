import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

cam = cv.VideoCapture(0)

lower_yellow = np.array([20,100,100])
upper_yellow = np.array([40,255,255])


while(True):
    ret,frame = cam.read()

    #Smooth the Image
    image_smooth = cv.GaussianBlur(frame,(7,7),0)

    #Threshold the image for yellow color
    image_hsv = cv.cvtColor(image_smooth,cv.COLOR_BGR2HSV)

    image_threshold = cv.inRange(image_hsv,lower_yellow,upper_yellow)

    #Find Contours
    image_contours = cv.findContours(image_threshold,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    contours, hierarchy = image_contours if len(image_contours) == 2 else image_contours[1:3]

    #Find the index of the largest contour

    if(len(contours)!=0):
        areas = [cv.contourArea(c) for c in contours]
        max_index = np.argmax(areas)
        cnt = contours[max_index]
        x_bound,y_bound,w_bound,h_bound = cv.boundingRect(cnt)
        cv.rectangle(frame,(x_bound,y_bound),(x_bound+w_bound , y_bound+h_bound),(255,0,0),2)
        


    ##cv.imshow('Frame',image_smooth)
    ##cv.imshow('Frame',image_threshold)
    cv.imshow('Frame',frame)   
    key = cv.waitKey(10)
    if key == 27:
        break


cam.release()
cv.destroyAllWindows()
