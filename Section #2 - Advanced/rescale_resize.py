#pylint:disable=no-member

import cv2 as cv

def main_rescale_resize():
    img = cv.imread('./Resources/Photos/cat.jpg')
    img_resized = rescaleFrame(img, scale=0.5)

    cv.imshow('Cat', img)           # Diaplay a image as a new window
    cv.imshow('Cat Resized', img_resized)
    cv.waitKey(0)  # Wait for a specific dealy in milisecond, 0 means wait for an infinit amount of time

    # Reading Videos
    capture = cv.VideoCapture('./Resources/Videos/dog.mp4')

    while True:
        isTrue, frame = capture.read()

        frame_resized = rescaleFrame(frame, scale=.5)
        
        cv.imshow('Video', frame)
        cv.imshow('Video Resized', frame_resized)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break

    capture.release()
    # cv.destroyAllWindows()

# This rescaleFrame method Works for Images, Videos and Live Video
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)             # frame.shape[1] is the width of the image
    height = int(frame.shape[0] * scale)            # frame.shape[0] is the height of the image
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Change the resolution of videos. Note: Only works for Live video
def changeRes(width,height):
    capture.set(3,width)    # 3 units of width
    capture.set(4,height)   # 4 units of height



if __name__ == '__main__':
    main_rescale_resize()