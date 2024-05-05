# Miguel Angel Huerta Castillo
# 21310236

# Este programa utiliza lógica difusa para calcular la propina en un restaurante.
# La lógica difusa permite manejar la incertidumbre y la imprecisión en los datos de entrada.

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Se definen los rangos de las variables de entrada y salida
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Se definen las funciones de membresía para cada variable
calidad['baja'] = fuzz.trimf(calidad.universe, [0, 0, 5])
calidad['media'] = fuzz.trimf(calidad.universe, [0, 5, 10])
calidad['alta'] = fuzz.trimf(calidad.universe, [5, 10, 10])

servicio['malo'] = fuzz.trimf(servicio.universe, [0, 0, 5])
servicio['regular'] = fuzz.trimf(servicio.universe, [0, 5, 10])
servicio['excelente'] = fuzz.trimf(servicio.universe, [5, 10, 10])

propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])

# Se visualizan las funciones de membresía
calidad.view()
servicio.view()
propina.view()

# Se definen las reglas difusas
regla1 = ctrl.Rule(calidad['baja'] | servicio['malo'], propina['baja'])
regla2 = ctrl.Rule(servicio['regular'], propina['media'])
regla3 = ctrl.Rule(servicio['excelente'] | calidad['alta'], propina['alta'])

# Se crea el sistema de control difuso
sistema_propina = ctrl.ControlSystem([regla1, regla2, regla3])
propina_final = ctrl.ControlSystemSimulation(sistema_propina)

# Se introducen valores de entrada
propina_final.input['calidad'] = 6.5
propina_final.input['servicio'] = 9.8

# Se calcula el resultado
propina_final.compute()

# Se muestra el resultado
print("Propina sugerida:", propina_final.output['propina'])
propina.view(sim=propina_final)
