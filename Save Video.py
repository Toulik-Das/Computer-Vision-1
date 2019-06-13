import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

#Define the codec and create VideoWriter Object
fourcc = cv.VideoWriter_fourcc(*'XVID')
output = cv.VideoWriter('Output.avi',fourcc,20.0,(640,480))

while(cam.isOpened()):
    ret,frame = cam.read()
    if ret == True:
        cv.imshow('frame',frame)
        output.write(frame)

        if cv.waitKey(1) == ord('q'):
            print('Saved Video')
            break
    else:
        print('Error')
        break
cam.release()
output.release()
cv.destroyAllWindows()
        
    

