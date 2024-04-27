# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo simple de Perceptrón utilizando movimientos como características. 
# El Perceptrón intentará clasificar si un objeto se está moviendo hacia la izquierda, hacia la derecha o si no se está moviendo en absoluto.

import numpy as np  # Importa la librería NumPy para cálculos numéricos

# Definición de la función de activación
def activation_function(x):  # Define una función de activación
    return 1 if x >= 0 else 0  # Retorna 1 si x es mayor o igual a cero, de lo contrario retorna 0

# Definición de la función de predicción
def predict(inputs, weights):  # Define una función para realizar predicciones
    summation = np.dot(inputs, weights)  # Realiza el producto punto entre las entradas y los pesos
    output = activation_function(summation)  # Aplica la función de activación al resultado del producto punto
    return output  # Retorna la salida de la predicción

# Entradas de entrenamiento (movimientos: izquierda, derecha, quieto)
training_inputs = np.array([
    [0, 0, 1],  # Objeto quieto
    [1, 1, 1],  # Objeto moviéndose hacia la derecha
    [1, 0, 1],  # Objeto moviéndose hacia la derecha
    [0, 1, 1]   # Objeto moviéndose hacia la izquierda
])

# Etiquetas de entrenamiento (0: quieto, 1: derecha, -1: izquierda)
labels = np.array([0, 1, 1, -1])  

# Pesos iniciales aleatorios
weights = np.random.rand(3)  # Inicializa los pesos aleatoriamente

# Definición de la tasa de aprendizaje
learning_rate = 0.01  # Tasa de aprendizaje para ajustar los pesos

# Entrenamiento del perceptrón
for _ in range(100):  # Itera 100 veces para entrenar el perceptrón
    for inputs, label in zip(training_inputs, labels):  # Itera sobre las entradas y etiquetas de entrenamiento
        prediction = predict(inputs, weights)  # Realiza una predicción con las entradas y los pesos actuales
        weights += learning_rate * (label - prediction) * inputs  # Ajusta los pesos basado en el error de la predicción

# Prueba del perceptrón con nuevos datos
new_inputs = np.array([1, 0, 1])  # Nuevas entradas para probar el perceptrón
output = predict(new_inputs, weights)  # Realiza una predicción con las nuevas entradas y los pesos entrenados

# Imprime el resultado de la predicción
if output == 1:
    print("El objeto se está moviendo hacia la derecha.")
elif output == -1:
    print("El objeto se está moviendo hacia la izquierda.")
else:
    print("El objeto está quieto.")
