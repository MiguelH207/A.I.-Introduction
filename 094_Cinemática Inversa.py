# Miguel Angel Huerta Castillo     21310236
# Este programa en Python implementa un ejemplo de Cinemática Inversa en robótica.
# La cinemática inversa se utiliza para determinar las posiciones y orientaciones de los actuadores de un robot con base en la posición y orientación deseada del extremo final del robot.

import numpy as np  # Importamos la librería numpy para realizar operaciones numéricas eficientes

# Definimos la función de cinemática inversa
def inverse_kinematics(x, y, z):
    L1 = 5  # Longitud del primer eslabón del brazo
    L2 = 4  # Longitud del segundo eslabón del brazo
    
    # Calculamos el ángulo del primer eslabón con respecto a la horizontal
    theta1 = np.arctan2(y, x)
    
    # Calculamos la distancia horizontal desde el origen al extremo del primer eslabón
    d = np.sqrt(x**2 + y**2)
    
    # Calculamos la distancia vertical desde el origen al extremo del segundo eslabón
    D = np.sqrt(z**2 + (d - L1)**2)
    
    # Calculamos el ángulo entre el segundo eslabón y la horizontal
    alpha = np.arccos((L2**2 - L1**2 - D**2) / (-2 * L1 * D))
    
    # Calculamos el ángulo del segundo eslabón con respecto a la vertical
    theta2 = np.pi - alpha - np.arctan2(z, d - L1)
    
    return np.degrees(theta1), np.degrees(theta2)  # Devolvemos los ángulos en grados

# Ejemplo de uso de la cinemática inversa
if __name__ == "__main__":
    x_desired = 3  # Posición x deseada del extremo final del robot
    y_desired = 4  # Posición y deseada del extremo final del robot
    z_desired = 5  # Posición z deseada del extremo final del robot
    
    # Calculamos los ángulos necesarios para alcanzar la posición deseada
    theta1, theta2 = inverse_kinematics(x_desired, y_desired, z_desired)
    
    # Imprimimos los ángulos resultantes
    print("Theta1 (en grados):", theta1)
    print("Theta2 (en grados):", theta2)
