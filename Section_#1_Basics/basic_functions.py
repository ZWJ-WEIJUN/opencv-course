#pylint:disable=no-member

import cv2 as cv

# Read in an image
img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Park', img) 


# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Blur 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)   # (7, 7) - kernal size needs to be in a odd number, used for defining windows size
cv.imshow('Blur', blur)



# Edge Cascade
canny = cv.Canny(blur, 125, 175)                # two threashold values
cv.imshow('Canny Edges', canny)


# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)


# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)


# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)


# Cropping
cropped = img[100:200, 200:400]     #50:200 - height   300:400 - width
cv.imshow('Cropped', cropped)

cv.waitKey(0)