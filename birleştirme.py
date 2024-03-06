import cv2
import numpy as np
img= cv2. imread("scenery.jpg")


#horizontal (yatay) birleştirme
hor = np.hstack((img,img))
cv2.imshow("horizontal", hor)


#vertical (dikey) birleştirme
ver = np.vstack((img,img))
cv2.imshow("vertical", ver)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows() 
