#Practical 9: Cropping
import cv2 as cv

img = cv.imread("OpenCV-codes/images/image.png")
cropped = img[0:490, 490:980]

cv.imshow("Image", cropped)

cv.waitKey(0)
cv.destroyAllWindows()