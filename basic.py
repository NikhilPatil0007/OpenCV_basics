import cv2 as cv

img  = cv.imread("D:\OpenCV\images\image.png")
cv.imshow('image', img)

#Converting to Greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Casscade
canny  =  cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

#Dilating the image 
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dialated', dilated)

#Eroding
eroded = cv.erode(dilated, (3,3), iterations = 1)

#resize
resized = cv.resize(img, (500,500))
cv.imshow("Resize", resized)

#Cropped 
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)
cv.waitKey(0)