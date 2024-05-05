# Miguel Angel Huerta Castillo     21310236
# Programa de lógica de primer orden utilizando encadenamiento hacia adelante y hacia atrás.
# Este programa implementa un ejemplo práctico de un sistema de recomendación de películas basado en reglas lógicas de primer orden.
# Utiliza encadenamiento hacia adelante y hacia atrás para inferir qué películas recomendar a un usuario dado sus intereses y preferencias.

class Pelicula:
    def __init__(self, titulo, genero):
        self.titulo = titulo  # Guarda el título de la película
        self.genero = genero  # Guarda el género de la película

class BaseConocimiento:
    def __init__(self):
        self.peliculas = []  # Lista de películas conocidas en la base de conocimiento

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)  # Agrega una nueva película a la base de conocimiento

    def peliculas_por_genero(self, genero):
        return [p for p in self.peliculas if p.genero == genero]  # Retorna películas del género dado

class SistemaRecomendacion:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento  # Guarda la base de conocimiento

    def recomendar_peliculas(self, intereses_usuario):
        peliculas_recomendadas = []  # Inicializa lista de películas recomendadas

        # Encadenamiento hacia adelante
        for interes in intereses_usuario:
            peliculas_interes = self.base_conocimiento.peliculas_por_genero(interes)
            peliculas_recomendadas.extend(peliculas_interes)  # Extiende la lista de películas recomendadas

        # Encadenamiento hacia atrás
        if not peliculas_recomendadas:  # Si no hay películas recomendadas por intereses directos
            peliculas_recomendadas = self.base_conocimiento.peliculas  # Recomendar todas las películas

        return peliculas_recomendadas

# Ejemplo de uso
base_conocimiento = BaseConocimiento()

# Agregar algunas películas a la base de conocimiento
base_conocimiento.agregar_pelicula(Pelicula("El Padrino", "Drama"))
base_conocimiento.agregar_pelicula(Pelicula("Inception", "Ciencia ficción"))
base_conocimiento.agregar_pelicula(Pelicula("Toy Story", "Animación"))
base_conocimiento.agregar_pelicula(Pelicula("Jurassic Park", "Aventura"))

# Definir los intereses del usuario
intereses_usuario = ["Ciencia ficción", "Aventura"]

# Crear el sistema de recomendación y obtener las películas recomendadas
sistema_recomendacion = SistemaRecomendacion(base_conocimiento)
peliculas_recomendadas = sistema_recomendacion.recomendar_peliculas(intereses_usuario)

# Imprimir las películas recomendadas
print("Películas recomendadas:")
for pelicula in peliculas_recomendadas:
    print("- ", pelicula.titulo)
