# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo práctico de Aprendizaje Profundo (Deep Learning) utilizando TensorFlow en Python.
# El ejemplo consiste en entrenar una red neuronal para clasificar imágenes de dígitos escritos a mano del conjunto de datos MNIST.

# Importar las bibliotecas necesarias
import tensorflow as tf  # Importar TensorFlow para construir y entrenar modelos de aprendizaje profundo
from tensorflow.keras import layers, models  # Importar capas y modelos de Keras, interfaz de alto nivel para construir y entrenar modelos en TensorFlow
from tensorflow.keras.datasets import mnist  # Importar el conjunto de datos MNIST

# Cargar el conjunto de datos MNIST, que contiene imágenes de dígitos escritos a mano y sus etiquetas correspondientes
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocesar los datos: Escalar las imágenes al rango [0, 1] dividiendo cada valor de píxel por 255
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

# Definir la arquitectura de la red neuronal convolucional
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),  # Capa convolucional con 32 filtros de tamaño 3x3, función de activación ReLU y forma de entrada (28, 28, 1)
    layers.MaxPooling2D((2, 2)),  # Capa de agrupación máxima con una ventana de tamaño 2x2
    layers.Conv2D(64, (3, 3), activation='relu'),  # Capa convolucional con 64 filtros de tamaño 3x3 y función de activación ReLU
    layers.MaxPooling2D((2, 2)),  # Capa de agrupación máxima con una ventana de tamaño 2x2
    layers.Conv2D(64, (3, 3), activation='relu'),  # Capa convolucional con 64 filtros de tamaño 3x3 y función de activación ReLU
    layers.Flatten(),  # Capa de aplanamiento para convertir los datos en un formato adecuado para la capa completamente conectada
    layers.Dense(64, activation='relu'),  # Capa completamente conectada con 64 unidades y función de activación ReLU
    layers.Dense(10, activation='softmax')  # Capa completamente conectada con 10 unidades y función de activación Softmax para la clasificación de 10 clases (dígitos del 0 al 9)
])

# Compilar el modelo especificando la función de pérdida, el optimizador y las métricas a monitorear durante el entrenamiento
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',  # Utilizar la entropía cruzada categórica escasa como función de pérdida
              metrics=['accuracy'])  # Monitorear la precisión durante el entrenamiento

# Entrenar el modelo utilizando los datos de entrenamiento
model.fit(train_images, train_labels, epochs=5, batch_size=64)

# Evaluar el modelo con los datos de prueba
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)
