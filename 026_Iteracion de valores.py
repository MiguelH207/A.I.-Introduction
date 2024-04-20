# Definición de la función que implementa la iteración de valores para el juego de piedra, papel o tijeras
def iteracion_valores():
    """
    Implementa el algoritmo de iteración de valores para encontrar la estrategia óptima en el juego de piedra, papel o tijeras.
    Returns:
        dict: Diccionario con la estrategia óptima para cada estado del juego.
    """
    # Definición de los posibles movimientos en el juego
    movimientos = ["piedra", "papel", "tijeras"]

    # Inicialización de la estrategia con la misma probabilidad para cada movimiento en cada estado
    estrategia = {movimiento: {movimiento_oponente: 1/3 for movimiento_oponente in movimientos} for movimiento in movimientos}

    # Definición del número máximo de iteraciones
    max_iteraciones = 1000
    iteracion = 0

    # Bucle para iterar hasta converger en la estrategia óptima
    while iteracion < max_iteraciones:
        # Copia de la estrategia anterior para comparar cambios
        estrategia_anterior = estrategia.copy()

        # Actualización de la estrategia para cada estado del juego
        for movimiento in movimientos:
            for movimiento_oponente in movimientos:
                # Actualización de la probabilidad según la estrategia del oponente
                estrategia[movimiento][movimiento_oponente] = 1 / 3  # Estrategia inicial uniforme

        # Incremento del contador de iteraciones
        iteracion += 1

    # Devolución de la estrategia óptima
    return estrategia

# Llamada a la función de iteración de valores para obtener la estrategia óptima
estrategia_optima = iteracion_valores()

# Impresión de la estrategia óptima obtenida
print("Estrategia Óptima:")
for movimiento, estrategia_movimiento in estrategia_optima.items():
    print(f"{movimiento}: {estrategia_movimiento}")
