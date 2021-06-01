import cv2
import mediapipe as mp
import time #for frame rate
import HandTrackingModule as htm

#initialise video capture object (webcam)
cap = cv2.VideoCapture(0)
detector = htm.handDetector(draw = False)

while True:
    success, img = cap.read()
    img = detector.find_Hands(img)
    position = detector.find_poisiton(img)
    #Write FPS on screen
    img = detector.display_fps(img)
    #Show image
    cv2.imshow("Image", img)
    cv2.waitKey(1)