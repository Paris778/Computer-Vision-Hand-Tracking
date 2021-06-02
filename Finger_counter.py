import cv2
import mediapipe as mp
import time #for frame rate
import HandTrackingModule as htm
import os

# Works only with the right hand 

##############################
#initialise video capture object (webcam)
cap = cv2.VideoCapture(0)
detector = htm.handDetector(detection_conf=0.7 ,track_conf=0.7,draw = True, show_fps = True)

##############################
#Make list of finger tip IDs
finger_tip_id_list = [4,8,12,16,20]

############################
# Number rectangle

rect_start_x = 15
rect_start_y = 330
rect_end_x = 100
rect_end_y = 460
rect_colour = (245,250,252)
#------
text_x = 11
text_y = 450
text_colour = (0,0,0)
text_font_scale = 10
text_thickness = 5

##############################
# Main Loops
while True:
    success, img = cap.read()
    img = detector.find_Hands(img)
    landmark_List = detector.find_poisiton(img)
    
    if len(landmark_List) != 0:
        finger_counter = 0
        for id in finger_tip_id_list:
            # Check thumb only
            if ((id == 4) and (landmark_List[id][1] > landmark_List[id-1][1])):   # 1 is x-axis , so we check if it's on the left
                finger_counter+=1
            # Check other fingers
            elif (id != 4) and (landmark_List[id][2] < landmark_List[id-2][2]): #This means that index finger is open 
                finger_counter+=1
        print("Finger count: ", finger_counter)
        
        # Draw rectnagle with number in it
        cv2.rectangle(img, (rect_start_x,rect_start_y), (rect_end_x,rect_end_y), color=rect_colour, thickness=cv2.FILLED)
        cv2.putText(img, text=str(finger_counter),org = (text_x,text_y),fontFace=cv2.FONT_HERSHEY_PLAIN, thickness=text_thickness, color=text_colour, fontScale=text_font_scale)
   
    #Show image
    cv2.imshow("Image", img)
    cv2.waitKey(1)