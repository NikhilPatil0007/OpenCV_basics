import cv2  as cv

img = cv.imread('D:\OpenCV\images\cat.jpeg')
cv.imshow('cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#Simple thresholding
threshold, thresh =  cv.threshold(gray, 50, 255, cv.THRESH_BINARY )
cv.imshow('Thresh', thresh)

# Adpative thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,3 )
cv.imshow('Adaptive threshold', adaptive_thresh)
cv.waitKey(0)