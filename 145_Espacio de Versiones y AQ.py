# Miguel Angel Huerta Castillo     21310236

# Este programa implementa un sistema de aprendizaje inductivo usando el Espacio de Versiones y el algoritmo AQ.
# El programa construye un conjunto de hipótesis que pueden clasificar un conjunto de ejemplos positivos y negativos.

# Definición de la función principal
def main():
    # Definición de los ejemplos positivos y negativos
    positive_examples = [
        {'color': 'rojo', 'forma': 'cuadrado'},
        {'color': 'azul', 'forma': 'triángulo'},
        {'color': 'verde', 'forma': 'círculo'}
    ]
    negative_examples = [
        {'color': 'verde', 'forma': 'cuadrado'},
        {'color': 'rojo', 'forma': 'triángulo'},
        {'color': 'azul', 'forma': 'círculo'}
    ]

    # Creación del espacio de versiones inicial con la hipótesis más general posible
    version_space = [{'color': None, 'forma': None}]

    # Iteración sobre cada ejemplo positivo
    for example in positive_examples:
        # Iteración sobre cada hipótesis en el espacio de versiones
        for hypothesis in version_space.copy():
            # Verificación de si la hipótesis cubre el ejemplo positivo
            if covers(hypothesis, example):
                # Remoción de todas las hipótesis que no cubren el ejemplo positivo
                version_space.remove(hypothesis)
                # Generación de todas las especializaciones de la hipótesis
                for specialized_hypothesis in specialize(hypothesis, example):
                    # Agregación de las especializaciones al espacio de versiones
                    version_space.append(specialized_hypothesis)

    # Iteración sobre cada ejemplo negativo
    for example in negative_examples:
        # Iteración sobre cada hipótesis en el espacio de versiones
        for hypothesis in version_space.copy():
            # Verificación de si la hipótesis cubre el ejemplo negativo
            if covers(hypothesis, example):
                # Remoción de la hipótesis que cubre el ejemplo negativo
                version_space.remove(hypothesis)

    # Impresión del espacio de versiones final
    print("Espacio de versiones final:")
    for hypothesis in version_space:
        print(hypothesis)

# Función para verificar si una hipótesis cubre un ejemplo
def covers(hypothesis, example):
    # Verificación de si todas las características de la hipótesis coinciden con las del ejemplo
    for attribute, value in example.items():
        if hypothesis[attribute] is not None and hypothesis[attribute] != value:
            return False
    return True

# Función para especializar una hipótesis dado un ejemplo positivo
def specialize(hypothesis, example):
    # Inicialización de la lista de especializaciones
    specializations = []
    # Iteración sobre cada característica del ejemplo
    for attribute, value in example.items():
        # Creación de una copia de la hipótesis
        specialized_hypothesis = dict(hypothesis)
        # Especificación de la característica del ejemplo en la hipótesis
        specialized_hypothesis[attribute] = value
        # Agregación de la especialización a la lista
        specializations.append(specialized_hypothesis)
    return specializations

# Llamada a la función principal
if __name__ == "__main__":
    main()
