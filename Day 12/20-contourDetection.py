#Practical 20: Contour Detection

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened:
    print("Camera not accessible.")
    exit

cv.namedWindow("Trackbars")

def nothing(x):
    pass

cv.createTrackbar("LH", "Trackbars", 0, 179, nothing)
cv.createTrackbar("LS", "Trackbars", 0, 255, nothing)
cv.createTrackbar("LV", "Trackbars", 0, 255, nothing)
cv.createTrackbar("UH", "Trackbars", 179, 179, nothing)
cv.createTrackbar("US", "Trackbars", 255, 255, nothing)
cv.createTrackbar("UV", "Trackbars", 255, 255, nothing)

kernel = np.ones((5,5), np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        print("An error occurred.")
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lh = cv.getTrackbarPos("LH", "Trackbars")
    ls = cv.getTrackbarPos("LS", "Trackbars")
    lv = cv.getTrackbarPos("LV", "Trackbars")  
    uh = cv.getTrackbarPos("UH", "Trackbars")
    us = cv.getTrackbarPos("US", "Trackbars")
    uv = cv.getTrackbarPos("UV", "Trackbars")

    lower_bound = np.array([lh, ls, lv])
    upper_bound = np.array([uh, us, uv])

    mask = cv.inRange(hsv, lower_bound, upper_bound)

    opened = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)

    contours, hierarchy = cv.findContours(opened, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    cv.drawContours(frame, contours, -1, (0,255,0), 1)

    for cnt in contours:
        if cv.contourArea(cnt) > 500:
            x, y, w, h = cv.boundingRect(cnt)

    cv.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 1)

    cv.imshow("Result", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()