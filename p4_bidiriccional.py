# Definimos la función de búsqueda bidireccional
def busqueda_bidireccional(vuelos, inicio, objetivo):
    # Verificamos si las ciudades de inicio y objetivo existen en el diccionario de vuelos
    if inicio not in vuelos or objetivo not in vuelos:  # Si una o ambas ciudades no existen, retornamos un mensaje indicándolo
        return "Una o ambas ciudades no existen en la red de vuelos."

    # Inicializamos las colas de búsqueda con las ciudades de inicio y objetivo
    cola_adelante = [inicio]
    cola_atras = [objetivo]

    # Inicializamos los conjuntos de ciudades visitadas
    visitados_adelante = {inicio}
    visitados_atras = {objetivo}

    # Mientras ambas colas no estén vacías, continuamos la búsqueda
    while cola_adelante and cola_atras:
        # Tomamos la próxima ciudad de la cola de búsqueda hacia adelante
        ciudad = cola_adelante.pop(0)
        # Si esta ciudad ya ha sido visitada en la búsqueda hacia atrás, hemos encontrado una ruta
        if ciudad in visitados_atras:
            # Retornamos un mensaje indicando que existe una ruta
            return "Existe una ruta entre {} y {}.".format(inicio, objetivo)
        # Agregamos la ciudad a las ciudades visitadas en la búsqueda hacia adelante
        visitados_adelante.add(ciudad)
        # Agregamos las ciudades conectadas a la ciudad actual que aún no han sido visitadas a la cola de búsqueda hacia adelante
        cola_adelante.extend(vuelos[ciudad] - visitados_adelante)

        # Hacemos lo mismo para la búsqueda hacia atrás
        ciudad = cola_atras.pop(0)
        if ciudad in visitados_adelante:
            return "Existe una ruta entre {} y {}.".format(inicio, objetivo)
        visitados_atras.add(ciudad)
        cola_atras.extend(vuelos[ciudad] - visitados_atras)

    # Si ambas colas están vacías y no hemos encontrado una ruta, retornamos un mensaje indicándolo
    return "No existe una ruta entre {} y {}.".format(inicio, objetivo)

# El grafo se representa como un diccionario en Python.
# Las claves del diccionario son las ciudades y los valores son conjuntos de ciudades conectadas por vuelos directos.
vuelos = {
    'Ciudad de México': {'Guadalajara', 'Monterrey'},  # La ciudad de 'Ciudad de México' tiene vuelos directos a 'Guadalajara' y 'Monterrey'
    'Guadalajara': {'Ciudad de México', 'Cancún'},  # La ciudad de 'Guadalajara' tiene vuelos directos a 'Ciudad de México' y 'Cancún'
    'Monterrey': {'Ciudad de México', 'Tijuana'},  # La ciudad de 'Monterrey' tiene vuelos directos a 'Ciudad de México' y 'Tijuana'
    'Cancún': {'Guadalajara'},  # La ciudad de 'Cancún' tiene vuelos directos a 'Guadalajara'
    'Tijuana': {'Monterrey'},  # La ciudad de 'Tijuana' tiene vuelos directos a 'Monterrey'
}

# 'print' es una función incorporada en Python que imprime el argumento dado a la consola.
# Aquí se utiliza para imprimir los resultados de la función 'busqueda_bidireccional'.
# La función 'busqueda_bidireccional' se llama con el grafo 'vuelos' y un par de ciudades como argumentos.
print(busqueda_bidireccional(vuelos, 'Ciudad de México', 'Tijuana'))  # Devuelve: "Existe una ruta entre Ciudad de México y Tijuana."
print(busqueda_bidireccional(vuelos, 'Ciudad de México', 'Mérida'))  # Devuelve: "Una o ambas ciudades no existen en la red de vuelos."