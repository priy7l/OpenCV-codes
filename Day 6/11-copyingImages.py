#Practical 11: Copying Images: Proper Copy

import cv2 as cv

img = cv.imread("OpenCV-codes/images/image1.png")
copy = img.copy()

cv.line(copy, (245,735), (735,245), (0,255,0), 2)
cv.imshow("copy",copy)
cv.imshow("image", img)

cv.waitKey(0)
cv.destroyAllWindows()