#Practical 16: Erosion

import cv2 as cv
import numpy as np

img1 = cv.imread("OpenCV-codes/images/image4.png")
img = cv.resize(img1, (480, 480))

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.namedWindow("Trackbars")

def nothing(x):
    pass

cv.createTrackbar("LH", "Trackbars", 0, 179, nothing)
cv.createTrackbar("LS", "Trackbars", 0, 255, nothing)
cv.createTrackbar("LV", "Trackbars", 0, 255, nothing)
cv.createTrackbar("UH", "Trackbars", 179, 179, nothing)
cv.createTrackbar("US", "Trackbars", 255, 255, nothing)
cv.createTrackbar("UV", "Trackbars", 255, 255, nothing)

while True:

    lh = cv.getTrackbarPos("LH", "Trackbars")
    ls = cv.getTrackbarPos("LS", "Trackbars")
    lv = cv.getTrackbarPos("LV", "Trackbars")
    uh = cv.getTrackbarPos("UH", "Trackbars")
    us = cv.getTrackbarPos("US", "Trackbars")
    uv = cv.getTrackbarPos("UV", "Trackbars")

    lower_bound = np.array([lh, ls, lv])
    upper_bound = np.array([uh, us, uv])

    mask = cv.inRange(hsv, lower_bound, upper_bound)

    kernel = np.ones((5, 5), np.uint8)

    eroded = cv.erode(mask, kernel, iterations = 1)

    result = cv.bitwise_and(img, img, mask=eroded)

    cv.imshow("Mask", eroded)
    cv.imshow("Result", result)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()