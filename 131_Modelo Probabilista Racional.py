# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo de Representación del Conocimiento utilizando el Modelo Probabilista Racional.
# El ejemplo consiste en modelar la probabilidad de que una persona pase un examen en función de su estudio previo y el nivel de dificultad del examen.

import numpy as np  # Importa la biblioteca numpy para operaciones numéricas

# Definir las probabilidades iniciales: P(Estudio), P(Dificultad del Examen) y P(Pasar el Examen)
prob_estudio = 0.7  # Probabilidad de que la persona haya estudiado
prob_dificultad_examen = 0.5  # Probabilidad de que el examen sea difícil
prob_pasar_examen = 0.0  # Probabilidad inicial de pasar el examen

# Función para calcular la probabilidad de pasar el examen utilizando el Modelo Probabilista Racional
def calcular_probabilidad_pasar_examen(prob_estudio, prob_dificultad_examen):
    # Calcula la probabilidad condicional de pasar el examen dado que la persona estudió y el examen es difícil
    prob_pasar_examen_dado_estudio_y_dificil = 0.8

    # Calcula la probabilidad condicional de pasar el examen dado que la persona estudió y el examen no es difícil
    prob_pasar_examen_dado_estudio_y_facil = 0.9

    # Calcula la probabilidad condicional de pasar el examen dado que la persona no estudió y el examen es difícil
    prob_pasar_examen_dado_no_estudio_y_dificil = 0.01

    # Calcula la probabilidad condicional de pasar el examen dado que la persona no estudió y el examen no es difícil
    prob_pasar_examen_dado_no_estudio_y_facil = 0.4

    # Calcula la probabilidad de pasar el examen utilizando el Teorema de Bayes
    prob_pasar_examen = (prob_pasar_examen_dado_estudio_y_dificil * prob_dificultad_examen * prob_estudio) + \
                        (prob_pasar_examen_dado_estudio_y_facil * (1 - prob_dificultad_examen) * prob_estudio) + \
                        (prob_pasar_examen_dado_no_estudio_y_dificil * prob_dificultad_examen * (1 - prob_estudio)) + \
                        (prob_pasar_examen_dado_no_estudio_y_facil * (1 - prob_dificultad_examen) * (1 - prob_estudio))
    return prob_pasar_examen

# Calcular la probabilidad de pasar el examen llamando a la función definida
prob_pasar_examen = calcular_probabilidad_pasar_examen(prob_estudio, prob_dificultad_examen)

# Imprimir el resultado
print("La probabilidad de pasar el examen es:", prob_pasar_examen)
