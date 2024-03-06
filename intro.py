import cv2
import numpy as np
img= cv2. imread("scenery.jpg")
cv2.imshow("Scenery" ,img)

#resmi ice aktar
img = cv2.resize(cv2.imread("scenery.jpg"),(256,256))

cv2.imshow("original", img)

cv2.waitKey(0)
cv2.destroyAllWindows() 
