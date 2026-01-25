#Practical 3: Drawing a Line
import cv2

img = cv2.imread("OpenCV-codes/images/image.png")

if img is None:
    print("Error: Image not found")
    exit()

cv2.line(img, (50, 50), (200, 200), (255, 0, 0), 3)

cv2.imshow("Line", img)

cv2.waitKey(0)
cv2.destroyAllWindows()