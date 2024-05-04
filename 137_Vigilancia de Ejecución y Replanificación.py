# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo de planificación utilizando vigilancia de ejecución y replanificación.
# La planificación consiste en asignar tareas a recursos con el objetivo de completar un conjunto de objetivos.
# La vigilancia de ejecución permite monitorear el progreso de las tareas asignadas y tomar decisiones de replanificación si es necesario.
# En este ejemplo, se simula la asignación de tareas a recursos y se realiza la vigilancia de ejecución para detectar si una tarea no se ha completado a tiempo.
# Si una tarea no se completa a tiempo, se replanifica asignando la tarea a otro recurso disponible.

class Tarea:
    def __init__(self, nombre, duracion):
        self.nombre = nombre  # Nombre de la tarea
        self.duracion = duracion  # Duración estimada de la tarea
        self.completada = False  # Indica si la tarea ha sido completada

class Recurso:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del recurso
        self.tarea_actual = None  # Tarea actual asignada al recurso

def planificar_tareas(tareas, recursos):
    for tarea in tareas:
        recurso_disponible = None
        for recurso in recursos:
            if recurso.tarea_actual is None:  # Verificar si el recurso está disponible
                recurso_disponible = recurso
                break
        if recurso_disponible:
            recurso_disponible.tarea_actual = tarea
            print(f"Tarea '{tarea.nombre}' asignada a {recurso_disponible.nombre}.")
        else:
            print(f"No hay recursos disponibles para la tarea '{tarea.nombre}'.")

def vigilar_ejecucion(recursos):
    for recurso in recursos:
        tarea_actual = recurso.tarea_actual
        if tarea_actual:
            print(f"Vigilando ejecución de '{tarea_actual.nombre}' por {recurso.nombre}.")
            # Simulación: si la tarea no se completa a tiempo, replanificar
            if not tarea_actual.completada and tarea_actual.duracion > 5:  # Simulación de tarea no completada a tiempo
                print(f"¡La tarea '{tarea_actual.nombre}' no se ha completado a tiempo! Replanificando...")
                recurso.tarea_actual = None

# Crear instancias de tareas
tarea1 = Tarea("Limpiar la casa", 4)
tarea2 = Tarea("Hacer la compra", 6)
tarea3 = Tarea("Cocinar la cena", 7)

# Crear instancias de recursos
recurso1 = Recurso("Juan")
recurso2 = Recurso("María")
recurso3 = Recurso("Carlos")

# Lista de tareas y recursos
tareas = [tarea1, tarea2, tarea3]
recursos = [recurso1, recurso2, recurso3]

# Planificar tareas
planificar_tareas(tareas, recursos)

# Simulación de vigilancia de ejecución
vigilar_ejecucion(recursos)
