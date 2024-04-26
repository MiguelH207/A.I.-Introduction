# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un modelo de Markov oculto (HMM) para predecir el clima basado en la ropa que una persona lleva puesta.
# El HMM tiene dos estados ocultos: soleado y lluvioso. La observación visible es la ropa que la persona lleva puesta.
# El modelo se entrena con datos históricos de la relación entre el clima y la ropa y luego se utiliza para predecir el clima dado la ropa observada.

import numpy as np

class HMM:
    def __init__(self, states, observations, start_prob, trans_prob, emit_prob):
        self.states = states  # Lista de estados ocultos
        self.observations = observations  # Lista de observaciones
        self.start_prob = start_prob  # Probabilidades iniciales de cada estado
        self.trans_prob = trans_prob  # Matriz de probabilidades de transición
        self.emit_prob = emit_prob  # Matriz de probabilidades de emisión

    def forward(self, observations):
        # Inicialización del paso forward
        alpha = np.zeros((len(observations), len(self.states)))

        # Paso forward para el primer tiempo
        for i, state in enumerate(self.states):
            alpha[0][i] = self.start_prob[i] * self.emit_prob[i][observations[0]]

        # Paso forward recursivo
        for t in range(1, len(observations)):
            for j, state_to in enumerate(self.states):
                prob = 0
                for i, state_from in enumerate(self.states):
                    prob += alpha[t-1][i] * self.trans_prob[i][j]
                alpha[t][j] = prob * self.emit_prob[j][observations[t]]

        return alpha

    def predict(self, observations):
        # Paso forward
        alpha = self.forward(observations)

        # Cálculo de la probabilidad total de observaciones dadas todas las secuencias de estados
        prob_total = sum(alpha[-1])

        # Probabilidades posteriores
        posteriors = alpha / prob_total

        # Predicción del estado más probable
        prediction = self.states[np.argmax(posteriors[-1])]

        return prediction

# Definición de estados y observaciones
states = ['Soleado', 'Lluvioso']
observations = ['Camisa', 'Suéter', 'Paraguas']

# Probabilidades iniciales de cada estado
start_prob = [0.6, 0.4]

# Matriz de probabilidades de transición
trans_prob = np.array([[0.7, 0.3],
                       [0.4, 0.6]])

# Matriz de probabilidades de emisión
emit_prob = np.array([[0.2, 0.4, 0.4],
                      [0.6, 0.3, 0.1]])

# Creación del modelo HMM
hmm_model = HMM(states, observations, start_prob, trans_prob, emit_prob)

# Observaciones de la ropa de una persona
observations_today = [1, 2, 2]  # Camisa, Suéter, Suéter

# Predicción del clima basado en las observaciones de ropa
predicted_weather = hmm_model.predict(observations_today)

print("El clima predicho para hoy es:", predicted_weather)
