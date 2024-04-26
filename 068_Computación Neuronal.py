# Miguel Angel Huerta Castillo     21310236
# Este programa implementa una red neuronal simple utilizando computación neuronal. Se crea una red neuronal con una sola neurona
# que aprende a realizar una operación de suma simple. Se utiliza el algoritmo de descenso de gradiente para entrenar la red
# y ajustar los pesos para minimizar el error.

import numpy as np  # Importa la librería numpy y la renombra como np

# Función de activación (función sigmoide)
def sigmoid(x):  
    return 1 / (1 + np.exp(-x))  # Retorna el valor de la función sigmoide aplicada a x

# Derivada de la función sigmoide
def sigmoid_derivative(x):  
    return x * (1 - x)  # Retorna la derivada de la función sigmoide evaluada en x

# Entradas de entrenamiento
training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Define las entradas de entrenamiento como una matriz numpy

# Salidas de entrenamiento
training_outputs = np.array([[0], [1], [1], [0]])  # Define las salidas de entrenamiento como una matriz numpy

# Semilla aleatoria para reproducibilidad
np.random.seed(1)

# Inicialización aleatoria de pesos
synaptic_weights = 2 * np.random.random((2, 1)) - 1  # Inicializa los pesos sinápticos de forma aleatoria

# Iteración de entrenamiento
for iteration in range(20000):  
    # Pasos de propagación hacia adelante
    input_layer = training_inputs  # La capa de entrada es la entrada de entrenamiento
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))  # Calcula las salidas utilizando la función sigmoide
    
    # Cálculo del error
    error = training_outputs - outputs  # Calcula el error restando las salidas esperadas de las salidas calculadas
    
    # Ajuste de pesos mediante el descenso de gradiente
    adjustments = error * sigmoid_derivative(outputs)  # Calcula los ajustes multiplicando el error por la derivada de la función sigmoide
    synaptic_weights += np.dot(input_layer.T, adjustments)  # Actualiza los pesos añadiendo el producto punto entre la transpuesta de la capa de entrada y los ajustes

# Imprime los pesos sinápticos después del entrenamiento
print("Pesos sinápticos después del entrenamiento:")
print(synaptic_weights)

# Imprime las salidas después del entrenamiento
print("Salidas después del entrenamiento:")
print(outputs)
