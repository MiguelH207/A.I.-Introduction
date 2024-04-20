# Importamos las bibliotecas necesarias
import pomdp_py
from pomdp_py.frameworks.pomdp import POMDP, State, Action, Observation
from pomdp_py.frameworks.transition_model import TransitionModel
from pomdp_py.frameworks.observation_model import ObservationModel
from pomdp_py.frameworks.reward_model import RewardModel

# Definimos el estado del mundo, que es la ubicación del robot.
class RobotState(State):
    def __init__(self, location):
        self.location = location

    def __hash__(self):
        return hash(self.location)

    def __eq__(self, other):
        return isinstance(other, RobotState) and self.location == other.location

# Definimos la acción del robot, que puede ser moverse en una dirección.
class RobotAction(Action):
    def __init__(self, direction):
        self.direction = direction

    def __hash__(self):
        return hash(self.direction)

    def __eq__(self, other):
        return isinstance(other, RobotAction) and self.direction == other.direction

# Definimos la observación del robot, que es una estimación de su ubicación.
class RobotObservation(Observation):
    def __init__(self, estimated_location):
        self.estimated_location = estimated_location

    def __hash__(self):
        return hash(self.estimated_location)

    def __eq__(self, other):
        return isinstance(other, RobotObservation) and self.estimated_location == other.estimated_location

# Definimos la transición de estado, que describe cómo el estado del mundo cambia con las acciones del robot.
class StateTransition(TransitionModel):
    def probability(self, next_state, state, action):
        # Aquí puedes definir cómo cambia el estado del mundo con las acciones del robot.
        return 1 if next_state.location == state.location + action.direction else 0

    def sample(self, state, action):
        # Aquí puedes definir una muestra de la próxima ubicación del robot dada su acción.
        return RobotState(state.location + action.direction)

# Definimos el modelo de observación, que describe cómo el robot observa el mundo.
class RobotObservationModel(ObservationModel):
    def probability(self, observation, next_state, action):
        # Aquí puedes definir cómo el robot observa el mundo.
        return 1 if observation.estimated_location == next_state.location else 0

    def sample(self, next_state, action):
        # Aquí puedes definir una muestra de la observación del robot dada su acción.
        return RobotObservation(next_state.location)

# Definimos la recompensa, que describe cuánto beneficio obtiene el robot por realizar una acción.
class RobotRewardModel(RewardModel):
    def get_reward(self, state, action):
        # Aquí puedes definir la recompensa que obtiene el robot por realizar una acción.
        return 1 if action.direction == (0, 1) else -1  # recompensa por moverse hacia arriba

# Finalmente, definimos el POMDP.
class GridRobotPOMDP(POMDP):
    def __init__(self):
        self.state_transition = StateTransition()
        self.observation_model = RobotObservationModel()
        self.reward_model = RobotRewardModel()
        self.gamma = 0.95  # factor de descuento