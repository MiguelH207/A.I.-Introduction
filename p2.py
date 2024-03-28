# Definición del grafo de ciudades
grafo = {
    'Guadalajara': ['Tepic', 'Zacatecas', 'Morelia'],  # Las ciudades conectadas a Guadalajara
    'Tepic': ['Mazatlán', 'Durango'],  # Las ciudades conectadas a Tepic
    'Zacatecas': ['Saltillo', 'Monterrey'],  # Las ciudades conectadas a Zacatecas
    'Morelia': ['Ciudad de México', 'Toluca'],  # Las ciudades conectadas a Morelia
    'Mazatlán': ['Culiacán'],  # Las ciudades conectadas a Mazatlán
    'Durango': ['Torreón'],  # Las ciudades conectadas a Durango
    'Saltillo': ['Monterrey'],  # Las ciudades conectadas a Saltillo
    'Monterrey': ['Laredo'],  # Las ciudades conectadas a Monterrey
    'Ciudad de México': ['Puebla'],  # Las ciudades conectadas a Ciudad de México
    'Toluca': ['Querétaro'],  # Las ciudades conectadas a Toluca
    'Culiacán': [],  # Culiacán no tiene ciudades conectadas
    'Torreón': [],  # Torreón no tiene ciudades conectadas
    'Laredo': [],  # Laredo no tiene ciudades conectadas
    'Puebla': [],  # Puebla no tiene ciudades conectadas
    'Querétaro': []  # Querétaro no tiene ciudades conectadas
}

# Función de búsqueda en profundidad limitada
def dls(grafo, ciudad_inicial, ciudad_objetivo, profundidad, ruta=[]):  # Definición de la función dls
    ruta = ruta + [ciudad_inicial]  # Agrega la ciudad inicial a la ruta
    if ciudad_inicial == ciudad_objetivo:  # Si la ciudad inicial es la ciudad objetivo
        return ruta  # Retorna la ruta
    if profundidad <= 0:  # Si se alcanzó la profundidad máxima
        return None  # Retorna None
    for ciudad in grafo[ciudad_inicial]:  # Para cada ciudad conectada a la ciudad inicial
        if ciudad not in ruta:  # Si la ciudad no ha sido visitada
            ruta_resultante = dls(grafo, ciudad, ciudad_objetivo, profundidad - 1, ruta)  # Llama a dls para la ciudad
            if ruta_resultante:  # Si se encontró una ruta
                return ruta_resultante  # Retorna la ruta
    return None  # Si no se encontró una ruta, retorna None

# Llamada a la función de búsqueda en profundidad limitada
ruta = dls(grafo, 'Guadalajara', 'Laredo', 3)  # Busca una ruta de Guadalajara a Laredo con profundidad limitada a 3

if ruta == None:
    print("La ruta no se encontró en los limietes establecidos")  # Imprime la ruta encontrada

elif ruta != None:
    print(f"La ruta de Guadalajara a Laredo con profundidad limitada a 3 es: {ruta}")  # Imprime la ruta encontrada
