# Importamos la biblioteca random para generar números aleatorios
import random

# Definimos una función que calcula la probabilidad de un evento dado una lista de resultados y sus probabilidades
def calcular_probabilidad(resultados, probabilidades, evento):
    # Inicializamos la probabilidad del evento en cero
    probabilidad_evento = 0
    
    # Iteramos sobre cada resultado y su probabilidad
    for i in range(len(resultados)):
        # Si el resultado es igual al evento, sumamos su probabilidad a la probabilidad total del evento
        if resultados[i] in evento:  # Corregimos la condición para verificar si el resultado está en el evento
            probabilidad_evento += probabilidades[i]
    
    # Retornamos la probabilidad del evento
    return probabilidad_evento

# Definimos los posibles resultados de lanzar un dado
resultados_dado = [1, 2, 3, 4, 5, 6]

# Definimos las probabilidades de cada resultado (en este caso, el dado es justo, por lo que todas las probabilidades son 1/6)
probabilidades_dado = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

# Definimos el evento de interés, en este caso, obtener un número par
evento_par = [2, 4, 6]

# Calculamos la probabilidad de obtener un número par al lanzar un dado
probabilidad_par = calcular_probabilidad(resultados_dado, probabilidades_dado, evento_par)

# Imprimimos la probabilidad calculada
print("La probabilidad de obtener un número par al lanzar un dado es:", probabilidad_par*100,"%")
