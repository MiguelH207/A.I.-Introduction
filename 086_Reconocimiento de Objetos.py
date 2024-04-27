# Miguel Angel Huerta Castillo     21310236
# Este programa en Python implementa un modelo de Percepción para el reconocimiento de objetos.
# Utiliza la biblioteca OpenCV para procesar imágenes y detectar objetos en ellas.

# Importamos la biblioteca OpenCV
import cv2

# Cargamos el archivo de configuración de la red neuronal pre-entrenada para la detección de objetos
net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')

# Cargamos la lista de nombres de clases
with open('yolov3_classes.txt', 'r') as f:
    classes = f.read().splitlines()

# Cargamos la imagen de prueba
img = cv2.imread('sample_image.jpg')

# Obtenemos las dimensiones de la imagen
height, width, _ = img.shape

# Normalizamos la imagen
blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0, 0, 0), swapRB=True, crop=False)

# Pasamos la imagen normalizada a través de la red neuronal
net.setInput(blob)
output_layers_names = net.getUnconnectedOutLayersNames()
layer_outputs = net.forward(output_layers_names)

# Inicializamos listas para almacenar información de detección
boxes = []
confidences = []
class_ids = []

# Iteramos sobre las salidas de cada capa
for output in layer_outputs:
    # Iteramos sobre cada detección
    for detection in output:
        # Extraemos la clase, confianza y coordenadas de la caja del objeto detectado
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            x = int(center_x - w/2)
            y = int(center_y - h/2)
            # Agregamos las coordenadas, confianza y clase a las listas respectivas
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Aplicamos la supresión de no máximos para eliminar detecciones redundantes
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# Iteramos sobre los índices de detección
for i in range(len(boxes)):
    if i in indexes:
        # Obtenemos las coordenadas y el nombre de la clase
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        # Dibujamos la caja del objeto y etiqueta en la imagen
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Mostramos la imagen con las detecciones
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
