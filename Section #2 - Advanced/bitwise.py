#pylint:disable=no-member

import cv2 as cv
import numpy as np

# image with the binary color
blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
    # (30, 30) start point of the rectangle
    # (370, 370) end point of the rectangle
    # Binary - Only one channel of the color, so 255 is good 
    # -1 means filled shape
circle = cv.circle( blank.copy(), (200,200), 200, 255, -1 )

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)
# cv.waitKey(0)

# bitwise AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# bitwise OR --> non-intersecting and intersecting regions 
# superimpose rectangle and circle together）
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR --> non-intersecting regions
# Can be get useing bitwise_or - bitwise_xor
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT --> invert the binary color
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Circle NOT', bitwise_not)

cv.waitKey(0)