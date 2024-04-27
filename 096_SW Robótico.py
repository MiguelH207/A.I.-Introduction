# Miguel Angel Huerta Castillo     21310236
# Este programa es un ejemplo de un controlador simple para un robot móvil utilizando un software robótico.
# Utiliza una biblioteca de control de robot llamada 'robotics' para controlar el movimiento del robot.
 
# Importamos la biblioteca 'robotics' para controlar el robot
import robotics

# Definimos la clase del controlador del robot
class RobotController:
    def __init__(self):
        # Inicializamos la conexión con el robot
        self.robot = robotics.Robot()

    def move_forward(self):
        # Hacemos que el robot avance
        self.robot.move(1, 0)

    def move_backward(self):
        # Hacemos que el robot retroceda
        self.robot.move(-1, 0)

    def turn_left(self):
        # Hacemos que el robot gire a la izquierda
        self.robot.move(0, -1)

    def turn_right(self):
        # Hacemos que el robot gire a la derecha
        self.robot.move(0, 1)

# Creamos una instancia del controlador del robot
controller = RobotController()

# Movemos el robot hacia adelante
controller.move_forward()

# Movemos el robot hacia atrás
controller.move_backward()

# Hacemos que el robot gire a la izquierda
controller.turn_left()

# Hacemos que el robot gire a la derecha
controller.turn_right()
