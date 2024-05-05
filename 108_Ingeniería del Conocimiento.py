# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo de Lógica de Primer Orden utilizando Ingeniería del Conocimiento.
# El ejemplo consiste en un sistema experto simple que recomienda actividades basadas en el clima.

# Definición de hechos
clima = "soleado"  # Se define el hecho del clima como soleado
temperatura = 25  # Se define el hecho de la temperatura como 25 grados Celsius

# Definición de reglas
def recomendar_actividad(clima, temperatura):
    if clima == "soleado" and temperatura > 20:  # Si el clima es soleado y la temperatura es mayor a 20 grados
        return "Ir a la playa"  # Se recomienda ir a la playa
    elif clima == "lluvioso":  # Si el clima es lluvioso
        return "Ver una película en casa"  # Se recomienda ver una película en casa
    else:  # En cualquier otro caso
        return "Dar un paseo por el parque"  # Se recomienda dar un paseo por el parque

# Consulta al sistema experto
actividad_recomendada = recomendar_actividad(clima, temperatura)  # Se consulta al sistema experto la actividad recomendada

# Impresión del resultado
print("Actividad recomendada:", actividad_recomendada)  # Se imprime la actividad recomendada
