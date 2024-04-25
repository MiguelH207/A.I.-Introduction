# Miguel Angel Huerta Castillo     21310236
# Este programa en Python implementa un ejemplo práctico de razonamiento probabilístico utilizando el método de ponderación de verosimilitud.
# El método de ponderación de verosimilitud se utiliza para calcular la probabilidad de que un evento pertenezca a una clase determinada dado cierto conjunto de características observadas.

import numpy as np

# Definición de las probabilidades a priori de las clases A y B
prior_prob_A = 0.6
prior_prob_B = 0.4

# Definición de las probabilidades condicionales P(característica|clase)
# En este ejemplo, se asumen dos características: característica_1 y característica_2.
# Las probabilidades se almacenan en forma de diccionario, donde las claves son las clases y los valores son los arrays de probabilidades condicionales.
cond_probs = {
    'A': np.array([0.8, 0.2]),  # Probabilidades condicionales para la clase A: P(característica_1|A), P(característica_2|A)
    'B': np.array([0.3, 0.7])   # Probabilidades condicionales para la clase B: P(característica_1|B), P(característica_2|B)
}

# Función para calcular la probabilidad de una clase dadas las características observadas
def likelihood_weighting(features):
    # Calcula la verosimilitud para cada clase
    likelihoods = {}
    for class_label, cond_prob in cond_probs.items():
        likelihood = np.prod(cond_prob ** features)  # Calcula el producto de las probabilidades condicionales elevadas a la potencia de las características observadas
        likelihoods[class_label] = likelihood
    
    # Realiza la ponderación de verosimilitud
    total_likelihood = sum(likelihoods.values())
    weighted_likelihoods = {class_label: likelihood / total_likelihood for class_label, likelihood in likelihoods.items()}
    
    return weighted_likelihoods

# Ejemplo de uso del programa
# Supongamos que tenemos dos características observadas: característica_1 es verdadera (1) y característica_2 es falsa (0)
observed_features = np.array([1, 0])

# Calcula las probabilidades ponderadas de pertenencia a cada clase
weighted_probs = likelihood_weighting(observed_features)

# Imprime los resultados
for class_label, prob in weighted_probs.items():
    print(f'La probabilidad ponderada de pertenencia a la clase {class_label} es: {prob}')
