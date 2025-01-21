import cv2 as cv
import numpy as np

img  = cv.imread('D:\OpenCV\images\image.png')
cv.imshow('Image', img)

# -x --> Left
# -y --> up
# x --> Right
# y --> Down

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)
cv.imshow('translated', translated)


#Rotation
def rotate (img, angle, roPoint=None):
    (height, width) = img.shape[:2]

    if roPoint is None:
        roPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(roPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
cv.imshow('Resized', resized)

rotated = rotate(img, 45)
cv.imshow("Rotated", rotated)
cv.waitKey(0)