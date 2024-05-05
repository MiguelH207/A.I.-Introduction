# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un sistema experto simple que determina si una persona puede obtener su licencia de conducir
# basándose en su edad y si ha pasado el examen teórico y práctico.

def sistema_experto(edad, examen_teórico, examen_práctico):
    """
    Función que determina si una persona puede obtener su licencia de conducir basándose en su edad y sus resultados en los exámenes.

    Argumentos:
    - edad: entero que representa la edad de la persona.
    - examen_teórico: booleano que indica si la persona pasó el examen teórico (True) o no (False).
    - examen_práctico: booleano que indica si la persona pasó el examen práctico (True) o no (False).

    Retorna:
    - Un mensaje indicando si la persona puede obtener su licencia de conducir o no.
    """
    if edad >= 18 and examen_teórico and examen_práctico:  # Si la edad es mayor o igual a 18 y pasó ambos exámenes
        return "¡Felicidades! Puedes obtener tu licencia de conducir."
    else:  # En cualquier otro caso
        return "Lo siento, no cumples con los requisitos para obtener tu licencia de conducir."

# Ejemplo de uso del sistema experto
edad = 20
examen_teórico = True
examen_práctico = True

# Llamada a la función sistema_experto con los datos de ejemplo y se imprime el resultado
print(sistema_experto(edad, examen_teórico, examen_práctico))
