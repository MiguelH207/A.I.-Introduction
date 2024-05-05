# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un sistema de planificación utilizando Redes Jerárquicas de Tareas.
# Las redes jerárquicas de tareas son una técnica de planificación en la que las tareas se organizan en una jerarquía,
# donde las tareas principales se dividen en subtareas más pequeñas, y así sucesivamente, hasta llegar a las tareas más simples.


class Task:  # Definición de la clase Task para representar una tarea
    def __init__(self, name, duration):  # Método constructor para inicializar los atributos de la tarea
        self.name = name  # Nombre de la tarea
        self.duration = duration  # Duración de la tarea en horas
        self.dependencies = []  # Lista de tareas de las que depende esta tarea

    def add_dependency(self, task):  # Método para agregar una dependencia a la tarea
        self.dependencies.append(task)  # Agrega la tarea de dependencia a la lista

def print_schedule(task, indent=0):  # Función para imprimir el horario de las tareas
    print("  " * indent + task.name + " (" + str(task.duration) + " horas)")  # Imprime el nombre y la duración de la tarea
    for dependency in task.dependencies:  # Recorre las dependencias de la tarea
        print_schedule(dependency, indent + 1)  # Imprime la dependencia con un nivel de indentación mayor

# Creación de las tareas
task1 = Task("Tarea principal", 4)
task2 = Task("Subtarea 1", 2)
task3 = Task("Subtarea 2", 3)
task4 = Task("Subtarea 3", 1)
task5 = Task("Subtarea 4", 2)

# Establecimiento de las dependencias entre tareas
task1.add_dependency(task2)
task1.add_dependency(task3)
task2.add_dependency(task4)
task3.add_dependency(task5)

# Impresión del horario de las tareas
print("Horario de tareas:")
print_schedule(task1)
