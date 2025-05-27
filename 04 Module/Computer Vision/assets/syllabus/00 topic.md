## Setting up the system 

### ✅(recommended) Window Download Anaconda IDE

- Download and Install [setup](https://www.anaconda.com/download/success)
- Download and extract [Exercise file](<../resource/image and video.zip>)

#### Boiler plate code 

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

<br>

### ✅(recommended) Linux Download Anaconda IDE

- Download and Install [setup](https://www.anaconda.com/download/success)
- Download and extract [Exercise file](<../resource/image and video.zip>)


#### How to open anaconda navigator

1. invoke terminal from anaoconda location.
2. type "activate" hit enter.
3. type "anaconda-navigator" hit enter.

#### Boiler plate code

```py
import cv2    #openCV use as cv2 in python

#Loads a color image. Any transparency of image will be neglected. It is the default flag.
#this function is used to read the image from location
img1 = cv2.imread("/home/joy/Pictures/cat.jpg",1)
img1 = cv2.resize(img1,(1280,700))#width ,height
cv2.imshow("Colored Image",img1)  #It accept two parameters 1)- Name of screen ,2) -  Image
print("Give image with color==\n",img1)


cv2.waitKey(0)  #here parameter inside waitkey handle the life duration of an image
cv2.destroyAllWindows()
```

<br>

### ❌(not recommended) Google collab IDE

1. [Google collab](https://colab.research.google.com/)
2. Go to file--> new notebook in drive
3. On left-side panel click on folder-icon--> right click -->upload--> (select any image from local disk)
4. copy code to cell

```py
# Import the specific function for displaying images in Google Colab
from google.colab.patches import cv2_imshow

#Loads a color image. Any transparency of image will be neglected. It is the default flag.
#this function is used to read the image from location
img1 = cv2.imread('fox.jpg',1)
# Use the Colab-specific function to display the image
cv2_imshow(img1)  # It accepts the image as a parameter
print("Give image with color==\n",img1)
```

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
