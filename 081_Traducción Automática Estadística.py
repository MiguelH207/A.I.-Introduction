# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo práctico de traducción automática estadística utilizando la biblioteca NLTK en Python.
# Utiliza un modelo de traducción estadística pre-entrenado para traducir una frase de inglés a español.

import nltk
nltk.download('punkt')  # Descarga de recursos necesarios para NLTK

from nltk.translate import IBMModel1  # Importa el modelo IBMModel1 para traducción estadística
from nltk.translate import AlignedSent  # Importa la clase AlignedSent para representar pares de oraciones alineadas

# Pares de oraciones paralelas inglés-español para el entrenamiento del modelo
english_sentences = [['I', 'love', 'you'], ['He', 'eats', 'apples'], ['She', 'drinks', 'milk']]
spanish_sentences = [['Yo', 'te', 'amo'], ['Él', 'come', 'manzanas'], ['Ella', 'bebe', 'leche']]

# Convertir las listas de oraciones en objetos de la clase AlignedSent
aligned_sentences = [AlignedSent(e, s) for e, s in zip(english_sentences, spanish_sentences)]

# Entrenamiento del modelo de traducción estadística
ibm1 = IBMModel1(aligned_sentences, 5)  # Se establece el número de iteraciones a 5

# Oración en inglés a ser traducida
english_sentence = ['She', 'eats', 'fruit']

# Traducción de la oración utilizando el modelo entrenado
spanish_translation = ibm1.translate(english_sentence)

# Impresión de la traducción
print("English sentence:", english_sentence)
print("Spanish translation:", spanish_translation)
