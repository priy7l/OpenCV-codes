#Practical 8: Resizing: Using Scale Factors
import cv2 as cv

img = cv.imread("OpenCV-codes/Images/image.png")

#Resizing Using Scale Factors
resized = cv.resize(img, None, fx=0.5, fy=0.3)
cv.imshow("resized image", resized)

cv.waitKey(0)
cv.destroyAllWindows()