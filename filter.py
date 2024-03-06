import cv2
import numpy as np

def apply_color_filter(scenery.jpg,color):
  
    # Görüntüyü BGR formatından RGB formatına dönüştür
    image_rgb = cv2.cvtColor(scenery.jpg, cv2.COLOR_BGR2RGB)

    # Renk filtresini uygula
    if color == 'red':
        lower_bound = np.array([0, 0, 100])
        upper_bound = np.array([100, 100, 255])
    elif color == 'green':
        lower_bound = np.array([0, 100, 0])
        upper_bound = np.array([100, 255, 100])
    elif color == 'blue':
        lower_bound = np.array([100, 0, 0])
        upper_bound = np.array([255, 100, 100])
    else:
        raise ValueError("Geçersiz renk filtresi")

    color_mask = cv2.inRange(image_rgb, lower_bound, upper_bound)
    filtered_image = cv2.bitwise_and(image_rgb, image_rgb, mask=color_mask)

    return filtered_image  

# Giriş görüntüsü yükleniyor
input_image_path = 'img_processing\scenery.jpg'
original_image = cv2.imread(input_image_path)

# Renk filtreleri uygulanıyor
red_filtered = apply_color_filter(original_image, 'red')
green_filtered = apply_color_filter(original_image, 'green')
blue_filtered = apply_color_filter(original_image, 'blue')

# Sonuçları görselleştirme
cv2.imshow('Original Image', cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
cv2.imshow('Red Filtered', red_filtered)
cv2.imshow('Green Filtered', green_filtered)
cv2.imshow('Blue Filtered', blue_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
