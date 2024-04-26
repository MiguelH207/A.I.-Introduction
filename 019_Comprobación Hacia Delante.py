# Miguel Angel Huerta Castillo     21310236
# Programa de Satisfacción de Restricciones usando Comprobación Hacia Delante (Forward Checking)
# Este programa implementa el algoritmo de satisfacción de restricciones utilizando la técnica de Comprobación Hacia Delante.
# El objetivo es encontrar una asignación de valores que cumpla con todas las restricciones definidas en un problema de restricciones.
# El algoritmo avanza de manera recursiva, asignando valores a variables y realizando comprobaciones para asegurarse de que no haya conflictos con las restricciones.

def forward_checking(variables, domains, constraints, assignment):
    if len(assignment) == len(variables):  # Si la asignación está completa, se retorna verdadero
        return True
    
    var = select_unassigned_variable(variables, assignment)  # Selecciona una variable no asignada
    
    for value in order_domain_values(var, domains, assignment):  # Ordena los valores de dominio de la variable
        if is_consistent(var, value, assignment, constraints):  # Verifica si la asignación es consistente con las restricciones
            assignment[var] = value  # Asigna el valor a la variable
            if forward_checking(variables, domains, constraints, assignment):  # Llamada recursiva
                return True
            assignment.pop(var)  # Retrocede si no se encuentra una solución
    return False

def select_unassigned_variable(variables, assignment):
    for var in variables:  # Itera sobre las variables
        if var not in assignment:  # Si la variable no está asignada, se retorna
            return var

def order_domain_values(var, domains, assignment):
    return domains[var]  # Retorna los valores de dominio en el orden original

def is_consistent(var, value, assignment, constraints):
    for constraint in constraints[var]:  # Itera sobre las restricciones de la variable
        if constraint[0] in assignment and not constraint[1](value, assignment[constraint[0]]):  # Verifica la consistencia
            return False
    return True

# Ejemplo de uso:

# Definición de variables
variables = ['A', 'B', 'C']

# Definición de dominios para cada variable
domains = {
    'A': [1, 2, 3],
    'B': [1, 2],
    'C': [2, 3]
}

# Definición de restricciones binarias entre variables
constraints = {
    'A': [('B', lambda a, b: a != b), ('C', lambda a, c: a != c)],
    'B': [('C', lambda b, c: b != c)],
    'C': [('A', lambda c, a: c != a), ('B', lambda c, b: c != b)]  # Se agrega la restricción para la variable 'C'
}


# Asignación inicial vacía
assignment = {}

# Llamada al algoritmo de comprobación hacia delante
result = forward_checking(variables, domains, constraints, assignment)

# Imprimir resultado
if result:
    print("Se encontró una asignación válida:", assignment)
else:
    print("No se encontró una asignación válida.")
