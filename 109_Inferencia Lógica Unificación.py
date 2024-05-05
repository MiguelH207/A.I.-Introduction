# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo de inferencia lógica de primer orden utilizando unificación en Python.
# La inferencia lógica de primer orden se refiere a la manipulación de fórmulas lógicas utilizando variables, cuantificadores y predicados.
# La unificación es un proceso que busca encontrar una asignación de valores a las variables de dos fórmulas lógicas de manera que estas se vuelvan idénticas.

def unify(var, x, theta):
    if theta is None:  # Si theta es None, devuelve None
        return None
    elif var == x:  # Si las variables son iguales, devuelve theta
        return theta
    elif isinstance(x, str) and x in theta:  # Si x es una variable y está en theta, realiza unificación recursiva
        return unify(var, theta[x], theta)
    elif isinstance(var, str) and var in theta:  # Si var es una variable y está en theta, realiza unificación recursiva
        return unify(theta[var], x, theta)
    elif isinstance(x, list) and isinstance(var, list):  # Si tanto var como x son listas
        if len(var) == len(x):  # Si las listas tienen la misma longitud
            return unify(var[1:], x[1:], unify(var[0], x[0], theta))  # Realiza unificación recursiva en cada elemento de las listas
        else:
            return None
    else:
        return None

def main():
    # Definimos las dos fórmulas lógicas que queremos unificar
    # Por ejemplo, queremos unificar P(x, y) con P(A, B)
    P = ['P', 'x', 'y']
    Q = ['P', 'A', 'B']

    # Realizamos la unificación de las dos fórmulas
    theta = unify(P, Q, {})

    # Imprimimos el resultado de la unificación
    if theta is not None:
        print("Unificación exitosa. θ =", theta)
    else:
        print("Unificación fallida.")

if __name__ == "__main__":
    main()
