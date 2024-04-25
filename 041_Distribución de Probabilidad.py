# Miguel Angel Huerta Castillo     21310236

import random  # Importamos la librería random para generar números aleatorios

# Definimos una función llamada 'lanzar_dado' que simula el lanzamiento de un dado de 6 caras
def lanzar_dado():
    return random.randint(1, 6)  # Devuelve un número aleatorio entre 1 y 6, simulando el resultado del lanzamiento

# Definimos una función llamada 'calcular_probabilidad' que calcula la probabilidad de obtener un número específico en 'lanzamientos' lanzamientos de dados
def calcular_probabilidad(numero_deseado, lanzamientos):
    contador = 0  # Inicializamos un contador para contar cuántas veces obtenemos el número deseado
    
    # Realizamos 'lanzamientos' lanzamientos de dados
    for _ in range(lanzamientos):
        resultado = lanzar_dado()  # Simulamos el lanzamiento de un dado
        if resultado == numero_deseado:  # Si el resultado coincide con el número deseado
            contador += 1  # Incrementamos el contador
    
    # Calculamos la probabilidad dividiendo el número de ocurrencias del número deseado entre el total de lanzamientos
    probabilidad = contador / lanzamientos
    
    return probabilidad  # Devolvemos la probabilidad calculada

# Solicitamos al usuario que ingrese el número deseado y el número de lanzamientos
numero_deseado = int(input("Ingresa el número deseado (1 al 6): "))
lanzamientos = int(input("Ingresa el número de lanzamientos: "))

# Calculamos la probabilidad de obtener el número deseado en los lanzamientos especificados
probabilidad = calcular_probabilidad(numero_deseado, lanzamientos)

# Mostramos el resultado al usuario
print(f"La probabilidad de obtener el número {numero_deseado} en {lanzamientos} lanzamientos es: {probabilidad}")
