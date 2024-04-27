# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo básico de inferencia difusa utilizando la librería skfuzzy en Python.
# La lógica difusa es útil para modelar y resolver problemas en los que las variables tienen valores imprecisos o difusos.
# En este ejemplo, se utilizará la inferencia difusa para determinar la calidad del servicio en un restaurante basándose en dos variables: la calidad de la comida y el servicio.

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Se definen las variables de entrada y salida difusas
# Se crea el Antecedente (input) 'calidad_comida' con tres funciones de membresía: mala, aceptable y buena
calidad_comida = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad_comida')
calidad_comida['mala'] = fuzz.trimf(calidad_comida.universe, [0, 0, 5])
calidad_comida['aceptable'] = fuzz.trimf(calidad_comida.universe, [0, 5, 10])
calidad_comida['buena'] = fuzz.trimf(calidad_comida.universe, [5, 10, 10])

# Se crea el Antecedente (input) 'servicio' con tres funciones de membresía: malo, aceptable y bueno
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
servicio['malo'] = fuzz.trimf(servicio.universe, [0, 0, 5])
servicio['aceptable'] = fuzz.trimf(servicio.universe, [0, 5, 10])
servicio['bueno'] = fuzz.trimf(servicio.universe, [5, 10, 10])

# Se crea la Consecuente (output) 'propina' con tres funciones de membresía: baja, media y alta
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')
propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])

# Se definen las reglas difusas
# Regla 1: Si la calidad de la comida es mala o el servicio es malo, entonces la propina es baja
# Regla 2: Si el servicio es aceptable, entonces la propina es media
# Regla 3: Si la calidad de la comida es buena o el servicio es bueno, entonces la propina es alta
regla1 = ctrl.Rule(calidad_comida['mala'] | servicio['malo'], propina['baja'])
regla2 = ctrl.Rule(servicio['aceptable'], propina['media'])
regla3 = ctrl.Rule(calidad_comida['buena'] | servicio['bueno'], propina['alta'])

# Se crea el sistema de control difuso
sistema_propina = ctrl.ControlSystem([regla1, regla2, regla3])

# Se simula el sistema de control difuso
propina_prediccion = ctrl.ControlSystemSimulation(sistema_propina)

# Se ingresan valores para la calidad de la comida y el servicio
propina_prediccion.input['calidad_comida'] = 6.5
propina_prediccion.input['servicio'] = 9.8

# Se calcula el resultado
propina_prediccion.compute()

# Se muestra el resultado
print("Propina predicha:", propina_prediccion.output['propina'])
propina.view(sim=propina_prediccion)
