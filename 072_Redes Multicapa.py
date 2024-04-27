# Miguel Angel Huerta Castillo     21310236
# Este programa implementa una red neuronal multicapa utilizando la biblioteca TensorFlow en Python.
# La red neuronal se entrena con un conjunto de datos de ejemplos y luego se utiliza para predecir la clase de un nuevo ejemplo.
# El ejemplo práctico consiste en entrenar la red para reconocer dígitos escritos a mano utilizando el conjunto de datos MNIST.

# Importar las bibliotecas necesarias
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist

# Cargar los datos de entrenamiento y prueba MNIST
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalizar los valores de píxeles entre 0 y 1
train_images, test_images = train_images / 255.0, test_images / 255.0

# Definir la arquitectura de la red neuronal
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Capa de entrada que aplanará la imagen 28x28 en un vector de 784 elementos
    layers.Dense(128, activation='relu'),  # Capa oculta con 128 neuronas y función de activación ReLU
    layers.Dropout(0.2),                   # Capa de dropout para regularización con una tasa de 0.2
    layers.Dense(10, activation='softmax') # Capa de salida con 10 neuronas (una para cada dígito) y función de activación softmax
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo con los datos de entrenamiento
model.fit(train_images, train_labels, epochs=5)

# Evaluar el modelo con los datos de prueba
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)

# Realizar predicciones con el modelo entrenado
predictions = model.predict(test_images)
