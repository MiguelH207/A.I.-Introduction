# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo de Razonamiento Probabilístico utilizando el concepto de Manto de Markov.
# El ejemplo simula el clima utilizando un modelo de cadena de Markov para predecir el clima de mañana basado en el clima actual.

import numpy as np  # Importa la biblioteca numpy para operaciones matemáticas
from numpy.random import choice  # Importa la función choice de la biblioteca numpy.random

# Definición de las probabilidades de transición entre estados (climas)
probabilidades_transicion = np.array([[0.7, 0.3],  # Probabilidad de pasar de soleado a soleado y de soleado a nublado
                                      [0.4, 0.6]]) # Probabilidad de pasar de nublado a soleado y de nublado a nublado

# Lista de posibles estados (soleado, nublado)
estados = ['soleado', 'nublado']

# Estado inicial (clima actual)
estado_actual = 'soleado'

# Número de días para simular
dias_simulados = 7

# Itera sobre el número de días a simular
for dia in range(dias_simulados):
    print("Día", dia+1, ":", estado_actual)  # Imprime el día actual y el clima actual
    
    # Calcula el siguiente estado (clima) basado en las probabilidades de transición
    estado_actual = choice(estados, p=probabilidades_transicion[estados.index(estado_actual)])

