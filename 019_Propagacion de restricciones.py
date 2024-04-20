# Importamos la librería numpy para manejar matrices
import numpy as np

# Definimos la función para verificar si es seguro colocar el dígito num en el tablero[fila][col]
def es_seguro(tablero, fila, col, num):
    # Verificamos si el dígito num ya está presente en la fila o la columna
    for x in range(9):
        if tablero[fila][x] == num or tablero[x][col] == num:
            return False

    # Verificamos si el dígito num ya está presente en la subcuadrícula 3x3
    inicio_fila = fila - fila % 3
    inicio_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if tablero[i + inicio_fila][j + inicio_col] == num:
                return False

    return True

# Definimos la función de propagación de restricciones para resolver el problema del Sudoku
def resolver_sudoku(tablero):
    # Buscamos una posición vacía en el tablero
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                # Intentamos colocar los dígitos del 1 al 9 en la posición vacía
                for num in range(1, 10):
                    if es_seguro(tablero, i, j, num):
                        tablero[i][j] = num

                        # Recursivamente intentamos resolver el Sudoku con el dígito colocado
                        if resolver_sudoku(tablero):
                            return True

                        # Si no podemos resolverlo, deshacemos el cambio y probamos con otro dígito
                        tablero[i][j] = 0

                # Si no podemos colocar ningún dígito en la posición vacía, volvemos atrás
                return False

    # Si no hay posiciones vacías, hemos resuelto el Sudoku
    return True

# Definimos el tablero del Sudoku como una matriz 9x9
tablero = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]])

# Resolvemos el Sudoku e imprimimos el resultado
if resolver_sudoku(tablero):
    print(tablero)
else:
    print("No se puede resolver")