import cv2
import numpy as np

# siyah resim 
img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

#line ekleme
cv2.line(img,       #resim
         (0,0),     #baslangic noktasi
         (512,512), #bitis noktasi
         (0,254,0), #renk
         2, )       #kalinlik
         
cv2.imshow("line", img)

#dikdortgen ekleme
cv2.rectangle(img,       #resim
         (0,0),          #baslangic noktasi
         (256,256),      #bitis noktasi
         (200,100,0),    #renk
         2, )            #kalinlik

cv2.imshow("rectangle", img)
 
 
#cember cizimi
cv2.circle(img,         #resim
           (300,300),   #merkez
           45,          #yaricap
           (0,0,255),   #renk
           )

cv2.imshow("circle", img)


#Metin ekleme
cv2.putText(img,                       #resim
            "TEXT",                    #text
            (350,350),                 #baslangic noktasi
            cv2.FONT_HERSHEY_COMPLEX,  #font
            2,                       #kalinlik
            (255,0,255))             #renk

cv2.imshow("text", img)


if cv2.waitKey(0):
    cv2.destroyAllWindows()
    