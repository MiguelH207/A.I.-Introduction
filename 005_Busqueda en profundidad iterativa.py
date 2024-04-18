def busqueda_iterativa_matriz(matriz, elemento):  # Define una función que toma una matriz y un elemento como argumentos.
    for i in range(len(matriz)):  # Itera sobre cada fila de la matriz.
        for j in range(len(matriz[i])):  # Itera sobre cada columna de la fila actual.
            if matriz[i][j] == elemento:  # Comprueba si el elemento en la posición actual es igual al elemento buscado.
                return (i, j)  # Si se encuentra el elemento, devuelve su posición como una tupla.
    return -1  # Si el elemento no se encuentra después de buscar en toda la matriz, devuelve -1.

# Prueba del algoritmo
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Define una matriz 3x3 para la prueba.
elemento = 4  # Define el elemento que queremos buscar en la matriz.
posicion = busqueda_iterativa_matriz(matriz, elemento)  # Llama a la función de búsqueda con la matriz y el elemento.

if posicion != -1:  # Si la función de búsqueda devolvió una posición válida (no -1),
    print(f"Elemento encontrado en la posición {posicion}")  # imprime un mensaje indicando que se encontró el elemento.
else:  # Si la función de búsqueda devolvió -1,
    print("Elemento no encontrado en la matriz")  # imprime un mensaje indicando que el elemento no se encontró.
