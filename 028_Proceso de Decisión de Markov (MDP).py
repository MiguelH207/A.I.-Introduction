import numpy as np  # Importamos la librería numpy para operaciones numéricas

# Definimos las recompensas para cada estado
rewards = np.array([
    [1, -1],  # Recompensas para el estado "Ganar"
    [-1, 1],  # Recompensas para el estado "Perder"
])

# Definimos la matriz de transición de probabilidades
transition_probs = np.array([
    [[0.5, 0.5],  # Transiciones desde el estado "Ganar" si se apuesta
     [0.2, 0.8]], # Transiciones desde el estado "Ganar" si no se apuesta

    [[0.3, 0.7],  # Transiciones desde el estado "Perder" si se apuesta
     [0.6, 0.4]], # Transiciones desde el estado "Perder" si no se apuesta
])

# Definimos una política aleatoria
policy = np.array([
    [1, 0],  # Política para el estado "Ganar" (apostar)
    [0, 1],  # Política para el estado "Perder" (no apostar)
])

# Definimos una función de valor
def value_iteration(transition_probs, rewards, policy, gamma=0.9, theta=1e-3):
    """
    Implementa el algoritmo de iteración de valor para encontrar la función de valor óptima.
    """
    num_states, _, num_actions = np.shape(transition_probs)  # Obtenemos el número de estados y acciones

    # Inicializamos la función de valor
    V = np.zeros(num_states)

    # Iteramos hasta que la función de valor converja
    while True:
        delta = 0
        # Iteramos sobre cada estado
        for s in range(num_states):
            v = V[s]
            # Calculamos el valor del estado s
            V[s] = sum(policy[s][a] * sum(transition_probs[s][a][s1] * (rewards[s][a] + gamma * V[s1]) for s1 in range(num_states)) for a in range(num_actions))
            # Actualizamos el delta máximo
            delta = max(delta, abs(v - V[s]))
        # Si la convergencia es menor que theta, salimos del bucle
        if delta < theta:
            break
    return V

# Calculamos la función de valor óptima
optimal_values = value_iteration(transition_probs, rewards, policy)

# Imprimimos la función de valor óptima
print("Función de valor óptima:")
print(optimal_values)
