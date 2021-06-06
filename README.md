# Computer-Vision-Hand-Tracking

# Description

A series of computer vision projects developed in order to increase my experience and further explore this innovative field.
This repositiory contains two projects and one generalist module which can be imported and used into different projects such as the Hand-Tracked Pong Game: https://github.com/Paris778/Computer-Vision-Pong-Hand-Tracked/

### Project 1: Finger Counter 
This project can identify how many fingers are shown to the camera using Google's mediapipe.

![Alt text](https://github.com/Paris778/Computer-Vision-Hand-Tracking/blob/main/computer%20vision%20media/Capture4.JPG "Title")
![Alt text](https://github.com/Paris778/Computer-Vision-Hand-Tracking/blob/main/computer%20vision%20media/Capture5.JPG "Title")

### Video Demo #1
[![IMAGE ALT TEXT HERE](https://github.com/Paris778/Computer-Vision-Hand-Tracking/blob/main/computer%20vision%20media/Capture4.JPG)](https://github.com/Paris778/Computer-Vision-Hand-Tracking/blob/main/computer%20vision%20media/fingerCounterVideo.mp4)

### Project 2: Gesture Volume Control 
This project allows the user to control the volume of their machine using the distance between their index finger and thumb.
If the two fingers touch, the volume is reduced to zero and at max distance the volume is at max. It is important to note that the distance of the hand from the camera matters in the volume calculation.

![Alt text](https://github.com/Paris778/Computer-Vision-Hand-Tracking/blob/main/computer%20vision%20media/Capture2.JPG "Title")
![Alt text](https://github.com/Paris778/Computer-Vision-Hand-Tracking/blob/main/computer%20vision%20media/Capture3.JPG "Title")
### Video Demo #2
[![IMAGE ALT TEXT HERE](https://github.com/Paris778/Computer-Vision-Hand-Tracking/blob/main/computer%20vision%20media/Capture2.JPG)](https://github.com/Paris778/Computer-Vision-Hand-Tracking/blob/main/computer%20vision%20media/volumeVideo.mp4)

## Dependencies & Run

#### Install dependancies:

#### Google mediapipe 

```bash
pip3 install mediapipe
```
#### numpy 

```bash
pip3 install numpy
```

#### pycaw (for the volume project) 

Original repo by AndreMiras : https://github.com/AndreMiras/pycaw

```bash
pip3 install pycaw
```
#### Run
- Clone repo
- Open in a text editor (i.e VSCode) and run the python file corresponding to each project

## License
[MIT](https://choosealicense.com/licenses/mit/)


