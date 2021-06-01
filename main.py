import cv2
import mediapipe as mp
import time #for frame rate

#initialise video capture object (webcam)
cap = cv2.VideoCapture(0)

# Variables
mpHands = mp.solutions.hands
hands = mpHands.Hands() # We keep default params
draw = mp.solutions.drawing_utils

while True: 
    success, img = cap.read()
    
    #Pass our image
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb) #this will process the frame and return results 
    # print(results.multi_hand_landmarks) # Check if something is detected 
    #Extract info 
    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            draw.draw_landmarks(img , hand, mpHands.HAND_CONNECTIONS)
            
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
