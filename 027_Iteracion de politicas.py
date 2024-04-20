import numpy as np
import gym

def policy_iteration(env, gamma=1.0):
    nS = env.observation_space.n  # Obtenemos el número de estados
    nA = env.action_space.n  # Obtenemos el número de acciones
    policy = np.ones([nS, nA]) / nA  # Inicializamos una política aleatoria uniforme
    while True:
        V = policy_evaluation(env, policy, gamma)
        new_policy = policy_improvement(env, V, gamma)
        if (new_policy == policy).all():
            break
        policy = new_policy
    return policy

def policy_evaluation(env, policy, gamma=1.0, theta=1e-8):
    nS = env.observation_space.n  # Obtenemos el número de estados
    V = np.zeros(nS)
    while True:
        delta = 0
        for s in range(nS):
            v = 0
            for a, action_prob in enumerate(policy[s]):
                for prob, next_state, reward, done in env.P[s][a]:
                    v += action_prob * prob * (reward + gamma * V[next_state])
            delta = max(delta, np.abs(v - V[s]))
            V[s] = v
        if delta < theta:
            break
    return V

def policy_improvement(env, V, gamma=1.0):
    nS = env.observation_space.n  # Obtenemos el número de estados
    nA = env.action_space.n  # Obtenemos el número de acciones
    policy = np.zeros([nS, nA])
    for s in range(nS):
        action_values = np.zeros(nA)
        for a in range(nA):
            for prob, next_state, reward, done in env.P[s][a]:
                action_values[a] += prob * (reward + gamma * V[next_state])
        best_action = np.argmax(action_values)
        policy[s][best_action] = 1.0
    return policy

env = gym.make('FrozenLake-v1')

optimal_policy = policy_iteration(env)

print("Política óptima:")
print(optimal_policy)
