## Industrial applications

39 - Harris and Shitomasi Corner Detection Method using OpencCV

40 - Background Subtraction from the video

41 - Object Tracking using Cam and Mean shift OpenCV

42 - Optical Flow Motion Tracking using OpenCV

43 - Face and Eyes Detection using Image

44 - Eyes and Face Tracking using Webcam

45 - Cat Face Tracking using OpenCV and Harcade

### 41 object Tracking

```py
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 17:34:13 2020

@author: NISHANT
"""
#Object Tracking using Meanshift Algo.
#The idea behind this algo is to move small window to get the high
#density pixels same as histogram backprojection.

#Steps to use this algo-----
#First setup target and find its histogram for backproject the traget.
#ALso set one initial location
#setup the termination criteria

import numpy as np
import cv2 as cv
cap = cv.VideoCapture('C:\\Users\\91958\\Pictures\\turtle.mp4')

# take first frame of the video
ret, frame = cap.read()

# setup initial location of window
x, y, width, height = 580, 30, 80,150
track = (x, y ,width, height)

# set up the ROI for tracking
roi = frame[y:y+height, x : x+width]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)),
np.array((180., 255., 255)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255,cv.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
termntn = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
cv.imshow('roi',roi)
while  True:
    ret, frame = cap.read()

    if ret == True:

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        # apply meanshift to get the new location
        ret, track = cv.meanShift(dst, track, termntn)

        # Draw it on image
        x,y,w,h = track
        final = cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)

        cv.imshow('dst', dst)
        frame = cv.resize(final,(600,600))
        cv.imshow('final_image',frame)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break
cv.destroyAllWindows()

#There are few disadvantages of this algo
#Fixe of target window should not be changed.
#to manuaaly pass roi and then detect our target
```

```py

#CAMshift (Continuously Adaptive Meanshift)


import numpy as np
import cv2 as cv
cap = cv.VideoCapture('C:\\Users\\91958\\Pictures\\turtle.mp4')

# take first frame of the video
ret, frame = cap.read()

# setup initial location of window
x, y, width, height = 580, 30, 80,150
track = (x, y ,width, height)

# set up the ROI for tracking
roi = frame[y:y+height, x : x+width]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255,cv.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
termntn = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
cv.imshow('roi',roi)
while  True:
    ret, frame = cap.read()

    if ret == True:

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        # apply meanshift to get the new location
        ret, track = cv.CamShift(dst, track, termntn)

        # Draw it on image
        #x,y,w,h = track
        #final = cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)

        #Try to draw rotating rectangle
        pts =cv.boxPoints(ret)
        pts = np.int64(pts)
        final = cv.polylines(frame,[pts],True,(255,0,0),2)






        cv.imshow('dst', dst)
        frame = cv.resize(final,(600,600))
        cv.imshow('final_image',frame)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break
cv.destroyAllWindows()
```

### 43 face eye detection

```py



#Face Detection using haarcascade file
import cv2
import numpy
face=cv2.CascadeClassifier("C:\\Users\\91958\\Pictures\\cascades\\haarcascade_frontalface_default.xml") #for detecting face
eye = cv2.CascadeClassifier('C:\\Users\\91958\\Pictures\\cascades\\haarcascade_eye.xml') #for detecting eyes

image=cv2.imread('C:\\Users\\91958\\Pictures\\a.jpg')
gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #convert into gray

#parameters(img,scale_factor[reduce image size],min_neighbour)
faces = face.detectMultiScale(gray,4,4)   #for  faces

for(x,y,w,h) in faces:

    image=cv2.rectangle(image,(x,y),(x+w,y+h),(127,0,205),3)

    #Now detect eyes
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye.detectMultiScale(roi_gray,1.2,1)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

image = cv2.resize(image,(800,700))
cv2.imshow("Face Detected",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

#### face eye dection on video

```py
#Face Detection using haarcascade file
import cv2
import numpy
face=cv2.CascadeClassifier("C:\\Users\\91958\\Pictures\\cascades\\haarcascade_frontalface_default.xml") #for detecting face
eye = cv2.CascadeClassifier('C:\\Users\\91958\\Pictures\\cascades\\haarcascade_eye.xml') #for detecting eyes


def dector(img):
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(127,0,125),3)

        roi_gray = gray[y:y+h, x:x+w]

        roi_color = img[y:y+h, x:x+w]

        eyes = eye.detectMultiScale(roi_gray,1.3,3)
        for (ex,ey,ew,eh) in eyes:
            cv2.circle(roi_color,(ex+27,ey+27),20,(255,255,0),2)

    return img

cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
while True:
    ret,frame =cap.read()
    frame = cv2.flip(frame,2)
    cv2.imshow("face dect",dector(frame))
    if cv2.waitKey(1)==13:   # press enter to terminate
        break

cap.release()
cv2.destroyAllWindows()
```

### 45 Cat face tracking

```py


#Cat face detection using har cascade
import cv2
import numpy
face=cv2.CascadeClassifier("C:\\Users\\91958\\Pictures\\cascades\\haarcascade_frontalcatface.xml") #for detecting face

image=cv2.imread("C:\\Users\\91958\\Pictures\\dogcat.jpg")
gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #convert into gray so color not effect accuracy

#parameters(img,scale_factor[reduce image size],min_neighbour)
faces = face.detectMultiScale(gray,1.1,1)   #for  faces

for(x,y,w,h) in faces:

    image=cv2.rectangle(image,(x,y),(x+w,y+h),(127,0,205),3)



image = cv2.resize(image,(800,700))
cv2.imshow("Face Detected",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

### 

- Cascade Trainer GUI [click](https://amin-ahmadi.com/cascade-trainer-gui/)