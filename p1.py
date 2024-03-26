# Miguel Angel Huerta Castillo #
# 21310236 # 

## BUSQUEDA EN ANCHURA ##

from collections import deque ## Importamos la clase deque del modulo collections, que permite agregar y eliminar elementos del principio y del final


# Definimos el grafo
rutas = {
    'Guadalajara': ['Zapopan', 'Tlaquepaque', 'Tonalá'],
    'Zapopan': ['Guadalajara', 'Tlajomulco de Zúñiga'],
    'Tlaquepaque': ['Guadalajara', 'Tonalá'],
    'Tonalá': ['Guadalajara', 'Tlaquepaque', 'El Salto'],
    'Tlajomulco de Zúñiga': ['Zapopan'],
    'El Salto': ['Tonalá']
}
## CADA CIUDAD ES UN NODO Y CADA RUTA ENTRE DOS CIUDADES ES UN ARISTA ## 
## POR EJEMPLO: DEL NODO GUADALAJARA HAY 3 RUTAS, UNA QUE LA CONECTA A ZAPOPAN, OTRA A TLAQUPAQUE Y OTRA A TONALA ## 


def bfs(grafico, inicio, fin): ## Se crea la funcion de busqueda en anchura (bfs: Breadth-First Search) donde grafico es el grafo donde estara buscando, y su nodo de inicio y fin 
    visitado = set() ## Creas un conjunto donde se van a ir guardando todos los nodos que ya visitaste
    cola = deque([[inicio]]) ## Se crea un conjunto con el nodo de inicio donde se guardaran los nodos no visitados 

    while cola: ## Iniciamos un bucle que se ejecutara mientras no se vacie la cola
        ruta = cola.popleft() ## Aqui se elimina el primer elemento de la cola, o sea, el nodo que se busco, desarrollo
        ciudad = ruta[-1] ## Aqui obtenemos el ultimo nodo, en esta caso la ultima ciudad 

        if ciudad == fin: ## Condicionamos si la ciudad actual es el nodo que estamos buscando (fin) entonces encontramos una ruta al nodo de destino y la devolvemos
            return ruta ## Se deculeve el nodo (ciudad)

        for vecino in grafico[ciudad]: ## Si no es la que estamos buscando recorremos cada uno de los vecinos de la ciudad actual.
            if vecino not in visitado: ## Vemos si el nodo vecino ya se visito, sino lo agregamos al conjunto para visitarlo 
                visitado.add(vecino) ## Agregamos el vecino al conjunto de nodos visitados
                ruta_nueva = list(ruta) ## Creamos una nueva ruta que es una copia de la ruta actual
                ruta_nueva.append(vecino) ## Agregamos el vecino a ruta nueva
                cola.append(ruta_nueva) ## Agregamos la nueva ruta a la cola de rutas por visitar


ruta = bfs(rutas, 'Guadalajara', 'Tlajomulco de Zúñiga') ## llamamos a la función bfs con el grafo rutas, el nodo de inicio ‘Guadalajara’ y el nodo de destino ‘El Salto’
print(f"La ruta más corta de Guadalajara a Tlajomulco de Zúñiga es: {' -> '.join(ruta)}") ## Imprimimos la ruta más corta de Guadalajara a El Salto
