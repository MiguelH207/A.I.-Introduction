# Miguel Angel Huerta Castillo     21310236
# Este programa implementa un sistema de lógica de primer orden utilizando agentes lógicos en Python.
# Se crea un agente lógico que puede realizar operaciones como conjunción, disyunción, negación y condicional entre dos proposiciones lógicas.

class LogicalAgent:
    def __init__(self):
        pass  # Inicialización del agente lógico
    
    def conjunction(self, p, q):
        return p and q  # Función para la conjunción lógica
    
    def disjunction(self, p, q):
        return p or q  # Función para la disyunción lógica
    
    def negation(self, p):
        return not p  # Función para la negación lógica
    
    def conditional(self, p, q):
        return (not p) or q  # Función para la implicación lógica

# Ejemplo de uso del agente lógico
if __name__ == "__main__":
    agent = LogicalAgent()  # Crear una instancia del agente lógico
    
    # Definir dos proposiciones lógicas
    proposition1 = True
    proposition2 = False
    
    # Realizar operaciones lógicas utilizando el agente
    result_conjunction = agent.conjunction(proposition1, proposition2)  # Conjunción
    result_disjunction = agent.disjunction(proposition1, proposition2)  # Disyunción
    result_negation = agent.negation(proposition1)  # Negación
    result_conditional = agent.conditional(proposition1, proposition2)  # Implicación
    
    # Imprimir los resultados
    print("Conjunction:", result_conjunction)
    print("Disjunction:", result_disjunction)
    print("Negation:", result_negation)
    print("Conditional:", result_conditional)
