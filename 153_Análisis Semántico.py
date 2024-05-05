# Miguel Angel Huerta Castillo     21310236
# Este programa realiza un análisis semántico de una frase ingresada por el usuario. 
# Utiliza la biblioteca NLTK (Natural Language Toolkit) para realizar el análisis.

import nltk  # Importa la biblioteca NLTK

nltk.download('punkt')  # Descarga los recursos necesarios para tokenización
nltk.download('averaged_perceptron_tagger')  # Descarga los recursos necesarios para el etiquetado gramatical

def semantic_analysis(sentence):  # Define una función para realizar el análisis semántico
    tokens = nltk.word_tokenize(sentence)  # Tokeniza la frase en palabras individuales
    tagged = nltk.pos_tag(tokens)  # Etiqueta gramaticalmente cada palabra en la frase
    return tagged  # Devuelve las palabras etiquetadas

# Ejemplo de uso:
input_sentence = input("Ingrese una frase: ")  # Solicita al usuario que ingrese una frase
result = semantic_analysis(input_sentence)  # Realiza el análisis semántico de la frase ingresada
print("Análisis Semántico:", result)  # Muestra el resultado del análisis semántico
