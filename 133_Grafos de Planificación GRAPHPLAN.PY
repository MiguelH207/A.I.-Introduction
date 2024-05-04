# Miguel Angel Huerta Castillo     21310236

# Este programa implementa el algoritmo GRAPHPLAN para la planificación en inteligencia artificial.
# Se utiliza un ejemplo práctico de planificación para ilustrar su funcionamiento.

from itertools import combinations

class GraphPlan:
    def __init__(self, initial_state, goal_state, operators):
        self.initial_state = initial_state  # Almacena el estado inicial del problema
        self.goal_state = goal_state  # Almacena el estado objetivo del problema
        self.operators = operators  # Almacena los operadores disponibles para modificar el estado

    def graph_plan(self):
        graph = [([], self.initial_state)]  # Crea el grafo de planificación inicial con el estado inicial
        while True:
            # Genera una nueva capa en el grafo de planificación
            new_layer = self.expand_graph(graph[-1][1])
            # Si la capa actual ya contiene el estado objetivo, se ha encontrado un plan
            if self.goal_state in new_layer:
                return self.extract_solution(graph)
            # Si se repite alguna capa, indica que no es posible alcanzar el estado objetivo
            if new_layer in graph:
                return None
            graph.append(([], new_layer))  # Agrega la nueva capa al grafo de planificación

    def expand_graph(self, previous_layer):
        new_layer = set()  # Inicializa la nueva capa como un conjunto vacío
        for operator in self.operators:
            # Intenta aplicar cada operador a cada combinación de estados en la capa anterior
            for combo in combinations(previous_layer, len(operator.preconditions)):
                if all(precondition in combo for precondition in operator.preconditions):
                    # Si todas las precondiciones del operador se cumplen, agrega el resultado a la nueva capa
                    new_layer.update(operator.apply(combo))
        return new_layer

    def extract_solution(self, graph):
        solution = []  # Inicializa la lista de acciones como vacía
        for i in range(len(graph) - 1, 0, -1):
            previous_layer, current_layer = graph[i - 1], graph[i]
            # Encuentra la diferencia entre las capas actual y anterior
            added = current_layer[1] - previous_layer[1]
            # Encuentra los operadores que produjeron la diferencia y los agrega a la solución
            for operator in previous_layer[0]:
                if operator.apply(()) in added:
                    solution.append(operator)
        return solution

class Operator:
    def __init__(self, name, preconditions, effects):
        self.name = name  # Nombre del operador
        self.preconditions = preconditions  # Precondiciones del operador
        self.effects = effects  # Efectos del operador

    def apply(self, state):
        # Aplica el operador al estado actual y devuelve el nuevo estado
        return state.union(self.effects)

# Ejemplo de uso del algoritmo GRAPHPLAN

# Definición del estado inicial, estado objetivo y operadores del problema
initial_state = {'A', 'B'}
goal_state = {'C'}
operators = [
    Operator('Op1', {'A'}, {'B'}),
    Operator('Op2', {'B'}, {'A'}),
    Operator('Op3', {'A', 'B'}, {'C'})
]

# Creación del objeto GraphPlan con los parámetros definidos
planner = GraphPlan(initial_state, goal_state, operators)

# Obtención del plan mediante el algoritmo GraphPlan
plan = planner.graph_plan()

# Imprime el plan encontrado, si existe
if plan:
    print("Plan encontrado:")
    for operator in plan:
        print(operator.name)
else:
    print("No se encontró un plan para alcanzar el estado objetivo.")
