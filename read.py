import cv2 as cv

# #Reading Images
# img = cv.imread('D:\OpenCV\images\Screenshot 2024-02-15 112301.png')
# cv.imshow('Screenshot 2024-02-15 112301', img)

# #Delay to key to be pressed
# cv.waitKey(0)

# #Reading videos
capture = cv.VideoCapture('D:\OpenCV\videos\WIN_20241225_14_53_14_Pro.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('WIN_20241225_14_53_14_Pro', frame)

    if cv.waitKey(20) & 0xff==ord('d'): #Basicalyy it says if pressed 'D' then break out of this loop and stop displaying video
        break
capture.release()
cv.destroyAllWindows()