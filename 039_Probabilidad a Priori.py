# Importamos la función Counter del módulo collections
from collections import Counter

# Definimos una función llamada calcular_probabilidad_a_priori que toma una lista de datos como entrada
def calcular_probabilidad_a_priori(datos):
    # Contamos la frecuencia de cada elemento en los datos y almacenamos los resultados en un diccionario
    conteo_elementos = Counter(datos)
    
    # Calculamos el número total de datos
    total_datos = len(datos)
    
    # Creamos un diccionario para almacenar las probabilidades a priori de cada elemento
    probabilidades_a_priori = {}
    
    # Iteramos sobre cada elemento y su conteo en el diccionario de conteo_elementos
    for elemento, conteo in conteo_elementos.items():
        # Calculamos la probabilidad a priori del elemento dividiendo su frecuencia por el total de datos
        probabilidad = conteo / total_datos
        
        # Almacenamos la probabilidad a priori del elemento en el diccionario probabilidades_a_priori
        probabilidades_a_priori[elemento] = probabilidad
    
    # Devolvemos el diccionario de probabilidades a priori
    return probabilidades_a_priori

# Ejemplo de uso del programa
if __name__ == "__main__":
    # Creamos una lista de datos de ejemplo
    datos_ejemplo = ['A', 'B', 'A', 'C', 'A', 'B', 'D', 'A', 'C']
    
    # Calculamos las probabilidades a priori de los datos de ejemplo llamando a la función calcular_probabilidad_a_priori
    probabilidades = calcular_probabilidad_a_priori(datos_ejemplo)
    
    # Imprimimos las probabilidades a priori calculadas
    print("Probabilidades a priori:")
    for elemento, probabilidad in probabilidades.items():
        print(f"{elemento}: {probabilidad*100,"%"}")
