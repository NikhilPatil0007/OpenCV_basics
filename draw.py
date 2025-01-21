import cv2 as cv
import numpy as np

blank  =  np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)
#img = cv.imread('D:\OpenCV\images\image.png')
#cv.imshow('image', img)


# 1. Paint the image a certain color
#blank[:] = 0, 255, 0
blank[200:300, 300:400] = 0,0,255
cv.imshow('Green', blank)


#Draw a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

#Putting Text on images
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2)
cv.imshow('Text', blank)
cv.waitKey(0)