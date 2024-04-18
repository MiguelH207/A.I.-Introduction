import numpy as np

# Definimos la función que queremos maximizar
def fitness_function(x):
    return -np.sum(np.square(x))

# Definimos los parámetros del algoritmo genético
population_size = 50
chromosome_length = 5
mutation_rate = 0.1
generations = 100

# Inicializamos la población aleatoriamente
population = np.random.uniform(low=-5, high=5, size=(population_size, chromosome_length))

# Comenzamos el bucle principal de generaciones
for generation in range(generations):
    # Evaluamos la aptitud de cada individuo en la población
    fitness_scores = [fitness_function(individual) for individual in population]
    
    # Seleccionamos a los individuos para el cruce basado en su aptitud relativa
    mating_pool = np.random.choice(population_size, size=population_size, replace=True, p=fitness_scores/np.sum(fitness_scores))
    
    # Creamos la nueva generación cruzando los individuos seleccionados
    new_population = []
    for i in range(population_size // 2):
        parent1_idx = mating_pool[i*2]
        parent2_idx = mating_pool[i*2 + 1]
        crossover_point = np.random.randint(1, chromosome_length) # Punto de cruce aleatorio
        child1 = np.concatenate((population[parent1_idx][:crossover_point], population[parent2_idx][crossover_point:]))
        child2 = np.concatenate((population[parent2_idx][:crossover_point], population[parent1_idx][crossover_point:]))
        new_population.extend([child1, child2])
    
    # Aplicamos la mutación a la nueva población
    for i in range(population_size):
        if np.random.rand() < mutation_rate:
            mutation_point = np.random.randint(chromosome_length)
            new_population[i][mutation_point] += np.random.uniform(low=-0.5, high=0.5)
    
    # Actualizamos la población
    population = np.array(new_population)

# Encontramos el mejor individuo después de todas las generaciones
best_individual_idx = np.argmax([fitness_function(individual) for individual in population])
best_individual = population[best_individual_idx]

print("Mejor solución encontrada:", best_individual)
print("Valor óptimo:", -fitness_function(best_individual))
