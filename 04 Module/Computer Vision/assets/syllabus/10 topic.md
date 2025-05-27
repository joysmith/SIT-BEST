## Filtering techniques

- Face Stylization demo [mediapipe](https://mediapipe-studio.webapps.google.com/studio/demo/face_stylizer)


```py
#Start with Basic operations on Image
import cv2
import numpy as np

#Read an Image---
img = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg')
img = cv2.resize(img,(600,400))
cv2.imshow("res",img)

print("shape==",img.shape) #returns a tuple of number of rows, columns, and channels
print("no.of pixels==",img.size) #returns Total number of pixels is accessed
print("datatype==",img.dtype) #returns Image datatype is obtained
print("Imagetype==",type(img))

#Now try to split an image
#split  -  return 3 channel of ur image which is blue,green,red
#print(cv2.split(img))
b,g,r = cv2.split(img)

cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
#Now if you want to mix the the channels then use merge

mr1 = cv2.merge((r,g,b))
cv2.imshow("rgb",mr1)
mr2 = cv2.merge((g,b,r))
cv2.imshow("gbr",mr2)

cv2.waitKey()
cv2.destroyAllWindows()

```

```py
#Start with Basic operations on Image
import cv2
import numpy as np


img = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg')
img = cv2.resize(img,(1024,700))
cv2.imshow("lion==",img)

#access a pixel value by its row and column coordinates.
px = img[520,580] #store cordinate in variable
print("the pixel of that co-ordinates==",px) #we get the pixel value

#Now try to find selected channel value from cordinate
#We know we have three channel -   0,1,2
# accessing only blue pixel
blue = img[520,580,0]
print("the pixel having blue color==",blue)

grn = img[520,580,1] #for green pass 1
print("the pixel having grn color==",grn)
red = img[520,580,2] #for red pass 2
print("the pixel having red color==",red)

cv2.waitKey(0)
cv2.destroyAllWindows()

```

### 14 Image blending

```py
#Image Blending with open cv
#Here We use two important functions cv2.add(), cv2.addWeighted() etc.
#Blending means addition of two images
#if you want to blend two images then both have same size
import cv2
import numpy as np

#read two different images of same channel
img1 = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg')
img1 = cv2.resize(img1,(500,700))
img2 = cv2.imread('C:\\Users\\91958\\Pictures\\tiger.jpg')
img2 = cv2.resize(img2,(500,700))
cv2.imshow("thor==",img1)
cv2.imshow("bro_thor==",img2)

#Now perform blending
result = img2+img1  #numpy addition in this we get module between value
#recommended to use cv2.add
result1 = cv2.add(img1,img2) #its your saturated oprn which means value to value

#sum of both the weight  = w1+w2 = 1(max)
#function cv2.addWeighted(img1,wt1,img2,wt2,gama_val)
result2 = cv2.addWeighted(img1,0.7,img2,0.3,0)

#cv2.imshow("result==",result)
#cv2.imshow("result1==",result1)
cv2.imshow("result2 = ",result2)

cv2.waitKey(0)
cv2.destroyAllWindows()

```

### 15 Image blending project

```py
#result Blending with Trackbars

import numpy as np
import cv2 as cv
#read two different images of same channel
img1 = cv.imread('C:\\Users\\91958\\Pictures\\fox.jpg')
img1 = cv.resize(img1,(500,700))
img2 = cv.imread('C:\\Users\\91958\\Pictures\\tiger.jpg')
img2 = cv.resize(img2,(500,700))

def blend(x):
    pass

img = np.zeros((400,400,3),np.uint8)
cv.namedWindow('win') #create track bar windows
cv.createTrackbar('alpha','win',1,100,blend)
switch = '0 : OFF \n 1 : ON'  #create switch for invoke the trackbars
cv.createTrackbar(switch,'win',0,1,blend)  #create track bar for switch
while(1):
    alpha = cv.getTrackbarPos('alpha','win')

    s = cv.getTrackbarPos(switch,'win')
    na = float(alpha/100)

    if s == 0:
        dst = img[:]
    else:
        dst = cv.addWeighted(img1,1-na,img2,na,0)
        cv.putText(dst, str(alpha), (20, 50), cv.FONT_ITALIC,
                   2, (0, 125, 255), 2)
    cv.imshow('dst',dst)

    k=cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.waitKey(0)

cv.destroyAllWindows()
```

### 25

```py

#Image Smoothing or bluring is most common used operation in Image Processing.
#It is use to remove noise from the images.
#There are so many filter  which is use for smoothing the image.
#There are LOW Pass Filter(LPS) which use to remove Noise from the images.
#There are High Pass Filter which use to detect and finding edges in an image.

#we discuss about various filters --
#like , homogeneous,blur(averaging),homogeneous,median,bilateral


import cv2
import numpy as np


img = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg')
img = cv2.resize(img,(400,400))
cv2.imshow("original==",img)
#define a kernal for homogeneous function
kernel = np.ones((5,5),np.float32)/25

#FILTER NUMBER -----1
#this filter  work like, each output pixel is the mean of its kernal neigbours
#it is aka homogeneous filter in this all pixel contribute with equal weight.
#kernal is a small shape or matrix which we apply on image.
#in this filter kernal is [(1/kernal(h,w))*kernal]
h_filter = cv2.filter2D(img,-1,kernel) # -1 is desired depth
cv2.imshow("homogeneous==",h_filter)

#FILtER NUMBER 2-----
#blur method or averaging
#takes the avg of all the pixels under kernel area and
#replaces the central element with this average..
blur = cv2.blur(img,(8,8)) #here we have image and kernel as parameter
cv2.imshow("blur==",blur)

#Filter Number 3------
#Gaussian Filter -here it using different weight kernel,in  row as well as col.
#means side values are small then centre .It manage distance b/w value of pixel.

gau= cv2.GaussianBlur(img,(5,5),0) #here 0 is sigma x value
cv2.imshow("gau blur=",gau)


#Filter Number 4--
#Median Filter --computes the median of all the pixels under the
#kernel window and the central pixel is replaced with this median value.
# This is highly effective in removing salt-and-pepper noise.
#here kernal size must be odd except one
med = cv2.medianBlur(img,5)
cv2.imshow("median filter",med)

#bilateral filter --- is highly effective at noise removal while preserving edges.
#It work like gaussian filter but more focus on edges
#it is slow as compare with other filters
#argument (img, neigbour_pixel_diameter,sigma_color,sigma_space)
bi_f = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("bi_f",bi_f)


#Now plot all the images on graph
titles = ["original_image","homo","blur","gauss","med","bi_f"]
images = [img,h_filter,blur,gau,med,bi_f]

#if you want then plot it
from matplotlib import pyplot as plt
for i in range(6):
    plt.subplot(2, 3, i+1),
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 26 Image gradient

```py
#Image Gradient--
#It is a directional change in the color or intensity in an image.
#It is most important part to find inormation from image
#Like finding edges within the images.
#There are various methods to find image gradient.
#These are - Laplacian Derivatives,SobelX and SobelY.
#All these functions have diff. mathematical approach to get result.
#All load image in the gray scale

#Don't Worry about Mathematics behind all these function
#we just use these to get our work in easy manner.

import cv2
import numpy as np


#load image into gray scale
img = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg')
img = cv2.resize(img,(400,300))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Laplacian Derivative---It calculate laplace derivate
#parameter(img,data_type for -ve val,ksize)
#kernal size must be odd
lap = cv2.Laplacian(img_gray,cv2.CV_64F,ksize = 3) #also pass kernal size
lap = np.uint8(np.absolute(lap))

#Sobel operation -
# is a joint Gausssian smoothing plus differentiation operation,
#so it is more  resistant to noise
#This is use for x and y bth
#parameter (img,type for -ve val,x = 1,y = 0,ksize)
#Sobel X focus on vertical lines
#Sobel y focus on horizontal lines

sobelX = cv2.Sobel(img_gray,cv2.CV_64F,1,0,ksize = 3) #here 1 means x direction
sobelY = cv2.Sobel(img_gray,cv2.CV_64F,0,1,ksize = 3) #here 1 means y direction

sobelX = np.uint8(np.absolute(sobelX))
sobelY= np.uint8(np.absolute(sobelY))

#finally combine sobelX and sobelY togather
sobelcombine = cv2.bitwise_or(sobelX,sobelY)

cv2.imshow("original==",img)
cv2.imshow("gray====",img_gray)
cv2.imshow("Laplacian==",lap)
cv2.imshow("SobelX===",sobelX)
cv2.imshow("SobelY==",sobelY)
cv2.imshow("COmbined image==",sobelcombine)



#Now plot all the images on graph
titles = ["original","gray","laplacian","sobelX","sobelY","combined"]
images = [img,img_gray,lap,sobelX,sobelY,sobelcombine]

#if you want then plot it
from matplotlib import pyplot as plt
for i in range(6):
    plt.subplot(3,2, i+1),
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

cv2.waitKey(0)
cv2.destroyAllWindows()

```

### 27 canny image

```py
#Canny Edge Detection using OpenCV
#Canny Edge Detection is a popular edge detection approach.
#It is use  multi-stage algorithm to detect a edges.
#It was developed by John F. Canny in 1986.
#This approach combine with 5 steps.
# 1) -  NOise reduction(gauss)), 2) -Gradient calculation( ,
# 3) - Non-maximum suppresson, 4) - Double Threshold,
# 5) - Edge Tracking by Hysteresis




import cv2
import numpy as np

#load image into gray scale
img = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg')
img = cv2.resize(img,(600,700))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#canny(img,thresh1,thres2)thresh 1 and thresh2 at different lvl
canny = cv2.Canny(img_gray,20,150)

cv2.imshow("original==",img)
cv2.imshow("gray====",img_gray)
cv2.imshow("canny==",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

```py

#Canny Edge Detection using OpenCV
#Canny Edge Detection is a popular edge detection approach.
#It is use  multi-stage algorithm to detect a edges.
#It was developed by John F. Canny in 1986.
#This approach combine with 5 steps.
# 1) -  NOise reduction(gauss)), 2) -Gradient calculation( ,
# 3) - Non-maximum suppresson, 4) - Double Threshold,
# 5) - Edge Tracking by Hysteresis




import cv2
import numpy as np


#building trackbar with canny edge

#load image into gray scale
img = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg')
img = cv2.resize(img,(600,700))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def nothing(x):
    pass

cv2.namedWindow("Canny")
cv2.createTrackbar("Threshold", "Canny", 0, 255, nothing)

while True:
    a= cv2.getTrackbarPos('Threshold','Canny')

    print(a)
    res = cv2.Canny(img_gray,a,255)
    cv2.imshow("Canny",res)
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

```

### 28 pyramid image

```py

#Image Pyramids in OpenCV
"""
We use Image Pyramid because somethimes we work on same imge
but different resolution.e.g. searching face, eye in an image
and it vary image to image so in this case we create a set
of images with diff. resolution which is called pyramid.
We also use these pyramids to blends the images.
"""
#There are two types of Image Pyramid-
# 1) Gaussian Pyramid and 2) Laplacian Pyramids


import cv2
import numpy as np


#load image into gray scale
img = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg')
img = cv2.resize(img,(700,700))

#Gaussian Pyramid Have 2 function-1) cv2.pyrUp(),2)-cv2.pyrDown()
#pyrdown----
pd1 = cv2.pyrDown(img)
pd2 = cv2.pyrDown(pd1)

#pyrup
#if we pyrup any pyrdown image both are not equal
pu1 = cv2.pyrUp(pd2)


#results------------------
cv2.imshow("original==",img)
cv2.imshow("pd1==",pd1)
cv2.imshow("pd2==",pd2)
cv2.imshow("pu1==",pu1)

cv2.waitKey(0)
cv2.destroyAllWindows()


```

```py

#Image Pyramids in OpenCV
"""
We use Image Pyramid because somethimes we work on same imge
but different resolution.e.g. searching face, eye in an image
and it vary image to image so in this case we create a set
of images with diff. resolution which is called pyramid.
We also use these pyramids to blends the images.
"""
#There are two types of Image Pyramid-
# 1) Gaussian Pyramid and 2) Laplacian Pyramids


import cv2
import numpy as np



img = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg')
img = cv2.resize(img,(700,700))

img1 = img.copy()
data = [img1]

for i in range(4):
    img1 = cv2.pyrDown(img1)
    data.append(img1)
    cv2.imshow("res"+str(i),img1)

cv2.imshow("original==",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 38 background removal

```py

#GrabCut Algoritm with the help of this algoritm we easily
#cutoff any foreground object from image or video.
#It works like a rectangle portion mark on the image
#and area outise the rectangle is treat as a extra part
#so this algo remove it completely.
#Gaussian mixtuere model help to achieve the target



import	numpy  as  np
import	cv2

img  =	cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg')
img = cv2.resize(img,(800,800))
mask =	np.zeros(img.shape[:2],np.uint8)


bgdModel =  np.zeros((1,65),np.float64)*255
fgdModel =  np.zeros((1,65),np.float64)*255

#parameter(img,mask,rect,bgmodel,fgmodel,iter,method)
rect =	(134,150,660,730)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,
            cv2.GC_INIT_WITH_RECT)


mask2  =  np.where((mask==2)|(mask==0),0,1).astype('uint8')
img  =	img*mask2[:,:,np.newaxis]

cv2.imshow("res==",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

### 40 background subraction video

```py
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 16:35:31 2020

@author: NISHANT
"""
#Background Subtraction is a way to access the foreground objects.
#Technically, you need to extract the moving
#foreground from static background.
#There are multiple approach for backgroud subtract

#We discuss all of them.

import numpy as np
import cv2 as cv
cap = cv.VideoCapture('C:\\Users\\91958\\Pictures\\turtle.mp4')


#old_algo = cv.bgsegm.createBackgroundSubtractorMOG()
algo1 = cv.createBackgroundSubtractorMOG2(detectShadows=True) #algo1
algo2 = cv.createBackgroundSubtractorKNN(detectShadows=True)  #algo2
while True:
    ret, frame = cap.read()
    frame = cv.resize(frame,(600,400))
    if frame is None:
        break
    res1 = algo1.apply(frame)
    res2 = algo2.apply(frame)


    cv.imshow('original', frame)
    cv.imshow('res1',res1)
    cv.imshow('res2',res2)

    keyboard = cv.waitKey(60)
    if keyboard == 'q' or keyboard == 27:
        break
cap.release()
cv.destroyAllWindows()

```
