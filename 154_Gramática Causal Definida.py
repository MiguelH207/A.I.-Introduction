# Miguel Angel Huerta Castillo 21310236
# Este programa implementa una gramática causal definida en Python para realizar un tratamiento lógico del lenguaje.
# La gramática causal definida permite representar relaciones causales entre eventos o conceptos.
# El programa incluye un ejemplo práctico donde se analiza un texto para identificar relaciones causales entre diferentes eventos.

import nltk
from nltk.parse import ShiftReduceParser

# Definición de la gramática causal
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    VP -> V NP | V NP PP
    PP -> P NP
    NP -> Det N | Det N PP
    Det -> 'el' | 'un'
    N -> 'perro' | 'gato' | 'hombre' | 'mujer'
    V -> 'mordió' | 'persiguió' | 'vio'
    P -> 'a' | 'con'
""")

# Creación del analizador sintáctico Shift-Reduce
sr_parser = ShiftReduceParser(grammar)

# Función para analizar una oración y encontrar relaciones causales
def analyze_sentence(sentence):
    tokens = sentence.split()  # Dividir la oración en tokens
    trees = sr_parser.parse(tokens)  # Analizar la oración
    for tree in trees:
        print(tree)  # Imprimir el árbol de análisis sintáctico

# Ejemplo práctico
example_sentence = "el perro persiguió al gato con furia"
analyze_sentence(example_sentence)
