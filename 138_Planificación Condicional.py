# Miguel Angel Huerta Castillo 21310236
# Este programa implementa un ejemplo práctico de planificación usando Planificación Condicional.
# El código define una serie de tareas con condiciones de ejecución y luego planifica la ejecución de estas tareas de acuerdo con las condiciones.


# Definición de las tareas y sus condiciones
tasks = {
    "Tarea 1": {"condición": False},  # Define la Tarea 1 con condición inicial como False
    "Tarea 2": {"condición": True},   # Define la Tarea 2 con condición inicial como True
    "Tarea 3": {"condición": False}   # Define la Tarea 3 con condición inicial como False
}

# Función para ejecutar una tarea si su condición es True
def ejecutar_tarea(tarea):
    if tarea["condición"]:  # Si la condición de la tarea es True
        print(f"Ejecutando {tarea}")  # Imprime que la tarea está siendo ejecutada
        # Aquí iría el código para ejecutar la tarea en un entorno real

# Planificación de las tareas
for tarea, detalles in tasks.items():  # Itera sobre cada tarea y sus detalles
    ejecutar_tarea(detalles)  # Llama a la función ejecutar_tarea con los detalles de la tarea
