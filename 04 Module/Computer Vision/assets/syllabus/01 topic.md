## Basic knowledge of computer vision systems

3 - Image read,write and save operation

4 - Read,write and save video using opencv

5 - Connect Mobile Camera in openCV

6 - Basic Screen Recording using OpenCV

### 3 - Image read,write and save operation

#### How to read image from computer

```py
import cv2    #openCV use as cv2 in python

#Loads a color image. Any transparency of image will be neglected. It is the default flag.
#this function is used to read the image from location
img1 = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg',1)
cv2.imshow("Colored Image",img1)  #It accept two parameters 1)- Name of screen ,2) -  Image
print("Give image with color==\n",img1)


cv2.waitKey(0)  #here parameter inside waitkey handle the life duration of an image
cv2.destroyAllWindows()
```

#### How to resize image

```py
import cv2    #openCV use as cv2 in python

#Loads a color image. Any transparency of image will be neglected. It is the default flag.
#this function is used to read the image from location
img1 = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg',1)
img1 = cv2.resize(img1,(1280,700))#width ,height
cv2.imshow("Colored Image",img1)  #It accept two parameters 1)- Name of screen ,2) -  Image
print("Give image with color==\n",img1)



cv2.waitKey(0)  #here parameter inside waitkey handle the life duration of an image
cv2.destroyAllWindows()
```

#### How to read image in gray-scale(black and white)

```py
import cv2    #openCV use as cv2 in python

#cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
img2 = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg',0)
img2 = cv2.resize(img2,(1280,700))#width ,height
cv2.imshow("Gray Scale Image",img2)
print("Image in gray scale==\n",img2)


cv2.waitKey(0)  #here parameter inside waitkey handle the life duration of an image
cv2.destroyAllWindows()
```

#### How to read image with alpha channel

```py
import cv2    #openCV use as cv2 in python

#cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
img3 = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg',-1)
img3 = cv2.resize(img3,(1280,700))#width ,height
cv2.imshow("Original Image",img3)
print("Image in original value==\n",img3)

cv2.waitKey(0)  #here parameter inside waitkey handle the life duration of an image
cv2.destroyAllWindows()
```

#### Putting all images together for comparison

```py
import cv2    #openCV use as cv2 in python

#Loads a color image. Any transparency of image will be neglected. It is the default flag.
#this function is used to read the image from location
img1 = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg',1)
img1 = cv2.resize(img1,(1280,700))#width ,height
cv2.imshow("Colored Image",img1)  #It accept two parameters 1)- Name of screen ,2) -  Image
print("Give image with color==\n",img1)

#cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
img2 = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg',0)
img2 = cv2.resize(img2,(1280,700))#width ,height
cv2.imshow("Gray Scale Image",img2)
print("Image in gray scale==\n",img2)

#cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
img3 = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg',-2)
img3 = cv2.resize(img3,(1280,700))#width ,height
cv2.imshow("Original Image",img3)
print("Image in original value==\n",img3)

cv2.waitKey(0)  #here parameter inside waitkey handle the life duration of an image
cv2.destroyAllWindows()
```

#### How to take path of image from console

```py
import cv2    #openCV use as cv2 in python

#Image conversion project colored image into grayscale.

path = input("Enter the Path and name of an image===")
print("You Enter this===",path)

#Now read image
img1 = cv2.imread(path,0) #convert image into grayscale
img1 = cv2.resize(img1,(560,700))
cv2.imshow("converted image==",img1)

cv2.waitKey(0)  #here parameter inside waitkey handle the life duration of an image
cv2.destroyAllWindows()

```

#### How to flip image

```py
import cv2    #openCV use as cv2 in python

#Image conversion project colored image into grayscale.


#Now read image
img1 = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg',0) #convert image into grayscale
img1 = cv2.resize(img1,(560,700))
img1 = cv2.flip(img1,0)#it accept 3 parameters 0,-1,1

cv2.imshow("converted image==",img1)

cv2.waitKey(0)  #here parameter inside waitkey handle the life duration of an image
cv2.destroyAllWindows()

```

#### How to save image using logic

```py
import cv2    #openCV use as cv2 in python

#Image conversion project colored image into grayscale.

#Now read image
img1 = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg',0) #convert image into grayscale
img1 = cv2.resize(img1,(560,700))

cv2.imshow("converted image==",img1)

k = cv2.waitKey(0) & 0xFF

if k == ord("q"):
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("C:\\Users\\91958\\Pictures\\output.jpg",img1)  #it accept name of image and data
    cv2.destroyAllWindows()
```

<br>

### 4 - Read,write and save video using opencv

#### How to read video from local disk

```py
#How to read Video from any folder using opencv

import cv2

#Here with the help of videoCapture fucntion we easily ready any video.

cap = cv2.VideoCapture("C:\\Users\\91958\\Pictures\\turtle.mp4")   #Here parameter is a path of any video

while True:
    ret, frame = cap.read()   #here read the frame
    #get height and width of frame
    print("Width ==>",cv2.CAP_PROP_FRAME_WIDTH)
    print("Height==>",cv2.CAP_PROP_FRAME_HEIGHT)

    frame = cv2.resize(frame,(700,450))
    cv2.imshow('Colorframe',frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):   #press to exit
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
```

#### How to perform grayscale operation and flip video

```py
#How to read Video from any folder using opencv

import cv2

#Here with the help of videoCapture fucntion we easily ready any video.

cap = cv2.VideoCapture("C:\\Users\\91958\\Pictures\\turtle.mp4")   #Here parameter is a path of any video

while True:
    ret, frame = cap.read()   #here read the frame
    #get height and width of frame
    print("Width ==>",cv2.CAP_PROP_FRAME_WIDTH)
    print("Height==>",cv2.CAP_PROP_FRAME_HEIGHT)

    frame = cv2.resize(frame,(700,450))
    gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame,-1)
    cv2.imshow('Colorframe',frame)
    cv2.imshow("Gray Frame",gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):   #press to exit
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
```

#### How to read video from webcam

```py
#How to read Video from any folder using opencv

import cv2



#Capture  video from webcam and save it

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   #Here parameter 0 is a path of any video use for webcam
print("check===",cap.isOpened())

#it is 4 byte code which is use to specify the video codec
#Various codec --
#DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0)

while(cap.isOpened()):
    ret, frame = cap.read()   #here read the frame

    if ret==True:

        gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #here flip is used to lip the video at recording time
        frame = cv2.flip(frame,0)
        output.write(gray)

        cv2.imshow("Gray Frame",gray)
        cv2.imshow('Colorframe',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press to exit
            break
    else:
        break

# Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()
```

### 5 - Connect Mobile Camera in openCV

### 6 - Basic Screen Recording using OpenCV
