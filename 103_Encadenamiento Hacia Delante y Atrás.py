# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un sistema de inferencia de lógica proposicional utilizando encadenamiento hacia adelante y hacia atrás.
# El programa contiene una base de conocimiento representada como un conjunto de reglas lógicas y hechos.
# Se proporciona un ejemplo práctico donde se usa el sistema de inferencia para determinar si un estudiante puede graduarse o no basándose en ciertas condiciones.

# Definición de la base de conocimiento (reglas lógicas y hechos)
base_conocimiento = {
    "reglas": {
        "regla1": {"antecedente": ["aprobo_matematicas", "aprobo_fisica"], "consecuente": "puede_graduarse"},
        "regla2": {"antecedente": ["aprobo_ingles", "aprobo_frances"], "consecuente": "puede_graduarse"},
        "regla3": {"antecedente": ["aprobo_tesis"], "consecuente": "puede_graduarse"}
    },
    "hechos": {
        "aprobo_matematicas": False,
        "aprobo_fisica": True,
        "aprobo_ingles": True,
        "aprobo_frances": False,
        "aprobo_tesis": True
    }
}

# Función para encadenamiento hacia adelante
def encadenamiento_hacia_adelante(base_conocimiento):
    hechos = base_conocimiento["hechos"]  # Extraemos los hechos de la base de conocimiento
    reglas = base_conocimiento["reglas"]  # Extraemos las reglas de la base de conocimiento
    while True:
        new_hechos = {}  # Creamos un diccionario vacío para almacenar nuevos hechos derivados
        for regla, contenido in reglas.items():  # Iteramos sobre cada regla
            antecedente = contenido["antecedente"]
            consecuente = contenido["consecuente"]
            if all(hechos[condicion] for condicion in antecedente) and not hechos.get(consecuente):
                # Verificamos si todas las condiciones del antecedente se cumplen y el consecuente no está en los hechos
                new_hechos[consecuente] = True  # Agregamos el consecuente como nuevo hecho
        hechos.update(new_hechos)  # Actualizamos los hechos con los nuevos hechos derivados
        if not new_hechos:  # Si no se agregaron nuevos hechos, salimos del bucle
            break
    return hechos  # Devolvemos los hechos derivados

# Función para encadenamiento hacia atrás
def encadenamiento_hacia_atras(base_conocimiento, objetivo):
    hechos = base_conocimiento["hechos"]  # Extraemos los hechos de la base de conocimiento
    reglas = base_conocimiento["reglas"]  # Extraemos las reglas de la base de conocimiento
    stack = [objetivo]  # Creamos una pila con el objetivo como primer elemento
    while stack:
        current = stack.pop()  # Tomamos el elemento superior de la pila
        if current not in hechos:  # Si el hecho no está en los hechos conocidos
            if current not in reglas:  # Si el hecho no está en las reglas conocidas
                return False  # No se puede determinar si el hecho es verdadero o falso
            else:
                regla = reglas[current]  # Obtenemos la regla que corresponde al hecho
                antecedente = regla["antecedente"]
                for condicion in antecedente:  # Iteramos sobre las condiciones del antecedente
                    stack.append(condicion)  # Agregamos las condiciones a la pila
    return True  # Si todas las condiciones se pueden verificar, el objetivo es alcanzable

# Ejemplo de uso del encadenamiento hacia adelante
print("Usando encadenamiento hacia adelante:")
nuevos_hechos_adelante = encadenamiento_hacia_adelante(base_conocimiento)
print("Hechos derivados:", nuevos_hechos_adelante)

# Ejemplo de uso del encadenamiento hacia atrás
print("\nUsando encadenamiento hacia atrás:")
objetivo = "puede_graduarse"
resultado_atras = encadenamiento_hacia_atras(base_conocimiento, objetivo)
print("Resultado:", resultado_atras)
