# Miguel Angel Huerta Castillo 21310236
# Programa en Python que implementa la lógica de primer orden usando resolución y Skolem.
# La lógica de primer orden permite razonar sobre objetos individuales y sus relaciones mediante predicados y cuantificadores.
# La resolución es un método de inferencia utilizado para probar la validez de fórmulas lógicas.
# Skolemización es un proceso que elimina los cuantificadores existenciales de una fórmula para convertirla en una forma prenexa.

# Importamos la librería sympy para manipular expresiones lógicas.
from sympy import symbols, satisfiable, Or, And, Not, to_cnf, simplify

# Definimos los símbolos que vamos a utilizar en nuestras fórmulas lógicas.
x, y = symbols('x y')

# Definimos una fórmula en lógica de primer orden, donde "P(x)" indica que x posee una propiedad.
formula = Or(And(Not(x), Not(y)), Or(x, y))

# Convertimos la fórmula a su forma normal conjuntiva (CNF) para aplicar resolución.
cnf_formula = to_cnf(formula)

# Simplificamos la fórmula CNF para mejorar el rendimiento del proceso de resolución.
simplified_formula = simplify(cnf_formula)

# Verificamos si la fórmula es satisfacible (es decir, si existe una asignación de valores que la hace verdadera).
satisfiable_result = satisfiable(simplified_formula)

# Imprimimos el resultado de la verificación de satisfacibilidad.
print("¿La fórmula es satisfacible?", satisfiable_result)
