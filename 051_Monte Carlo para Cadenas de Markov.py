# Miguel Angel Huerta Castillo     21310236
# Este programa utiliza el método de Monte Carlo para simular cadenas de Markov.
# Se genera una cadena de Markov con transiciones probabilísticas entre estados.
# Luego, se utiliza el método de Monte Carlo para simular el comportamiento de la cadena
# y estimar la probabilidad de que la cadena esté en un estado determinado después de un número de pasos dado.

import random  # Importamos el módulo random para generar números aleatorios

# Definimos la matriz de transición de la cadena de Markov.
# Cada fila representa las probabilidades de transición desde un estado hacia los demás estados.
# La suma de las probabilidades en cada fila debe ser 1.
transition_matrix = [
    [0.5, 0.2, 0.3],  # Probabilidades de transición desde el estado 1 hacia los estados 1, 2 y 3 respectivamente
    [0.3, 0.4, 0.3],  # Probabilidades de transición desde el estado 2 hacia los estados 1, 2 y 3 respectivamente
    [0.2, 0.6, 0.2]   # Probabilidades de transición desde el estado 3 hacia los estados 1, 2 y 3 respectivamente
]

# Función para simular un paso en la cadena de Markov
def step(current_state):
    # Utilizamos la matriz de transición y la distribución acumulativa para decidir el próximo estado
    probabilities = transition_matrix[current_state]
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    # Generamos un número aleatorio entre 0 y 1
    rand = random.random()
    # Determinamos el próximo estado basado en la distribución acumulativa
    next_state = 0
    while rand > cumulative_probabilities[next_state]:
        next_state += 1
    return next_state

# Función para simular la cadena de Markov utilizando el método de Monte Carlo
def monte_carlo_simulation(initial_state, steps):
    # Inicializamos el contador de visitas a cada estado
    visits = [0, 0, 0]
    current_state = initial_state
    # Realizamos 'steps' pasos en la cadena de Markov
    for _ in range(steps):
        # Realizamos un paso en la cadena de Markov
        current_state = step(current_state)
        # Incrementamos el contador de visitas al estado actual
        visits[current_state] += 1
    # Calculamos la probabilidad de que la cadena esté en cada estado después de 'steps' pasos
    probabilities = [visit / steps for visit in visits]
    return probabilities

# Definimos el estado inicial y el número de pasos para la simulación
initial_state = 0  # Estado inicial: 1
steps = 1000       # Número de pasos en la simulación

# Realizamos la simulación utilizando el método de Monte Carlo
result = monte_carlo_simulation(initial_state, steps)

# Imprimimos los resultados
print("Después de {} pasos, las probabilidades de estar en los estados 1, 2 y 3 son:".format(steps))
print("Estado 1:", result[0])
print("Estado 2:", result[1])
print("Estado 3:", result[2])
