## Image segmentation

- Image segmentation demo [mediapipe](https://mediapipe-studio.webapps.google.com/studio/demo/image_segmenter)


- Interactive segementation demo [mediapipe](https://mediapipe-studio.webapps.google.com/studio/demo/interactive_segmenter)


29 - Contours and its Introduction

30 - Contour and its functions

31 - Contours and its Properties

32 - Contour detection using webcam

33 - Image Histogram and Utilization

34 - Image BackProjection using OpenCv

35 - Template Matching using opencv

36 - Hough Tranform using Opencv

37 - Circle detection using webcam

38 - Background removal using grabcut algo

### 16 bitwise operation

```py
#Bitwise Operations includes AND, OR, NOT and XOR
#It is most important and use for various purpose like masking
#and find roi(region of intereset) which is in complex shape.

import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1,(150, 100), (200, 250), (255, 255, 255), -1)
img2 = np.zeros((250, 500, 3), np.uint8)
img2 = cv2.rectangle(img2,(10, 10), (170, 190), (255, 255, 255), -1)

bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img2, img1)
bitXor = cv2.bitwise_xor(img1, img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

#cv2.imshow('bitAnd', bitAnd)
#cv2.imshow('bitOr', bitOr)
#cv2.imshow('bitXor', bitXor)
#cv2.imshow('bitNot1', bitNot1)
#cv2.imshow('bitNot2', bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()
```
