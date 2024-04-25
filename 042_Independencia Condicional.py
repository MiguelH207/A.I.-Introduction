# Miguel Angel Huerta Castillo     21310236 

# Importamos la función product de la librería itertools para calcular el producto cartesiano de dos conjuntos.
from itertools import product

# Definimos la función para calcular la probabilidad condicional de A dado B.
def conditional_probability(A, B, P):
    # Calculamos el producto cartesiano de A y B.
    cartesian_product = list(product(A, B))
    # Contamos el número de elementos en el producto cartesiano.
    total_outcomes = len(cartesian_product)
    # Contamos el número de elementos en B.
    outcomes_in_B = len(B)
    # Inicializamos un contador para los eventos en A dado B.
    outcomes_in_A_given_B = 0
    # Iteramos sobre el producto cartesiano.
    for event in cartesian_product:
        # Si el evento está en A y en B, incrementamos el contador.
        if event[0] in A and event[1] in B:
            outcomes_in_A_given_B += 1
    # Calculamos la probabilidad condicional de A dado B.
    probability = outcomes_in_A_given_B / outcomes_in_B
    return probability

# Definimos los eventos A y B como conjuntos de posibles resultados.
A = {'H', 'T'}  # Evento A: lanzar una moneda, donde 'H' es cara y 'T' es cruz.
B = {'1', '2', '3', '4', '5', '6'}  # Evento B: lanzar un dado de seis caras.
# Definimos la probabilidad de obtener cada resultado en el evento B.
P_B = {result: 1/6 for result in B}
# Calculamos la probabilidad condicional de A dado B.
probability_A_given_B = conditional_probability(A, B, P_B)
# Imprimimos el resultado.
print("La probabilidad de obtener cara en la moneda, dado que se ha obtenido un número par en el dado, es:", probability_A_given_B)
