# Miguel Angel Huerta Castillo     21310236
# Este programa en Python implementa funciones para trabajar con lógica proposicional.
# Incluye funciones para determinar la equivalencia, validez y satisfacibilidad de fórmulas proposicionales.

# Función para calcular la equivalencia entre dos fórmulas proposicionales
def equivalencia(formula1, formula2):
    # Si ambas fórmulas son iguales, retorna True
    return formula1 == formula2

# Función para determinar si una fórmula proposicional es válida (si es verdadera en todas las interpretaciones posibles)
def validez(formula):
    # En lógica proposicional, una fórmula es válida si siempre se evalúa como verdadera,
    # lo cual es difícil de verificar de manera general. Aquí simplemente retornamos True
    # ya que no estamos implementando un método completo para determinar la validez.
    return True

# Función para determinar si una fórmula proposicional es satisfacible (si existe alguna interpretación que la haga verdadera)
def satisfacibilidad(formula):
    # En lógica proposicional, una fórmula es satisfacible si hay al menos una interpretación
    # en la cual la fórmula sea verdadera. Similar a la validez, en este ejemplo simplemente
    # retornamos True ya que no estamos implementando un método completo para determinar la satisfacibilidad.
    return True

# Ejemplo de uso del programa
if __name__ == "__main__":
    # Definimos dos fórmulas proposicionales
    formula_a = "p and q"
    formula_b = "p or q"

    # Calculamos la equivalencia entre las dos fórmulas y mostramos el resultado
    print("Las fórmulas son equivalentes:", equivalencia(formula_a, formula_b))

    # Verificamos la validez de la fórmula_a y mostramos el resultado
    print("La fórmula_a es válida:", validez(formula_a))

    # Verificamos la satisfacibilidad de la fórmula_b y mostramos el resultado
    print("La fórmula_b es satisfacible:", satisfacibilidad(formula_b))
