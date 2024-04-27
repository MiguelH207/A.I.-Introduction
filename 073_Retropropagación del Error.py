# Miguel Angel Huerta Castillo
# 21310236

# Este programa implementa una red neuronal de una capa oculta utilizando retropropagación del error para el entrenamiento.
# La red neuronal se entrena con un conjunto de datos de ejemplo para predecir la salida de una función lógica XOR.

import numpy as np  # Importamos la librería NumPy para realizar operaciones matemáticas eficientes

# Definimos la función de activación sigmoide y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))  # Retorna el valor de la función sigmoide aplicada a x

def sigmoid_derivative(x):
    return x * (1 - x)  # Retorna la derivada de la función sigmoide aplicada a x

# Definimos el conjunto de entrenamiento (entradas y salidas esperadas)
training_inputs = np.array([[0,0],[0,1],[1,0],[1,1]])  # Entradas para la función XOR
training_outputs = np.array([[0],[1],[1],[0]])  # Salidas esperadas para la función XOR

# Inicializamos los pesos de manera aleatoria
np.random.seed(1)  # Fijamos la semilla aleatoria para reproducibilidad
input_layer_neurons = 2  # Número de neuronas en la capa de entrada
hidden_layer_neurons = 2  # Número de neuronas en la capa oculta
output_layer_neurons = 1  # Número de neuronas en la capa de salida
hidden_weights = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))  # Pesos para la capa oculta
output_weights = np.random.uniform(size=(hidden_layer_neurons, output_layer_neurons))  # Pesos para la capa de salida

# Especificamos el número de iteraciones de entrenamiento
epochs = 10000  # Número de iteraciones de entrenamiento

# Entrenamiento de la red neuronal
for epoch in range(epochs):
    # Propagación hacia adelante
    hidden_layer_activation = sigmoid(np.dot(training_inputs, hidden_weights))  # Activación de la capa oculta
    output_layer_activation = sigmoid(np.dot(hidden_layer_activation, output_weights))  # Activación de la capa de salida

    # Retropropagación del error
    # Cálculo del error en la capa de salida
    error = training_outputs - output_layer_activation  # Error entre la salida real y la esperada
    # Cálculo de los gradientes en la capa de salida
    delta_output = error * sigmoid_derivative(output_layer_activation)  # Gradiente en la capa de salida

    # Cálculo del error en la capa oculta
    error_hidden_layer = delta_output.dot(output_weights.T)  # Error propagado hacia atrás a la capa oculta
    # Cálculo de los gradientes en la capa oculta
    delta_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_activation)  # Gradiente en la capa oculta

    # Actualización de los pesos
    output_weights += hidden_layer_activation.T.dot(delta_output)  # Actualización de los pesos de la capa de salida
    hidden_weights += training_inputs.T.dot(delta_hidden_layer)  # Actualización de los pesos de la capa oculta

# Impresión de los pesos finales
print("Pesos finales de la capa oculta:")
print(hidden_weights)
print("Pesos finales de la capa de salida:")
print(output_weights)

# Prueba de la red neuronal con nuevos datos
new_input = np.array([[1,0]])  # Nueva entrada para probar la red
hidden_layer_activation = sigmoid(np.dot(new_input, hidden_weights))  # Activación de la capa oculta
output_layer_activation = sigmoid(np.dot(hidden_layer_activation, output_weights))  # Activación de la capa de salida
print("Predicción para la nueva entrada [1,0]:")
print(output_layer_activation)  # Imprimimos la predicción
