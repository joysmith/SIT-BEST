## Robot interface for vision data


### Creating a finger counter computer vision

1. Install library

```sh
pip install mediapipe

pip install pyautogui
```

2. code
```py
import cv2
import mediapipe as mp

mp_hand = mp.solutions.hands
hands = mp_hand.Hands(static_image_mode=False,max_num_hands=1,min_detection_confidence=0.7)
mp_drawing= mp.solutions.drawing_utils

def count_finger(hand_landmarks):
    fingers =[]
    landmarks = hand_landmarks.landmark
    
    fingers.append(landmarks[4].x < landmarks[3].x)
    
    for tip in[8,12,16,20]:
        fingers.append(landmarks[tip].y < landmarks[tip -2].y)
    
    return fingers.count(True)

cap =cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    frame =cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    result = hands.process(rgb_frame)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame,hand_landmarks,mp_hand.HAND_CONNECTIONS)
            
            finger_count = count_finger(hand_landmarks)
            cv2.putText(frame,f"Fingers:{finger_count}",(10,70),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)
            
    cv2.imshow("Finger Counter",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
            
```


### Brightness control with hand detection

1. Install library

```sh
pip install opencv-python mediapipe

pip install pyautogui

pip install screen-brightness-control
```


2. code
```py
import cv2
import mediapipe as mp
import screen_brightness_control as sbc
from math import hypot
import numpy as np

mpHands = mp.solutions.hands
hands = mpHands.Hands(
	static_image_mode = False,
	model_complexity=1,
	min_detection_confidence=0.75,
	min_tracking_confidence=0.75,
	max_num_hands=2
)

Draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
   _,frame = cap.read()
   frame =cv2.flip(frame,1)
   frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
   Process = hands.process(frameRGB)
   landmarkList= []
   
   if Process.multi_hand_landmarks:
       for handlm in Process.multi_hand_landmarks:
           for _id,landmarks in enumerate(handlm.landmark):
               height,width,color_channels = frame.shape
               x,y = int(landmarks.x * width) , int(landmarks.y * height)
               landmarkList.append([_id,x,y])
               
           Draw.draw_landmarks(frame,handlm,mpHands.HAND_CONNECTIONS)
           
   if landmarkList != []:
       
       x_1,y_1= landmarkList[4][1],landmarkList[4][2]
       x_2,y_2= landmarkList[8][1],landmarkList[8][2]
       
       cv2.circle(frame,(x_1,y_1),7,(0,255,0),cv2.FILLED)
       cv2.circle(frame,(x_2,y_2),7,(0,255,0),cv2.FILLED)
       cv2.line(frame,(x_1,y_1),(x_2,y_2),(0,255,0),3)
       
       L = hypot(x_2-x_1,y_2-y_1)
       
       b_level =np.interp(L,[15,220],[0,100])
       sbc.set_brightness(int(b_level))
       
   cv2.imshow("Image",frame)
   if cv2.waitKey(1) &0xff == ord('q'):
       break
```