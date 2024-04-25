# Miguel Angel Huerta Castillo #
# 21310236 # 

## BUSQUEDA COSTE UNIFORME ##
import heapq ## 

# Definimos el mapa con las distancias entre las ciudades
rutas = {
    'Guadalajara': {'Zapopan': 7, 'Tlaquepaque': 15, 'Tonalá': 20},
    'Zapopan': {'Guadalajara': 7, 'Tlajomulco de Zúñiga': 50},
    'Tlaquepaque': {'Guadalajara': 15, 'Tonalá': 30},
    'Tonalá': {'Guadalajara': 20, 'Tlaquepaque': 30, 'El Salto': 10},
    'Tlajomulco de Zúñiga': {'Zapopan': 50},
    'El Salto': {'Tonalá': 10}
}
## CADA CIUDAD ES UN NODO Y CADA RUTA ENTRE DOS CIUDADES ES UN ARISTA ## 
## POR EJEMPLO: DEL NODO GUADALAJARA HAY 3 RUTAS, UNA QUE LA CONECTA A ZAPOPAN, OTRA A TLAQUPAQUE Y OTRA A TONALA ## 
## AHORA A CADA RUTA LE DESTINAMOS UN COSTE EN ESTE CASO LOS KILOMETROS DE DISTANCIA ## 


def bcu(grafico, inicio, fin): ## Se crea la funcion de busqueda coste uniforme (bcu) donde grafico es el grafo donde estara buscando, y su nodo de inicio y fin.
    cola = [(0, inicio)]  ## Inicializamos una cola de prioridad con el nodo de inicio y un costo de 0. La cola se utilizará para almacenar los nodos que aún no hemos visitado.
    visitado = set() ## Creamos un conjunto donde se van a ir guardando todos los nodos que ya visitaste.
    while cola: ## Mientras la cola no esté vacía.
        (costo, ciudad) = heapq.heappop(cola) ## Eliminamos y devolvemos el primer elemento de la cola, que es el nodo con el costo total más bajo. En este caso, el primer elemento es una tupla que contiene un costo y un nodo.
        if ciudad not in visitado: ## Verificamos si el nodo actual ya ha sido visitado. Si no es así, lo agregamos al conjunto de nodos visitados y exploramos sus vecinos.
            visitado.add(ciudad) ## Agregamos el nodo actual al conjunto de nodos visitados.
            if ciudad == fin: ## Verificamos si el nodo actual es el nodo que estamos buscando (fin). Si es así, hemos encontrado una ruta al nodo de destino y devolvemos el costo total.
                return costo ## Devolvemos el costo total de la ruta desde el nodo de inicio hasta el nodo de destino.
            for vecina, costo_vecina in grafico[ciudad].items(): ## Si el nodo actual no es el nodo que estamos buscando, recorremos cada uno de los vecinos del nodo actual.
                if vecina not in visitado: ## Verificamos si el vecino actual ya ha sido visitado. Si no es así, lo agregamos a la cola de nodos por visitar.
                    heapq.heappush(cola, (costo + costo_vecina, vecina)) ## Agregamos el vecino a la cola de nodos por visitar, junto con el costo total de la ruta desde el nodo de inicio hasta el vecino a través del nodo actual.


costo = bcu(rutas, 'Guadalajara', 'Tlajomulco de Zúñiga') ## llamamos la funcion bcu con sus valores iniciales.
print(f"La distancia más corta de Guadalajara a Tlajomulco de Zúñiga es: {costo} km") ## ## Imprimimos la ruta con menos coste de Guadalajara a Tlajomulco de Zúñiga
