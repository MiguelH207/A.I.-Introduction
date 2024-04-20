# Definimos el número total de elementos que necesitamos distribuir
num_elementos = 30

# Definimos la capacidad máxima de cada contenedor
capacidad_contenedor = 12

# Calculamos la cantidad total de contenedores necesarios
num_contenedores = num_elementos // capacidad_contenedor
# Si hay elementos sobrantes, necesitaremos un contenedor adicional
if num_elementos % capacidad_contenedor != 0:
    num_contenedores += 1

# Calculamos cuántos elementos quedan sin distribuir
elementos_sobrantes = (num_contenedores * capacidad_contenedor) - num_elementos

# Mostramos los resultados
print("Número total de contenedores necesarios:", num_contenedores)
print("Elementos sobrantes:", elementos_sobrantes)
