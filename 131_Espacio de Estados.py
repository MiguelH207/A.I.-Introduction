# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo de planificación utilizando Espacio de Estados.
# El programa resuelve un problema de planificación utilizando búsqueda en anchura (BFS) en un espacio de estados.
# El problema de ejemplo consiste en encontrar el camino más corto desde el punto inicial (S) hasta el punto final (G)
# en un grafo representado como un diccionario de listas de adyacencia.

from collections import deque

# Definición del grafo como un diccionario de listas de adyacencia
graph = {
    'S': ['A', 'B'],
    'A': ['S', 'C', 'D'],
    'B': ['S', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['A', 'B', 'G'],
    'E': ['B', 'G'],
    'F': ['C', 'G'],
    'G': ['D', 'E', 'F']
}

# Función para buscar el camino más corto utilizando búsqueda en anchura (BFS)
def bfs_shortest_path(graph, start, goal):
    visited = set()  # Conjunto para almacenar nodos visitados
    queue = deque([[start]])  # Cola de listas que almacena caminos a explorar

    if start == goal:
        return "¡La meta ya es el punto de inicio!"

    while queue:
        path = queue.popleft()  # Sacar el primer camino de la cola
        node = path[-1]  # Obtener el último nodo del camino

        if node not in visited:
            neighbors = graph[node]  # Obtener los vecinos del nodo actual

            for neighbor in neighbors:
                new_path = list(path)  # Crear un nuevo camino
                new_path.append(neighbor)  # Agregar el vecino al camino

                queue.append(new_path)  # Agregar el nuevo camino a la cola

                if neighbor == goal:
                    return new_path  # Devolver el camino si se llega a la meta

            visited.add(node)  # Marcar el nodo como visitado

    return "¡No se encontró un camino!"

# Definición del punto inicial y final
start = 'S'
goal = 'G'

# Llamada a la función bfs_shortest_path para encontrar el camino más corto
shortest_path = bfs_shortest_path(graph, start, goal)

# Imprimir el camino más corto encontrado
print("El camino más corto desde", start, "hasta", goal, "es:", shortest_path)
