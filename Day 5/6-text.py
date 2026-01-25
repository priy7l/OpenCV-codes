#Practical 6: Adding Text
import cv2

img = cv2.imread("OpenCV-codes/images/image.png")

if img is None:
    print("Error: Image not found")
    exit()

cv2.putText(img, "Hello OpenCV", (50,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

cv2.imshow("Line", img)

cv2.waitKey(0)
cv2.destroyAllWindows()