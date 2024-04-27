# Miguel Angel Huerta Castillo     21310236

# Este programa implementa tres tipos de redes neuronales en Python: Perceptrón, ADALINE y MADALINE.
# Cada tipo de red neuronal se utiliza para resolver un problema específico, como la clasificación binaria
# en el caso del Perceptrón y ADALINE, y la clasificación multiclase en el caso de MADALINE.
# Las redes neuronales se implementan utilizando clases en Python, donde cada clase representa una red neuronal
# con sus respectivas funciones de entrenamiento y predicción.

import numpy as np

class Perceptron:
    def __init__(self, input_size, lr=1, epochs=100):
        self.W = np.zeros(input_size+1)  # Inicializa los pesos con ceros
        self.epochs = epochs  # Número de iteraciones de entrenamiento
        self.lr = lr  # Tasa de aprendizaje

    def activation_fn(self, x):
        return 1 if x >= 0 else 0  # Función de activación del Perceptrón (función escalón)

    def predict(self, x):
        x = np.insert(x, 0, 1)  # Agrega el sesgo al vector de entrada
        z = self.W.T.dot(x)  # Calcula la suma ponderada de las entradas
        a = self.activation_fn(z)  # Aplica la función de activación
        return a

    def fit(self, X, d):
        for _ in range(self.epochs):
            for i in range(d.shape[0]):
                y = self.predict(X[i])  # Realiza una predicción
                e = d[i] - y  # Calcula el error
                self.W = self.W + self.lr * e * np.insert(X[i], 0, 1)  # Actualiza los pesos

class Adaline:
    def __init__(self, input_size, lr=0.01, epochs=100):
        self.W = np.zeros(input_size+1)  # Inicializa los pesos con ceros
        self.epochs = epochs  # Número de iteraciones de entrenamiento
        self.lr = lr  # Tasa de aprendizaje

    def activation_fn(self, x):
        return x  # Función de activación de ADALINE (lineal)

    def predict(self, x):
        x = np.insert(x, 0, 1)  # Agrega el sesgo al vector de entrada
        z = self.W.T.dot(x)  # Calcula la suma ponderada de las entradas
        a = self.activation_fn(z)  # Aplica la función de activación
        return a

    def fit(self, X, d):
        for _ in range(self.epochs):
            for i in range(d.shape[0]):
                y = self.predict(X[i])  # Realiza una predicción
                e = d[i] - y  # Calcula el error
                self.W = self.W + self.lr * e * np.insert(X[i], 0, 1)  # Actualiza los pesos

class Madaline:
    def __init__(self, input_size, num_classes, lr=0.01, epochs=100):
        self.W = np.zeros((num_classes, input_size+1))  # Inicializa los pesos con ceros
        self.epochs = epochs  # Número de iteraciones de entrenamiento
        self.lr = lr  # Tasa de aprendizaje
        self.num_classes = num_classes

    def activation_fn(self, x):
        return 1 if x >= 0 else 0  # Función de activación del Perceptrón (función escalón)

    def predict(self, x):
        x = np.insert(x, 0, 1)  # Agrega el sesgo al vector de entrada
        z = self.W.dot(x)  # Calcula la suma ponderada de las entradas
        a = np.array([self.activation_fn(z[i]) for i in range(self.num_classes)])  # Aplica la función de activación
        return a

    def fit(self, X, d):
        for _ in range(self.epochs):
            for i in range(d.shape[0]):
                y = self.predict(X[i])  # Realiza una predicción
                e = d[i] - y  # Calcula el error
                for j in range(self.num_classes):
                    self.W[j] = self.W[j] + self.lr * e[j] * np.insert(X[i], 0, 1)  # Actualiza los pesos

# Ejemplo de uso del Perceptrón para clasificación binaria
X_perceptron = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Entradas
d_perceptron = np.array([0, 0, 0, 1])  # Salidas esperadas

perceptron = Perceptron(input_size=2)  # Inicializa el Perceptrón
perceptron.fit(X_perceptron, d_perceptron)  # Entrena el Perceptrón

print("Perceptron Predictions:")
for i in range(X_perceptron.shape[0]):
    print(X_perceptron[i], '-->', perceptron.predict(X_perceptron[i]))

# Ejemplo de uso de ADALINE para regresión
X_adaline = np.array([[0], [1], [2], [3]])  # Entradas
d_adaline = np.array([0, 1, 2, 3])  # Salidas esperadas

adaline = Adaline(input_size=1)  # Inicializa ADALINE
adaline.fit(X_adaline, d_adaline)  # Entrena ADALINE

print("\nAdaline Predictions:")
for i in range(X_adaline.shape[0]):
    print(X_adaline[i], '-->', adaline.predict(X_adaline[i]))

# Ejemplo de uso de MADALINE para clasificación multiclase
X_madaline = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Entradas
d_madaline = np.array([[1, 0], [0, 1], [0, 1], [1, 0]])  # Salidas esperadas

madaline = Madaline(input_size=2, num_classes=2)  # Inicializa MADALINE
madaline.fit(X_madaline, d_madaline)  # Entrena MADALINE

print("\nMadaline Predictions:")
for i in range(X_madaline.shape[0]):
    print(X_madaline[i], '-->', madaline.predict(X_madaline[i]))
