# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo de razonamiento probabilístico utilizando inferencia por enumeración.
# Se define un conjunto de variables aleatorias y sus respectivas distribuciones de probabilidad condicional.
# Luego, se realiza inferencia por enumeración para calcular la probabilidad de una variable dada evidencia.

# Importamos la librería para trabajar con distribuciones de probabilidad
from collections import defaultdict

# Definimos las distribuciones de probabilidad condicional para cada variable
# P(A)
P_A = {'T': 0.7, 'F': 0.3}
# P(B | A)
P_B_given_A = {'T': {'T': 0.9, 'F': 0.2}, 'F': {'T': 0.1, 'F': 0.8}}
# P(C | A)
P_C_given_A = {'T': {'T': 0.8, 'F': 0.3}, 'F': {'T': 0.2, 'F': 0.7}}

# Definimos la función de inferencia por enumeración
def enumeration_ask(X, e, bn):
    # Inicializamos un diccionario para almacenar las probabilidades
    Q = defaultdict(float)
    # Para cada posible valor de X
    for xi in bn[X]:
        # Asignamos la probabilidad inicial de X
        Q[xi] = enumerate_all(X, e, bn)
    # Normalizamos las probabilidades y devolvemos el resultado
    return normalize(Q)

# Definimos la función auxiliar para enumerar todas las posibles combinaciones de valores
def enumerate_all(var, e, bn):
    # Si no hay más variables, devolvemos 1
    if not var:
        return 1.0
    # Obtenemos la primera variable
    Y, rest = var[0], var[1:]
    # Si la variable está en la evidencia
    if Y in e:
        # Calculamos la probabilidad condicional
        return P(Y, e[Y], bn) * enumerate_all(rest, e, bn)
    else:
        # Calculamos la suma de las probabilidades para cada valor de la variable
        return sum(P(Y, y, bn, e) * enumerate_all(rest, extend(e, Y, y), bn) for y in bn[Y])

# Definimos la función auxiliar para normalizar las probabilidades
def normalize(Q):
    # Calculamos la suma de todas las probabilidades
    total = sum(Q.values())
    # Normalizamos dividiendo cada probabilidad por la suma total
    for x in Q:
        Q[x] /= total
    # Devolvemos el diccionario normalizado
    return Q

# Definimos la función auxiliar para extender la evidencia con una nueva variable
def extend(e, var, val):
    # Creamos una copia de la evidencia
    e2 = e.copy()
    # Asignamos el valor a la nueva variable
    e2[var] = val
    # Devolvemos la evidencia extendida
    return e2

def P(var, val, bn, e):
    # Si la variable no tiene padres
    if len(bn[var]) == 1:
        # Devolvemos la probabilidad directamente
        return bn[var][val]
    else:
        # Obtenemos los padres de la variable
        parents = list(bn[var].keys())[1:]
        # Verificamos si todos los padres tienen valores en la evidencia
        if all(parent in e for parent in parents):
            # Obtenemos los valores de los padres en la evidencia
            parent_vals = tuple(e[parent] for parent in parents)
            # Devolvemos la probabilidad condicional correspondiente
            return bn[var][parent_vals][val]
        else:
            # Si no todos los padres tienen valores en la evidencia, devolvemos 1 (probabilidad uniforme)
            return 1.0

# Definimos la red bayesiana
# Cada variable tiene como llave un diccionario que contiene las probabilidades condicionales
# '': representa el conjunto vacío de padres, es decir, la variable no tiene padres
# Las demás llaves son los posibles valores de la variable, y los valores son diccionarios con las probabilidades condicionales
bn = {'A': P_A, 'B': P_B_given_A, 'C': P_C_given_A}

# Realizamos una consulta de inferencia para obtener la probabilidad de A dado B=True y C=False
result = enumeration_ask('A', {'B': 'T', 'C': 'F'}, bn)
# Imprimimos el resultado
print("P(A | B=T, C=F) =", result['T'])
