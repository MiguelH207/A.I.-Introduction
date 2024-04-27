# Miguel Angel Huerta Castillo     21310236

# Este programa en Python representa el conocimiento utilizando eventos y objetos mentales (creencias).
# El ejemplo práctico es un sistema simple de registro de notas de estudiantes.
# El programa permite agregar creencias sobre el rendimiento académico de un estudiante, como su nombre, materia y nota.

class Creencia:
    def __init__(self, sujeto, predicado, objeto):
        self.sujeto = sujeto  # Define el sujeto de la creencia
        self.predicado = predicado  # Define el predicado de la creencia
        self.objeto = objeto  # Define el objeto de la creencia

    def __str__(self):
        return f"Creencia: {self.sujeto} {self.predicado} {self.objeto}"  # Devuelve la representación de la creencia como string

class SistemaConocimiento:
    def __init__(self):
        self.creencias = []  # Inicializa la lista de creencias del sistema

    def agregar_creencia(self, sujeto, predicado, objeto):
        nueva_creencia = Creencia(sujeto, predicado, objeto)  # Crea una nueva creencia
        self.creencias.append(nueva_creencia)  # Agrega la nueva creencia a la lista

    def mostrar_creencias(self):
        for creencia in self.creencias:
            print(creencia)  # Imprime cada creencia en la lista

# Crear un objeto de la clase SistemaConocimiento
sistema = SistemaConocimiento()

# Agregar algunas creencias al sistema
sistema.agregar_creencia("Juan", "obtuvo", "8.5 en Matemáticas")
sistema.agregar_creencia("María", "obtuvo", "9.0 en Historia")

# Mostrar todas las creencias en el sistema
sistema.mostrar_creencias()
