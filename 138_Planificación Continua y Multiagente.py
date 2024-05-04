# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo de planificación continua y multiagente en Python.
# Utiliza una simulación simple donde varios agentes tienen que planificar su ruta para alcanzar un objetivo común, evitando obstáculos.

import numpy as np  # Importa la librería numpy para trabajar con matrices y operaciones numéricas

class Agent:
    def __init__(self, position, goal):
        self.position = position  # Posición actual del agente
        self.goal = goal  # Posición del objetivo del agente

    def plan(self):
        # Simula la planificación de la ruta del agente
        # En este ejemplo, simplemente devuelve una ruta directa hacia el objetivo
        return [self.goal]

class Environment:
    def __init__(self, size):
        self.size = size  # Tamaño del entorno
        self.obstacles = []  # Lista de obstáculos en el entorno

    def add_obstacle(self, obstacle):
        # Añade un obstáculo al entorno
        self.obstacles.append(obstacle)

    def is_obstacle(self, position):
        # Verifica si una posición dada está ocupada por un obstáculo
        return position in self.obstacles

    def is_within_bounds(self, position):
        # Verifica si una posición dada está dentro de los límites del entorno
        return 0 <= position[0] < self.size[0] and 0 <= position[1] < self.size[1]

    def is_valid_position(self, position):
        # Verifica si una posición dada es válida (no es un obstáculo y está dentro de los límites)
        return self.is_within_bounds(position) and not self.is_obstacle(position)

def main():
    # Configuración del entorno
    env_size = (10, 10)  # Tamaño del entorno
    env = Environment(env_size)  # Creación del entorno

    # Agregar obstáculos al entorno
    env.add_obstacle((2, 2))
    env.add_obstacle((3, 3))
    env.add_obstacle((4, 4))

    # Creación de agentes
    num_agents = 3  # Número de agentes
    agents = [Agent((0, 0), (9, 9)) for _ in range(num_agents)]  # Creación de agentes en posiciones iniciales aleatorias

    # Simulación de la planificación de los agentes
    for agent in agents:
        plan = agent.plan()  # Planificación de la ruta del agente
        print("Ruta del agente:", plan)

if __name__ == "__main__":
    main()
