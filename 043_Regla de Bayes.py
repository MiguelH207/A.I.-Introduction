# Miguel Angel Huerta Castillo     21310236
# Este programa en Python implementa la Regla de Bayes para calcular la probabilidad condicional de un evento dado el conocimiento de otros eventos.

# Definición de la función para calcular la probabilidad condicional usando la Regla de Bayes
def regla_de_bayes(probabilidad_A, probabilidad_B_dado_A, probabilidad_B_dado_no_A):
    # Calcula la probabilidad complementaria de A
    probabilidad_no_A = 1 - probabilidad_A
    # Calcula la probabilidad de B usando la fórmula de Bayes
    probabilidad_B = (probabilidad_A * probabilidad_B_dado_A) + (probabilidad_no_A * probabilidad_B_dado_no_A)
    # Calcula la probabilidad condicional de A dado B usando la fórmula de Bayes
    probabilidad_A_dado_B = (probabilidad_A * probabilidad_B_dado_A) / probabilidad_B
    return probabilidad_A_dado_B

# Probabilidad de que un paciente tenga la enfermedad
probabilidad_enfermedad = 0.01
# Probabilidad de que el paciente tenga un resultado positivo en la prueba si tiene la enfermedad
probabilidad_positivo_dado_enfermedad = 0.95
# Probabilidad de que el paciente tenga un resultado positivo en la prueba si no tiene la enfermedad
probabilidad_positivo_dado_no_enfermedad = 0.10

# Calcula la probabilidad condicional de que el paciente tenga la enfermedad dado que el resultado de la prueba es positivo
probabilidad_enfermedad_dado_positivo = regla_de_bayes(probabilidad_enfermedad, probabilidad_positivo_dado_enfermedad, probabilidad_positivo_dado_no_enfermedad)

# Imprime el resultado
print("La probabilidad de que el paciente tenga la enfermedad dado un resultado positivo en la prueba es:", probabilidad_enfermedad_dado_positivo)
