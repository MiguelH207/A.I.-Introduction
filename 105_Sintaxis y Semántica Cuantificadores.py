# Miguel Angel Huerta Castillo     21310236
# Este programa en Python implementa un ejemplo práctico de lógica de primer orden utilizando cuantificadores.
# El ejemplo consiste en encontrar si un conjunto de números contiene algún número par.

# Definimos una lista de números.
numeros = [1, 3, 5, 7, 9]

# Definimos una función que utiliza cuantificador existencial para verificar si algún número en la lista es par.
def algun_numero_par(lista):
    # Iteramos sobre cada número en la lista.
    for numero in lista:
        # Si el número es par (es decir, su residuo al dividir entre 2 es 0), retornamos True.
        if numero % 2 == 0:
            return True
    # Si ningún número en la lista es par, retornamos False.
    return False

# Llamamos a la función y almacenamos el resultado en la variable resultado.
resultado = algun_numero_par(numeros)

# Verificamos el resultado y mostramos un mensaje apropiado.
if resultado:
    print("La lista contiene al menos un número par.")
else:
    print("La lista no contiene ningún número par.")
