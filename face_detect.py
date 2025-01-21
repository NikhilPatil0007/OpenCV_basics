import cv2 as cv

img = cv.imread('D:\OpenCV\images\man2.jpeg')
cv.imshow("Man", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

haar_cascade = cv.CascadeClassifier('haar_casecade.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of face found = {len(faces_rect)}')
cv.waitKey(0)
