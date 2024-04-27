# Miguel Angel Huerta Castillo     21310236
# Este programa simula el movimiento de un robot con incertidumbre en un ambiente de dos dimensiones.

import numpy as np  # Importa la librería numpy para cálculos numéricos

# Clase que define un robot
class Robot:
    def __init__(self, x, y):
        self.x = x  # Posición en el eje x
        self.y = y  # Posición en el eje y

    # Método para mover el robot con incertidumbre
    def move(self, dx, dy):
        self.x += dx + np.random.normal(0, 0.1)  # Movimiento en el eje x con incertidumbre gaussiana
        self.y += dy + np.random.normal(0, 0.1)  # Movimiento en el eje y con incertidumbre gaussiana

# Función principal
def main():
    robot = Robot(0, 0)  # Crea un robot en la posición (0, 0)

    # Realiza 10 movimientos del robot
    for _ in range(10):
        dx = np.random.uniform(-1, 1)  # Genera una distancia aleatoria en el eje x
        dy = np.random.uniform(-1, 1)  # Genera una distancia aleatoria en el eje y
        robot.move(dx, dy)  # Mueve el robot con las distancias aleatorias y la incertidumbre

        print(f"Posición actual: ({robot.x}, {robot.y})")  # Imprime la posición actual del robot

if __name__ == "__main__":
    main()  # Llama a la función principal si el programa se ejecuta directamente
