# Miguel Angel Huerta Castillo     21310236

# Este programa implementa un ejemplo de Razonamiento Probabilístico en el tiempo utilizando
# técnicas de Filtrado, Predicción, Suavizado y Explicación. El ejemplo se basa en predecir la 
# temperatura promedio mensual en una ciudad utilizando un modelo de espacio de estado. El modelo 
# considera la temperatura promedio del mes anterior y el cambio en la temperatura como variables 
# de estado. Se utiliza el algoritmo de Filtro de Kalman para estimar el estado actual, predecir 
# el estado futuro y suavizar el estado pasado.

import numpy as np

# Definición de las matrices del modelo de espacio de estado
# Matriz de transición de estado: describe cómo evolucionan las variables de estado en el tiempo
# En este caso, la temperatura promedio mensual y su cambio
A = np.array([[1, 1], [0, 1]])

# Matriz de observación: describe cómo se relacionan las variables de estado con las observaciones
# En este caso, la temperatura promedio mensual
H = np.array([[1, 0]])

# Covarianza del ruido de proceso: describe la incertidumbre en la evolución de las variables de estado
# En este caso, se asume una pequeña incertidumbre en el cambio de temperatura
Q = np.array([[0.1, 0], [0, 0.1]])

# Covarianza del ruido de medición: describe la incertidumbre en las observaciones
# En este caso, se asume una pequeña incertidumbre en la medición de la temperatura
R = np.array([[1]])

# Estado inicial: temperatura promedio del primer mes y su cambio
x0 = np.array([[20], [0]])

# Covarianza inicial: incertidumbre en el estado inicial
P0 = np.array([[1, 0], [0, 1]])

# Definición del número de meses a predecir
num_months = 12

# Simulación de datos de temperatura promedio mensual (ejemplo)
# Se genera un arreglo de temperaturas aleatorias con media 20°C y desviación estándar de 5°C
temperature_data = np.random.normal(20, 5, num_months)

# Implementación del algoritmo de Filtro de Kalman
x = x0
P = P0
predicted_temperatures = []

for z in temperature_data:
    # Predicción del siguiente estado
    x_pred = np.dot(A, x)
    P_pred = np.dot(np.dot(A, P), A.T) + Q
    
    # Actualización del estado basado en la nueva observación
    y = z - np.dot(H, x_pred)
    S = np.dot(np.dot(H, P_pred), H.T) + R
    K = np.dot(np.dot(P_pred, H.T), np.linalg.inv(S))
    x = x_pred + np.dot(K, y)
    P = P_pred - np.dot(np.dot(K, H), P_pred)
    
    # Almacenamiento de la temperatura predicha para este mes
    predicted_temperatures.append(x[0, 0])

# Impresión de las temperaturas predichas
print("Temperaturas predichas para los próximos", num_months, "meses:")
for i, temp in enumerate(predicted_temperatures):
    print("Mes", i+1, ":", temp)
