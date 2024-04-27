# Miguel Angel Huerta Castillo     21310236
# Programa de ejemplo de lógica difusa utilizando conjuntos difusos.
# Este programa implementa un sistema de control difuso simple para controlar la velocidad de un ventilador basado en la temperatura ambiente.
# La lógica difusa se utiliza para manejar la imprecisión y la incertidumbre en el control del ventilador.

import numpy as np  # Importamos la librería numpy para cálculos numéricos

# Funciones de pertenencia para conjuntos difusos
# Se definen tres funciones de pertenencia: baja, media y alta, para la temperatura y la velocidad del ventilador.

# Función de pertenencia para la temperatura ambiente
def temperatura_baja(x):
    if x <= 20:
        return 1
    elif 20 < x <= 25:
        return (25 - x) / 5
    else:
        return 0

def temperatura_media(x):
    if 20 < x <= 25:
        return (x - 20) / 5
    elif 25 < x <= 30:
        return (30 - x) / 5
    else:
        return 0

def temperatura_alta(x):
    if x <= 25:
        return 0
    elif 25 < x <= 30:
        return (x - 25) / 5
    else:
        return 1

# Función de pertenencia para la velocidad del ventilador
def velocidad_baja(x):
    if x <= 30:
        return 1
    elif 30 < x <= 50:
        return (50 - x) / 20
    else:
        return 0

def velocidad_media(x):
    if 30 < x <= 50:
        return (x - 30) / 20
    elif 50 < x <= 70:
        return (70 - x) / 20
    else:
        return 0

def velocidad_alta(x):
    if x <= 50:
        return 0
    elif 50 < x <= 70:
        return (x - 50) / 20
    else:
        return 1

# Definición de reglas difusas
# Se definen las reglas difusas que relacionan la temperatura con la velocidad del ventilador.

# Reglas difusas: Si la temperatura es baja, entonces la velocidad del ventilador es baja.
# Si la temperatura es media, entonces la velocidad del ventilador es media.
# Si la temperatura es alta, entonces la velocidad del ventilador es alta.

# Inferencia difusa
# Dada la temperatura actual, se infiere la velocidad del ventilador según las reglas definidas.

def inferencia(temperatura):
    velocidad_baja_inferida = min(temperatura_baja(temperatura), velocidad_baja(30))
    velocidad_media_inferida = min(temperatura_media(temperatura), velocidad_media(50))
    velocidad_alta_inferida = min(temperatura_alta(temperatura), velocidad_alta(70))
    return max(velocidad_baja_inferida, velocidad_media_inferida, velocidad_alta_inferida)

# Definición de la temperatura actual (puede ser ingresada por el usuario)
temperatura_actual = 24

# Inferencia difusa para determinar la velocidad del ventilador
velocidad_resultante = inferencia(temperatura_actual)

# Impresión del resultado
print("Temperatura actual:", temperatura_actual)
print("Velocidad del ventilador:", velocidad_resultante)
