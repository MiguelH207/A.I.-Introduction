# Miguel Angel Huerta Castillo     21310236

import numpy as np  # Importa la librería NumPy para manipulación de datos numéricos

# Función que simula el proceso de recuperación de datos basado en la probabilidad de ocurrencia
def recuperacion_probabilistica(documentos, consulta):
    # Calcula la frecuencia de términos en los documentos
    frecuencia_documentos = np.sum(documentos, axis=1)
    
    # Calcula la probabilidad de ocurrencia de los términos en los documentos
    probabilidad_documentos = frecuencia_documentos / np.sum(frecuencia_documentos)
    
    # Calcula la probabilidad de ocurrencia de los términos en la consulta
    probabilidad_consulta = np.sum(consulta * documentos, axis=1) / np.sum(consulta)
    
    # Calcula la probabilidad de recuperación de cada documento
    probabilidad_recuperacion = probabilidad_consulta * probabilidad_documentos
    
    # Ordena los documentos por su probabilidad de recuperación en orden descendente
    documentos_ordenados = np.argsort(probabilidad_recuperacion)[::-1]
    
    return documentos_ordenados

# Ejemplo de uso
if __name__ == "__main__":
    # Matriz de documentos (cada fila representa un documento y cada columna representa un término)
    documentos = np.array([[1, 1, 0, 1],
                           [0, 1, 1, 0],
                           [1, 0, 0, 1]])
    
    # Consulta del usuario (vector de términos)
    consulta = np.array([1, 0, 1, 0])
    
    # Llama a la función de recuperación probabilística y obtiene el orden de los documentos
    orden_documentos = recuperacion_probabilistica(documentos, consulta)
    
    # Imprime el orden de los documentos según su probabilidad de recuperación
    print("Orden de los documentos según su probabilidad de recuperación:", orden_documentos)
