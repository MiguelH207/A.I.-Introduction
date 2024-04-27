# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un perceptrón simple utilizando etiquetados de líneas.
# El perceptrón se entrena para clasificar muestras de datos en dos clases distintas.
# El ejemplo práctico utilizado aquí es la clasificación de flores Iris en dos especies diferentes.

import numpy as np  # Importamos la librería numpy para operaciones matemáticas eficientes

class Perceptron:
    def __init__(self, input_size, learning_rate=0.01):  # Definimos el constructor del perceptrón
        self.input_size = input_size  # Tamaño de las entradas
        self.learning_rate = learning_rate  # Tasa de aprendizaje
        self.weights = np.zeros(input_size)  # Inicializamos los pesos a cero

    def predict(self, inputs):  # Método para predecir la salida del perceptrón
        summation = np.dot(inputs, self.weights)  # Sumatoria de las entradas multiplicadas por los pesos
        return 1 if summation > 0 else 0  # Función de activación: devuelve 1 si la sumatoria es mayor a cero, 0 en otro caso

    def train(self, training_inputs, labels, epochs):  # Método para entrenar el perceptrón
        for _ in range(epochs):  # Iteramos sobre el número de épocas de entrenamiento
            for inputs, label in zip(training_inputs, labels):  # Recorremos las muestras de entrenamiento y sus etiquetas
                prediction = self.predict(inputs)  # Realizamos una predicción con el perceptrón
                self.weights += self.learning_rate * (label - prediction) * inputs  # Actualizamos los pesos según el error de la predicción

# Datos de entrenamiento
training_inputs = np.array([[5.1, 3.5], [4.9, 3.0], [6.7, 3.1], [6.0, 3.0]])  # Características de las flores Iris
labels = np.array([1, 0, 1, 0])  # Etiquetas correspondientes a cada muestra (especie de flor)

# Creamos un perceptrón con dos entradas (dos características)
perceptron = Perceptron(2)

# Entrenamos el perceptrón con los datos de entrenamiento durante 10 épocas
perceptron.train(training_inputs, labels, epochs=10)

# Realizamos predicciones con el perceptrón entrenado
inputs = np.array([5.5, 3.6])  # Nuevas características de una flor Iris
print(perceptron.predict(inputs))  # Clasificamos la flor Iris en una de las dos especies posibles
