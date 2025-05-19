## Motion, object detection, Optical character recognition

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

#### 🔴(not working) How to draw ellipse

```py
import numpy as np
import cv2


img = cv2.imread("C:\\Users\\91958\\Pictures\\turtle.jpg")
img = cv2.resize(img,(600,700))

#Creating Blank Image---

img = np.zeros([512, 512, 3], np.uint8)*255  #For black screen

#ellipse-accept(img,start_cor,(length,height),color,thickness)
img = cv2.ellipse(img,(400,600),(100,50),0,0,180,155,5)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

```

#### How to draw custom shape

```py
import numpy as np
import cv2


img = cv2.imread("C:\\Users\\91958\\Pictures\\turtle.jpg")
img = cv2.resize(img,(600,700))

#Creating Blank Image---

img = np.zeros([512, 512, 3], np.uint8)*255  #For black screen

pts = np.array([[100,150],[200,30],[170,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,155))

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

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

10 - Color Picker Project using OpenCV

11 - Merge,split,size function ,Basic operations on image using opencv

12 - Find Roi of an Image and perform operations using Open CV

13 - Making Borders of an image using openCV

14 - Image Blending and Addition using opencv

15 - Project on Image Blending using OpenCV

16 - Bitwise Operations on Images using OpenCV

17 - Object Tracking in Image using OpenCV

18 - Color Tracking in video using OPenCV
