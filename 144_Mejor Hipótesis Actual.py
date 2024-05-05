# Miguel Angel Huerta Castillo     21310236

# Este programa implementa el algoritmo de Aprendizaje Inductivo usando la estrategia de Mejor Hipótesis Actual.
# El programa toma como entrada un conjunto de ejemplos de entrenamiento, donde cada ejemplo consiste en una lista de atributos y su respectiva etiqueta.
# Luego, utiliza estos ejemplos para generar la mejor hipótesis posible que clasifique correctamente los ejemplos de entrenamiento.

# Define la función para encontrar la mejor hipótesis actual
def find_best_hypothesis(examples):
    # Inicializa la mejor hipótesis como una lista vacía
    best_hypothesis = []
    
    # Por cada atributo en los ejemplos de entrenamiento
    for i in range(len(examples[0])):
        # Inicializa la hipótesis actual para este atributo como None
        current_hypothesis = None
        
        # Por cada ejemplo en los ejemplos de entrenamiento
        for example in examples:
            # Si la etiqueta del ejemplo es positiva (1)
            if example[-1] == 1:
                # Si la hipótesis actual para este atributo aún no ha sido establecida
                if current_hypothesis is None:
                    # La hipótesis actual para este atributo es el valor del atributo en este ejemplo
                    current_hypothesis = example[i]
                # Si la hipótesis actual ya ha sido establecida
                else:
                    # Si el valor del atributo en este ejemplo es diferente al de la hipótesis actual
                    if example[i] != current_hypothesis:
                        # Actualiza la hipótesis actual para este atributo como '?'
                        current_hypothesis = '?'
        # Agrega la hipótesis actual para este atributo a la mejor hipótesis
        best_hypothesis.append(current_hypothesis)
    
    # Retorna la mejor hipótesis
    return best_hypothesis

# Ejemplo de conjunto de entrenamiento
training_examples = [
    ['soleado', 'caluroso', 'alta', 'debil', 0],
    ['soleado', 'caluroso', 'alta', 'fuerte', 0],
    ['nublado', 'caluroso', 'alta', 'debil', 1],
    ['lluvioso', 'templado', 'alta', 'debil', 1],
    ['lluvioso', 'frio', 'normal', 'debil', 1],
    ['lluvioso', 'frio', 'normal', 'fuerte', 0],
    ['nublado', 'frio', 'normal', 'fuerte', 1],
    ['soleado', 'templado', 'alta', 'debil', 0],
    ['soleado', 'frio', 'normal', 'debil', 1],
    ['lluvioso', 'templado', 'normal', 'debil', 1],
    ['soleado', 'templado', 'normal', 'fuerte', 1],
    ['nublado', 'templado', 'alta', 'fuerte', 1],
    ['nublado', 'caluroso', 'normal', 'debil', 1],
    ['lluvioso', 'caluroso', 'alta', 'fuerte', 0]
]

# Encuentra la mejor hipótesis para el conjunto de entrenamiento dado
best_hypothesis = find_best_hypothesis(training_examples)

# Imprime la mejor hipótesis encontrada
print("Mejor hipótesis actual:", best_hypothesis)
