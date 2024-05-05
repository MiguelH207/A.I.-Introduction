# Miguel Angel Huerta Castillo     21310236
# Este programa muestra un ejemplo de tratamiento lógico del lenguaje utilizando análisis sintáctico.
# Toma una oración como entrada y realiza un análisis sintáctico para identificar los sustantivos y verbos presentes en la oración.

import nltk  # Importa la librería NLTK (Natural Language Toolkit) para procesamiento del lenguaje natural

nltk.download('punkt')  # Descarga los datos necesarios para tokenización

from nltk.tokenize import word_tokenize  # Importa la función word_tokenize de NLTK para tokenizar las palabras

# Definición de la función para realizar el análisis sintáctico
def analisis_sintactico(oracion):
    tokens = word_tokenize(oracion)  # Tokeniza la oración en palabras individuales
    tagged = nltk.pos_tag(tokens)  # Etiqueta gramaticalmente cada palabra en la oración
    
    sustantivos = []  # Lista para almacenar los sustantivos
    verbos = []  # Lista para almacenar los verbos
    
    for palabra, etiqueta in tagged:  # Itera sobre cada palabra y su etiqueta gramatical
        if etiqueta.startswith('NN'):  # Si la etiqueta gramatical indica un sustantivo
            sustantivos.append(palabra)  # Agrega la palabra a la lista de sustantivos
        elif etiqueta.startswith('VB'):  # Si la etiqueta gramatical indica un verbo
            verbos.append(palabra)  # Agrega la palabra a la lista de verbos
    
    return sustantivos, verbos  # Devuelve las listas de sustantivos y verbos

# Ejemplo de uso
oracion_ejemplo = "El gato corre rápidamente hacia la puerta."  # Define una oración de ejemplo
sustantivos_ejemplo, verbos_ejemplo = analisis_sintactico(oracion_ejemplo)  # Realiza el análisis sintáctico

print("Sustantivos:", sustantivos_ejemplo)  # Imprime los sustantivos encontrados en la oración
print("Verbos:", verbos_ejemplo)  # Imprime los verbos encontrados en la oración
