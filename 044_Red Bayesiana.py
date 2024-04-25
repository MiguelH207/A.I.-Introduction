# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un ejemplo de razonamiento probabilístico utilizando una Red Bayesiana.
# Se simula una red bayesiana simple para modelar la probabilidad condicional de que un estudiante pase o no un examen,
# dado su nivel de estudio y la dificultad del examen.

import numpy as np  # Importamos la librería numpy para trabajar con arreglos multidimensionales
from pgmpy.models import BayesianModel  # Importamos la clase BayesianModel de la librería pgmpy
from pgmpy.factors.discrete import TabularCPD  # Importamos la clase TabularCPD para definir distribuciones de probabilidad condicional

# Creamos un objeto de la clase BayesianModel que representa la red bayesiana
modelo = BayesianModel([('Dificultad', 'Examen'), ('Estudio', 'Examen')])

# Definimos las probabilidades condicionales para el nodo 'Dificultad'
cpd_dificultad = TabularCPD(variable='Dificultad', variable_card=2, values=[[0.6], [0.4]])

# Definimos las probabilidades condicionales para el nodo 'Estudio'
cpd_estudio = TabularCPD(variable='Estudio', variable_card=2, values=[[0.7], [0.3]])

# Definimos las probabilidades condicionales para el nodo 'Examen' basadas en 'Dificultad' y 'Estudio'
cpd_examen = TabularCPD(variable='Examen', variable_card=2,
                        values=[[0.9, 0.6, 0.8, 0.1],  # P(Examen=T|Dificultad=T, Estudio=T), P(Examen=T|Dificultad=T, Estudio=F)
                                [0.1, 0.4, 0.2, 0.9]],  # P(Examen=F|Dificultad=T, Estudio=T), P(Examen=F|Dificultad=T, Estudio=F)
                        evidence=['Dificultad', 'Estudio'],  # Las variables de las que dependen las probabilidades condicionales
                        evidence_card=[2, 2])  # El número de estados para cada variable de evidencia

# Añadimos las probabilidades condicionales al modelo
modelo.add_cpds(cpd_dificultad, cpd_estudio, cpd_examen)

# Verificamos si el modelo es válido
print("¿El modelo es válido?", modelo.check_model())

# Imprimimos la distribución de probabilidad condicional del nodo 'Examen'
print("Distribución de probabilidad condicional del nodo 'Examen':")
print(modelo.get_cpds('Examen'))

# Calculamos la probabilidad P(Examen=T|Estudio=T, Dificultad=T)
probabilidad = modelo.get_cpds('Examen').values[1, 1]
print("P(Examen=T|Estudio=T, Dificultad=T) =", probabilidad)
