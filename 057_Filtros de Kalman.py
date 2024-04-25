# Miguel Angel Huerta Castillo 21310236
# Este programa implementa un filtro de Kalman para realizar un razonamiento probabilístico en el tiempo.
# El filtro de Kalman es un método de estimación recursiva que utiliza una serie de mediciones observadas a lo largo del tiempo y produce estimaciones de variables desconocidas que tienden a ser más precisas que las que se obtendrían simplemente a partir de una sola medición.
# El ejemplo práctico utilizado en este programa es el de estimar la posición y velocidad de un objeto en movimiento en una dimensión.

import numpy as np

# Función que implementa el filtro de Kalman
def kalman_filter(mu, sigma, z, u, A, B, C, R, Q):
    # Predicción del nuevo estado
    mu_bar = np.dot(A, mu) + np.dot(B, u)
    # Predicción de la nueva covarianza
    sigma_bar = np.dot(np.dot(A, sigma), A.T) + R
    # Calcular el error de la predicción
    y = z - np.dot(C, mu_bar)
    # Calcular la ganancia de Kalman
    K = np.dot(np.dot(sigma_bar, C.T), np.linalg.inv(np.dot(np.dot(C, sigma_bar), C.T) + Q))
    # Actualizar el estado estimado
    mu = mu_bar + np.dot(K, y)
    # Actualizar la covarianza estimada
    sigma = np.dot((np.eye(len(mu)) - np.dot(K, C)), sigma_bar)

    return mu, sigma

# Parámetros iniciales
# Posición y velocidad inicial estimada
mu = np.array([[0.0], [0.0]])
# Covarianza inicial estimada
sigma = np.array([[1000.0, 0.0], [0.0, 1000.0]])
# Medida de la posición
z = np.array([[5.0]])
# Vector de control
u = np.array([[0.0]])
# Matriz de transición de estado
A = np.array([[1.0, 1.0], [0.0, 1.0]])
# Matriz de control
B = np.array([[0.0], [0.0]])
# Matriz de observación
C = np.array([[1.0, 0.0]])
# Covarianza del ruido de proceso
R = np.array([[0.1, 0.0], [0.0, 0.1]])
# Covarianza del ruido de medición
Q = np.array([[0.1]])

# Ejecutar el filtro de Kalman
mu, sigma = kalman_filter(mu, sigma, z, u, A, B, C, R, Q)

# Imprimir los resultados
print("Estimacion de la posicion (Mu):")
print(mu)
print("Covarianza (Sigma):")
print(sigma)
