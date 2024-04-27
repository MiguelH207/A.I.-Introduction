# Miguel Angel HJuerta Castillo     21310236

import numpy as np  # Importamos la librería numpy para operaciones matemáticas eficientes

# Definimos las probabilidades iniciales de que el semáforo esté en verde o rojo
prob_verde_inicial = 0.5  # Probabilidad inicial de que el semáforo esté en verde
prob_rojo_inicial = 0.5   # Probabilidad inicial de que el semáforo esté en rojo

# Definimos las probabilidades de transición de estado del semáforo (verde a verde, verde a rojo, rojo a verde, rojo a rojo)
prob_transicion = np.array([[0.7, 0.3],   # Probabilidad de transición de verde a verde y verde a rojo
                            [0.4, 0.6]])  # Probabilidad de transición de rojo a verde y rojo a rojo

# Definimos la función para calcular la probabilidad del estado del semáforo en el tiempo t
def calcular_probabilidad_estado(t):
    # Inicializamos la probabilidad inicial en el tiempo t=0
    prob_estado_t = np.array([prob_verde_inicial, prob_rojo_inicial])
    
    # Realizamos la actualización iterativa de la probabilidad del estado en cada paso de tiempo
    for _ in range(t):
        prob_estado_t = np.dot(prob_estado_t, prob_transicion)  # Actualizamos la probabilidad del estado utilizando la matriz de transición
    
    return prob_estado_t

# Definimos el tiempo máximo hasta el cual queremos calcular la probabilidad del estado
tiempo_maximo = 5

# Calculamos la probabilidad del estado del semáforo en cada instante de tiempo hasta tiempo_maximo
for t in range(tiempo_maximo + 1):
    prob_estado = calcular_probabilidad_estado(t)  # Calculamos la probabilidad del estado en el tiempo t
    print(f"Probabilidad en el tiempo {t}: Verde={prob_estado[0]}, Rojo={prob_estado[1]}")  # Imprimimos la probabilidad del estado en el tiempo t
