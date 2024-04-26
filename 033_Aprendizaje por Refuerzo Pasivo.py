import numpy as np  # Importamos la librería numpy para operaciones numéricas eficientes

# Definimos los posibles movimientos en el juego: piedra, papel, tijeras (0, 1, 2)
movimientos = ['piedra', 'papel', 'tijeras']

# Definimos la matriz de recompensas
# -1 indica que el agente perdió, 0 indica empate y 1 indica que el agente ganó
recompensas = np.array([[0, -1, 1],  # Piedra
                        [1, 0, -1],  # Papel
                        [-1, 1, 0]])  # Tijeras

# Definimos la matriz de políticas inicialmente uniforme
politica = np.ones((3, 3)) / 3  # Inicialmente, cada acción tiene la misma probabilidad

# Simulamos 1000 juegos para que el agente aprenda
for _ in range(1000):
    # El oponente elige un movimiento al azar
    movimiento_oponente = np.random.randint(0, 3)
    # El agente elige un movimiento basado en la política actual
    movimiento_agente = np.random.choice([0, 1, 2], p=politica[movimiento_oponente])
    
    # Actualizamos la política según el resultado del juego
    politica[movimiento_oponente, movimiento_agente] += 0.1 * recompensas[movimiento_oponente, movimiento_agente]
    # Normalizamos la política para que las probabilidades sumen 1
    politica[movimiento_oponente] /= np.sum(politica[movimiento_oponente])

# Imprimimos la política aprendida
print("Política aprendida:")
for i, movimiento in enumerate(movimientos):
    print(f"{movimiento}: {politica[i]}")
