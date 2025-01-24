import numpy as np  #NumPy (Numerical Python) is a Python library used for numerical computations and working with arrays.
import cv2          #OpenCV (Open Source Computer Vision Library) is a library focused on real-time computer vision and image processing tasks.

color =cv2.imread("butterfly.jpg",1)

gray  = cv2.cvtColor(color,cv2.COLOR_RGB2GRAY)
cv2.imwrite("gray.jpg",gray)

b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

rgba = cv2.merge((b,g,r,g))
cv2.imwrite("rgba.png",rgba)

