# Miguel Angel Huerta Castillo     21310236

# Este programa en Python implementa una Gramática Probabilística Lexicalizada del Contexto (CFL). 
# Utiliza la librería nltk para definir la gramática y generar oraciones aleatorias basadas en esa gramática.

import nltk
from nltk.parse.generate import generate  # Importamos la función generate desde nltk.parse.generate

# Definimos la gramática probabilística

"""
    S -> NP VP [1.0]  # Regla inicial: S (frase) se compone de NP (sintagma nominal) seguido de VP (sintagma verbal) con probabilidad 1.0
    NP -> Det N [0.5] | N [0.3] | NP PP [0.2]  # Reglas para NP: Det (determinante) seguido de N (nombre) con probabilidad 0.5, solo N con probabilidad 0.3, o NP seguido de PP (sintagma preposicional) con probabilidad 0.2
    VP -> V NP [0.6] | VP PP [0.4]  # Reglas para VP: V (verbo) seguido de NP con probabilidad 0.6, o VP seguido de PP con probabilidad 0.4
    PP -> P NP [1.0]  # Regla para PP: P (preposición) seguido de NP con probabilidad 1.0
    Det -> 'el' [0.4] | 'un' [0.6]  # Reglas para Det: 'el' con probabilidad 0.4, 'un' con probabilidad 0.6
    N -> 'perro' [0.7] | 'gato' [0.3]  # Reglas para N: 'perro' con probabilidad 0.7, 'gato' con probabilidad 0.3
    V -> 'persigue' [0.8] | 'juega' [0.2]  # Reglas para V: 'persigue' con probabilidad 0.8, 'juega' con probabilidad 0.2
    P -> 'a' [0.6] | 'con' [0.4]  # Reglas para P: 'a' con probabilidad 0.6, 'con' con probabilidad 0.4
"""

grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.5] | N [0.3] | NP PP [0.2]
    VP -> V NP [0.6] | VP PP [0.4]
    PP -> P NP [1.0]
    Det -> 'el' [0.4] | 'un' [0.6]
    N -> 'perro' [0.7] | 'gato' [0.3]
    V -> 'persigue' [0.8] | 'juega' [0.2]
    P -> 'a' [0.6] | 'con' [0.4]
""")

# Generamos 5 oraciones aleatorias de acuerdo a la gramática definida
for sentence in generate(grammar, n=5):
    print(' '.join(sentence))  # Imprimimos cada oración generada separando las palabras por espacios
