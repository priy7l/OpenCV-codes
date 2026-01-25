#Pracical 12: HSV color space Illustration

import cv2 as cv

img = cv.imread("OpenCV-codes/images/image.png")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

h, s, v = cv.split(hsv)

cv.imshow("Hue",h)
cv.imshow("Saturation", s)
cv.imshow("Value", v)

cv.waitKey()
cv.destroyAllWindows()