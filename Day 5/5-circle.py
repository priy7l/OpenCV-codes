#Practical 5: Drawing a Circle
import cv2

img = cv2.imread("OpenCV-codes/images/image.png")

if img is None:
    print("Error: Image not found")
    exit()

cv2.circle(img, (250,250), 50, (0,0,255), 2)

cv2.imshow("Line", img)

cv2.waitKey(0)
cv2.destroyAllWindows()