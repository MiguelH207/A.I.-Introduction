# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un clasificador inductivo en Python utilizando el algoritmo ID3. 
# El programa utiliza explicaciones e información relevante para clasificar ejemplos en un conjunto de datos.
# El algoritmo ID3 construye un árbol de decisión dividiendo los datos en base a los atributos más informativos.

import numpy as np

class NodoArbol:
    def __init__(self, atributo='', valor=None, hijos=None, resultado=None):
        self.atributo = atributo    # Atributo en el que se divide el nodo
        self.valor = valor          # Valor del atributo
        self.hijos = hijos or {}   # Diccionario de hijos (valor del atributo: nodo hijo)
        self.resultado = resultado  # Resultado si es una hoja (clase)

def entropy(s):
    if len(s) == 0:
        return 0
    counts = np.bincount(s)             # Contar la frecuencia de cada clase en s
    probabilities = counts / len(s)     # Calcular las probabilidades de cada clase
    entropy = -np.sum([p * np.log2(p) if p > 0 else 0 for p in probabilities])  # Calcular la entropía
    return entropy

def information_gain(y, x):  # Calcula la ganancia de información para un atributo dado
    if len(y) == 0 or len(x) == 0:
        return 0
    original_entropy = entropy(y)           # Entropía antes de dividir por atributo x
    values, counts = np.unique(x, return_counts=True)  # Obtener los valores únicos y sus frecuencias
    weighted_entropy = np.sum([(counts[i] / np.sum(counts)) * entropy(y[x == values[i]]) for i in range(len(values))])  # Calcular la entropía ponderada después de dividir por cada valor de x
    information_gain = original_entropy - weighted_entropy   # Ganancia de información
    return information_gain

def id3(X, y, atributos):
    if len(np.unique(y)) <= 1:  # Si todos los ejemplos en y tienen la misma clase
        return NodoArbol(resultado=np.unique(y)[0])  # Devolver un nodo hoja con la clase única
    if len(atributos) == 0:  # Si no quedan atributos para dividir
        return NodoArbol(resultado=np.bincount(y).argmax())  # Devolver un nodo hoja con la clase más común en y

    ganancias = [information_gain(y, X[:, i]) for i in range(len(atributos))]  # Calcular la ganancia de información para cada atributo
    mejor_atributo = np.argmax(ganancias)  # Obtener el índice del atributo con mayor ganancia de información
    nodo = NodoArbol(atributos[mejor_atributo])  # Crear un nodo con el mejor atributo como división

    valores, counts = np.unique(X[:, mejor_atributo], return_counts=True)  # Obtener los valores únicos y sus frecuencias para el mejor atributo
    for valor in valores:
        idx = X[:, mejor_atributo] == valor  # Índices de ejemplos con el valor del mejor atributo
        hijo = id3(X[idx], y[idx], [a for i, a in enumerate(atributos) if i != mejor_atributo])  # Llamar recursivamente a id3 para los ejemplos con el valor del mejor atributo
        nodo.hijos[valor] = hijo  # Agregar el hijo al nodo con su valor correspondiente

    return nodo

def predecir(arbol, muestra):
    if arbol.resultado is not None:  # Si es un nodo hoja
        return arbol.resultado  # Devolver la clase del nodo hoja
    valor = muestra[arbol.atributo]  # Valor del atributo del nodo
    if valor not in arbol.hijos:  # Si no hay un hijo para ese valor
        return np.random.choice(list(arbol.hijos.values())).resultado  # Devolver una clase aleatoria de los hijos
    return predecir(arbol.hijos[valor], muestra)  # Llamar recursivamente a predecir para el hijo correspondiente

# Ejemplo de uso del algoritmo ID3

# Datos de entrenamiento
X = np.array([
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [2, 1, 0, 0],
    [2, 2, 1, 0],
    [2, 2, 1, 1],
    [1, 2, 1, 1],
    [0, 1, 0, 0],
    [0, 2, 1, 0],
    [2, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 0],
    [2, 1, 0, 1]
])

y = np.array([0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0])

atributos = ['outlook', 'temperature', 'humidity', 'wind']

arbol = id3(X, y, atributos)  # Entrenar el árbol de decisión

# Ejemplo de predicción
muestra = {'outlook': 0, 'temperature': 0, 'humidity': 0, 'wind': 1}
print("Resultado de la predicción:", predecir(arbol, muestra))  # Realizar una predicción usando el árbol entrenado
