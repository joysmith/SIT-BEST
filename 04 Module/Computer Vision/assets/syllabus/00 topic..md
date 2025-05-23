## Basic knowledge of computer vision systems

#### Download Anaconda IDE

- [Download and Install](https://www.anaconda.com/download/success)
- [Download and extract](<../resource/image and video.zip>)

#### Try with google collab

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
