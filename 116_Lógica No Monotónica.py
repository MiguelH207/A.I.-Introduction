# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo práctico de lógica no monotónica en Python.
# La lógica no monotónica es un tipo de lógica en la que la adición de nuevas premisas puede llevar a la revisión de conclusiones previamente alcanzadas.

class LógicaNoMonotónica:
    def __init__(self):
        self.premisas = []  # Inicializa una lista vacía para almacenar las premisas

    def agregar_premisa(self, premisa):
        self.premisas.append(premisa)  # Agrega una premisa a la lista

    def revisar_conclusion(self, conclusion):
        if "A" in self.premisas and "B" in self.premisas:  # Si se cumplen ciertas premisas
            print("Conclusiones revisadas: ", conclusion)  # Imprime la conclusión revisada
        else:
            print("Las premisas A y B no están presentes, la conclusión no se puede sostener.")  # Si no se cumplen las premisas necesarias

# Creación de una instancia de la clase LógicaNoMonotónica
sistema = LógicaNoMonotónica()

# Agregar algunas premisas
sistema.agregar_premisa("A")
sistema.agregar_premisa("B")

# Revisar una conclusión
sistema.revisar_conclusion("C")

