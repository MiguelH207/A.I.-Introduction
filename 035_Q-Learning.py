# Miguel Angel Huerta Castillo     21310236
# 
# Este programa implementa un ejemplo simple de Aprendizaje por Refuerzo utilizando el algoritmo Q-Learning.
# El ejemplo consiste en un agente que aprende a navegar en un laberinto representado como una matriz.
# El agente tiene como objetivo llegar al estado objetivo (G) mientras evita los obstáculos (O).
# El algoritmo Q-Learning actualiza la matriz de Q-valores en función de las recompensas recibidas y utiliza
# esta matriz para tomar decisiones sobre qué acción tomar en cada estado.

import numpy as np

# Definir la matriz de recompensas y obstáculos
R = np.array([
    [-1, -1, -1, -1, 0, -1],
    [-1, -1, -1, 0, -1, 100],
    [-1, -1, -1, 0, -1, -1],
    [-1, 0, 0, -1, 0, -1],
    [0, -1, -1, 0, -1, 100],
    [-1, 0, -1, -1, 0, 100]
])

# Inicializar la matriz Q con ceros
Q = np.zeros_like(R, dtype=np.float32)

# Factor de descuento
gamma = 0.8

# Número de episodios
num_episodes = 1000

# Algoritmo de Q-Learning
for _ in range(num_episodes):
    # Seleccionar un estado inicial aleatorio
    state = np.random.randint(0, R.shape[0])

    # Mientras no se alcance el estado objetivo
    while state != 5:
        # Seleccionar una acción basada en la política epsilon-greedy
        action = np.random.choice(np.where(R[state] >= 0)[0])

        # Calcular el valor Q para el estado-acción actual
        max_action = np.argmax(Q[action])
        Q[state, action] = R[state, action] + gamma * Q[action, max_action]

        # Ir al siguiente estado
        state = action

# Imprimir la matriz de Q-valores aprendida
print("Matriz de Q-valores aprendida:")
print(Q)

# Función para encontrar el camino óptimo
def find_optimal_path(start_state):
    path = [start_state]
    while start_state != 5:
        next_state = np.argmax(Q[start_state])
        path.append(next_state)
        start_state = next_state
    return path

# Encontrar el camino óptimo desde el estado inicial
initial_state = 2
optimal_path = find_optimal_path(initial_state)

# Imprimir el camino óptimo
print(f"Camino óptimo desde el estado inicial {initial_state}:")
print(optimal_path)
