# Definimos la función para verificar si una reina puede ser colocada en el tablero[pos][col]
def es_seguro(tablero, fila, col, n):
    # Verificamos la fila en el lado izquierdo
    for i in range(col):
        if tablero[fila][i] == 1:
            return False

    # Verificamos la diagonal superior en el lado izquierdo
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False

    # Verificamos la diagonal inferior en el lado izquierdo
    for i, j in zip(range(fila, n, 1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False

    return True

# Definimos la función de backtracking para resolver el problema de las N-Reinas
def resolver_n_reinas(tablero, col, n):
    # Si todas las reinas están colocadas, entonces retornamos verdadero
    if col >= n:
        return True

    # Colocamos esta reina en todas las filas una por una
    for i in range(n):
        if es_seguro(tablero, i, col, n):
            # Colocamos esta reina en el tablero[i][col]
            tablero[i][col] = 1

            # Recursivamente colocamos el resto de las reinas
            if resolver_n_reinas(tablero, col + 1, n):
                return True

            # Si colocar la reina en el tablero[i][col] no conduce a una solución, entonces quitamos la reina del tablero[i][col]
            tablero[i][col] = 0

    # Si la reina no puede ser colocada en ninguna fila en esta columna col, entonces retornamos falso
    return False

# Definimos la función principal para resolver el problema de las N-Reinas utilizando backtracking
def n_reinas(n):
    tablero = [[0]*n for _ in range(n)]

    if not resolver_n_reinas(tablero, 0, n):
        print("No existe solución")
        return False

    # Imprimimos la solución
    for i in range(n):
        for j in range(n):
            print(tablero[i][j], end = " ")
        print()

    return True

# Llamamos a la función principal con N = 4
n_reinas(4)