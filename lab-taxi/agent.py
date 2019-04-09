import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6, alpha=.15, gamma=.9, eps_start=.5):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.alpha = alpha
        self.gamma = gamma
        self.eps_start = eps_start
        self.i_episode = 1
        
    def _get_target(self, next_state):
        policy_s = self._get_epsilon_greedy_probs(next_state)         
        return np.dot(self.Q[next_state], policy_s)    
        
        
    def _update_Q(self, state, action, next_state, reward):
        return self.Q[state][action] + (self.alpha * (reward + (self.gamma * self._get_target(next_state) - self.Q[state][action])))
    
                                        
    def _get_epsilon_greedy_probs(self, state):
        """
        Get epsilon-greedy probabilities
        """
        epsilon = self.eps_start/self.i_episode
        probs = np.ones(self.nA)*epsilon/self.nA
        probs[np.argmax(self.Q[state])] += 1 - epsilon

        return probs
    

    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        policy_s = self._get_epsilon_greedy_probs(state)
        action = np.random.choice(np.arange(self.nA), p=policy_s)
        return action

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        if not done:
            self.i_episode += 1
        self.Q[state][action] = self._update_Q(state, action, next_state, reward)