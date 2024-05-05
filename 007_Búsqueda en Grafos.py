# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un algoritmo de búsqueda no informada utilizando búsqueda en grafos.
# Se utiliza el algoritmo de búsqueda en anchura (BFS) para encontrar el camino más corto desde un nodo inicial a un nodo objetivo en un grafo.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Crea un diccionario donde se almacenarán las listas de adyacencia de los nodos del grafo.

    def add_edge(self, u, v):
        self.graph[u].append(v)  # Añade una arista (u, v) al grafo.

    def bfs(self, start, end):
        visited = set()  # Conjunto para almacenar nodos visitados.
        queue = []  # Cola para el algoritmo BFS.
        path = []  # Lista para almacenar el camino encontrado.

        queue.append([start])  # Agrega el nodo inicial a la cola.

        while queue:
            path = queue.pop(0)  # Obtiene el camino más antiguo en la cola.
            node = path[-1]  # Obtiene el último nodo del camino.

            if node == end:  # Si el nodo actual es el nodo objetivo, se retorna el camino encontrado.
                return path

            if node not in visited:  # Si el nodo no ha sido visitado.
                neighbours = self.graph[node]  # Obtiene los vecinos del nodo.
                for neighbour in neighbours:
                    new_path = list(path)  # Copia el camino actual.
                    new_path.append(neighbour)  # Añade el vecino al camino.
                    queue.append(new_path)  # Agrega el nuevo camino a la cola.
                visited.add(node)  # Marca el nodo como visitado.

        return None  # Retorna None si no se encuentra un camino desde el nodo inicial al objetivo.

# Ejemplo de uso
if __name__ == "__main__":
    # Crea un grafo
    g = Graph()
    # Añade las aristas
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('C', 'G')
    # Realiza la búsqueda en anchura desde el nodo 'A' al nodo 'G'
    result = g.bfs('A', 'G')
    if result:
        print("El camino encontrado es:", result)
    else:
        print("No se encontró un camino desde el nodo inicial al objetivo.")
