# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un perceptrón simple que puede clasificar objetos basados en características de texturas y sombras.
# El perceptrón se entrena con un conjunto de datos de ejemplo y luego se usa para predecir la clase de un nuevo objeto.

import numpy as np  # Importamos la librería numpy para realizar operaciones matemáticas eficientes

# Definimos la función de activación step, que devuelve 1 si el valor es mayor o igual a cero, y 0 en otro caso
def step_function(x):
    return 1 if x >= 0 else 0

# Definimos la función de entrenamiento del perceptrón
def train_perceptron(X, y, epochs, learning_rate):
    # Inicializamos los pesos con ceros
    weights = np.zeros(X.shape[1])
    # Iteramos sobre el número de épocas
    for epoch in range(epochs):
        # Iteramos sobre cada muestra de entrenamiento
        for i in range(X.shape[0]):
            # Calculamos la suma ponderada de las características
            weighted_sum = np.dot(X[i], weights)
            # Aplicamos la función de activación step
            prediction = step_function(weighted_sum)
            # Actualizamos los pesos según el error
            weights += learning_rate * (y[i] - prediction) * X[i]
    return weights

# Definimos la función para predecir la clase de un nuevo objeto
def predict_perceptron(X, weights):
    # Calculamos la suma ponderada de las características del nuevo objeto
    weighted_sum = np.dot(X, weights)
    # Aplicamos la función de activación step para obtener la predicción
    prediction = step_function(weighted_sum)
    return prediction

# Conjunto de datos de ejemplo: características de texturas y sombras (X) y las clases correspondientes (y)
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Características de texturas y sombras
y_train = np.array([0, 1, 1, 1])  # Clases correspondientes (0 = sin sombra, 1 = con sombra)

# Hiperparámetros del perceptrón
epochs = 10  # Número de épocas de entrenamiento
learning_rate = 0.1  # Tasa de aprendizaje

# Entrenamos el perceptrón
trained_weights = train_perceptron(X_train, y_train, epochs, learning_rate)

# Ejemplo de predicción con un nuevo objeto
new_object = np.array([1, 0])  # Características del nuevo objeto (textura y sombra)
prediction = predict_perceptron(new_object, trained_weights)  # Predicción de la clase del nuevo objeto
print("Predicción:", prediction)  # Imprimimos la predicción
