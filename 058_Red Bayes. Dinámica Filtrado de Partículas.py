# Miguel Angel Huerta Castillo 21310236
# Este programa implementa un filtro de partículas utilizando inferencia bayesiana para estimar la posición de un objeto en el tiempo.
# El filtro de partículas utiliza una distribución de probabilidad para representar la creencia del estado del sistema y actualiza esta creencia utilizando mediciones y un modelo de transición.

import numpy as np

# Función para mover las partículas según el modelo de transición
def move_particles(particles, velocity):
    particles += velocity + np.random.randn(len(particles)) * 0.1

# Función para calcular la probabilidad de observar una medida dada la posición
def likelihood(measurement, particles):
    return np.exp(-0.5 * (particles - measurement) ** 2 / 0.1 ** 2).sum()

# Función principal del filtro de partículas
def particle_filter(observations, initial_particles, initial_velocity, num_particles):
    particles = initial_particles
    velocity = initial_velocity

    for observation in observations:
        # Movimiento de las partículas
        move_particles(particles, velocity)
        
        # Cálculo de pesos
        weights = np.array([likelihood(observation, particles) for _ in range(num_particles)])
        weights += 1e-300  # Evitar divisiones por cero
        weights /= np.sum(weights)
        
        # Resampling
        indices = np.random.choice(np.arange(num_particles), size=num_particles, replace=True, p=weights)
        particles = particles[indices]
        
        # Estimación de la velocidad (en este caso, es constante)
        velocity += np.random.randn() * 0.1
        
        # Mostrar la estimación de la posición
        print("Estimated position:", np.mean(particles))

# Observaciones simuladas
observations = np.array([1.5, 2.0, 2.5, 3.0])

# Parámetros iniciales
initial_particles = np.random.uniform(0, 5, 1000)
initial_velocity = 0.1
num_particles = 1000

# Llamada a la función principal
particle_filter(observations, initial_particles, initial_velocity, num_particles)
