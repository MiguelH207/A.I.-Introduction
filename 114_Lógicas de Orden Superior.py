# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo práctico de lógica de orden superior en Python.
# Se utiliza la función filter() para filtrar elementos de una lista según cierto criterio definido por una función lambda.

# Definición de la función principal
def main():
    # Lista de números
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Filtrar los números pares utilizando la función filter() y una función lambda
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    # Imprimir los números pares
    print("Números pares:", even_numbers)

# Llamar a la función principal si este script es ejecutado directamente
if __name__ == "__main__":
    main()
