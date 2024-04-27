# Miguel Angel Huerta Castillo     21310236
# Este programa muestra cómo representar conocimiento utilizando ingeniería del conocimiento y ontologías en Python.
#Este programa utiliza la librería rdflib para representar conocimiento utilizando ingeniería del conocimiento y ontologías en Python. Define un grafo RDF (Resource Description Framework) donde se almacena una ontología simple con una tripleta sujeto-predicado-objeto. Luego, serializa el grafo en formato RDF/XML y lo guarda en un archivo llamado "ontologia.rdf".


# Importar la librería rdflib para trabajar con ontologías
from rdflib import Graph, Namespace, URIRef

# Crear un nuevo grafo para almacenar la ontología
g = Graph()

# Definir un namespace para la ontología
ns = Namespace("http://ejemplo.org/")

# Definir URIs para los recursos
sujeto = URIRef(ns + "Miguel")  # URI para el sujeto
predicado = URIRef(ns + "es")    # URI para el predicado
objeto = URIRef(ns + "ingeniero")  # URI para el objeto

# Agregar tripleta al grafo (sujeto, predicado, objeto)
g.add((sujeto, predicado, objeto))

# Serializar el grafo en formato RDF/XML y guardarlo en un archivo
g.serialize("ontologia.rdf", format="xml")
