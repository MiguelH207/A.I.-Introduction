# Miguel Angel Huerta Castillo    21310236

# Definición de la función para calcular la probabilidad condicionada
def probabilidad_condicionada(prob_A, prob_B_dado_A, prob_B_dado_no_A):
    # Calcula la probabilidad condicionada utilizando el teorema de Bayes
    return (prob_A * prob_B_dado_A) / ((prob_A * prob_B_dado_A) + ((1 - prob_A) * prob_B_dado_no_A))

# Definición de la función para normalizar las probabilidades
def normalizar_probabilidades(probabilidades):
    # Suma de todas las probabilidades
    suma = sum(probabilidades)
    # Normalización dividiendo cada probabilidad por la suma total
    return [prob / suma for prob in probabilidades]

# Probabilidad de tener diabetes en la población general
prob_diabetes = 0.01

# Probabilidad de obtener un resultado positivo en la prueba de diabetes si tiene diabetes
prob_positivo_dado_diabetes = 0.9

# Probabilidad de obtener un resultado positivo en la prueba de diabetes si no tiene diabetes
prob_positivo_dado_no_diabetes = 0.1

# Calcula la probabilidad condicionada de tener diabetes dado un resultado positivo en la prueba
prob_diabetes_dado_positivo = probabilidad_condicionada(prob_diabetes, prob_positivo_dado_diabetes, prob_positivo_dado_no_diabetes)

# Calcula la probabilidad de no tener diabetes dado un resultado positivo en la prueba
prob_no_diabetes_dado_positivo = 1 - prob_diabetes_dado_positivo

# Normaliza las probabilidades para que sumen 1
probabilidades_normalizadas = normalizar_probabilidades([prob_diabetes_dado_positivo, prob_no_diabetes_dado_positivo])

# Imprime los resultados
print("Probabilidad de tener diabetes dado un resultado positivo en la prueba:", prob_diabetes_dado_positivo*100,"%")
print("Probabilidad de no tener diabetes dado un resultado positivo en la prueba:", prob_no_diabetes_dado_positivo*100,"%")
print("Probabilidades normalizadas:", probabilidades_normalizadas)
