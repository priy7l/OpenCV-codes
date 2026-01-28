#Practical 15: Color Detection in Live Video

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Camera not accessible")
    exit()

# Dummy function
def nothing(x):
    pass

# Create a Window
cv.namedWindow("Trackbars")

# Create Trackbars
cv.createTrackbar("LH", "Trackbars", 0, 179, nothing)
cv.createTrackbar("LS", "Trackbars", 0, 255, nothing)
cv.createTrackbar("LV", "Trackbars", 0, 255, nothing)
cv.createTrackbar("UH", "Trackbars", 179, 179, nothing)
cv.createTrackbar("US", "Trackbars", 255, 255, nothing)
cv.createTrackbar("UV", "Trackbars", 255, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        print("An Error Occurred")
        break

    # Convert Into HSV Image
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Get Trackbar Position
    lh = cv.getTrackbarPos("LH", "Trackbars")
    ls = cv.getTrackbarPos("LS", "Trackbars")
    lv = cv.getTrackbarPos("LV", "Trackbars")

    uh = cv.getTrackbarPos("UH", "Trackbars")
    us = cv.getTrackbarPos("US", "Trackbars")
    uv = cv.getTrackbarPos("UV", "Trackbars")

    # Update Threshold
    lowerbound = np.array([lh, ls, lv])
    upperbound = np.array([uh, us, uv])

    # Mask
    mask = cv.inRange(hsv, lowerbound, upperbound)

    # Apply the Mask
    result = cv.bitwise_and(frame, frame, mask=mask)

    # Display the result
    cv.imshow("Mask", mask)
    cv.imshow("Result", result)

    # Exit on 'q' Press
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()