# Miguel Angel Huerta Castillo     21310236
# Este programa implementa dos métodos de razonamiento probabilístico: muestreo directo y por rechazo.
# El muestreo directo genera muestras directamente de una distribución de probabilidad conocida, mientras que el muestreo por rechazo
# genera muestras de una distribución objetivo utilizando una distribución de propuesta y un factor de escala.
# El ejemplo práctico que se presenta es la generación de muestras de una distribución normal utilizando ambos métodos.

import numpy as np  # Importamos la librería numpy para realizar cálculos numéricos

# Definimos la función de densidad de probabilidad (PDF) de una distribución normal estándar
def normal_pdf(x):
    return np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)

# Muestreo directo: generamos muestras de una distribución normal estándar utilizando el método de Box-Muller
def direct_sampling(n):
    u1 = np.random.rand(n)  # Generamos n números aleatorios uniformemente distribuidos en el intervalo [0, 1)
    u2 = np.random.rand(n)  # Generamos n números aleatorios uniformemente distribuidos en el intervalo [0, 1)
    z1 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)  # Transformación de Box-Muller para generar muestras de una distribución normal
    z2 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)  # Transformación de Box-Muller para generar muestras de una distribución normal
    return z1, z2

# Muestreo por rechazo: generamos muestras de una distribución normal utilizando una distribución de propuesta uniforme
def rejection_sampling(n):
    samples = []  # Inicializamos una lista para almacenar las muestras aceptadas
    while len(samples) < n:
        x = np.random.uniform(-4, 4)  # Generamos una muestra de la distribución de propuesta uniforme en el intervalo [-4, 4]
        u = np.random.rand()  # Generamos un número aleatorio uniformemente distribuido en el intervalo [0, 1)
        if u < normal_pdf(x) / 0.4:  # Comprobamos si la muestra es aceptada según el criterio de rechazo
            samples.append(x)  # Si la muestra es aceptada, la agregamos a la lista de muestras
    return np.array(samples)

# Definimos el tamaño de la muestra
n_samples = 1000

# Generamos muestras utilizando ambos métodos
direct_samples = direct_sampling(n_samples)
rejection_samples = rejection_sampling(n_samples)

# Imprimimos las primeras 10 muestras generadas por cada método
print("Muestreo directo:")
print(direct_samples[:10])
print("\nMuestreo por rechazo:")
print(rejection_samples[:10])
