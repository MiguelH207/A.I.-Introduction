# Importamos la librería heapq para implementar la cola de prioridad
import heapq

# Definimos la función de búsqueda A*
def astar(graph, start, goal):
    # Inicializamos la cola de prioridad con el nodo de inicio
    queue = []
    heapq.heappush(queue, (0, start))  # La prioridad es 0 al inicio

    # Inicializamos los conjuntos de nodos visitados y los costos
    visited = set()
    costs = {start: 0}
    path = {start: None}

    # Mientras la cola no esté vacía
    while queue:
        # Obtenemos el nodo con la menor prioridad
        cost, node = heapq.heappop(queue)

        # Si el nodo es el objetivo, hemos terminado
        if node == goal:
            return cost, path

        # Si no, expandimos el nodo
        for neighbour in graph[node]:
            # El costo para moverse a un vecino es siempre 1 en una red social
            neighbour_cost = 1

            # Calculamos el costo total hasta el vecino
            total_cost = cost + neighbour_cost

            # Si el vecino no ha sido visitado o si encontramos un camino más corto
            if neighbour not in visited or total_cost < costs[neighbour]:
                # Actualizamos el costo
                costs[neighbour] = total_cost
                # Actualizamos el camino
                path[neighbour] = node
                # Añadimos el vecino a la cola con la nueva prioridad
                heapq.heappush(queue, (total_cost, neighbour))
                # Marcamos el vecino como visitado
                visited.add(neighbour)

    # Si no encontramos un camino, retornamos None
    return None

# Definimos el gráfico
graph = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'Charlie', 'David'],
    'Charlie': ['Alice', 'Bob', 'David'],
    'David': ['Bob', 'Charlie']
}

# Imprimimos el gráfico
print("Gráfico:")
for node, neighbours in graph.items():
    print(f"{node}: {neighbours}")

# Realizamos la búsqueda A*
cost, path = astar(graph, 'Alice', 'David')

# Imprimimos el resultado
if cost is not None and path is not None:
    print(f"\nCosto del camino más corto de Alice a David: {cost}")
    # print("Camino más corto de Alice a David:")
    # node = 'David'
    # path_to_goal = []
    # while node is not None:
    #     path_to_goal.append(node)
    #     node = path[node]
    # path_to_goal.reverse()
    # for node in path_to_goal:
    #     print(node)
else:
    print("\nNo se encontró un camino de Alice a David.")