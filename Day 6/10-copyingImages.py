#Practical 10: Copying Images: Shallow Copying

import cv2 as cv

img = cv.imread("OpenCV-codes/images/image1.png")
copy = img

cv.line(copy, (245,735), (735,245), (0,255,0), 2)
cv.imshow("image",img)

cv.waitKey(0)
cv.destroyAllWindows()