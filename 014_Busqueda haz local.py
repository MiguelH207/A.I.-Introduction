import random  # Importamos el módulo random para generar números aleatorios

def funcion_objetivo(x):  # Definimos una función objetivo, puedes cambiarla según tus necesidades
    return -(x ** 2) + 10  # Esta es una función cuadrática con máximo en x = 0

def hill_climbing(iteraciones, paso):  # Definimos la función de búsqueda de haz local
    x_actual = random.uniform(-10, 10)  # Empezamos en un punto aleatorio dentro de un rango
    for _ in range(iteraciones):  # Iteramos un número fijo de veces
        vecino = x_actual + random.uniform(-paso, paso)  # Generamos un vecino cercano
        if funcion_objetivo(vecino) > funcion_objetivo(x_actual):  # Si el vecino es mejor que el actual
            x_actual = vecino  # Movemos hacia el vecino
    return x_actual  # Devolvemos la mejor solución encontrada

if __name__ == "__main__":  # Si este script se ejecuta como programa principal
    iteraciones = 1000  # Número de iteraciones
    paso = 0.1  # Tamaño del paso
    solucion = hill_climbing(iteraciones, paso)  # Ejecutamos la búsqueda de haz local
    print("Máximo local encontrado:", solucion)  # Imprimimos la solución encontrada
    print("Valor de la función en el máximo local:", funcion_objetivo(solucion))  # Imprimimos el valor de la función en la solución
