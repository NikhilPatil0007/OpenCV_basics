import cv2 as cv
import numpy as np
img  = cv.imread('D:\OpenCV\images\download.jpeg')
cv.imshow("cat", img)

blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('Balnk', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Images', canny)

ret , thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

contours , hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

#Drawing Contours on Blank image
cv.drawContours(blank, contours, -1, (0,0, 255), 1)
cv.imshow("Contours Drawn", blank)
cv.waitKey(0)