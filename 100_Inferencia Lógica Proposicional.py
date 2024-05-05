# Miguel Angel Huerta Castillo     21310236

# Este programa implementa la inferencia lógica proposicional. Permite definir proposiciones, reglas y realizar inferencias para determinar si una proposición es verdadera o falsa basada en las reglas definidas.

# Definición de la clase Proposicion que representa una proposición lógica
class Proposicion:
    # Método constructor que inicializa la proposición con su nombre y su valor de verdad
    def __init__(self, nombre, valor):
        self.nombre = nombre  # Nombre de la proposición
        self.valor = valor    # Valor de verdad de la proposición (True o False)

# Definición de la clase Regla que representa una regla de inferencia lógica
class Regla:
    # Método constructor que inicializa la regla con su nombre y su expresión lógica
    def __init__(self, nombre, expresion):
        self.nombre = nombre      # Nombre de la regla
        self.expresion = expresion    # Expresión lógica que define la regla

    # Método para evaluar la expresión lógica de la regla
    def evaluar(self, valores):
        return eval(self.expresion, {}, valores)  # Se corrige para pasar el diccionario de valores de verdad

# Definición de la función de inferencia lógica que determina si una proposición es verdadera o falsa según las reglas definidas
def inferencia_logica(proposiciones, reglas):
    # Diccionario para almacenar los valores de verdad de las proposiciones
    valores = {prop.nombre: prop.valor for prop in proposiciones}
    # Iteración sobre todas las reglas
    for regla in reglas:
        # Si la regla es verdadera, actualiza el valor de verdad de la proposición correspondiente
        if regla.evaluar(valores):
            valores[regla.nombre] = True
    # Retorna el valor de verdad de la proposición objetivo
    return valores[proposiciones[-1].nombre]

# Ejemplo de uso del programa
if __name__ == "__main__":
    # Definición de las proposiciones
    p = Proposicion("P", True)
    q = Proposicion("Q", False)
    r = Proposicion("R", True)
    # Definición de las reglas de inferencia
    regla1 = Regla("Regla 1", "valores['P'] and valores['Q']")  # Si P y Q son verdaderos, entonces...
    regla2 = Regla("Regla 2", "valores['R']")  # Si R es verdadero, entonces...
    # Lista de todas las proposiciones
    proposiciones = [p, q, r]
    # Lista de todas las reglas
    reglas = [regla1, regla2]
    # Aplicación de la inferencia lógica para determinar si la proposición final es verdadera o falsa
    resultado = inferencia_logica(proposiciones, reglas)
    # Imprime el resultado de la inferencia
    print("La inferencia lógica es:", resultado)
