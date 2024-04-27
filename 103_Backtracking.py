# Miguel Angel Huerta Castillo 21310236
# Programa de lógica proposicional usando Backtracking.
# El programa implementa un solucionador de problemas de satisfacción de restricciones utilizando el algoritmo de Backtracking.
# El usuario debe proporcionar una fórmula en lógica proposicional en forma de lista de cláusulas, donde cada cláusula es una lista de literales.
# El programa intentará encontrar una asignación de verdad que satisfaga todas las cláusulas, utilizando Backtracking.

def backtracking_satisfiable(formula, assignment):
    """
    Función que determina si una fórmula en lógica proposicional es satisfacible utilizando Backtracking.

    Args:
        formula (list): Lista de cláusulas, donde cada cláusula es una lista de literales.
        assignment (dict): Asignación de verdad actual.

    Returns:
        bool: True si la fórmula es satisfacible, False de lo contrario.
    """
    # Verificar si todas las cláusulas han sido satisfechas
    if all(len(clause) == 0 for clause in formula):
        return True  # Si es así, la fórmula es satisfacible

    # Seleccionar un literal no asignado
    for literal in formula[0]:
        if literal not in assignment and -literal not in assignment:
            break

    # Intentar asignar verdadero al literal
    assignment[literal] = True
    new_formula = [clause for clause in formula if literal not in clause]

    # Llamar recursivamente con la asignación actualizada
    if backtracking_satisfiable(new_formula, assignment):
        return True

    # Si no se satisface con el literal verdadero, intentar asignar falso al literal
    del assignment[literal]
    assignment[-literal] = False
    new_formula = [clause for clause in formula if -literal not in clause]

    # Llamar recursivamente con la asignación actualizada
    if backtracking_satisfiable(new_formula, assignment):
        return True

    # Si ninguna asignación satisface la fórmula, devolver False
    return False

# Ejemplo de uso
if __name__ == "__main__":
    # Fórmula en forma de lista de cláusulas
    # Cada cláusula es una lista de literales
    formula = [[1, 2, -3], [-1, 3], [-2, 3], [-3]]

    # Asignación inicial vacía
    assignment = {}

    # Verificar si la fórmula es satisfacible
    if backtracking_satisfiable(formula, assignment):
        print("La fórmula es satisfacible.")
    else:
        print("La fórmula no es satisfacible.")
