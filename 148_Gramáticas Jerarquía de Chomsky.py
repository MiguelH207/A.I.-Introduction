# Miguel Angel Huerta Castillo     21310236
# Este programa implementa una gramática de la jerarquía de Chomsky en Python para realizar un tratamiento lógico del lenguaje.
# Se proporciona un ejemplo práctico de cómo utilizar la gramática para analizar y generar frases.

import nltk

# Definición de la gramática en la Jerarquía de Chomsky
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'el' | 'la' | 'un' | 'una'
    N -> 'perro' | 'gato' | 'pelota' | 'casa'
    V -> 'persigue' | 'juega' | 'corre'
    P -> 'en' | 'con' | 'sobre' | 'a'
    Det -> 'al' 
""")

# Creación del analizador sintáctico
parser = nltk.ChartParser(grammar)

# Frase de entrada para ser analizada
sentence = "el perro persigue al gato con una pelota"

# Tokenización de la frase
tokens = nltk.word_tokenize(sentence)

# Análisis sintáctico de la frase
for tree in parser.parse(tokens):
    print(tree)
