# Clase para representar un intervalo de tiempo (horario)
class Horario:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin
    
    # Método para verificar si este horario se solapa con otro horario
    def se_solapa_con(self, otro_horario):
        return (self.inicio < otro_horario.fin and self.fin > otro_horario.inicio)

# Definición de la función para verificar si un horario dado es seguro para una actividad en particular.
def es_horario_seguro(actividades, actividad, horario, horarios_asignados):
    for otra_actividad, otro_horario in horarios_asignados.items():
        if otra_actividad != actividad and horario.se_solapa_con(otro_horario):
            return False
    return True

# Función principal de asignación de horarios utilizando el algoritmo de Backtracking con Forward Checking.
def asignar_horarios(actividades, horarios_disponibles, horarios_asignados={}):
    if len(horarios_asignados) == len(actividades):
        return horarios_asignados

    actividad_sin_horario = None
    for actividad in actividades:
        if actividad not in horarios_asignados:
            actividad_sin_horario = actividad
            break

    for horario in horarios_disponibles:
        if es_horario_seguro(actividades, actividad_sin_horario, horario, horarios_asignados):
            horarios_asignados[actividad_sin_horario] = horario
            resultado = asignar_horarios(actividades, horarios_disponibles, horarios_asignados)
            if resultado is not None:
                return resultado
            del horarios_asignados[actividad_sin_horario]

    return None

# Ejemplo de uso
if __name__ == "__main__":
    # Definición de las actividades y sus horarios de inicio y fin
    actividades = {
        'Clase de Matemáticas': Horario(8, 10),
        'Reunión de Equipo': Horario(9, 11),
        'Almuerzo': Horario(12, 13),
        'Tutoría de Física': Horario(14, 16),
        'Deporte': Horario(17, 19)
    }

    # Lista de horarios disponibles
    horarios_disponibles = [
        Horario(8, 10),
        Horario(10, 12),
        Horario(12, 14),
        Horario(14, 16),
        Horario(16, 18),
        Horario(18, 20)
    ]

    # Llamada a la función principal para asignar horarios a las actividades
    horarios_asignados = asignar_horarios(actividades, horarios_disponibles)

    # Imprimir el resultado
    if horarios_asignados is not None:
        print("Horarios asignados:")
        for actividad, horario in horarios_asignados.items():
            print(f"{actividad}: {horario.inicio}-{horario.fin}")
    else:
        print("No se pudo encontrar una asignación de horarios válida.")
