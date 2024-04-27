# Miguel Angel Huerta Castillo     21310236
# Este programa en Python implementa un reconocimiento de escritura utilizando perceptrón. El perceptrón es entrenado
# para reconocer dígitos escritos a mano representados como matrices de 0 y 1. El ejemplo práctico consistirá en 
# entrenar el perceptrón con dígitos del 0 al 9 y luego probarlo con un dígito escrito a mano.

import numpy as np

# Definición de la función de activación (step function)
def step_function(x):
    return 1 if x >= 0 else 0

# Definición de la función de predicción del perceptrón
def predict(weights, inputs):
    activation = np.dot(weights, inputs)
    return step_function(activation)

# Entrenamiento del perceptrón
def train(X, y, learning_rate=0.1, epochs=100):
    # Inicialización de pesos
    weights = np.zeros(X.shape[1])
    for _ in range(epochs):
        for inputs, label in zip(X, y):
            prediction = predict(weights, inputs)
            # Actualización de pesos
            weights += learning_rate * (label - prediction) * inputs
    return weights

# Datos de entrenamiento: dígitos escritos a mano representados como matrices de 0 y 1
X_train = np.array([
    [0, 0, 1, 1, 0, 0, 0, 0, 0],  # 0
    [0, 1, 1, 1, 1, 0, 0, 0, 0],  # 1
    [0, 0, 0, 1, 1, 1, 0, 0, 0],  # 2
    [0, 0, 0, 0, 1, 1, 1, 0, 0],  # 3
    [0, 0, 0, 0, 0, 1, 1, 1, 0],  # 4
    [0, 0, 0, 0, 0, 0, 1, 1, 1],  # 5
    [1, 0, 0, 0, 0, 0, 0, 1, 1],  # 6
    [1, 1, 0, 0, 0, 0, 0, 0, 1],  # 7
    [1, 1, 1, 0, 0, 0, 0, 0, 0],  # 8
    [0, 1, 1, 1, 0, 0, 0, 0, 0]   # 9
])

# Etiquetas correspondientes a los dígitos
y_train = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Entrenamiento del perceptrón
weights = train(X_train, y_train)

# Dígito a probar (por ejemplo, el número 3)
X_test = np.array([0, 0, 0, 0, 1, 1, 1, 0, 0])

# Predicción del perceptrón
prediction = predict(weights, X_test)

# Imprimir la predicción
print("La predicción es:", prediction)
