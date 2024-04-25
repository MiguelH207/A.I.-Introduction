# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo de razonamiento probabilístico utilizando el método de Eliminación de Variables.

# Importamos la librería numpy para operaciones numéricas
import numpy as np

# Definimos las probabilidades condicionales P(B|A), P(C|A), P(D|B,C) y P(E|C)
P_B_given_A = np.array([[0.6, 0.4], [0.3, 0.7]])  # P(B|A)
P_C_given_A = np.array([[0.8, 0.2], [0.1, 0.9]])  # P(C|A)
P_D_given_BC = np.array([[[0.9, 0.1], [0.2, 0.8]], [[0.4, 0.6], [0.01, 0.99]]])  # P(D|B,C)
P_E_given_C = np.array([[0.7, 0.3], [0.5, 0.5]])  # P(E|C)

# Eliminación de la variable B
def eliminate_B(P_B_given_A, P_C_given_A, P_D_given_BC):
    # Calculamos P(BC) sumando sobre B: P(BC) = sum_B(P(B|A) * P(C|A))
    P_BC = np.dot(P_B_given_A, P_C_given_A)
    
    # Calculamos P(D|BC) sumando sobre B: P(D|BC) = sum_B(P(D|B,C) * P(B|A) * P(C|A))
    P_D_given_BC_new = np.dot(np.expand_dims(P_B_given_A, axis=2), np.expand_dims(P_C_given_A, axis=1)) * P_D_given_BC
    P_D_given_BC_new = np.sum(P_D_given_BC_new, axis=0)
    
    # Devolvemos P(BC) y P(D|BC)
    return P_BC, P_D_given_BC_new

# Eliminación de la variable C
def eliminate_C(P_BC, P_D_given_BC, P_E_given_C):
    # Calculamos P(BD) sumando sobre C: P(BD) = sum_C(P(BC) * P(D|BC))
    P_BD = np.dot(P_BC, P_D_given_BC)
    
    # Calculamos P(E|BD) sumando sobre C: P(E|BD) = sum_C(P(E|C) * P(C|A) * P(BC))
    P_E_given_C_new = np.dot(np.expand_dims(P_C_given_A, axis=2), np.expand_dims(P_BC, axis=1)) * P_E_given_C
    P_E_given_C_new = np.sum(P_E_given_C_new, axis=0)
    
    # Devolvemos P(BD) y P(E|BD)
    return P_BD, P_E_given_C_new

# Llamamos a las funciones de eliminación de variables
P_BC, P_D_given_BC_new = eliminate_B(P_B_given_A, P_C_given_A, P_D_given_BC)
P_BD, P_E_given_C_new = eliminate_C(P_BC, P_D_given_BC_new, P_E_given_C)

# Imprimimos los resultados
print("P(BD):\n", P_BD)
print("P(E|BD):\n", P_E_given_C_new)

# Descripción del método de Eliminación de Variables
"""
El método de Eliminación de Variables es una técnica utilizada en razonamiento probabilístico para calcular
distribuciones de probabilidad condicional de variables de interés, eliminando variables intermedias.
Funciona mediante la multiplicación de probabilidades condicionales y sumas sobre las variables a eliminar.
Sirve para simplificar el cálculo de probabilidades en redes Bayesianas y otros modelos probabilísticos,
permitiendo obtener información sobre variables de interés a partir de un conjunto de datos y relaciones
probabilísticas conocidas. En resumen, este método permite realizar inferencias probabilísticas eficientes
en modelos con múltiples variables.
"""
