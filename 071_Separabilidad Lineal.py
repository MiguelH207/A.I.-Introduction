# Miguel Angel Huerta Castillo     21310236
# Este programa implementa una red neuronal artificial con una sola neurona para clasificar datos linealmente separables.
# La red neuronal utilizará el algoritmo de descenso de gradiente para entrenar los pesos de la neurona y poder separar los datos en dos clases.

import numpy as np  # Importa la librería numpy y la renombra como np

# Definición de la función de activación (función escalón unitario)
def step_function(x):  # Define una función llamada step_function que toma un argumento x
    return 1 if x >= 0 else 0  # Devuelve 1 si x es mayor o igual a 0, de lo contrario devuelve 0

# Definición de la función de predicción
def predict(weights, inputs):  # Define una función llamada predict que toma dos argumentos: weights (pesos) e inputs (entradas)
    activation = np.dot(inputs, weights)  # Calcula la suma ponderada de las entradas y los pesos
    return step_function(activation)  # Aplica la función de activación a la suma ponderada y devuelve la predicción

# Datos de entrada (características de los puntos)
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Define una matriz de numpy con las características de los puntos de entrada

# Etiquetas (clases a las que pertenecen los puntos)
labels = np.array([0, 0, 0, 1])  # Define un vector de numpy con las etiquetas de los puntos de entrada

# Inicialización aleatoria de los pesos
weights = np.random.rand(2)  # Inicializa un vector de pesos de tamaño 2 con valores aleatorios entre 0 y 1

# Parámetros del algoritmo de entrenamiento
learning_rate = 0.1  # Tasa de aprendizaje
epochs = 100  # Número de iteraciones de entrenamiento

# Entrenamiento de la red neuronal
for epoch in range(epochs):  # Itera sobre el número de épocas especificado
    for i, input in enumerate(inputs):  # Itera sobre cada par de entrada y etiqueta
        prediction = predict(weights, input)  # Realiza una predicción con la red neuronal
        error = labels[i] - prediction  # Calcula el error de predicción
        weights += learning_rate * error * input  # Actualiza los pesos según el error y la entrada

# Prueba del modelo entrenado
print("Prueba del modelo entrenado:")
for input in inputs:  # Itera sobre cada entrada
    prediction = predict(weights, input)  # Realiza una predicción con el modelo entrenado
    print(f"Entrada: {input}, Predicción: {prediction}")  # Imprime la entrada y la predicción realizada por el modelo
