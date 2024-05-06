# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo básico de Aprendizaje por Refuerzo Activo (Active Reinforcement Learning) utilizando Q-Learning.
# El agente aprende a navegar en un laberinto simple para alcanzar un objetivo mientras evita obstáculos.

import numpy as np

# Definir el laberinto como una matriz
# 0 representa un espacio libre
# 1 representa un obstáculo
# 2 representa el objetivo
maze = np.array([
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 2],
    [1, 1, 0, 1]
])

# Definir las posiciones inicial y objetivo del agente
start_state = (0, 0)
goal_state = (2, 3)

# Definir los parámetros del algoritmo de Q-Learning
learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.1
epochs = 1000

# Inicializar la matriz Q con valores arbitrarios
Q = np.zeros((maze.shape[0], maze.shape[1], 4))

# Definir las acciones posibles: arriba, abajo, izquierda, derecha
actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Función para obtener la próxima acción basada en epsilon-greedy
def get_next_action(state, epsilon):
    if np.random.uniform(0, 1) < epsilon:
        return np.random.choice(len(actions))
    else:
        return np.argmax(Q[state[0], state[1]])

# Iterar a través de las épocas de entrenamiento
for epoch in range(epochs):
    state = start_state
    done = False

    while not done:
        # Seleccionar la próxima acción
        action_index = get_next_action(state, epsilon)
        action = actions[action_index]

        # Obtener la nueva posición
        new_state = (state[0] + action[0], state[1] + action[1])

        # Verificar si la nueva posición es válida
        if 0 <= new_state[0] < maze.shape[0] and 0 <= new_state[1] < maze.shape[1]:
            reward = maze[new_state[0], new_state[1]]

            # Actualizar la matriz Q utilizando la ecuación de Bellman
            Q[state[0], state[1], action_index] = (1 - learning_rate) * Q[state[0], state[1], action_index] + \
                                                   learning_rate * (reward + discount_factor * np.max(Q[new_state[0], new_state[1]]))
            
            # Actualizar el estado
            state = new_state

            # Verificar si el objetivo ha sido alcanzado
            if state == goal_state:
                done = True
        else:
            # La acción lleva a una posición fuera del laberinto, penalizar
            reward = -1
            Q[state[0], state[1], action_index] = (1 - learning_rate) * Q[state[0], state[1], action_index] + \
                                                   learning_rate * (reward + discount_factor * np.max(Q[new_state[0], new_state[1]]))
            done = True

# Imprimir la matriz Q aprendida
print("Matriz Q:")
print(Q)
