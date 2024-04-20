# Definición de la función de utilidad
def calcular_utilidad(ventas, costos):
    """
    Calcula la utilidad neta dado el total de ventas y los costos.
    
    Args:
        ventas (float): El total de ventas.
        costos (float): Los costos totales.
        
    Returns:
        float: La utilidad neta calculada.
    """
    utilidad = ventas - costos  # Calcula la diferencia entre las ventas y los costos
    return utilidad  # Retorna la utilidad neta

# Solicitar al usuario que ingrese los datos de ventas y costos
ventas = float(input("Ingrese el total de ventas: "))  # Solicita al usuario el total de ventas
costos = float(input("Ingrese el total de costos: "))  # Solicita al usuario el total de costos

# Calcular la utilidad utilizando la función definida
utilidad_neta = calcular_utilidad(ventas, costos)  # Llama a la función de utilidad con los valores ingresados

# Mostrar el resultado al usuario
print("La utilidad neta es:", utilidad_neta)  # Muestra la utilidad neta calculada al usuario
