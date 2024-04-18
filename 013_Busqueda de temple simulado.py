import random
import math

# Función para calcular la distancia entre dos ciudades
def calcular_distancia(ciudad1, ciudad2):
    # Utilizamos la fórmula de la distancia euclidiana entre dos puntos en un plano cartesiano
    return math.sqrt((ciudad1[0] - ciudad2[0]) ** 2 + (ciudad1[1] - ciudad2[1]) ** 2)

# Función para calcular la distancia total de una ruta
def calcular_distancia_total(ruta, ciudades):
    distancia_total = 0.0
    # Iteramos sobre la ruta, sumando las distancias entre ciudades consecutivas
    for i in range(len(ruta) - 1):
        ciudad_actual = ciudades[ruta[i]]
        siguiente_ciudad = ciudades[ruta[i + 1]]
        distancia_total += calcular_distancia(ciudad_actual, siguiente_ciudad)
    # Agregamos la distancia de regreso a la ciudad inicial
    distancia_total += calcular_distancia(ciudades[ruta[-1]], ciudades[ruta[0]])
    return distancia_total

# Función para generar una solución aleatoria
def generar_solucion_aleatoria(num_ciudades):
    # Creamos una lista con los índices de las ciudades y la mezclamos aleatoriamente
    ruta = list(range(num_ciudades))
    random.shuffle(ruta)
    return ruta

# Función para el Temple Simulado
def temple_simulado(ciudades, temperatura_inicial, factor_enfriamiento, iteraciones_por_temperatura):
    num_ciudades = len(ciudades)
    # Generamos una solución inicial aleatoria y calculamos su distancia total
    mejor_ruta = generar_solucion_aleatoria(num_ciudades)
    mejor_distancia = calcular_distancia_total(mejor_ruta, ciudades)

    temperatura_actual = temperatura_inicial

    # Iteramos hasta que la temperatura sea lo suficientemente baja
    while temperatura_actual > 0.1:
        for _ in range(iteraciones_por_temperatura):
            # Generamos una nueva solución vecina intercambiando dos ciudades aleatorias
            nueva_ruta = mejor_ruta[:]
            i, j = sorted(random.sample(range(num_ciudades), 2))
            nueva_ruta[i:j+1] = reversed(nueva_ruta[i:j+1])

            # Calculamos la distancia de la nueva ruta
            nueva_distancia = calcular_distancia_total(nueva_ruta, ciudades)

            # Decidimos si aceptamos la nueva solución
            if nueva_distancia < mejor_distancia or random.random() < math.exp((mejor_distancia - nueva_distancia) / temperatura_actual):
                mejor_ruta = nueva_ruta
                mejor_distancia = nueva_distancia

        # Enfriamos la temperatura
        temperatura_actual *= factor_enfriamiento

    return mejor_ruta, mejor_distancia

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos las ciudades con coordenadas (x, y)
    ciudades = [(1, 3), (4, 6), (7, 2), (9, 8), (5, 5)]

    # Parámetros del Temple Simulado
    temperatura_inicial = 100
    factor_enfriamiento = 0.95
    iteraciones_por_temperatura = 2000

    # Ejecutamos el Temple Simulado
    mejor_ruta, mejor_distancia = temple_simulado(ciudades, temperatura_inicial, factor_enfriamiento, iteraciones_por_temperatura)

    print("Mejor ruta encontrada:", mejor_ruta)
    print("Distancia de la mejor ruta:", mejor_distancia)
