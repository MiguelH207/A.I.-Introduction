# Miguel Angel Huerta Castillo     21310236

# Este programa en Python representa el conocimiento usando incertidumbre y factores de certeza.
# Utiliza un ejemplo práctico de un sistema experto que evalúa si una persona puede o no conducir un automóvil
# basado en su edad y en si ha consumido alcohol o no.

class Regla:
    def __init__(self, antecedente, consecuente, factor_certeza):
        self.antecedente = antecedente  # Almacena el antecedente de la regla
        self.consecuente = consecuente  # Almacena el consecuente de la regla
        self.factor_certeza = factor_certeza  # Almacena el factor de certeza de la regla

def evaluar_reglas(reglas, edad, alcohol):
    certeza_total = 0  # Inicializa la certeza total como 0
    for regla in reglas:
        if regla.antecedente(edad, alcohol):  # Si el antecedente de la regla se cumple
            certeza_total += regla.factor_certeza  # Incrementa la certeza total con el factor de certeza de la regla
    return certeza_total  # Retorna la certeza total

def regla_edad(edad, alcohol):
    return edad >= 18  # La persona es mayor o igual de 18 años

def regla_alcohol(edad, alcohol):
    if alcohol:  # Si la persona ha consumido alcohol
        return -0.5  # Retorna un factor de certeza negativo
    else:
        return 0.5  # Retorna un factor de certeza positivo

# Creación de reglas
reglas = [
    Regla(regla_edad, "Puede conducir", 0.8),  # Regla: Si la persona es mayor o igual de 18 años, tiene 0.8 de certeza para conducir
    Regla(regla_alcohol, "No puede conducir", 0.7)  # Regla: Si la persona ha consumido alcohol, tiene 0.7 de certeza para no conducir
]

# Evaluación de reglas
edad = 20  # Edad de la persona
alcohol = True  # Indica si la persona ha consumido alcohol (True o False)

certeza = evaluar_reglas(reglas, edad, alcohol)  # Evalúa las reglas con la edad y el consumo de alcohol
print("Certidumbre de poder conducir:", certeza)  # Imprime la certeza de poder conducir basado en las reglas evaluadas
