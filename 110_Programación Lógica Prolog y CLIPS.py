# Miguel Angel Huerta Castillo     21310236
# Este programa en Python define un sistema de recomendación de películas basado en el género y la edad del usuario.
# Dado un género y una edad, el programa recomienda una película adecuada basada en esas preferencias.

# Definición de la base de datos de películas con su respectivo género.
peliculas = {
    'accion': ['Die Hard', 'Mad Max: Fury Road', 'John Wick'],
    'comedia': ['Superbad', 'The Hangover', 'Anchorman'],
    'terror': ['The Conjuring', 'Get Out', 'A Nightmare on Elm Street']
}

# Función para recomendar una película basada en el género y la edad.
def recomendar_pelicula(genero, edad):
    if genero == 'accion' and edad >= 18:
        return peliculas['accion'][0]  # Se recomienda la primera película de acción si es mayor de edad.
    elif genero == 'comedia':
        return peliculas['comedia'][0]  # Se recomienda la primera película de comedia.
    elif genero == 'terror':
        return peliculas['terror'][0]   # Se recomienda la primera película de terror.
    else:
        return "Lo siento, no hay recomendaciones para ese género y edad."

# Ejemplos de uso
print(recomendar_pelicula('accion', 25))  # Output esperado: Die Hard
print(recomendar_pelicula('comedia', 20)) # Output esperado: Superbad
print(recomendar_pelicula('terror', 30))   # Output esperado: The Conjuring
print(recomendar_pelicula('drama', 25))    # Output esperado: Lo siento, no hay recomendaciones para ese género y edad.
