# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un sistema de diagnóstico utilizando lógica de primer orden.
# Se definen reglas de diagnóstico y causales para determinar la causa de un problema dado un conjunto de síntomas.

# Definición de reglas de diagnóstico
def reglas_diagnosticas(sintomas):
    # Regla 1: Si el paciente tiene fiebre y tos, es probable que tenga gripe.
    if 'fiebre' in sintomas and 'tos' in sintomas:
        return 'gripe'
    # Regla 2: Si el paciente tiene dolor de cabeza y dolor de garganta, es probable que tenga resfriado.
    elif 'dolor de cabeza' in sintomas and 'dolor de garganta' in sintomas:
        return 'resfriado'
    else:
        return 'desconocido'

# Definición de reglas causales
def reglas_causales(problema):
    # Regla 1: Si el problema es gripe, la causa probable es un virus de la gripe.
    if problema == 'gripe':
        return 'virus de la gripe'
    # Regla 2: Si el problema es resfriado, la causa probable es un virus del resfriado.
    elif problema == 'resfriado':
        return 'virus del resfriado'
    else:
        return 'causa desconocida'

# Función principal para realizar el diagnóstico y determinar la causa
def diagnostico(sintomas):
    problema = reglas_diagnosticas(sintomas)  # Aplica las reglas de diagnóstico para determinar el problema
    causa = reglas_causales(problema)         # Aplica las reglas causales para determinar la causa del problema
    return problema, causa

# Ejemplo de uso del programa
if __name__ == "__main__":
    # Síntomas del paciente
    sintomas_paciente = ['fiebre', 'tos']

    # Realizar el diagnóstico y determinar la causa
    problema_diagnosticado, causa_probable = diagnostico(sintomas_paciente)

    # Imprimir resultados
    print("Problema diagnosticado:", problema_diagnosticado)
    print("Causa probable:", causa_probable)
