#Practical 4: Drawing a Rectangle
import cv2

img = cv2.imread("OpenCV-codes/images/image.png")

if img is None:
    print("Error: Image not found")
    exit()

cv2.rectangle(img, (100,100), (300,300), (0,255,0), 2)

cv2.imshow("Line", img)

cv2.waitKey(0)
cv2.destroyAllWindows()