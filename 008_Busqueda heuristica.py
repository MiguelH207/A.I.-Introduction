import heapq  # Importamos el módulo heapq para utilizar una cola de prioridad

class Nodo:
    def __init__(self, estado, padre=None, costo=0, heuristica=0):
        self.estado = estado  # Estado del nodo (posición en el mapa)
        self.padre = padre    # Nodo padre
        self.costo = costo    # Costo acumulado para llegar a este nodo
        self.heuristica = heuristica  # Valor heurístico para la estimación del costo restante

    def __lt__(self, otro):
        return (self.costo + self.heuristica) < (otro.costo + otro.heuristica)

def a_estrella(inicio, objetivo, obtener_vecinos, calcular_heuristica):
    frontera = []  # Creamos una cola de prioridad vacía
    heapq.heappush(frontera, inicio)  # Agregamos el nodo inicial a la cola de prioridad

    while frontera:
        actual = heapq.heappop(frontera)  # Obtenemos el nodo con menor costo de la frontera

        if actual.estado == objetivo:
            # Hemos alcanzado el objetivo, reconstruimos el camino
            camino = []
            while actual:
                camino.append(actual.estado)
                actual = actual.padre
            return list(reversed(camino))

        for vecino in obtener_vecinos(actual.estado):
            costo_vecino = actual.costo + 1  # Suponemos que todos los movimientos tienen un costo de 1
            heuristica_vecino = calcular_heuristica(vecino, objetivo)
            nuevo_nodo = Nodo(vecino, actual, costo_vecino, heuristica_vecino)

            heapq.heappush(frontera, nuevo_nodo)  # Agregamos el nuevo nodo a la frontera

    return None  # No se encontró camino

# Función heurística: distancia Manhattan
def distancia_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Función para obtener vecinos: movimientos arriba, abajo, izquierda y derecha
def obtener_vecinos(estado):
    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    vecinos = [(estado[0] + dy, estado[1] + dx) for dy, dx in movimientos]
    return [(y, x) for y, x in vecinos if 0 <= y < 10 and 0 <= x < 10]  # Limitamos los vecinos al mapa de 10x10

# Ejemplo de uso
inicio = (0, 0)
objetivo = (9, 9)
camino = a_estrella(Nodo(inicio), objetivo, obtener_vecinos, distancia_manhattan)
print("Camino encontrado:", camino)
