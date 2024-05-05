# Miguel Angel Huerta Castillo 21310236
# Este programa implementa un analizador léxico simple en Python. 
# El análisis léxico es el proceso de convertir una secuencia de caracteres en una secuencia de tokens (palabras clave, identificadores, operadores, etc.) para un lenguaje de programación.

# Definición de tokens
tokens = {
    'suma': r'\+',
    'resta': r'-',
    'multiplicacion': r'\*',
    'division': r'/',
    'numero': r'\d+',
    'espacio': r'\s+',
}

# Importar módulo re para expresiones regulares
import re

# Función principal del analizador léxico
def analizador_lexico(entrada):
    # Inicializar lista para almacenar los tokens encontrados
    token_encontrados = []

    # Iterar sobre la entrada hasta que se consuma por completo
    while entrada:
        # Variable para mantener el token actual
        token_actual = None
        
        # Iterar sobre todos los tokens definidos
        for token, patron in tokens.items():
            # Intentar hacer coincidir el patrón con el inicio de la entrada
            coincidencia = re.match(patron, entrada)
            if coincidencia:
                # Si hay coincidencia, agregar el token a la lista y actualizar la entrada
                valor = coincidencia.group(0)
                token_encontrados.append((token, valor))
                entrada = entrada[len(valor):]
                break
        
        # Si no se encontró ningún token, hay un error léxico
        else:
            print("Error léxico: no se pudo reconocer el siguiente token:", entrada[0])
            return
        
    # Retornar la lista de tokens encontrados
    return token_encontrados

# Ejemplo de uso del analizador léxico
if __name__ == "__main__":
    # Entrada de ejemplo
    entrada = "3 + 4 * 5"

    # Llamar a la función del analizador léxico con la entrada dada
    tokens_encontrados = analizador_lexico(entrada)

    # Imprimir los tokens encontrados
    print("Tokens encontrados:")
    for token in tokens_encontrados:
        print(token)
