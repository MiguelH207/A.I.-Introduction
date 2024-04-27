# Miguel Angel Huerta Castillo
# 21310236

# Este programa implementa la localización de un robot utilizando el algoritmo de Monte Carlo.
# El robot se moverá en un área cuadrada, y se utilizarán medidas de rango y dirección para actualizar la creencia del robot sobre su posición.
# El ejemplo práctico consistirá en un robot que navega en un laberinto simple, utilizando sensores de proximidad para detectar obstáculos y actualizar su posición estimada.

import numpy as np

# Función para simular el movimiento del robot en el laberinto
def move_robot(position, movement):
    x, y = position
    dx, dy = movement
    new_x = x + dx
    new_y = y + dy
    return (new_x, new_y)

# Función para simular la lectura de sensores de proximidad del robot
def sense_obstacle(position, maze):
    x, y = position
    return maze[y][x] == 1

# Función para simular la medición de distancia con ruido
def measure_distance(position, target):
    true_distance = np.linalg.norm(np.array(position) - np.array(target))
    noise = np.random.normal(0, 0.5) # Introducir ruido gaussiano en la medición
    noisy_distance = true_distance + noise
    return noisy_distance

# Función para inicializar las partículas (estimaciones) de la posición del robot
def initialize_particles(grid_size, num_particles):
    particles = []
    for _ in range(num_particles):
        x = np.random.randint(0, grid_size[0])
        y = np.random.randint(0, grid_size[1])
        particles.append((x, y))
    return particles

# Función para generar las nuevas partículas utilizando el movimiento del robot
def move_particles(particles, movement):
    new_particles = []
    for particle in particles:
        new_particle = move_robot(particle, movement)
        new_particles.append(new_particle)
    return new_particles

# Función para calcular la probabilidad de observar una lectura de sensor dada una posición estimada y una lectura real
def measurement_probability(position, target, measured_distance):
    true_distance = np.linalg.norm(np.array(position) - np.array(target))
    # Calculamos la probabilidad usando una distribución gaussiana
    probability = 1.0 / np.sqrt(2 * np.pi * 0.5) * np.exp(-0.5 * ((measured_distance - true_distance) / 0.5) ** 2)
    return probability

# Función principal que implementa el algoritmo de localización de Monte Carlo
def monte_carlo_localization(maze, initial_position, num_particles, movements, measurements):
    # Inicializar las partículas aleatoriamente
    particles = initialize_particles((len(maze[0]), len(maze)), num_particles)
    # Estimación inicial de la posición del robot
    estimated_position = initial_position

    # Actualizar la posición del robot con cada movimiento
    for i in range(len(movements)):
        movement = movements[i]
        measurement = measurements[i]
        
        # Mover las partículas de acuerdo al movimiento del robot
        particles = move_particles(particles, movement)
        
        # Calcular la probabilidad de observar la medición actual para cada partícula
        weights = []
        for particle in particles:
            weight = measurement_probability(particle, estimated_position, measurement)
            weights.append(weight)
        
        # Normalizar los pesos
        weights = np.array(weights) / np.sum(weights)
        
        # Actualizar la posición estimada del robot usando el filtro de partículas
        estimated_position = np.average(particles, axis=0, weights=weights)

    return estimated_position

# Definir el tamaño del laberinto
maze = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Posición inicial del robot
initial_position = (0, 0)

# Número de partículas (estimaciones) para el filtro de Monte Carlo
num_particles = 1000

# Secuencia de movimientos del robot
movements = [(1, 0), (0, 1), (1, 0), (0, 1)]

# Medidas de distancia observadas por el robot en cada paso
measurements = [measure_distance(initial_position, (3, 4)),
                measure_distance(move_robot(initial_position, movements[0]), (3, 4)),
                measure_distance(move_robot(move_robot(initial_position, movements[0]), movements[1]), (3, 4)),
                measure_distance(move_robot(move_robot(move_robot(initial_position, movements[0]), movements[1]), movements[2]), (3, 4))]

# Ejecutar el algoritmo de localización de Monte Carlo
estimated_position = monte_carlo_localization(maze, initial_position, num_particles, movements, measurements)
print("Posición estimada del robot:", estimated_position)
