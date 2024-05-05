# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un solucionador de lógica proposicional que utiliza el método de resolución
# para encontrar la satisfactibilidad de una fórmula en forma normal conjuntiva (FNC).

def clausula_unitaria(clausulas):
    # Función para encontrar una cláusula unitaria en una lista de cláusulas.
    for clausula in clausulas:
        if len(clausula) == 1:
            return clausula[0]
    return None

def complemento(literal):
    # Función para obtener el complemento de un literal.
    if literal[0] == '-':
        return literal[1:]
    else:
        return '-' + literal

def resolver(clausulas, literal):
    # Función para aplicar la regla de resolución a una lista de cláusulas y un literal dado.
    clausulas_resueltas = []
    for clausula in clausulas:
        if literal in clausula:
            clausulas_resueltas.append([x for x in clausula if x != literal])
        elif complemento(literal) in clausula:
            clausulas_resueltas.append([x for x in clausula if x != complemento(literal)])
    return clausulas_resueltas

def resolver_fnc(formula):
    # Función principal para resolver una fórmula en forma normal conjuntiva (FNC).
    clausulas = [c.split(' v ') for c in formula.split(' ^ ')]
    while True:
        unidad = clausula_unitaria(clausulas)
        if unidad is None:
            break
        clausulas = resolver(clausulas, unidad)
    return clausulas

# Ejemplo de uso:
formula = "(p v q) ^ (-p v r) ^ (-q v -r)"
print("Fórmula original en FNC:", formula)
solucion = resolver_fnc(formula)
print("Resultado después de resolver:", solucion)
