# Importamos la librería de numpy para manejar matrices
import numpy as np

# Definimos la función que verifica si un número puede ser colocado en una posición específica
def es_valido(arr, fila, col, num):
    # Verificamos si el número ya está presente en la fila o columna
    for x in range(9):
        if arr[fila][x] == num or arr[x][col] == num:
            return False

    # Verificamos si el número ya está presente en la submatriz 3x3
    inicio_fila = fila - fila % 3
    inicio_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if arr[i + inicio_fila][j + inicio_col] == num:
                return False

    return True

# Definimos la función de backtracking para resolver el Sudoku
def resolver_sudoku(arr):
    # Buscamos una posición vacía en el tablero
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                # Intentamos colocar los números del 1 al 9 en la posición vacía
                for num in range(1, 10):
                    if es_valido(arr, i, j, num):
                        arr[i][j] = num

                        # Recursivamente intentamos resolver el Sudoku con el número colocado
                        if resolver_sudoku(arr):
                            return True

                        # Si no podemos resolverlo, deshacemos el cambio y probamos con otro número
                        arr[i][j] = 0

                # Si no podemos colocar ningún número en la posición vacía, volvemos atrás
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