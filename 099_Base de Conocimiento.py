# Miguel Angel Huerta Castillo     21310236
# Este programa en Python implementa un sistema de lógica proposicional utilizando una base de conocimiento.
# La lógica proposicional es un sistema formal que estudia las proposiciones y las conectivas que pueden usarse para combinarlas.
# La base de conocimiento en este caso se representa como un diccionario donde las claves son las variables proposicionales y los valores son los valores de verdad correspondientes.

# Definición de la base de conocimiento
base_conocimiento = {
    'p': True,  # Se define la variable proposicional 'p' con valor verdadero
    'q': False,  # Se define la variable proposicional 'q' con valor falso
    'r': True    # Se define la variable proposicional 'r' con valor verdadero
}

# Función para evaluar una expresión proposicional dada una base de conocimiento
def evaluar_expresion(expresion, base):
    # Se sustituyen las variables en la expresión por sus valores de la base de conocimiento
    for variable, valor in base.items():
        expresion = expresion.replace(variable, str(valor))
    # Se evalúa la expresión utilizando la función eval de Python
    resultado = eval(expresion)
    return resultado

# Ejemplo de uso
expresion_ejemplo = "(p and q) or (not r)"  # Se define una expresión proposicional
resultado_ejemplo = evaluar_expresion(expresion_ejemplo, base_conocimiento)  # Se evalúa la expresión
print("El resultado de la expresión es:", resultado_ejemplo)  # Se imprime el resultado
