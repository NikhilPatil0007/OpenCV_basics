import  cv2 as cv
import numpy as np

img =  cv.imread('D:\OpenCV\images\cat.jpeg')
cv.imshow('cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#Laplacion Edges
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian", lap)

#Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combine_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("Combine Sobel", combine_sobel)
cv.imshow("Sobelx", sobelx)
cv.imshow("Sobely", sobely)

canny =cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny )
cv.waitKey(0)