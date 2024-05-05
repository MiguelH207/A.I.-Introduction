# Miguel Angel Huerta Castillo 21310236
# Este programa implementa la lógica por defecto en Python.
# La lógica por defecto es un enfoque en el que se establecen reglas y hechos predeterminados,
# los cuales se utilizan para deducir conclusiones o inferir información adicional.

# Definición de hechos
hechos = {
    'llueve': False,  # Establece el hecho de que no está lloviendo inicialmente
    'dia_laboral': True  # Establece el hecho de que es un día laboral inicialmente
}

# Definición de reglas
def regla_1():
    """Regla que indica si se necesita llevar paraguas o no."""
    if hechos['llueve']:
        return 'Llevar paraguas'
    else:
        return 'No llevar paraguas'

# Función principal para inferir información
def logica_por_defecto():
    # Si es un día laboral y no está lloviendo, la regla_1 indica que no se necesita llevar paraguas
    if hechos['dia_laboral']:
        print("Es día laboral.")
        print("¿Está lloviendo?")
        respuesta = input("Respuesta (s/n): ")
        if respuesta.lower() == 's':
            hechos['llueve'] = True
        conclusion = regla_1()
        print(conclusion)
    else:
        print("No es día laboral, no se necesita llevar paraguas.")

# Llamada a la función principal
logica_por_defecto()
