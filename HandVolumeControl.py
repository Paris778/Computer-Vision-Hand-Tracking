import cv2
import HandTrackingModule as htm
import time
import numpy as np
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#########################################

#initialise video capture object (webcam)
cap = cv2.VideoCapture(0)
detector = htm.handDetector( detection_conf= 0.7, track_conf= 0.7 , draw = True, show_fps = True)

# Volume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate( IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
volume.GetVolumeRange()
volume.SetMasterVolumeLevel(-20.0, None)

while True:
    success, img = cap.read()
    img = detector.find_Hands(img)
    landmark_List = detector.find_poisiton(img)
    
    if len(landmark_List) != 0:
        # Get positions of thumb (4) and index (8) 
        thumb_finger = landmark_List[4]
        index_finger = landmark_List[8]
        
        #Get x and y
        x1,y1 = thumb_finger[1], thumb_finger[2]
        x2,y2 = index_finger[1] , index_finger[2]
        #Get center of line
        cx, cy = (x1+x2)//2 , (y1+y2)//2
        
        #Draw Line between the tips 
        cv2.line(img, (x1,y1), (x2,y2), (255,100,0), 3)
        cv2.circle(img,(cx, cy), radius=7, color=(255,255,0), thickness=cv2.FILLED)
        
        line_length = math.hypot(x2-x1, y2-y1)
        print(line_length)
        
        if line_length < 21:
            cv2.circle(img,(cx, cy), radius=7, color=(0,255,0), thickness=cv2.FILLED)
   
    #Show image
    cv2.imshow("Image", img)
    cv2.waitKey(1)