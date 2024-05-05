# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un algoritmo de búsqueda local para resolver un problema de lógica proposicional.
# El programa intenta encontrar una asignación de valores de verdad a las variables proposicionales que haga verdadera una fórmula lógica dada.
# Funciona iterativamente cambiando aleatoriamente el valor de verdad de una variable para mejorar la solución hasta que se alcanza un estado óptimo o se alcanza un límite de iteraciones.

import random  # Importamos el módulo random para generar números aleatorios.

def generar_solucion(n_variables):
    """Genera una solución inicial aleatoria."""
    return [random.choice([True, False]) for _ in range(n_variables)]  # Generamos una lista de valores de verdad aleatorios para las variables.

def evaluar_solucion(solucion, formula):
    """Evalúa la solución dada en la fórmula lógica."""
    return eval(formula, {'__builtins__': None}, {f'x{i}': solucion[i] for i in range(len(solucion))})  # Evaluamos la fórmula lógica con la solución dada.

def busqueda_local(formula, n_variables, max_iter):
    """Realiza la búsqueda local para encontrar una solución que satisfaga la fórmula."""
    solucion_actual = generar_solucion(n_variables)  # Generamos una solución inicial aleatoria.
    mejor_solucion = solucion_actual[:]  # Inicializamos la mejor solución como la solución actual.
    mejor_valor = evaluar_solucion(mejor_solucion, formula)  # Evaluamos la mejor solución en la fórmula.
    
    for _ in range(max_iter):  # Iteramos un número máximo de veces.
        indice_variable = random.randint(0, n_variables - 1)  # Elegimos aleatoriamente una variable para cambiar su valor.
        solucion_vecina = solucion_actual[:]  # Creamos una copia de la solución actual.
        solucion_vecina[indice_variable] = not solucion_vecina[indice_variable]  # Cambiamos el valor de verdad de la variable seleccionada.
        valor_vecino = evaluar_solucion(solucion_vecina, formula)  # Evaluamos la solución vecina.
        
        if valor_vecino > mejor_valor:  # Si la solución vecina es mejor que la mejor solución actual:
            mejor_solucion = solucion_vecina[:]  # Actualizamos la mejor solución.
            mejor_valor = valor_vecino  # Actualizamos el mejor valor.
        
        solucion_actual = solucion_vecina[:]  # Movemos la solución actual a la solución vecina para la siguiente iteración.
    
    return mejor_solucion  # Devolvemos la mejor solución encontrada.

# Ejemplo de uso:
formula_logica = "(x0 or x1) and (x1 or not x2)"  # Definimos una fórmula lógica.
num_variables = 3  # Definimos el número de variables en la fórmula.
max_iteraciones = 1000  # Definimos el número máximo de iteraciones.

solucion_encontrada = busqueda_local(formula_logica, num_variables, max_iteraciones)  # Realizamos la búsqueda local para encontrar una solución que satisfaga la fórmula.

print("Solución encontrada:", solucion_encontrada)  # Imprimimos la solución encontrada.
print("Fórmula evaluada en la solución encontrada:", evaluar_solucion(solucion_encontrada, formula_logica))  # Imprimimos el resultado de evaluar la fórmula en la solución encontrada.
