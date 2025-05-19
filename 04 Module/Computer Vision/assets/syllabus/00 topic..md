## Basic knowledge of computer vision systems

#### Download Anaconda IDE

- [Download and Install](https://www.anaconda.com/download/success)
- Open anaconda

### Boiler plate code

```py
import cv2    #pip install opencv-python

#Loads a color image. Any transparency of image will be neglected. It is the default flag.
#this function is used to read the image from location
img1 = cv2.imread('C:\\Users\\91958\\Pictures\\fox.jpg',1)
cv2.imshow("Colored Image",img1)  #It accept two parameters 1)- Name of screen ,2) -  Image
print("Give image with color==\n",img1)


cv2.waitKey(0)  #here parameter inside waitkey handle the life duration of an image
cv2.destroyAllWindows()
```
