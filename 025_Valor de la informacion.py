# Definimos una función para calcular el valor de la información
def valor_informacion(num_datos_previos, num_datos_nuevos):
    # Calculamos la diferencia en el número de datos
    diferencia_datos = num_datos_nuevos - num_datos_previos
    # Retornamos la diferencia como valor de la información
    return diferencia_datos

# Definimos el número de datos previos y el número de nuevos datos obtenidos
num_datos_previos = 100
num_datos_nuevos = 120

# Calculamos el valor de la información llamando a la función
info_value = valor_informacion(num_datos_previos, num_datos_nuevos)

# Imprimimos el resultado
print("El valor de la información es:", info_value)
