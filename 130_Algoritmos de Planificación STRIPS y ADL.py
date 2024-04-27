# Miguel Angel Huerta Castillo     21310236

# Este programa implementa un planificador utilizando los algoritmos STRIPS y ADL.
# El programa permite definir acciones, estados iniciales y metas para encontrar un plan que lleve del estado inicial al estado objetivo.

class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name  # Nombre de la acción
        self.preconditions = preconditions  # Precondiciones de la acción
        self.effects = effects  # Efectos de la acción

class State:
    def __init__(self, predicates):
        self.predicates = predicates  # Predicados que describen el estado

def strips(state, goal, actions):
    plan = []  # Plan inicialmente vacío

    while not all(goal_predicate in state.predicates for goal_predicate in goal.predicates):
        applicable_actions = [action for action in actions if all(precondition in state.predicates for precondition in action.preconditions)]
        chosen_action = applicable_actions[0]  # Escoge la primera acción aplicable (puede haber múltiples)

        plan.append(chosen_action)  # Añade la acción al plan
        state.predicates = [predicate for predicate in state.predicates if predicate not in chosen_action.effects] + chosen_action.effects  # Actualiza el estado

    return plan

# Ejemplo práctico
if __name__ == "__main__":
    # Definición de acciones
    action1 = Action("Ir_al_supermercado", ["Estoy_en_casa"], ["Estoy_en_supermercado"])
    action2 = Action("Comprar_comestibles", ["Estoy_en_supermercado"], ["Tengo_comida"])
    action3 = Action("Cocinar", ["Tengo_comida", "Estoy_en_casa"], ["Tengo_comida_cocinada"])

    # Estado inicial
    initial_state = State(["Estoy_en_casa"])

    # Estado objetivo
    goal_state = State(["Tengo_comida_cocinada"])

    # Lista de acciones disponibles
    actions = [action1, action2, action3]

    # Planificación usando STRIPS
    plan = strips(initial_state, goal_state, actions)

    # Impresión del plan
    print("Plan generado:")
    for action in plan:
        print(action.name)
