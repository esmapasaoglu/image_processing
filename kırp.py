import cv2
import numpy as np
img= cv2. imread("scenery.jpg")
cv2.imshow("Scenery" ,img)


imgCropped = img[:200, 0:300]

cv2.imshow("Cropped Image", imgCropped)
 
cv2.waitKey(0)
cv2.destroyAllWindows() 
