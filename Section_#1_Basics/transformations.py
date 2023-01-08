#pylint:disable=no-member

import cv2 as cv
import numpy as np

img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Translation
def translate(img, x, y):  # x , y stand for the number of pixels
    transMat = np.float32([[1,0,x],[0,1,y]])            #[1,0,x],[0,1,y]
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)  # shift the image left by 100 pixels and down by 100 pixels
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)  # 1.0 is a scaling factor
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated_cw45 = rotate(img, -45)
cv.imshow('rotated_cw45', rotated_cw45)

rotated_rotated_cw45 = rotate(rotated_cw45, -45)
cv.imshow('rotated_rotated_cw45', rotated_rotated_cw45)

rotated_cw90 = rotate(img, -90)
cv.imshow('Rotated Rotated', rotated_cw90)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 1)  
    # 0 -> flip the the iamge vertically(over the x axis)
    # 1 -> flip the image horizontally (over the y axis)
    # -1 -> flip the image both vertically and horizontally
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)