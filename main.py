import cv2
import mediapipe as mp
import time #for frame rate


#######################
# Functions
#######################

#function to update current and previous time and calculate FPS

def get_fps(previous_time, current_time):
    fps = 1/(current_time - previous_time)    
    return current_time, fps



#initialise video capture object (webcam)
cap = cv2.VideoCapture(0)

#######################
# Variables
#######################
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands = 4) # We keep default params
draw = mp.solutions.drawing_utils

previous_time = 0
current_time = 0


#######################
# Main Loop
#######################
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
            
    #Get FPS
    previous_time, fps = get_fps(previous_time,time.time())
    
    #Display FPS on screen
    cv2.putText(img, str(int(fps)), org = (10,40), fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, fontScale=1, color=(0,20,255), thickness=2)
    
    #Show image
    cv2.imshow("Image", img)
    cv2.waitKey(1)
