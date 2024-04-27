# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un modelo probabilístico del lenguaje utilizando un corpus.
# Calcula la probabilidad de ocurrencia de una palabra en base a su frecuencia en el corpus.

import random

# Definición del corpus
corpus = "El perro come carne. El gato come pescado. El pájaro vuela alto. El pez nada rápido."

# Tokenización del corpus
tokens = corpus.split()

# Creación del diccionario de frecuencia de palabras
freq_dict = {}
for token in tokens:
    if token in freq_dict:
        freq_dict[token] += 1
    else:
        freq_dict[token] = 1

# Función para calcular la probabilidad de una palabra en el corpus
def prob_palabra(palabra):
    if palabra in freq_dict:
        return freq_dict[palabra] / len(tokens)
    else:
        return 0

# Ejemplo de uso del modelo probabilístico
ejemplo_palabra = "come"
probabilidad = prob_palabra(ejemplo_palabra)
print("La probabilidad de que la palabra '{}' ocurra en el corpus es: {:.2f}".format(ejemplo_palabra, probabilidad))
