import cv2

# resmi oku
img = cv2.imread("scenery.jpg", 0)
print("Image size: ", img.shape)

cv2.imshow("Orginal", img)
if cv2.waitKey(0) & 0xFF == ord("q"): 
    cv2.destroyAllWindows()