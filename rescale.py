import cv2 as cv

img = cv.imread('D:\OpenCV\images\Screenshot 2024-02-15 112301.png')
cv.imshow('Screenshot 2024-02-15 112301', img)

cv.imshow()

def rescaleFrame(frame, scale=0.75):
    # this will work on Images, Videos and Live Videos
    width =int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions =  (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Screenshot 2024-02-15 112301' ,resized_image)

def changeRes(width, height):
    #It only works on live video
    capture.set(3,width)
    capture.set(4,height)

    
# #Reading videos
capture = cv.VideoCapture('D:\OpenCV\videos\WIN_20241225_14_53_14_Pro.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    cv.imshow('WIN_20241225_14_53_14_Pro', frame)
    cv.imshow('WIN_20241225_14_53_14_Pro', frame_resized)
    
    if cv.waitKey(20) & 0xff==ord('d'): #Basicalyy it says if pressed 'D' then break out of this loop and stop displaying video
        break
capture.release()
cv.destroyAllWindows()