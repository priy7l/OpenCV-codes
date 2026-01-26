#Practical 13: Color Detection in HSV

import cv2 as cv
import numpy as np

img1 = cv.imread("OpenCV-codes/images/image2.png")
img = cv.resize(img1, (480,480))

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])

mask = cv.inRange(hsv, lower_blue, upper_blue)

result = cv.bitwise_and(img, img, mask=mask)

cv.imshow("Original", img)
cv.imshow("Mask", mask)
cv.imshow("Result", result)

cv.waitKey(0)
cv.destroyAllWindows()