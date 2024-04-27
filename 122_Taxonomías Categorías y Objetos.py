# Miguel Angel Huerta Castillo     21310236
# Programa para representar el conocimiento usando taxonomías: categorías y objetos.
# Este programa define una estructura de datos para representar categorías y objetos dentro de esas categorías.

# Definición de la clase Categoría
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la categoría
        self.objetos = []     # Lista para almacenar los objetos pertenecientes a esta categoría

# Definición de la clase Objeto
class Objeto:
    def __init__(self, nombre, categoria):
        self.nombre = nombre        # Nombre del objeto
        self.categoria_pertenencia = categoria  # Categoría a la que pertenece el objeto

# Función para imprimir la taxonomía
def imprimir_taxonomia(categorias):
    for categoria in categorias:  # Iterar sobre cada categoría
        print("Categoría:", categoria.nombre)  # Imprimir el nombre de la categoría
        for objeto in categoria.objetos:  # Iterar sobre cada objeto en la categoría
            print("  -", objeto.nombre)   # Imprimir el nombre del objeto

# Función principal
def main():
    # Crear algunas categorías
    categoria_animales = Categoria("Animales")
    categoria_frutas = Categoria("Frutas")
    
    # Crear algunos objetos y asignarlos a las categorías correspondientes
    perro = Objeto("Perro", categoria_animales)
    gato = Objeto("Gato", categoria_animales)
    manzana = Objeto("Manzana", categoria_frutas)
    platano = Objeto("Plátano", categoria_frutas)
    
    # Agregar objetos a sus categorías respectivas
    categoria_animales.objetos.append(perro)
    categoria_animales.objetos.append(gato)
    categoria_frutas.objetos.append(manzana)
    categoria_frutas.objetos.append(platano)
    
    # Crear una lista de categorías
    taxonomia = [categoria_animales, categoria_frutas]
    
    # Imprimir la taxonomía
    imprimir_taxonomia(taxonomia)

# Llamada a la función principal
if __name__ == "__main__":
    main()
