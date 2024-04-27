# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo práctico de robótica utilizando el concepto de Espacio de Configuración.
# El programa calcula y muestra el espacio de configuración de un robot simple con dos grados de libertad.

import numpy as np  # Importa la librería numpy para cálculos numéricos

# Función para calcular el espacio de configuración
def configuracion(robot):
    # Inicializa el espacio de configuración como una lista vacía
    espacio_configuracion = []

    # Itera sobre los ángulos de articulación del robot
    for q1 in range(-90, 91, 5):  # Ángulo de articulación 1 de -90 a 90 grados con paso de 5 grados
        for q2 in range(-90, 91, 5):  # Ángulo de articulación 2 de -90 a 90 grados con paso de 5 grados
            # Agrega la configuración actual a la lista de espacio de configuración
            espacio_configuracion.append([q1, q2])

    return espacio_configuracion  # Devuelve el espacio de configuración calculado

# Define un robot simple con dos grados de libertad
robot = "2-DOF Robot"

# Calcula el espacio de configuración del robot
espacio_configuracion = configuracion(robot)

# Imprime el espacio de configuración del robot
print("Espacio de Configuración del Robot:", espacio_configuracion)
