import random  # Importamos el módulo random para generar números aleatorios

# Definimos la función objetivo
def f(x):
    return -x**2 + 4*x - 5

# Definimos la función de búsqueda de ascensión de colinas
def hill_climbing_search(f, x_start, step_size, max_iter):
    x_current = x_start  # Inicializamos la posición inicial
    for _ in range(max_iter):
        # Generamos un nuevo punto vecino dentro de un rango alrededor del punto actual
        x_neighbor = x_current + random.uniform(-step_size, step_size)
        # Evaluamos si el nuevo punto vecino tiene un valor de la función mayor que el actual
        if f(x_neighbor) > f(x_current):
            x_current = x_neighbor  # Movemos la posición actual al nuevo punto
    return x_current  # Devolvemos la posición final

# Parámetros del algoritmo
x_start = random.uniform(-10, 10)  # Punto inicial aleatorio
step_size = 0.1  # Tamaño del paso
max_iter = 100  # Número máximo de iteraciones

# Ejecutamos el algoritmo de búsqueda de ascensión de colinas
max_x = hill_climbing_search(f, x_start, step_size, max_iter)

# Mostramos el resultado
print("El máximo de la función se encuentra en x =", max_x)
print("El valor máximo de la función es f(x) =", f(max_x))
