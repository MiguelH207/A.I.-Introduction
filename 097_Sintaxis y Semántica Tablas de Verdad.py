# Miguel Angel Huerta Castillo     21310236
# Este programa en Python implementa la lógica proposicional utilizando sintaxis y semántica de tablas de verdad.
# Primero define las funciones para generar todas las combinaciones posibles de valores de verdad para un conjunto dado de variables proposicionales.
# Luego define una función para evaluar una expresión proposicional dada utilizando las combinaciones de valores de verdad generadas.
# Finalmente, muestra la tabla de verdad de la expresión proposicional dada por el usuario.

from itertools import product  # Importa la función product del módulo itertools

def generate_truth_values(variables):
    """Genera todas las combinaciones posibles de valores de verdad para un conjunto dado de variables proposicionales."""
    return list(product([False, True], repeat=len(variables)))  # Genera todas las combinaciones de valores de verdad para las variables

def evaluate_expression(expression, truth_values):
    """Evalúa una expresión proposicional dada utilizando las combinaciones de valores de verdad generadas."""
    values_dict = dict(zip(variables, truth_values))  # Crea un diccionario que mapea variables a valores de verdad
    return eval(expression, values_dict)  # Evalúa la expresión utilizando los valores de verdad dados en el diccionario

if __name__ == "__main__":
    expression = input("Ingrese una expresión proposicional en Python (usando 'and', 'or', 'not', '(', ')', etc.): ")  # Solicita al usuario ingresar una expresión proposicional
    variables = set(filter(str.isalpha, expression))  # Obtiene las variables presentes en la expresión
    truth_values = generate_truth_values(variables)  # Genera todas las combinaciones de valores de verdad para las variables
    print("Tabla de verdad:")  # Imprime un encabezado para la tabla de verdad
    print("".join(variables), "|", expression)  # Imprime la primera fila de la tabla de verdad (variables y expresión)
    print("-" * (len(variables) + len(expression) + 3))  # Imprime una línea de separación entre el encabezado y los valores
    for values in truth_values:  # Itera sobre cada combinación de valores de verdad
        values_str = "".join(map(str, values))  # Convierte los valores de verdad a cadenas y los concatena
        result = evaluate_expression(expression, values)  # Evalúa la expresión con la combinación actual de valores de verdad
        print(values_str, "|", int(result))  # Imprime la fila de la tabla de verdad correspondiente a la combinación de valores y el resultado de la expresión
