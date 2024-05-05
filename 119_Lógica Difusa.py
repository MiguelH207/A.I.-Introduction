# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo práctico de lógica difusa en Python.
# La lógica difusa permite manejar valores imprecisos o difusos, lo cual es útil en situaciones donde las categorías son ambiguas o no se pueden definir con precisión.
# En este ejemplo, vamos a crear un sistema difuso simple para determinar la calificación de un estudiante en base a su desempeño numérico en un examen.

import numpy as np  # Importamos la biblioteca numpy para operaciones numéricas
import skfuzzy as fuzz  # Importamos la biblioteca scikit-fuzzy para lógica difusa
from skfuzzy import control as ctrl  # Importamos el módulo de control de scikit-fuzzy

# Creamos las variables de entrada y salida del sistema difuso
puntuacion = ctrl.Antecedent(np.arange(0, 101, 1), 'puntuacion')  # Variable de entrada: puntuación del estudiante
calificacion = ctrl.Consequent(np.arange(0, 11, 1), 'calificacion')  # Variable de salida: calificación del estudiante

# Definimos las funciones de membresía para la variable de entrada "puntuacion"
puntuacion['mala'] = fuzz.trimf(puntuacion.universe, [0, 0, 50])  # Función de membresía para puntuación mala
puntuacion['regular'] = fuzz.trimf(puntuacion.universe, [40, 60, 80])  # Función de membresía para puntuación regular
puntuacion['buena'] = fuzz.trimf(puntuacion.universe, [70, 100, 100])  # Función de membresía para puntuación buena

# Definimos las funciones de membresía para la variable de salida "calificacion"
calificacion['mala'] = fuzz.trimf(calificacion.universe, [0, 0, 5])  # Función de membresía para calificación mala
calificacion['regular'] = fuzz.trimf(calificacion.universe, [4, 6, 8])  # Función de membresía para calificación regular
calificacion['buena'] = fuzz.trimf(calificacion.universe, [7, 10, 10])  # Función de membresía para calificación buena

# Reglas difusas para determinar la calificación
rule1 = ctrl.Rule(puntuacion['mala'], calificacion['mala'])  # Si la puntuación es mala, la calificación es mala
rule2 = ctrl.Rule(puntuacion['regular'], calificacion['regular'])  # Si la puntuación es regular, la calificación es regular
rule3 = ctrl.Rule(puntuacion['buena'], calificacion['buena'])  # Si la puntuación es buena, la calificación es buena

# Creamos el sistema de control difuso
calificacion_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

# Creamos el simulador del sistema de control difuso
calificacion_simulador = ctrl.ControlSystemSimulation(calificacion_ctrl)

# Simulamos el sistema con una puntuación de ejemplo
calificacion_simulador.input['puntuacion'] = 75  # Asignamos una puntuación de ejemplo
calificacion_simulador.compute()  # Calculamos la calificación

# Imprimimos el resultado
print("Calificación:", calificacion_simulador.output['calificacion'])

# Visualizamos las funciones de membresía y la salida difusa
puntuacion.view()
calificacion.view()
