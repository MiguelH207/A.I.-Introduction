# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo práctico de planificación utilizando SATPLAN,
# un algoritmo de planificación basado en SAT (Satisfiability).
# Primero, define funciones para generar todas las combinaciones posibles de acciones y para verificar si un conjunto de acciones satisface un objetivo dado. Luego, implementa la función principal satplan que busca una secuencia de acciones que satisfaga el objetivo dado el estado inicial y las acciones disponibles. Finalmente, se llama a satplan con un estado inicial, acciones disponibles y objetivo, y se imprime el plan encontrado. 


import itertools

# Función para generar todas las combinaciones posibles de un conjunto de acciones
def generate_action_combinations(actions):
    return list(itertools.product([False, True], repeat=len(actions)))

# Función para comprobar si un conjunto de acciones satisface todos los efectos de un objetivo
def satisfies_goal(actions, goal):
    # Verifica si al menos una acción en el conjunto puede satisfacer cada objetivo
    return all(any(action[i] == effect for i, effect in enumerate(goal)) for action in actions)

# Función principal para SATPLAN
def satplan(initial_state, actions, goal):
    # Bucle principal
    while True:
        # Genera todas las combinaciones posibles de acciones
        for action_combination in generate_action_combinations(actions):
            # Comprueba si la combinación de acciones satisface el objetivo
            if satisfies_goal(action_combination, goal):
                return [actions[i] for i, a in enumerate(action_combination) if a]
        
        # Si no se encuentra una solución, se expande el conjunto de acciones
        actions.append([])

# Definición del estado inicial, acciones y objetivo
initial_state = ["A", "B"]
actions = [["A", "C"], ["B", "C"], ["C"]]
goal = ["C"]

# Llamada a la función SATPLAN para encontrar una secuencia de acciones que satisfaga el objetivo
plan = satplan(initial_state, actions, goal)

# Imprime el plan encontrado
print("Plan encontrado:", plan)
