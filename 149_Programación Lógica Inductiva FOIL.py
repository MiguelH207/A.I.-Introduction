# Miguel Angel Huerta Castillo     21310236

# Este programa implementa un ejemplo práctico de Aprendizaje Inductivo utilizando Programación Lógica Inductiva (FOIL).
# Utiliza la biblioteca de aprendizaje automático llamada "PyFOIL" para realizar la inferencia de reglas.

# Importar la clase FOIL desde PyFOIL
from pyfoil import FOIL

# Definir datos de entrenamiento
# Cada instancia es una lista de características y la última entrada es la etiqueta de clase
data = [
    (['sunny', 'warm', 'normal', 'strong'], 'yes'),
    (['sunny', 'warm', 'high', 'strong'], 'yes'),
    (['cloudy', 'cold', 'high', 'strong'], 'no'),
    (['rainy', 'cold', 'high', 'strong'], 'no'),
    (['rainy', 'cold', 'normal', 'weak'], 'no')
]

# Definir las etiquetas de las características
feature_labels = ['outlook', 'temperature', 'humidity', 'wind']

# Definir el nombre de la etiqueta de clase
class_label = 'play'

# Crear una instancia de la clase FOIL con los datos de entrenamiento, etiquetas de características y etiqueta de clase
foil = FOIL(data, feature_labels, class_label)

# Ejecutar FOIL para inferir reglas
rules = foil.run()

# Imprimir las reglas inferidas
for rule in rules:
    print(rule)
