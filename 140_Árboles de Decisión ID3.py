# Miguel Angel Huerta Castillo     21310236
# Este programa implementa el algoritmo de Aprendizaje Inductivo utilizando Árboles de Decisión con el método ID3.
# El programa incluye un ejemplo práctico para clasificar el clima como "soleado", "nublado" o "lluvioso" basado en las características de "temperatura", "humedad" y "viento".

import numpy as np

class NodoDecision:
    def __init__(self, caracteristica=None, valor=None, true_branch=None, false_branch=None, resultado=None):
        self.caracteristica = caracteristica  # Guarda la característica en la cual se divide el nodo
        self.valor = valor  # Guarda el valor en el que se divide la característica
        self.true_branch = true_branch  # Guarda la rama verdadera del árbol
        self.false_branch = false_branch  # Guarda la rama falsa del árbol
        self.resultado = resultado  # Guarda el resultado de clasificación si es una hoja

def contar_clases(y):
    clases, counts = np.unique(y, return_counts=True)  # Cuenta las ocurrencias de cada clase en el conjunto de datos
    return dict(zip(clases, counts))  # Devuelve un diccionario con las clases y sus conteos

def entropia(y):
    clases, counts = np.unique(y, return_counts=True)  # Obtiene las clases y sus conteos
    probabilidad = counts / len(y)  # Calcula las probabilidades de cada clase
    return -np.sum(probabilidad * np.log2(probabilidad))  # Calcula la entropía del conjunto de datos

def ganancia_informacion(X, y, caracteristica, valor):
    ix = X[:, caracteristica] == valor  # Filtra las instancias con el valor de la característica especificada
    y_subset = y[ix]  # Obtiene las etiquetas correspondientes a esas instancias
    entropia_total = entropia(y)  # Calcula la entropía total antes de la división
    entropia_subset = entropia(y_subset)  # Calcula la entropía después de la división
    prop_subset = len(y_subset) / len(y)  # Calcula la proporción de instancias en el subset
    prop_complemento = 1 - prop_subset  # Calcula la proporción de instancias en el complemento del subset
    ganancia = entropia_total - (prop_subset * entropia_subset + prop_complemento * entropia(y[~ix]))  # Calcula la ganancia de información
    return ganancia  # Devuelve la ganancia de información

def mejor_division(X, y):
    mejor_ganancia = 0
    mejor_caracteristica = None
    mejor_valor = None
    for caracteristica in range(X.shape[1]):  # Itera sobre todas las características
        valores = np.unique(X[:, caracteristica])  # Obtiene los valores únicos para la característica actual
        for valor in valores:  # Itera sobre los valores de la característica actual
            ganancia = ganancia_informacion(X, y, caracteristica, valor)  # Calcula la ganancia de información para esta división
            if ganancia > mejor_ganancia:  # Si la ganancia es mayor que la mejor ganancia hasta ahora
                mejor_ganancia = ganancia  # Actualiza la mejor ganancia
                mejor_caracteristica = caracteristica  # Actualiza la mejor característica
                mejor_valor = valor  # Actualiza el mejor valor
    return mejor_caracteristica, mejor_valor  # Devuelve la mejor característica y su valor de división

def construir_arbol(X, y):
    if len(np.unique(y)) == 1:  # Si todas las instancias tienen la misma clase
        return NodoDecision(resultado=y[0])  # Devuelve un nodo hoja con esa clase como resultado
    mejor_caracteristica, mejor_valor = mejor_division(X, y)  # Encuentra la mejor división para el conjunto de datos
    if mejor_caracteristica is None:  # Si no se puede hacer más división
        return NodoDecision(resultado=np.argmax(contar_clases(y)))  # Devuelve un nodo hoja con la clase más común
    ix = X[:, mejor_caracteristica] == mejor_valor  # Filtra las instancias para la rama verdadera y falsa
    true_branch = construir_arbol(X[ix], y[ix])  # Construye la rama verdadera recursivamente
    false_branch = construir_arbol(X[~ix], y[~ix])  # Construye la rama falsa recursivamente
    return NodoDecision(caracteristica=mejor_caracteristica, valor=mejor_valor, true_branch=true_branch, false_branch=false_branch)  # Devuelve el nodo de decisión

def predecir(arbol, instancia):
    if arbol.resultado is not None:  # Si el nodo es una hoja
        return arbol.resultado  # Devuelve la clase de la hoja
    if instancia[arbol.caracteristica] == arbol.valor:  # Si la instancia coincide con el valor de la característica en el nodo
        return predecir(arbol.true_branch, instancia)  # Predice recursivamente en la rama verdadera
    else:
        return predecir(arbol.false_branch, instancia)  # Predice recursivamente en la rama falsa

# Datos de entrenamiento
X_train = np.array([
    [30, 85, 0],  # soleado
    [28, 90, 1],  # nublado
    [22, 95, 1],  # lluvioso
    [25, 70, 1],  # lluvioso
    [20, 80, 0],  # soleado
    [18, 75, 1],  # lluvioso
    [15, 70, 0],  # soleado
    [12, 80, 1],  # lluvioso
    [10, 75, 0],  # soleado
    [8, 85, 0]    # soleado
])

y_train = np.array(['soleado', 'nublado', 'lluvioso', 'lluvioso', 'soleado', 'lluvioso', 'soleado', 'lluvioso', 'soleado', 'soleado'])

# Construir el árbol de decisión
arbol_decision = construir_arbol(X_train, y_train)

# Datos de prueba
X_test = np.array([
    [25, 80, 0],  # soleado
    [22, 85, 1],  # nublado
    [20, 90, 1],  # lluvioso
    [18, 70, 0],  # soleado
    [15, 75, 1]   # lluvioso
])

# Predecir el clima para los datos de prueba
for instancia in X_test:
    prediccion = predecir(arbol_decision, instancia)
    print("Predicción:", prediccion)

