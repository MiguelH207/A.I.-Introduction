# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un tratamiento probabilístico del lenguaje utilizando gramáticas probabilísticas independientes del contexto (PCFG). 
# Se utiliza la biblioteca NLTK para definir una gramática PCFG y generar oraciones aleatorias basadas en esa gramática.

import nltk
from nltk.grammar import PCFG, Production
from nltk.corpus import PlaintextCorpusReader

# Se carga un corpus de texto para entrenar la gramática PCFG
corpus = PlaintextCorpusReader('.', 'corpus.txt')

# Se tokeniza el corpus en oraciones
sentences = corpus.sents()

# Se inicializa un diccionario para contar las producciones gramaticales
production_counts = {}

# Se recorren todas las oraciones en el corpus
for sentence in sentences:
    # Se recorren todas las producciones en cada oración
    for production in nltk.CFG.fromstring("S -> " + " ".join(sentence)).productions():
        # Se incrementa el conteo de la producción en el diccionario
        production_counts[production] = production_counts.get(production, 0) + 1

# Se inicializa una lista de producciones
productions = []

# Se recorren las producciones y sus conteos
for production, count in production_counts.items():
    # Se crea un objeto Production con la producción y su probabilidad
    productions.append(Production(production.lhs(), production.rhs(), prob=count/len(sentences)))

# Se crea una gramática PCFG con las producciones y sus probabilidades
pcfg = PCFG(nltk.Nonterminal('S'), productions)

# Se generan 5 oraciones aleatorias utilizando la gramática PCFG
for i in range(5):
    # Se elige aleatoriamente una oración basada en la gramática PCFG
    sentence = nltk.generate.generate(pcfg, depth=5)
    # Se imprime la oración generada
    print(' '.join(sentence))
