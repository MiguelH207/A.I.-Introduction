# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo de representación del conocimiento utilizando razonamiento por defecto y no monotónico en Python.

# Definición de la clase de hechos
class Hecho:
    def __init__(self, nombre, valor):
        self.nombre = nombre  # Guarda el nombre del hecho
        self.valor = valor    # Guarda el valor del hecho (verdadero o falso)

# Definición de la clase de reglas
class Regla:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente  # Guarda el antecedente de la regla (lista de hechos)
        self.consecuente = consecuente  # Guarda el consecuente de la regla (hecho)

# Definición de la base de conocimiento
base_conocimiento = []

# Función para verificar si un hecho está presente en la base de conocimiento
def verificar_hecho(hecho, base):
    for f in base:
        if f.nombre == hecho.nombre:
            return f.valor
    return None

# Función para inferir nuevos hechos a partir de la base de conocimiento y las reglas
def inferir(reglas, base):
    nuevos_hechos = []
    for regla in reglas:
        verdad = True
        for hecho in regla.antecedente:
            valor = verificar_hecho(hecho, base)
            if valor is None or not valor:
                verdad = False
                break
        if verdad:
            nuevos_hechos.append(regla.consecuente)
    return nuevos_hechos

# Función para agregar nuevos hechos a la base de conocimiento
def agregar_hechos(hechos, base):
    for hecho in hechos:
        base.append(hecho)

# Definición de los hechos iniciales
hechos_iniciales = [Hecho('llueve', False)]

# Definición de las reglas
reglas = [
    Regla([Hecho('llueve', False)], Hecho('tierra_moja', False)),
    Regla([Hecho('tierra_moja', False)], Hecho('llueve', True))
]

# Inferencia inicial de nuevos hechos
nuevos_hechos = inferir(reglas, hechos_iniciales)

# Agregar nuevos hechos a la base de conocimiento
agregar_hechos(nuevos_hechos, hechos_iniciales)

# Imprimir la base de conocimiento
print("Base de conocimiento después de la inferencia inicial:")
for hecho in hechos_iniciales:
    print(hecho.nombre, ":", hecho.valor)

# Más inferencias después de agregar nuevos hechos
nuevos_hechos = inferir(reglas, hechos_iniciales)

# Agregar nuevos hechos a la base de conocimiento
agregar_hechos(nuevos_hechos, hechos_iniciales)

# Imprimir la base de conocimiento final
print("\nBase de conocimiento después de las inferencias adicionales:")
for hecho in hechos_iniciales:
    print(hecho.nombre, ":", hecho.valor)
