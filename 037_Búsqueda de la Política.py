# Miguel Angel Huerta Castillo
# 21310236

# Este programa implementa un algoritmo de Aprendizaje por Refuerzo utilizando Búsqueda de la Política.
# Se utiliza un ejemplo práctico de un agente que aprende a navegar un laberinto simple.
# El agente toma decisiones basadas en una política de exploración hasta que alcanza el estado objetivo.

import numpy as np

# Definir el laberinto como una matriz donde 0 representa un espacio vacío, 1 representa un obstáculo y 2 representa el estado objetivo.
# En este ejemplo, el laberinto es de 5x5 y el estado objetivo está en la esquina superior derecha.
maze = np.array([
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [2, 0, 0, 0, 0]
])

# Definir las acciones posibles: mover hacia arriba, abajo, izquierda o derecha.
# Esto se representa como un conjunto de direcciones (arriba, abajo, izquierda, derecha) en forma de matriz.
actions = [
    (-1, 0),  # Arriba
    (1, 0),   # Abajo
    (0, -1),  # Izquierda
    (0, 1)    # Derecha
]

# Definir una política inicial. En este caso, se elige una política aleatoria donde cada acción tiene la misma probabilidad de ser seleccionada.
# La política se representa como una matriz de probabilidades de forma (número de estados, número de acciones).
policy = np.ones([maze.shape[0], maze.shape[1], len(actions)]) / len(actions)

# Definir una función de utilidad que devuelve la recompensa por llegar al estado objetivo.
# En este caso, la recompensa es 1 si llega al estado objetivo y 0 en cualquier otro caso.
def utility(state):
    return maze[state[0], state[1]] == 2

# Implementar el algoritmo de búsqueda de la política.
def policy_search():
    # Iterar hasta que el agente alcance el estado objetivo.
    while True:
        # Inicializar el estado actual en la esquina inferior izquierda del laberinto.
        state = (maze.shape[0] - 1, 0)
        # Verificar si el estado actual es el estado objetivo.
        if utility(state):
            break

        # Seleccionar una acción basada en la política actual.
        action = np.random.choice(np.arange(len(actions)), p=policy[state[0], state[1]])

        # Obtener las coordenadas del nuevo estado después de tomar la acción seleccionada.
        new_state = (state[0] + actions[action][0], state[1] + actions[action][1])

        # Verificar si el nuevo estado está dentro del laberinto y si no es un obstáculo.
        if 0 <= new_state[0] < maze.shape[0] and 0 <= new_state[1] < maze.shape[1] and maze[new_state[0], new_state[1]] != 1:
            # Actualizar la política para que el agente aprenda de su experiencia.
            # En este ejemplo simple, la política se mantiene constante.
            policy[state[0], state[1]] = np.eye(len(actions))[action]

# Ejecutar la búsqueda de política.
policy_search()

# Imprimir la política resultante.
print("Política resultante:")
print(policy)
