# Miguel Angel Huerta Castillo 21310236

# Importar la librería necesaria para generar números aleatorios
import random

# Definir una función para simular el comportamiento del agente en un entorno de aprendizaje por refuerzo
def reinforcement_learning(epsilon, total_episodes):
    # Inicializar el valor de las acciones posibles
    action_values = [0, 0, 0]
    # Inicializar el recuento de selección de acciones
    action_counts = [0, 0, 0]
    
    # Ciclo a través de todos los episodios
    for episode in range(total_episodes):
        # Decidir si se realiza una acción de exploración o explotación
        if random.random() < epsilon:  # Si el número aleatorio es menor que epsilon, explorar
            # Elegir una acción aleatoria
            action = random.randint(0, 2)
        else:  # De lo contrario, explotar
            # Elegir la acción con el valor máximo
            action = action_values.index(max(action_values))
        
        # Incrementar el recuento de selección de la acción elegida
        action_counts[action] += 1
        
        # Simular el resultado de tomar la acción
        reward = simulate_environment(action)
        
        # Actualizar el valor de la acción elegida utilizando la regla de actualización de la acción promedio
        action_values[action] += (1 / action_counts[action]) * (reward - action_values[action])
    
    # Devolver los valores finales de las acciones después de completar todos los episodios
    return action_values

# Función para simular el resultado de tomar una acción en el entorno
def simulate_environment(action):
    # Definir las recompensas asociadas con cada acción
    rewards = [1, 0, -1]
    # Devolver la recompensa correspondiente a la acción seleccionada
    return rewards[action]

# Definir el valor de epsilon (tasa de exploración)
epsilon = 0.1
# Definir el número total de episodios de aprendizaje
total_episodes = 1000

# Llamar a la función de aprendizaje por refuerzo para obtener los valores finales de las acciones
final_action_values = reinforcement_learning(epsilon, total_episodes)

# Imprimir los valores finales de las acciones
print("Valores finales de las acciones:", final_action_values)
