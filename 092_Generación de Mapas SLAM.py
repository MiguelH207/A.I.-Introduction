# Miguel Angel Huerta Castillo 21310236
# Este programa en Python implementa un ejemplo práctico de SLAM (Simultaneous Localization and Mapping),
# utilizando la librería Robotics Toolbox para la generación de mapas.

import numpy as np  # Importa la librería numpy para operaciones matemáticas
from matplotlib import pyplot as plt  # Importa pyplot de matplotlib para graficar
from roboticstoolbox import ERobotics  # Importa la clase ERobotics de la librería Robotics Toolbox

# Definición de parámetros del entorno
n_landmarks = 5  # Número de puntos de referencia en el mapa
size = 10  # Tamaño del entorno (cuadrado)

# Creación de un entorno 2D
env = ERobotics('map', n_landmarks=n_landmarks, xlim=[-size, size], ylim=[-size, size])

# Inicialización del robot en una posición aleatoria
env.add_robot('Simple')

# Ejecución del SLAM para actualizar la posición del robot y el mapa
for t in range(50):  # 50 iteraciones de movimiento
    # Movimiento aleatorio del robot
    v = 0.1 * np.random.randn()  # Velocidad lineal
    w = 0.1 * np.random.randn()  # Velocidad angular
    env.step(0.1, [v, w])  # Actualiza la posición del robot

    # Medición de distancias a los puntos de referencia (simulando sensores)
    r = env.sense()

    # Actualización del mapa y estimación de la posición del robot (SLAM)
    env.update_map(r)

# Graficación del mapa generado
env.plot()
plt.show()
