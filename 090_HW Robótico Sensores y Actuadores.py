# Miguel Angel Huerta Castillo     21310236
# Este programa muestra un ejemplo práctico de un sistema robótico simple utilizando sensores y actuadores.
# El programa simula un robot que sigue una línea negra sobre un fondo blanco utilizando un sensor de línea infrarroja.

# Importamos la librería gpiozero para controlar los componentes hardware
from gpiozero import Robot, LineSensor
from signal import pause

# Definimos los pines GPIO conectados al motor izquierdo y derecho del robot
robot = Robot(left=(17, 18), right=(22, 23))

# Creamos un sensor de línea que detecta el color negro (que es lo que queremos seguir)
line_sensor = LineSensor(4)

# Definimos una función para mover el robot hacia adelante
def on_line():
    robot.forward()

# Definimos una función para detener el robot cuando no detecta la línea
def off_line():
    robot.stop()

# Asignamos las funciones a los eventos del sensor de línea
line_sensor.when_line = on_line
line_sensor.when_no_line = off_line

# Mantenemos el programa en ejecución
pause()
