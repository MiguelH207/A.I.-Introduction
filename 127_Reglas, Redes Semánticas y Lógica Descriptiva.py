# Miguel Angel Huerta Castillo     21310236
# Este programa en Python ilustra cómo representar conocimiento utilizando reglas, redes semánticas y lógica descriptiva.
# El ejemplo práctico utilizado aquí es el de un sistema de recomendación de películas basado en preferencias de género.

class Reglas:  # Definición de una clase para representar reglas
    def __init__(self, antecedente, consecuente):  # Método para inicializar la clase con antecedente y consecuente
        self.antecedente = antecedente  # Asignación del antecedente
        self.consecuente = consecuente  # Asignación del consecuente

class RedSemantica:  # Definición de una clase para representar redes semánticas
    def __init__(self, concepto, relaciones):  # Método para inicializar la clase con concepto y relaciones
        self.concepto = concepto  # Asignación del concepto
        self.relaciones = relaciones  # Asignación de las relaciones

class LogicaDescriptiva:  # Definición de una clase para representar lógica descriptiva
    def __init__(self, predicado, variables):  # Método para inicializar la clase con predicado y variables
        self.predicado = predicado  # Asignación del predicado
        self.variables = variables  # Asignación de las variables

# Función para recomendar películas basadas en preferencias de género
def recomendar_pelicula(preferencias, reglas):
    recomendaciones = []  # Lista para almacenar las recomendaciones
    
    for regla in reglas:
        if all(genre in preferencias for genre in regla.antecedente):
            recomendaciones.append(regla.consecuente)
    
    return recomendaciones

# Creación de instancias de Reglas, RedSemantica y LogicaDescriptiva con ejemplos específicos

# Ejemplo de reglas que dicen: "Si le gusta la acción y la ciencia ficción, recomienda 'Avengers'."
regla_1 = Reglas(["acción", "ciencia ficción"], "Avengers")
regla_2 = Reglas(["drama", "romance"], "Titanic")
regla_3 = Reglas(["comedia"], "The Hangover")

# Lista de todas las reglas
reglas = [regla_1, regla_2, regla_3]

# Preferencias del usuario
preferencias_usuario = ["acción", "ciencia ficción"]

# Recomendación de películas basadas en las preferencias del usuario
recomendaciones_usuario = recomendar_pelicula(preferencias_usuario, reglas)

# Imprimir recomendaciones
print("Películas recomendadas para ti:")
for pelicula in recomendaciones_usuario:
    print("-", pelicula)
