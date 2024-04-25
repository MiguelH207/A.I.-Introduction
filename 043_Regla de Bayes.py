# Definición de la función que calcula la probabilidad condicional utilizando la regla de Bayes
def bayes_rule(prior_A, prob_B_given_A, prob_B_given_not_A):
    # Calcula la probabilidad complementaria de A (no tener la enfermedad)
    not_A = 1 - prior_A
    # Calcula el numerador de la regla de Bayes
    numerator = prob_B_given_A * prior_A
    # Calcula el denominador de la regla de Bayes
    denominator = numerator + prob_B_given_not_A * not_A
    # Calcula la probabilidad condicional usando la regla de Bayes
    posterior_A = numerator / denominator
    # Devuelve la probabilidad condicional
    return posterior_A

# Probabilidad de tener la enfermedad antes de realizar la prueba (prior probability)
prior_disease = 0.01
# Sensibilidad de la prueba (probabilidad de obtener un resultado positivo si se tiene la enfermedad)
sensitivity = 0.95
# Especificidad de la prueba (probabilidad de obtener un resultado negativo si no se tiene la enfermedad)
specificity = 0.90

# Probabilidad de obtener un resultado positivo si se tiene la enfermedad (probabilidad condicional)
prob_positive_given_disease = sensitivity
# Probabilidad de obtener un resultado positivo si no se tiene la enfermedad (probabilidad condicional)
prob_positive_given_no_disease = 1 - specificity

# Aplicación de la regla de Bayes para calcular la probabilidad de tener la enfermedad dado un resultado positivo en la prueba
posterior_disease = bayes_rule(prior_disease, prob_positive_given_disease, prob_positive_given_no_disease)

# Impresión del resultado
print("La probabilidad de tener la enfermedad dado un resultado positivo en la prueba es:", posterior_disease)
