import cv2 as cv

img  =  cv.imread('D:\OpenCV\images\cat.jpeg')
cv.imshow("img", img)


#Averaging
average = cv.blur(img, (3,3))
cv.imshow('blur', average)

#GaussianBlur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('gauss', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

#bilaateral
bilateral = cv.bilateralFilter(img, 10, 35, 25 )
cv.imshow('bi', bilateral)
cv.waitKey(0)