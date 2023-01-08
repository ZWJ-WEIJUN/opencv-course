#pylint:disable=no-member

import cv2 as cv

img = cv.imread('./Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
average = cv.blur(img, (3,3))   # (3, 3) kernel size means 3by3 grid of pixels
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)  # 0 - represent sigma (standard deviation)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)  
 # 10 - diameter of the pixels
 # 35 - sigma color, larger number with sigma color means more pixels being reaching out for the centeral pixel calculation
 # 25 - space sigma
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)