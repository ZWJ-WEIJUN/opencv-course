#pylint:disable=no-member

import cv2 as cv
import numpy as np 

#(500, 500, 3) - (Height, width, # of image channels)
blank = np.zeros((500, 500, 3), dtype='uint8')  # 'uint8' is a datatype of an image
print(blank)
# cv.imshow('Blank', blank)


# 1. Paint the image a certain colour
blank[50:300, 350:400] = 0,0,255    # B, G, R
# cv.imshow('Green', blank)


# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)     # shape[1]-width, shape[0]-height.  thickness=-1 means color filled shape
# cv.imshow('Rectangle', blank)


# 3. Draw A circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)   # radius of 40 pixels
# cv.imshow('Circle', blank)


# 4. Draw a line
cv.line(blank, (100,250), (500,500), (255,255,255), thickness=3)
# cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Weijun Zhang!!!', (0,250), cv.FONT_HERSHEY_PLAIN, 1.0, (255,0,0), 1)     # (§00, 250) is the start point of the text
cv.imshow('Text', blank)

cv.waitKey(0)