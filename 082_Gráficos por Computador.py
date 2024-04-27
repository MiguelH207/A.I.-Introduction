# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo simple de perceptrón utilizando gráficos por computadora.
# El perceptrón toma dos entradas (x1 y x2), aplica pesos y un sesgo, y produce una salida binaria (0 o 1) basada en una función de activación.
# El programa grafica la función de decisión del perceptrón y muestra cómo clasifica los puntos en el plano.

import numpy as np  # Importa la biblioteca numpy para cálculos numéricos
import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib para graficar

# Definición de la función de activación (función escalón)
def step_function(x):
    return 1 if x >= 0 else 0  # Devuelve 1 si x es mayor o igual a 0, de lo contrario devuelve 0

# Definición del perceptrón
def perceptron_output(weights, bias, x):
    calculation = np.dot(weights, x) + bias  # Calcula el producto punto de los pesos y las entradas, y le suma el sesgo
    return step_function(calculation)  # Aplica la función de activación al resultado

# Datos de entrenamiento (entradas)
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Define los puntos de entrada como una matriz numpy

# Pesos y sesgo del perceptrón
weights = np.array([1, 1])  # Define los pesos del perceptrón
bias = -1.5  # Define el sesgo del perceptrón

# Clasificación de los puntos de entrada
classified_points = [perceptron_output(weights, bias, x) for x in inputs]  # Clasifica los puntos de entrada utilizando el perceptrón

# Graficación de los puntos y la función de decisión
plt.scatter(inputs[:,0], inputs[:,1], c=classified_points)  # Grafica los puntos y los colorea según su clasificación
plt.plot([0, 1], [1.5, 0.5], color='r')  # Grafica la función de decisión del perceptrón
plt.title('Perceptrón Simple')  # Título del gráfico
plt.xlabel('X1')  # Etiqueta del eje x
plt.ylabel('X2')  # Etiqueta del eje y
plt.grid(True)  # Habilita la cuadrícula en el gráfico
plt.show()  # Muestra el gráfico
