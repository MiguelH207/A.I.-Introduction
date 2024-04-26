# Miguel Angel Huerta Castillo     21310236
# Programa de Aprendizaje Probabilístico utilizando el algoritmo EM.
# El algoritmo EM (Expectation-Maximization) es utilizado para encontrar estimaciones de los parámetros de un modelo estadístico cuando los datos tienen variables ocultas o faltantes.
# En este ejemplo, se utilizará el algoritmo EM para estimar los parámetros de un modelo de mezcla de Gaussianas.

import numpy as np
from scipy.stats import norm

# Función para calcular la probabilidad de pertenencia de cada punto a cada componente
def expectation(data, means, variances, weights):
    num_components = len(means)
    num_points = len(data)
    responsibilities = np.zeros((num_points, num_components))  # Inicializar matriz de responsabilidades

    for i in range(num_points):
        for j in range(num_components):
            responsibilities[i, j] = weights[j] * norm.pdf(data[i], means[j], np.sqrt(variances[j]))  # Calcular la probabilidad usando la densidad de probabilidad normal

        responsibilities[i, :] /= np.sum(responsibilities[i, :])  # Normalizar las responsabilidades para cada punto

    return responsibilities

# Función para actualizar los parámetros del modelo
def maximization(data, responsibilities):
    num_components = responsibilities.shape[1]
    num_points = len(data)
    means = np.zeros(num_components)
    variances = np.zeros(num_components)
    weights = np.zeros(num_components)

    for j in range(num_components):
        weights[j] = np.sum(responsibilities[:, j]) / num_points  # Calcular el peso de cada componente

        means[j] = np.sum(responsibilities[:, j] * data) / np.sum(responsibilities[:, j])  # Calcular la media de cada componente

        variances[j] = np.sum(responsibilities[:, j] * (data - means[j])**2) / np.sum(responsibilities[:, j])  # Calcular la varianza de cada componente

    return means, variances, weights

# Función para ejecutar el algoritmo EM
def em_algorithm(data, num_components, max_iter=100, tol=1e-4):
    # Inicialización aleatoria de los parámetros
    means = np.random.randn(num_components)
    variances = np.abs(np.random.randn(num_components))
    weights = np.ones(num_components) / num_components

    log_likelihood = -np.inf

    for _ in range(max_iter):
        # Expectation step
        responsibilities = expectation(data, means, variances, weights)

        # Maximization step
        means, variances, weights = maximization(data, responsibilities)

        # Calcular log-likelihood para verificar la convergencia
        new_log_likelihood = 0
        for i in range(len(data)):
            new_log_likelihood += np.log(np.sum(weights * norm.pdf(data[i], means, np.sqrt(variances))))

        # Verificar convergencia
        if np.abs(new_log_likelihood - log_likelihood) < tol:
            break

        log_likelihood = new_log_likelihood

    return means, variances, weights

# Ejemplo de uso
if __name__ == "__main__":
    # Generar datos de dos distribuciones normales
    np.random.seed(0)
    data1 = np.random.normal(loc=5, scale=1, size=100)
    data2 = np.random.normal(loc=10, scale=2, size=100)
    data = np.concatenate((data1, data2))

    # Ejecutar algoritmo EM para encontrar los parámetros del modelo de mezcla de Gaussianas
    num_components = 2
    means, variances, weights = em_algorithm(data, num_components)

    print("Means:", means)
    print("Variances:", variances)
    print("Weights:", weights)
