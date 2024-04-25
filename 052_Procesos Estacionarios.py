# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo de Razonamiento Probabilístico en el tiempo utilizando Procesos Estacionarios.
# El código simula el comportamiento de una red de computadoras y calcula la probabilidad de que un servidor esté ocupado en función del tiempo.

import numpy as np  # Importamos la librería numpy para cálculos numéricos

# Definimos la función para simular el proceso estacionario
def stationary_process(p, T):
    """
    Simula un proceso estacionario.

    Args:
        p (float): Probabilidad de que un servidor esté ocupado en un paso de tiempo.
        T (int): Número de pasos de tiempo.

    Returns:
        numpy.array: Array con los estados de ocupación del servidor en cada paso de tiempo.
    """
    states = []  # Lista para almacenar los estados de ocupación
    state = 0  # Estado inicial: servidor desocupado
    for _ in range(T):
        states.append(state)  # Agregamos el estado actual a la lista de estados
        if np.random.rand() < p:  # Generamos un número aleatorio y comparamos con la probabilidad p
            state = 1  # Si el número aleatorio es menor que p, el servidor está ocupado en el siguiente paso
        else:
            state = 0  # Si el número aleatorio es mayor o igual que p, el servidor está desocupado en el siguiente paso
    return np.array(states)  # Devolvemos los estados como un array numpy

# Definimos la probabilidad de que el servidor esté ocupado en un paso de tiempo
p = 0.3

# Definimos el número de pasos de tiempo
T = 100

# Simulamos el proceso estacionario
server_states = stationary_process(p, T)

# Contamos la cantidad de veces que el servidor estuvo ocupado
num_busy = np.sum(server_states)

# Calculamos la probabilidad de que el servidor esté ocupado en algún momento
prob_busy = num_busy / T

# Imprimimos los resultados
print("Número de veces que el servidor estuvo ocupado:", num_busy)
print("Probabilidad de que el servidor esté ocupado en algún momento:", prob_busy)
