#Practical 7: Resizing: By Declaring Exact Dimensions
import cv2 as cv

img = cv.imread("OpenCV-codes/Images/image.png")

#Resizing by Declaring Exact Dimensions
resized = cv.resize(img, (300,400))
cv.imshow("resized image", resized)

cv.waitKey(0)
cv.destroyAllWindows()