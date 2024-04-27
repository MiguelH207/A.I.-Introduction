# Miguel Angel Huerta Castillo     21310236
# Programa de Redes Neuronales utilizando Mapas Autoorganizados de Kohonen
# Un mapa autoorganizado de Kohonen es una red neuronal artificial que aprende a partir de datos no etiquetados y los organiza en una estructura bidimensional.

import numpy as np  # Importar la librería numpy para operaciones matemáticas eficientes

class KohonenNetwork:
    def __init__(self, input_dim, output_dim):
        self.input_dim = input_dim  # Dimensión de entrada de la red
        self.output_dim = output_dim  # Dimensión de salida de la red
        self.weights = np.random.rand(output_dim, input_dim)  # Inicialización aleatoria de los pesos de la red
    
    def train(self, data, epochs, learning_rate):
        for epoch in range(epochs):  # Iteración sobre cada época de entrenamiento
            for sample in data:  # Iteración sobre cada muestra de datos
                winner_idx = np.argmin(np.linalg.norm(self.weights - sample, axis=1))  # Índice de la neurona ganadora
                self.weights[winner_idx] += learning_rate * (sample - self.weights[winner_idx])  # Actualización de pesos basada en la neurona ganadora

    def predict(self, data):
        predictions = []  # Lista para almacenar las predicciones
        for sample in data:  # Iteración sobre cada muestra de datos
            winner_idx = np.argmin(np.linalg.norm(self.weights - sample, axis=1))  # Índice de la neurona ganadora
            predictions.append(winner_idx)  # Agregar el índice de la neurona ganadora a las predicciones
        return predictions  # Devolver las predicciones

# Ejemplo de uso de la red de Kohonen
if __name__ == "__main__":
    # Datos de entrada
    data = np.array([[0.1, 0.2, 0.3],
                     [0.5, 0.5, 0.6],
                     [0.8, 0.8, 0.9]])
    
    input_dim = data.shape[1]  # Dimensión de entrada de los datos
    output_dim = 2  # Dimensión de salida de la red (2 neuronas en este ejemplo)
    
    # Crear una instancia de la red de Kohonen
    kohonen_net = KohonenNetwork(input_dim, output_dim)
    
    # Entrenar la red con los datos
    kohonen_net.train(data, epochs=100, learning_rate=0.01)
    
    # Predecir utilizando la red entrenada
    predictions = kohonen_net.predict(data)
    
    print("Predictions:", predictions)  # Imprimir las predicciones
