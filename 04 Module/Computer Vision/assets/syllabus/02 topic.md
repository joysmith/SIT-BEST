## Motion, object detection, Optical character recognition

- Object detection demo [mediapipe](https://mediapipe-studio.webapps.google.com/studio/demo/object_detector)

- Face detection demo [mediapipe](https://mediapipe-studio.webapps.google.com/studio/demo/face_detector)


- Face Landmark Detection demo [mediapipe](https://mediapipe-studio.webapps.google.com/studio/demo/face_landmarker)

- Pose Landmark Detection demo [mediapipe](https://mediapipe-studio.webapps.google.com/studio/demo/pose_landmarker)



7 - Drawing Functions in OpenCV

8 - Set Date Time and frame size using OpenCv

9 - Handling Mouse Event using OvenCv

10 - Color Picker Project using OpenCV

11 - Merge,split,size function ,Basic operations on image using opencv

12 - Find Roi of an Image and perform operations using Open CV

13 - Making Borders of an image using openCV

14 - Image Blending and Addition using opencv

15 - Project on Image Blending using OpenCV

16 - Bitwise Operations on Images using OpenCV

17 - Object Tracking in Image using OpenCV

18 - Color Tracking in video using OPenCV

---

7 - Drawing Functions in OpenCV

#### How to create white image

```py
import numpy as np
import cv2


img = cv2.imread("C:\\Users\\91958\\Pictures\\turtle.jpg")
img = cv2.resize(img,(600,700))

#Creating Blank Image---

img = np.ones([512,512,3], np.uint8)*255 #create window of an white screen


cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

#### Documentation

- np.ones() [reference](https://www.geeksforgeeks.org/numpy-ones-python/)


<br>

#### How to create black image

```py
import numpy as np
import cv2


img = cv2.imread("C:\\Users\\91958\\Pictures\\turtle.jpg")
img = cv2.resize(img,(600,700))

#Creating Blank Image---

img = np.zeros([512, 512, 3], np.uint8)*255  #For black screen


cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

#### Documentation

- np.zeros() [reference](https://numpy.org/doc/2.1/reference/generated/numpy.zeros.html)
- np.zeros() [reference](https://www.geeksforgeeks.org/numpy-zeros-python/)
- () [reference]()
- () [reference]()
- () [reference]()

<br>

#### How to draw line

```py
import numpy as np
import cv2


img = cv2.imread("C:\\Users\\91958\\Pictures\\turtle.jpg")
img = cv2.resize(img,(600,700))

#Creating Blank Image---

img = np.zeros([512, 512, 3], np.uint8)*255  #For black screen

#Here line accept 5 parameter (img,starting,ending,color,thickness)
img = cv2.line(img, (0,0), (200,200), (154, 92, 424), 8) #color format BGR

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
```


#### Documentation

- cv2.line() [reference](https://www.geeksforgeeks.org/python-opencv-cv2-line-method/)

<br>

#### How to draw arrowed line

```py
import numpy as np
import cv2


img = cv2.imread("C:\\Users\\91958\\Pictures\\turtle.jpg")
img = cv2.resize(img,(600,700))

#Creating Blank Image---

img = np.zeros([512, 512, 3], np.uint8)*255  #For black screen

#arrowed line accept also accpet 5 parameter  (img,starting,ending,color,thickness)
img = cv2.arrowedLine(img, (0,125), (255,255), (255, 0, 125), 10)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
```


#### Documentation

- cv2.arrowedLine() [reference](https://www.geeksforgeeks.org/python-opencv-cv2-arrowedline-method/)

<br>

#### How to draw rectangle

```py
import numpy as np
import cv2


img = cv2.imread("C:\\Users\\91958\\Pictures\\turtle.jpg")
img = cv2.resize(img,(600,700))

#Creating Blank Image---

img = np.zeros([512, 512, 3], np.uint8)*255  #For black screen

#Rectangle - accept parameter(img,start_co,end_co,colot ,thickness)
img = cv2.rectangle(img, (384, 10), (510, 128), (128, 0, 255), 8)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
```


#### Documentation

- cv2.rectangle() [reference](https://www.geeksforgeeks.org/python-opencv-cv2-rectangle-method/)

<br>

#### How to draw circle

```py
import numpy as np
import cv2


img = cv2.imread("C:\\Users\\91958\\Pictures\\turtle.jpg")
img = cv2.resize(img,(600,700))

#Creating Blank Image---

img = np.zeros([512, 512, 3], np.uint8)*255  #For black screen

#circle - accept(img,star_co,radius,color,thickness)
img = cv2.circle(img, (447, 125), 63, (214, 255, 0), -5)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

```


#### Documentation

- cv2.circle() [reference](https://www.geeksforgeeks.org/python-opencv-cv2-circle-method/)

<br>

#### How to draw text

```py
import numpy as np
import cv2


img = cv2.imread("C:\\Users\\91958\\Pictures\\turtle.jpg")
img = cv2.resize(img,(600,700))

#Creating Blank Image---

img = np.zeros([512, 512, 3], np.uint8)*255  #For black screen

font = cv2.FONT_ITALIC
#puttext -accept(img,text,start_co,font,fontsize,color,thickness,linetype)
img = cv2.putText(img, 'JOY', (20, 500), font, 4, (0, 125, 255), 10,cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

```


#### Documentation

- cv2.FONT_ITALIC [reference](https://docs.opencv.org/4.x/d6/d6e/group__imgproc__draw.html)
- cv2.putText() [reference](https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/)

<br>

#### How to draw ellipse

```py
import cv2
import numpy as np

# Create a blank image (black background)
image = np.zeros((500, 500, 3), dtype=np.uint8)

# Define ellipse parameters
center_coordinates = (250, 250)      # Center of the ellipse
axes_length = (100, 50)              # Length of the axes (major, minor)
angle = 30                           # Angle of rotation of ellipse in degrees
start_angle = 0                      # Starting angle of the elliptic arc
end_angle = 360                      # Ending angle of the elliptic arc (360 = full ellipse)
color = (0, 255, 0)                  # Color in BGR (Green)
thickness = 2                        # Thickness of the ellipse outline

# Draw the ellipse
cv2.ellipse(image, center_coordinates, axes_length, angle, start_angle, end_angle, color, thickness)

# Display the image
cv2.imshow('Ellipse', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```


#### Documentation

- cv2.ellipse() [reference](https://www.geeksforgeeks.org/python-opencv-cv2-ellipse-method/)


<br>

#### How to draw custom shape

```py
# Python program to explain 
# cv2.polylines() method 

import cv2
import numpy as np



image = cv2.imread("/home/joy/Pictures/cat.jpg",1)


# Window name in which image is
# displayed
window_name = 'Image'

# Polygon corner points coordinates
pts = np.array([[25, 70], [25, 160], 
                [110, 200], [200, 160], 
                [200, 70], [110, 20]],
               np.int32)

pts = pts.reshape((-1, 1, 2))

isClosed = True

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.polylines() method
# Draw a Blue polygon with 
# thickness of 1 px
image = cv2.polylines(image, [pts], 
                      isClosed, color, thickness)

# Displaying the image
while(1):
    
    cv2.imshow('image', image)
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()
```


#### Documentation

- cv2.polylines() [reference](https://www.geeksforgeeks.org/python-opencv-cv2-polylines-method/)

<br>

### 8 - Set Date Time and frame size using OpenCv

```py
import cv2
import datetime
cap = cv2.VideoCapture(0)  #for warn 0 just pass cv2.CAP_DSHOW
print("for width===",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("for height==",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3, 600)  #here 3 for width
cap.set(4, 800)  #here 4 for height
print("Width====",cap.get(3))
print("Height===",cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

       font = cv2.FONT_HERSHEY_COMPLEX_SMALL
       text = ' Height: ' + str(cap.get(4))+' Width: '+ str(cap.get(3))
       date_data = "Date: "+str(datetime.datetime.now())
       frame = cv2.putText(frame, text, (10, 20), font, 1,
                           (0, 155, 255), 1, cv2.LINE_AA)
       frame = cv2.putText(frame, date_data, (20, 50), font, 1,
                           (100, 255, 255), 1, cv2.LINE_AA)
       #Rectangle - accept parameter(img,start_co,end_co,colot ,thickness)
       cv2.rectangle(frame, (384, 10), (510, 128), (128, 0, 255), 8)
       cv2.imshow('frame', frame)

       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()
```


#### Documentation

- cv2.putText() [reference](https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/)

<br>

### 9 - Handling Mouse Event using OpenCv

```py
import numpy as np
import cv2

# mouse callback function
def draw(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDBLCLK:

        cv2.circle(img,(x,y),100,(125,0,255),5)

    if event == cv2.EVENT_RBUTTONDBLCLK:

        cv2.rectangle(img,(x,y),(x+100,y+75),(125,125,255),2)
cv2.namedWindow(winname = "res")
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.setMouseCallback("res",draw)

while True:
    cv2.imshow("res",img)
    # press ESC to quit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
#Create a function which help to find coordinate of any pixel and its color
```



#### Documentation

- cv2.EVENT_LBUTTONDBLCLK() [reference](https://www.tutorialspoint.com/opencv_python/opencv_python_handling_mouse_events.htm)

<br>

#### Create a fucntion which help to find cordinate of any pixel and its color

```py
import numpy as np
import cv2



def mouse_event(event, x, y, flg, param):
    print("event==",event)
    print("x==",x)
    print("y==",y)
    print("flg==",flg)
    print("param==",param)
    font = cv2.FONT_HERSHEY_PLAIN
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ' ,y)

        cord = ". "+str(x) + ', '+ str(y)
        cv2.putText(img, cord, (x, y), font, 1, (155,125 ,100), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        b= img[y, x, 0] #for blue channel is 0
        g = img[y, x, 1] #for green channel is 1
        r = img[y, x, 2] #for red channel is 2

        color_bgr = ". "+str(b) + ', '+ str(g)+ ', '+ str(r)
        cv2.putText(img, color_bgr, (x, y), font, 1, (152, 255, 130), 2)
        cv2.imshow('image', img)

#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('C:\\Users\\91958\\Pictures\\jelly fish.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', mouse_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

