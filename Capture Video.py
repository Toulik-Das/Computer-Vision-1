import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

while(True):
    #Capture Video Contineously
    ret,frame = cam.read()

    #Display The Resulting Frame
    cv.imshow('Frame',frame)
    key = cv.waitKey(10)
    if key == 27: #wait for ESC key to exit
        break
#When Done
cam.release()
cv.destroyAllWindows()
