# Miguel Angel Huerta Castillo 21310236
# Este programa implementa un ejemplo práctico de lógica modal en Python.
# La lógica modal es un sistema formal que extiende la lógica proposicional con operadores modales,
# que expresan posibilidad, necesidad, obligación, etc.

# Importamos la librería necessaria para trabajar con la lógica modal
from modal import *

# Creamos un mundo posible inicial
w = World()

# Definimos dos proposiciones atómicas
p = Atomic('p')
q = Atomic('q')

# Agregamos las proposiciones al mundo
w.add(p)
w.add(q)

# Creamos una fórmula que expresa que p es posible
f = Possibly(p)

# Imprimimos la fórmula
print(f)

# Verificamos si la fórmula es válida en el mundo actual
print(w.valid(f))
