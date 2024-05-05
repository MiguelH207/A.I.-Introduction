# Miguel Angel Huerta Castillo
# 21310236

# Este programa representa el conocimiento utilizando marcos, acciones, situaciones y eventos.
# Define una clase Marco para representar las características de cada situación.
# Luego, crea instancias de la clase Marco para representar diferentes situaciones.
# Finalmente, muestra información sobre cada situación creada.

class Marco:
    def __init__(self, nombre, lugar, tiempo, accion, resultado):
        # Constructor de la clase Marco que inicializa las características de la situación.
        self.nombre = nombre  # Nombre de la situación.
        self.lugar = lugar  # Lugar donde ocurre la situación.
        self.tiempo = tiempo  # Tiempo en que ocurre la situación.
        self.accion = accion  # Acción realizada en la situación.
        self.resultado = resultado  # Resultado de la acción en la situación.

# Creación de instancias de la clase Marco para representar diferentes situaciones.
situacion1 = Marco("Compra en el supermercado", "Supermercado XYZ", "Mañana", "Comprar comida", "Compra exitosa")
situacion2 = Marco("Estudio en casa", "Mi casa", "Tarde", "Estudiar para el examen", "Entendimiento del tema")
situacion3 = Marco("Cita con el médico", "Hospital ABC", "Tarde", "Consulta médica", "Diagnóstico y tratamiento")

# Mostrar información sobre cada situación creada.
print("Situación 1:")
print("Nombre:", situacion1.nombre)
print("Lugar:", situacion1.lugar)
print("Tiempo:", situacion1.tiempo)
print("Acción:", situacion1.accion)
print("Resultado:", situacion1.resultado)
print()

print("Situación 2:")
print("Nombre:", situacion2.nombre)
print("Lugar:", situacion2.lugar)
print("Tiempo:", situacion2.tiempo)
print("Acción:", situacion2.accion)
print("Resultado:", situacion2.resultado)
print()

print("Situación 3:")
print("Nombre:", situacion3.nombre)
print("Lugar:", situacion3.lugar)
print("Tiempo:", situacion3.tiempo)
print("Acción:", situacion3.accion)
print("Resultado:", situacion3.resultado)
