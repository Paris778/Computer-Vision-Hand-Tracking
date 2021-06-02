from sys import base_prefix
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

#############
# Volume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate( IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

vol_range = volume.GetVolumeRange()
volume_level = 0
min_vol = vol_range[0]
max_vol = vol_range[1]

#########################
# Volume Bar Variables

bar_start_x = 15
bar_start_y = 120
bar_end_x = 30
bar_end_y = 400
bar_colour = (255,0,0)
bar_thickness = 3
volume_bar_height = bar_start_y

################
# Main loop
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
        
        #Convert volume range to line length range
        volume_level = np.interp(line_length, [20, 210], [min_vol,max_vol])
        print("Volume : " , volume_level)
        #Convert into bar dimensions
        volume_bar_height = np.interp(line_length, [20, 210], [bar_end_y,bar_start_y])
        print("Volume : " , volume_level)
        
        # Set system volume
        volume.SetMasterVolumeLevel(volume_level, None)
        
        #Display green circle when fingers almost touch
        if line_length < 21:
            cv2.circle(img,(cx, cy), radius=7, color=(0,255,0), thickness=cv2.FILLED)
            
    # Create volume level rectangle
    cv2.rectangle(img, (bar_start_x,bar_start_y), (bar_end_x,bar_end_y), color=bar_colour, thickness=bar_thickness)   # Frame
    cv2.rectangle(img, (bar_start_x,int(volume_bar_height)),(bar_end_x,bar_end_y), color=bar_colour, thickness = cv2.FILLED)
   
    #Show image
    cv2.imshow("Image", img)
    cv2.waitKey(1)