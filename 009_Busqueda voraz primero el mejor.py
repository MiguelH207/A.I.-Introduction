# Importamos la librería heapq para manejar la cola de prioridad
import heapq

# Definimos la función para el algoritmo de búsqueda
def best_first_search(graph, start, goal):
    # Creamos una cola de prioridad para almacenar las ciudades por visitar
    queue = []

    # Agregamos la ciudad inicial a la cola con prioridad 0
    heapq.heappush(queue, (0, start))

    # Creamos un conjunto para almacenar las ciudades visitadas
    visited = set()

    # Creamos un diccionario para almacenar la ruta desde el inicio hasta cada ciudad
    came_from = {start: None}

    # Mientras la cola no esté vacía
    while queue:
        # Obtenemos la ciudad con la menor prioridad (distancia)
        distance, city = heapq.heappop(queue)

        # Si la ciudad es el objetivo, terminamos la búsqueda
        if city == goal:
            # Creamos una lista para almacenar la ruta
            path = []

            # Retrocedemos desde la ciudad objetivo hasta la ciudad inicial
            while city is not None:
                # Agregamos la ciudad a la ruta
                path.append(city)
                city = came_from[city]

            # Invertimos la ruta para que vaya desde la ciudad inicial hasta la ciudad objetivo
            path.reverse()

            # Imprimimos la ruta
            print(' -> '.join(path))
            return

        # Si la ciudad no ha sido visitada
        if city not in visited:
            # La marcamos como visitada
            visited.add(city)

            # Visitamos todas las ciudades vecinas
            for i in graph[city]:
                # Si la ciudad vecina no ha sido visitada, la agregamos a la cola con la prioridad igual a su distancia
                if i not in visited:
                    total_distance = distance + graph[city][i]
                    heapq.heappush(queue, (total_distance, i))
                    # Almacenamos la ciudad desde la que llegamos a la ciudad vecina
                    came_from[i] = city

# Definimos el mapa con las ciudades y las distancias entre ellas
map = {
    'Londres': {'Manchester': 200, 'Birmingham': 120},
    'Manchester': {'Londres': 200, 'Liverpool': 35},
    'Birmingham': {'Londres': 120, 'Liverpool': 100},
    'Liverpool': {'Manchester': 35, 'Birmingham': 100, 'Edimburgo': 350},
    'Edimburgo': {'Liverpool': 350}
}

# Llamamos a la función de búsqueda para encontrar la ruta más corta de Londres a Edimburgo
best_first_search(map, 'Londres', 'Edimburgo')