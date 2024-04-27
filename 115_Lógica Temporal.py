# Miguel Angel Huerta Castillo     21310236

# Resumen del código:
# Este programa en Python implementa un ejemplo práctico de lógica temporal.
# Utiliza la librería Temporal Logic (templog) para realizar operaciones lógicas temporales.
# El ejemplo simula el cambio de estado de una luz intermitente, donde la luz está encendida
# durante un periodo de tiempo y luego se apaga, repitiendo este ciclo en un bucle infinito.

# Importar la librería Temporal Logic
from templog import *

# Definir las proposiciones atómicas
light_on = Atom("light_on")  # Luz encendida
light_off = Atom("light_off")  # Luz apagada

# Definir la lógica temporal
formula = Eventually(And(light_on, Next(Not(light_on))))  # Eventualmente, la luz está encendida y en el siguiente paso está apagada

# Definir el modelo temporal
model = TemporalModel()

# Definir las transiciones del modelo
model.add_transition({light_on}, {light_off})  # Transición: Luz encendida -> Luz apagada
model.add_transition({light_off}, {light_on})  # Transición: Luz apagada -> Luz encendida

# Verificar si la fórmula se cumple en el modelo temporal
result = model.check(formula)

# Imprimir el resultado de la verificación
if result:
    print("La fórmula se cumple en el modelo temporal.")
else:
    print("La fórmula no se cumple en el modelo temporal.")
