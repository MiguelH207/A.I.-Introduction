import random  # Importamos el módulo random para generar números aleatorios

def euclidean_distance(city1, city2):  # Función para calcular la distancia euclidiana entre dos ciudades
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

def total_distance(route, cities):  # Función para calcular la distancia total de una ruta
    distance = 0
    for i in range(len(route) - 1):
        distance += euclidean_distance(cities[route[i]], cities[route[i + 1]])
    distance += euclidean_distance(cities[route[-1]], cities[route[0]])  # Añadimos la distancia de regreso a la ciudad inicial
    return distance

def generate_initial_solution(num_cities):  # Función para generar una solución inicial aleatoria
    return random.sample(range(num_cities), num_cities)

def get_neighborhood(route):  # Función para obtener vecindario de una ruta intercambiando dos ciudades
    neighborhood = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            new_route = route[:]  # Copiamos la ruta original para no modificarla directamente
            new_route[i], new_route[j] = new_route[j], new_route[i]  # Intercambiamos dos ciudades
            neighborhood.append(new_route)
    return neighborhood

def tabu_search(cities, max_iter, tabu_size):  # Función que implementa la Búsqueda Tabú
    current_solution = generate_initial_solution(len(cities))  # Generamos una solución inicial
    best_solution = current_solution[:]  # Inicializamos la mejor solución como la solución actual
    tabu_list = []  # Inicializamos la lista tabú vacía
    iter_count = 0

    while iter_count < max_iter:
        neighborhood = get_neighborhood(current_solution)  # Obtenemos el vecindario de la solución actual

        # Encontramos la mejor solución en el vecindario que no esté en la lista tabú
        best_neighbor = min(neighborhood, key=lambda x: total_distance(x, cities))
        
        # Si la mejor solución del vecindario no está en la lista tabú, la aceptamos
        if best_neighbor not in tabu_list:
            current_solution = best_neighbor[:]
            iter_count += 1

            # Actualizamos la mejor solución encontrada si es mejor que la anterior
            if total_distance(current_solution, cities) < total_distance(best_solution, cities):
                best_solution = current_solution[:]

            # Añadimos el movimiento a la lista tabú
            tabu_list.append(best_neighbor)
            if len(tabu_list) > tabu_size:
                tabu_list.pop(0)  # Eliminamos el movimiento más antiguo de la lista tabú
        
        # Si la mejor solución del vecindario está en la lista tabú, exploramos otra solución
        else:
            iter_count += 1

    return best_solution

# Ejemplo de uso
cities = [(0, 0), (1, 2), (3, 1), (5, 2), (4, 4)]  # Coordenadas de las ciudades
max_iter = 100  # Número máximo de iteraciones
tabu_size = 5  # Tamaño de la lista tabú
best_route = tabu_search(cities, max_iter, tabu_size)  # Aplicamos Búsqueda Tabú para encontrar la mejor ruta
print("Mejor ruta encontrada:", best_route)
print("Distancia total:", total_distance(best_route, cities))
