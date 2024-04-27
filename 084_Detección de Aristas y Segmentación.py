# Miguel Angel Huerta Castillo     21310236
# Este programa realiza detección de bordes y segmentación en una imagen utilizando la librería OpenCV en Python.
# La detección de bordes se realiza utilizando el algoritmo de Canny, que detecta cambios abruptos de intensidad en la imagen.
# Luego, se aplica segmentación utilizando el algoritmo de umbralización para separar las regiones de interés de la imagen.

# Importar la librería OpenCV
import cv2

# Leer la imagen de entrada
image = cv2.imread('image.jpg')

# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar el algoritmo de Canny para detectar bordes
edges = cv2.Canny(gray_image, 100, 200)

# Aplicar umbralización para segmentar la imagen
ret, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Mostrar la imagen original
cv2.imshow('Original Image', image)

# Mostrar la imagen de bordes detectados
cv2.imshow('Edge Detected Image', edges)

# Mostrar la imagen binarizada segmentada
cv2.imshow('Segmented Image', binary_image)

# Esperar a que se presione una tecla y luego cerrar todas las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
