# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo básico de Aprendizaje Inductivo utilizando tipos de razonamiento y aprendizaje.
# El programa crea un clasificador simple para determinar si una fruta es una manzana o una naranja basándose en dos características: color y textura.

import numpy as np  # Importamos la librería numpy

classificador = None  # Se inicializa el clasificador como nulo

# Definición de la función para entrenar el clasificador
def entrenar_clasificador(datos_entrenamiento):
    # Convertimos los datos de entrenamiento en una matriz NumPy
    datos_entrenamiento = np.array(datos_entrenamiento)
    # Selecciona las características (color y textura) y las etiquetas (manzana o naranja) de los datos de entrenamiento
    caracteristicas = datos_entrenamiento[:, :-1]  
    etiquetas = datos_entrenamiento[:, -1]  
    
    # Creamos un diccionario vacío para almacenar las clases de las características
    clases = {}  
    
    # Recorre cada etiqueta en las etiquetas
    for i in range(len(etiquetas)):  
        # Si la etiqueta no está en el diccionario de clases, se agrega
        if etiquetas[i] not in clases:  
            clases[etiquetas[i]] = []  
        # Se agregan las características correspondientes a cada clase
        clases[etiquetas[i]].append(caracteristicas[i])  
    
    # Se calcula el promedio de cada característica para cada clase y se almacena en un nuevo diccionario
    medias = {clase: np.mean(valores, axis=0) for clase, valores in clases.items()}  
    
    return medias  # Se devuelve el diccionario con las medias de las características para cada clase

# Definición de la función para predecir la clase de una nueva instancia
def predecir(instancia, medias):
    # Calcula la distancia euclidiana entre la instancia y las medias de cada clase
    distancias = {clase: np.sqrt(np.sum((instancia - media) ** 2)) for clase, media in medias.items()}  
    
    # Devuelve la clase con la distancia euclidiana más corta
    return min(distancias, key=distancias.get)  

# Definición de los datos de entrenamiento (color [0: rojo, 1: naranja], textura [0: rugoso, 1: suave], etiqueta [0: manzana, 1: naranja])
datos_entrenamiento = [
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 1],
    [0, 1, 1]
]

# Entrenar el clasificador con los datos de entrenamiento
classificador = entrenar_clasificador(datos_entrenamiento)  

# Nueva instancia a predecir (color: rojo, textura: rugoso)
nueva_instancia = [0, 0]  

# Realizar la predicción de la clase de la nueva instancia
prediccion = predecir(nueva_instancia, classificador)  

# Imprimir la predicción
print("La fruta es una:", "manzana" if prediccion == 0 else "naranja")
