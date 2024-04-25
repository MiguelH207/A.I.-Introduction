# Miguel Angel Huerta Castillo     21310236
# Este programa en Python implementa el razonamiento probabilístico utilizando la Regla de la Cadena.
# El código calcula la probabilidad condicional P(A|B) utilizando la Regla de la Cadena, donde se tiene P(A|B) = P(A ∩ B) / P(B).

# Definición de la función para calcular la probabilidad condicional utilizando la Regla de la Cadena
def regla_de_la_cadena(P_A, P_B_dado_A, P_B):
    # Calcula la probabilidad de la intersección de A y B
    P_A_interseccion_B = P_A * P_B_dado_A
    # Calcula la probabilidad condicional P(A|B)
    P_A_dado_B = P_A_interseccion_B / P_B
    # Devuelve la probabilidad condicional P(A|B)
    return P_A_dado_B

# Probabilidad de A
P_A = 0.4
# Probabilidad de B dado A
P_B_dado_A = 0.7
# Probabilidad de B
P_B = 0.5

# Calcula la probabilidad condicional P(A|B) utilizando la Regla de la Cadena
resultado = regla_de_la_cadena(P_A, P_B_dado_A, P_B)

# Imprime el resultado
print("La probabilidad condicional P(A|B) es:", resultado)
