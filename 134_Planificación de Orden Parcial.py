# Miguel Angel Huerta Castillo 21310236
# Programa de Planificación usando Planificación de Orden Parcial
# Este programa implementa un algoritmo de planificación utilizando la técnica de Planificación de Orden Parcial.
# La Planificación de Orden Parcial es un enfoque que permite planificar y ordenar tareas en un proyecto sin necesidad de tener todas las dependencias definidas de antemano.
 
class Task:
    def __init__(self, name):
        self.name = name
        self.dependencies = set()  # Crea un conjunto vacío para almacenar las dependencias de la tarea
        self.dependents = set()    # Crea un conjunto vacío para almacenar las tareas dependientes de esta tarea

    def add_dependency(self, task):
        self.dependencies.add(task)  # Agrega una tarea como dependencia de esta tarea
        task.dependents.add(self)    # Agrega esta tarea como dependiente de la tarea dada

    def __str__(self):
        return self.name

def partial_order_planning(tasks):
    schedule = []  # Crea una lista para almacenar el orden parcial de las tareas
    remaining_tasks = set(tasks)  # Crea un conjunto de tareas restantes para planificar

    while remaining_tasks:
        schedulable_tasks = [task for task in remaining_tasks if not task.dependencies]  # Encuentra las tareas que no tienen dependencias
        if not schedulable_tasks:
            raise ValueError("No es posible planificar: ciclo de dependencias")  # Lanza un error si hay un ciclo de dependencias
        for task in schedulable_tasks:
            schedule.append(task)  # Agrega la tarea al orden parcial de planificación
            remaining_tasks.remove(task)  # Remueve la tarea de las tareas restantes
            for dependent in task.dependents:
                dependent.dependencies.remove(task)  # Remueve la tarea planificada de las dependencias de las tareas dependientes

    return schedule

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos instancias de tareas
    task1 = Task("Tarea 1")
    task2 = Task("Tarea 2")
    task3 = Task("Tarea 3")
    task4 = Task("Tarea 4")

    # Definimos las dependencias entre las tareas
    task2.add_dependency(task1)
    task3.add_dependency(task2)
    task4.add_dependency(task2)

    # Creamos una lista de tareas
    tasks = [task1, task2, task3, task4]

    # Realizamos la planificación de orden parcial
    schedule = partial_order_planning(tasks)

    # Imprimimos el orden parcial de las tareas
    print("Orden parcial de planificación:")
    for task in schedule:
        print(task)
