import cv2 as cv
import numpy as np

#create a black Image
img = np.zeros((512,512,3),np.uint8)
#create a diagonal blue line with thickness of 5px by giving 2 end points
cv.line(img,(0,0),(511,511),(255,0,0),5)

#draw a Rectangle
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
#draw a circle
cv.circle(img,(447,63),63,(0,0,255),-1)

#draw a polygon
pts = np.array([[100,50],[200,300],[70,200],[50,100]],np.int32)
cv.polylines(img,[pts],True,(0,255,255),3)

#Write text by giving bottom left corner,font type,size,coloe,thickness
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Skyfi Labs',(0,480),font,2,(255,255,255),2)

cv.imshow('Image',img)

cv.waitKey(0)
cv.destroyAllWindows()
