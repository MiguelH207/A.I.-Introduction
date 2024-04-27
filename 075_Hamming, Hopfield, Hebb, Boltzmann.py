# Miguel Angel Huerta Castillo     21310236
# Este programa implementa cuatro tipos de redes neuronales en Python: Hamming, Hopfield, Hebb y Boltzmann.
# Cada red neuronal se define con su propia clase y se proporciona un ejemplo práctico de uso para cada una de ellas.

import numpy as np  # Importamos la librería NumPy para realizar operaciones numéricas eficientes

class HammingNetwork:
    def __init__(self, weights):
        self.weights = weights  # Inicializamos los pesos de la red

    def predict(self, input_pattern):
        output = np.dot(input_pattern, self.weights)  # Calculamos el producto punto entre el patrón de entrada y los pesos
        output[output >= 0] = 1  # Si el resultado es mayor o igual que cero, asignamos 1
        output[output < 0] = -1  # Si el resultado es menor que cero, asignamos -1
        return output

class HopfieldNetwork:
    def __init__(self, weights):
        self.weights = weights  # Inicializamos los pesos de la red

    def predict(self, input_pattern, max_iterations=100):
        output = np.sign(np.dot(input_pattern, self.weights))  # Calculamos la salida de la red
        iterations = 0
        while not np.array_equal(output, input_pattern) and iterations < max_iterations:
            input_pattern = output  # Actualizamos el patrón de entrada con la salida actual
            output = np.sign(np.dot(input_pattern, self.weights))  # Calculamos una nueva salida
            iterations += 1
        return output

class HebbianNetwork:
    def __init__(self):
        pass

    def train(self, input_patterns):
        num_patterns, pattern_length = input_patterns.shape
        weights = np.zeros((pattern_length, pattern_length))  # Inicializamos los pesos
        for pattern in input_patterns:
            weights += np.outer(pattern, pattern)  # Actualizamos los pesos según la regla de Hebb
        np.fill_diagonal(weights, 0)  # Los valores diagonales se establecen en cero para evitar que los nodos se retroalimenten a sí mismos
        return weights

class BoltzmannMachine:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes  # Número de nodos en la red
        self.weights = np.random.normal(0, 1, (num_nodes, num_nodes))  # Inicializamos los pesos aleatoriamente

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))  # Función de activación sigmoide

    def update_node(self, node_index, activation_probabilities, temperature):
        activation_probabilities[node_index] = 1 if np.random.rand() < self.sigmoid(np.dot(self.weights[node_index], activation_probabilities) / temperature) else 0
        return activation_probabilities

    def gibbs_sampling(self, num_iterations, temperature):
        activation_probabilities = np.random.choice([0, 1], size=self.num_nodes)  # Inicializamos aleatoriamente las probabilidades de activación
        for _ in range(num_iterations):
            for i in range(self.num_nodes):
                activation_probabilities = self.update_node(i, activation_probabilities, temperature)  # Actualizamos cada nodo de acuerdo con la distribución de Boltzmann
        return activation_probabilities

# Ejemplo de uso de cada tipo de red neuronal

# Hamming Network
hamming_weights = np.array([[1, -1, 1], [-1, 1, -1]])  # Definimos los pesos para la red de Hamming
hamming_network = HammingNetwork(hamming_weights)  # Creamos la red de Hamming
input_pattern = np.array([1, -1])  # Definimos un patrón de entrada
output = hamming_network.predict(input_pattern)  # Obtenemos la salida de la red
print("Hamming Network output:", output)

# Hopfield Network
hopfield_weights = np.array([[0, 1, -1], [1, 0, 1], [-1, 1, 0]])  # Definimos los pesos para la red de Hopfield
hopfield_network = HopfieldNetwork(hopfield_weights)  # Creamos la red de Hopfield
input_pattern = np.array([1, 1, -1])  # Definimos un patrón de entrada
output = hopfield_network.predict(input_pattern)  # Obtenemos la salida de la red
print("Hopfield Network output:", output)

# Hebbian Network
hebbian_network = HebbianNetwork()  # Creamos la red de Hebb
input_patterns = np.array([[1, 1, -1], [1, -1, 1], [-1, 1, 1]])  # Definimos los patrones de entrada
weights = hebbian_network.train(input_patterns)  # Entrenamos la red de Hebb con los patrones de entrada
print("Hebbian Network weights:", weights)

# Boltzmann Machine
boltzmann_network = BoltzmannMachine(num_nodes=5)  # Creamos la máquina de Boltzmann con 5 nodos
num_iterations = 1000  # Número de iteraciones para el muestreo de Gibbs
temperature = 1  # Temperatura para el muestreo de Gibbs
output = boltzmann_network.gibbs_sampling(num_iterations, temperature)  # Realizamos el muestreo de Gibbs
print("Boltzmann Machine output:", output)
