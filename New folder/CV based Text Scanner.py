import cv2 as cv
import numpy as np
import pytesseract as pyt



img = cv.imread('Skyfilabs.png')

text = pyt.image_to_string(img)

print(text)

cv.imshow('Original',img)

cv.waitKey(0)
cv.destroyAllWindows()
