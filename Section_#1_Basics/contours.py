#pylint:disable=no-member

import cv2 as cv
import numpy as np

img = cv.imread('./Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)  # (5,5)-kernel size 
cv.imshow('Blur', blur)
 
canny = cv.Canny(blur, 125, 175)       # 125 and 175 are two threshold values
cv.imshow('Canny Edges', canny)        

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# # If a particular pixel is below 125, it will be set to zero or black
# # If the pixel value is above 125, it will be set to 255 or white
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# cv.RETR_LIST - find and return all the contours find in the image
# cv.RETR_EXTERNAL - find and returan only the external contours
# cv.RETR_TREE - find and returan all the hierarchical contours
# cv.CHAIN_APPROX_NONE - Get all the coordinates of the points of the contour (say a contour of a straight line)
# cv.CHAIN_APPROX_SIMPLE - contour aproximation method - SIMPLE compresses all the points to ONLY two end points of the line
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,255,0), 1)  # -1 --> all of the contour; (B, G, R);  1 - thickness
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)