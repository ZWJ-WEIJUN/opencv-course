#pylint:disable=no-member

import cv2 as cv

img = cv.imread('./Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )
    # 150 - threshold value, if pixel value less than 150, the value goes to zero (white)
    # 255 - max value, if pixel value larger than 150, the vaue goes to max vlaue 255 (black)
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV )
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
    # 11 - the kernal size
    # 9 - C value is an integer that used to subtract from mean value, which allowing for fine tune
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)