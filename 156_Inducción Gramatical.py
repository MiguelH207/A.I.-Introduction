# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo de Tratamiento Lógico del Lenguaje utilizando Inducción Gramatical.
# Utiliza una pequeña gramática para reconocer y procesar frases simples en español.

# Definición de la gramática:
# S -> NP VP
# NP -> Det N
# VP -> V NP
# Det -> 'el' | 'un'
# N -> 'gato' | 'perro'
# V -> 'persigue' | 'come'

# Función para analizar una oración utilizando la gramática definida.
def analizar_oracion(oracion):
    palabras = oracion.split()  # Divide la oración en una lista de palabras
    # Verifica si la estructura de la oración es válida según la gramática
    if len(palabras) == 4 and palabras[0] in ['el', 'un'] and palabras[1] in ['gato', 'perro'] and palabras[2] in ['persigue', 'come']:
        return True  # Si la estructura es válida, devuelve True
    else:
        return False  # Si la estructura no es válida, devuelve False

# Función principal
def main():
    # Solicita al usuario que ingrese una oración
    oracion = input("Ingrese una oración en español (por ejemplo, 'el gato persigue un ratón'): ")
    # Llama a la función para analizar la oración y muestra el resultado
    if analizar_oracion(oracion):
        print("La oración es válida según la gramática definida.")
    else:
        print("La oración no es válida según la gramática definida.")

# Llama a la función principal
if __name__ == "__main__":
    main()
