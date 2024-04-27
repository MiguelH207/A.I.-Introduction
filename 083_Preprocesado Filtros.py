# Miguel Angel Huerta Castillo 21310236
# Programa de Percepción en Python usando Preprocesado: Filtros
# Este programa realiza el preprocesamiento de una imagen utilizando filtros.
# Se aplica un filtro de suavizado para eliminar el ruido de la imagen.
# El filtro de suavizado utilizado es el filtro de media.
# El programa utiliza la biblioteca OpenCV para cargar y mostrar la imagen, así como para aplicar el filtro.

import cv2  # Importa la biblioteca OpenCV para el procesamiento de imágenes

# Define la función para aplicar el filtro de suavizado
def aplicar_filtro_suavizado(imagen):
    # Aplica un filtro de media a la imagen con un kernel de 5x5
    imagen_suavizada = cv2.blur(imagen, (5, 5))
    return imagen_suavizada  # Retorna la imagen suavizada

# Carga la imagen desde el archivo
imagen_original = cv2.imread("imagen.jpg")

# Aplica el filtro de suavizado a la imagen
imagen_suavizada = aplicar_filtro_suavizado(imagen_original)

# Muestra la imagen original y la imagen suavizada
cv2.imshow("Imagen Original", imagen_original)
cv2.imshow("Imagen Suavizada", imagen_suavizada)

# Espera hasta que se presione una tecla
cv2.waitKey(0)

# Cierra todas las ventanas
cv2.destroyAllWindows()
