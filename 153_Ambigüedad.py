# Miguel Angel Huerta Castillo     21310236

# Este programa demuestra el uso de ambigüedad en el procesamiento del lenguaje natural.
# La ambigüedad se refiere a situaciones en las que una frase o palabra puede tener múltiples interpretaciones.
# Aquí, utilizamos un ejemplo práctico de ambigüedad en el procesamiento del lenguaje.

import nltk  # Importamos la librería NLTK (Natural Language Toolkit) para procesamiento del lenguaje natural

# Definimos una función para identificar la ambigüedad en una frase
def identify_ambiguity(sentence):
    words = nltk.word_tokenize(sentence)  # Tokenizamos la frase en palabras
    tagged_words = nltk.pos_tag(words)  # Etiquetamos las palabras con sus partes del discurso
    
    # Creamos un conjunto para almacenar las palabras ambiguas
    ambiguous_words = set()
    
    # Iteramos sobre las palabras etiquetadas para identificar las palabras ambiguas
    for word, tag in tagged_words:
        if tag.startswith('N'):  # Si la palabra es un sustantivo,
            ambiguous_words.add(word)  # la agregamos al conjunto de palabras ambiguas
    
    return ambiguous_words  # Devolvemos el conjunto de palabras ambiguas

# Ejemplo de frase ambigua
ambiguous_sentence = "The bank is closed."

# Llamamos a la función para identificar la ambigüedad en la frase
ambiguous_words = identify_ambiguity(ambiguous_sentence)

# Imprimimos las palabras ambiguas identificadas
print("Ambiguous words:", ambiguous_words)
