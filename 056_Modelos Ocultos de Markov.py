# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo de Razonamiento Probabilístico en el tiempo utilizando Modelos Ocultos de Markov.
# Se crea un modelo oculto de Markov para simular el estado de un sistema que puede estar en uno de dos estados: "bueno" o "malo".
# Las transiciones entre estados tienen una cierta probabilidad asociada.
# Se generan observaciones basadas en el estado del sistema, las cuales pueden estar sujetas a ruido.
# El objetivo es utilizar el algoritmo de Viterbi para estimar la secuencia de estados ocultos más probable a partir de las observaciones.

import numpy as np  # Importa la librería numpy para operaciones matemáticas eficientes

# Definición del modelo oculto de Markov
class HiddenMarkovModel:
    def __init__(self, initial_prob, transition_prob, emission_prob):
        self.initial_prob = initial_prob  # Probabilidades iniciales de estar en cada estado
        self.transition_prob = transition_prob  # Probabilidades de transición entre estados
        self.emission_prob = emission_prob  # Probabilidades de observación dadas los estados

    # Algoritmo de Viterbi para encontrar la secuencia de estados más probable
    def viterbi(self, observations):
        T = len(observations)  # Longitud de la secuencia de observaciones
        N = len(self.initial_prob)  # Número de estados

        # Inicialización de matrices de probabilidad y matrices de backtracking
        delta = np.zeros((N, T))  # Matriz de probabilidad máxima en el tiempo t para cada estado
        psi = np.zeros((N, T), dtype=int)  # Matriz de índices para realizar backtracking

        # Paso de inicialización
        delta[:, 0] = self.initial_prob * self.emission_prob[:, observations[0]]

        # Paso recursivo
        for t in range(1, T):
            for j in range(N):
                delta[j, t] = np.max(delta[:, t - 1] * self.transition_prob[:, j] * self.emission_prob[j, observations[t]])
                psi[j, t] = np.argmax(delta[:, t - 1] * self.transition_prob[:, j])

        # Paso de terminación
        states = np.zeros(T, dtype=int)  # Secuencia de estados más probable
        states[T - 1] = np.argmax(delta[:, T - 1])

        # Backtracking para encontrar la secuencia de estados más probable
        for t in range(T - 2, -1, -1):
            states[t] = psi[states[t + 1], t + 1]

        return states

# Probabilidades iniciales de los estados
initial_prob = np.array([0.5, 0.5])

# Probabilidades de transición entre estados
transition_prob = np.array([[0.7, 0.3],
                            [0.4, 0.6]])

# Probabilidades de observación dadas los estados
emission_prob = np.array([[0.9, 0.1],
                          [0.2, 0.8]])

# Observaciones del sistema
observations = [0, 1, 0, 0, 1]  # 0 representa una observación de "bueno" y 1 una observación de "malo"

# Crear el modelo oculto de Markov
hmm = HiddenMarkovModel(initial_prob, transition_prob, emission_prob)

# Aplicar el algoritmo de Viterbi para estimar la secuencia de estados ocultos más probable
estimated_states = hmm.viterbi(observations)
print("La secuencia de estados ocultos más probable es:", estimated_states)
