#pylint:disable=no-member

import cv2 as cv

# Reading Images
# img = cv.imread('./Resources/Photos/cat.jpg')   # Shorter path to acess the .jpg file
# img = cv.imread('/Users/zhangweijun/Documents/GitHub/opencv-course/Resources/Photos/cat_large.jpg')
# cv.imshow('Cats', img)

# cv.waitKey(0)  # Wait for a specific dealy


# Reading Videos
# capture = cv.VideoCapture('./Resources/Videos/dog.mp4')
capture = cv.VideoCapture(0)



while True:
    isTrue, frame = capture.read()
    
#     if cv.waitKey(20) & 0xFF==ord('d'):
#     This is the preferred way - if `isTrue` is false (the frame could 
#     not be read, or we're at the end of the video), we immediatelyk
#     break from the loop. 
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(1) & 0xFF==ord('d'):   # Each frame will be played for each 1000ms, the video play will quit if press key 'd'
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()
