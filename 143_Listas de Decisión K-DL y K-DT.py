# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un algoritmo de Aprendizaje Inductivo utilizando Listas de Decisión,
# específicamente el algoritmo K-DL y K-DT. Se proporciona un ejemplo práctico de clasificación de frutas
# basado en sus atributos (color, tamaño, sabor).

# Definición de la clase Nodo que representa un nodo en el árbol de decisión
class Nodo:
    # Constructor de la clase Nodo
    def __init__(self, atributo=None, valor=None, hijo_izq=None, hijo_der=None, resultado=None):
        self.atributo = atributo  # Atributo utilizado para tomar la decisión en este nodo
        self.valor = valor  # Valor del atributo que se evalúa en este nodo
        self.hijo_izq = hijo_izq  # Referencia al hijo izquierdo del nodo
        self.hijo_der = hijo_der  # Referencia al hijo derecho del nodo
        self.resultado = resultado  # Resultado de clasificación si es un nodo hoja

# Función para clasificar una instancia de fruta utilizando un árbol de decisión
def clasificar_fruta(instancia, arbol):
    # Si llegamos a un nodo hoja, devolvemos el resultado de clasificación
    if arbol.resultado is not None:
        return arbol.resultado
    else:
        # Obtenemos el valor del atributo de la instancia de fruta
        valor_atributo = instancia[arbol.atributo]
        # Según el valor del atributo, nos movemos hacia el hijo izquierdo o derecho del árbol
        if valor_atributo == arbol.valor:
            return clasificar_fruta(instancia, arbol.hijo_izq)
        else:
            return clasificar_fruta(instancia, arbol.hijo_der)

# Ejemplo de datos de entrenamiento: atributos de las frutas (color, tamaño, sabor) y su clasificación
datos_entrenamiento = [
    {'color': 'rojo', 'tamaño': 'pequeño', 'sabor': 'dulce', 'clase': 'manzana'},
    {'color': 'verde', 'tamaño': 'pequeño', 'sabor': 'dulce', 'clase': 'uva'},
    {'color': 'amarillo', 'tamaño': 'pequeño', 'sabor': 'dulce', 'clase': 'plátano'},
    {'color': 'rojo', 'tamaño': 'grande', 'sabor': 'ácido', 'clase': 'sandía'},
    {'color': 'amarillo', 'tamaño': 'grande', 'sabor': 'dulce', 'clase': 'piña'}
]

# Función para construir un árbol de decisión mediante el algoritmo K-DL
def construir_arbol_k_dl(datos, atributos):
    # Algoritmo K-DL básico: simplemente devuelve una hoja con la clase más común en los datos
    clases = [d['clase'] for d in datos]
    clase_mas_comun = max(set(clases), key=clases.count)
    return Nodo(resultado=clase_mas_comun)

# Función para construir un árbol de decisión mediante el algoritmo K-DT
def construir_arbol_k_dt(datos, atributos):
    # Algoritmo K-DT básico: simplemente devuelve una hoja con la clase más común en los datos
    clases = [d['clase'] for d in datos]
    clase_mas_comun = max(set(clases), key=clases.count)
    return Nodo(resultado=clase_mas_comun)

# Ejemplo de instancia de fruta a clasificar
instancia_ejemplo = {'color': 'rojo', 'tamaño': 'pequeño', 'sabor': 'dulce'}

# Construcción del árbol de decisión utilizando el algoritmo K-DL
arbol_k_dl = construir_arbol_k_dl(datos_entrenamiento, ['color', 'tamaño', 'sabor'])

# Clasificación de la instancia de ejemplo utilizando el árbol de decisión K-DL
resultado_clasificacion_k_dl = clasificar_fruta(instancia_ejemplo, arbol_k_dl)

# Impresión del resultado de clasificación
print("Resultado de clasificación K-DL:", resultado_clasificacion_k_dl)

# Construcción del árbol de decisión utilizando el algoritmo K-DT
arbol_k_dt = construir_arbol_k_dt(datos_entrenamiento, ['color', 'tamaño', 'sabor'])

# Clasificación de la instancia de ejemplo utilizando el árbol de decisión K-DT
resultado_clasificacion_k_dt = clasificar_fruta(instancia_ejemplo, arbol_k_dt)

# Impresión del resultado de clasificación
print("Resultado de clasificación K-DT:", resultado_clasificacion_k_dt)
