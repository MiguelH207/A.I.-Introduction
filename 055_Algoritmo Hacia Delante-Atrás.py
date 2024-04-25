import numpy as np  # Importamos NumPy para operaciones matriciales

# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un algoritmo de razonamiento probabilístico en el tiempo utilizando el algoritmo Hacia Delante-Atrás.
# El programa simula un ejemplo práctico de inferencia probabilística en un sistema de monedas y la probabilidad de obtener cierto número de caras en un número específico de lanzamientos de monedas.

def forward_backward_algorithm(observations, prior_probability, transition_model, sensor_model):
    """
    Función que implementa el algoritmo Hacia Delante-Atrás para razonamiento probabilístico en el tiempo.
    
    :param observations: Lista de observaciones (datos observados).
    :param prior_probability: Probabilidad a priori (distribución inicial).
    :param transition_model: Modelo de transición (probabilidades de transición entre estados).
    :param sensor_model: Modelo sensorial (probabilidades de observar ciertos datos dado un estado).
    :return: Distribución de probabilidad posterior.
    """
    # Inicialización del paso hacia adelante
    forward_messages = [prior_probability]
    for t in range(1, len(observations) + 1):
        # Paso hacia adelante: Predicción
        prediction = np.dot(transition_model, forward_messages[t - 1])
        # Paso hacia adelante: Corrección
        correction = sensor_model[observations[t - 1]] * prediction
        forward_messages.append(correction)
    
    # Inicialización del paso hacia atrás
    backward_message = 1.0
    posterior = []
    for t in range(len(observations), 0, -1):
        # Paso hacia atrás: Actualización del mensaje hacia atrás
        updated_backward_message = backward_message * sensor_model[observations[t - 1]] * prior_probability
        # Calculando la probabilidad posterior
        posterior.insert(0, forward_messages[t] * updated_backward_message)
        # Actualización del mensaje hacia atrás
        backward_message = np.dot(np.transpose(transition_model), backward_message)
    
    # Normalización de la distribución posterior
    posterior_sum = sum(posterior)
    normalized_posterior = [prob / posterior_sum for prob in posterior]
    
    return normalized_posterior

# Ejemplo de uso del algoritmo Hacia Delante-Atrás
if __name__ == "__main__":
    # Definición de parámetros del modelo
    observations = [0, 1, 0, 0]  # Secuencia de observaciones: 0 representa cara, 1 representa sello
    prior_probability = [0.5, 0.5]  # Distribución de probabilidad a priori
    transition_model = np.array([[0.8, 0.2],  # Modelo de transición: Probabilidad de permanecer en el mismo estado o cambiar
                                 [0.3, 0.7]])
    sensor_model = np.array([[0.6, 0.4],  # Modelo sensorial: Probabilidad de observar cada resultado dado el estado
                              [0.4, 0.6]])

    # Llamada al algoritmo Hacia Delante-Atrás
    posterior = forward_backward_algorithm(observations, prior_probability, transition_model, sensor_model)
    
    # Resultado
    posterior_flat = [posterior_t.tolist() for posterior_t in posterior]  # Convertir matrices de NumPy a listas
    print("Distribución de probabilidad posterior:")
    for t, posterior_t in enumerate(posterior_flat):
        print(f"Tiempo {t+1}: {posterior_t}")  # Imprimir la distribución de probabilidad posterior en cada paso de tiempo
