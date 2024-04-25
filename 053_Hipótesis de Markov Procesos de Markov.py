# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo de Razonamiento Probabilístico en el tiempo utilizando la Hipótesis de Markov.
# Se simula un proceso de Markov para predecir el clima durante varios días.

import numpy as np  # Importa la librería numpy para cálculos numéricos

# Definir las probabilidades de transición del clima (soleado, nublado, lluvioso)
# La matriz representa la probabilidad de cambiar de un estado a otro
# Las filas representan el estado actual y las columnas representan el próximo estado
transition_matrix = np.array([[0.7, 0.2, 0.1],  # Soleado -> Soleado: 0.7, Soleado -> Nublado: 0.2, Soleado -> Lluvioso: 0.1
                              [0.3, 0.4, 0.3],  # Nublado -> Soleado: 0.3, Nublado -> Nublado: 0.4, Nublado -> Lluvioso: 0.3
                              [0.2, 0.3, 0.5]]) # Lluvioso -> Soleado: 0.2, Lluvioso -> Nublado: 0.3, Lluvioso -> Lluvioso: 0.5

# Definir los estados posibles del clima
states = ['Soleado', 'Nublado', 'Lluvioso']

# Definir la probabilidad inicial del clima (distribución inicial)
initial_probabilities = np.array([0.6, 0.3, 0.1])  # Probabilidad inicial de que el primer día sea soleado, nublado o lluvioso

# Definir la función para simular el clima durante varios días
def simulate_weather(days):
    current_state = np.random.choice(states, p=initial_probabilities)  # Selecciona un estado inicial basado en las probabilidades iniciales
    
    # Realiza la simulación del clima para los días especificados
    for _ in range(days):
        print("Día {}: {}".format(_ + 1, current_state))  # Imprime el día actual y el estado del clima
        current_state = np.random.choice(states, p=transition_matrix[states.index(current_state)])  # Elige el próximo estado basado en la matriz de transición

# Simular el clima durante 7 días
simulate_weather(7)
