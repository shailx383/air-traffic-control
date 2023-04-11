import numpy as np
import random
import pandas as pd

print(np.pi)

class Aircraft:
    def __init__(self, name, pos, angle):
        self.name = name
        
        self.pos = pos
        
        # angle of plane w.r.t positive x-axis
        self.angle = angle
        

# outside funcs: update_env after action taken by ownship and intruder

# environment provides the episodes 

# def episodeGeneration(ownship: Aircraft, intruder: Aircraft):
#     init_state = 

class CollisionAgent:
    def __init__(self, action_space, lr, gamma, epsilon, ownship, intruder):
        self.actions = action_space
        self.lr = lr
        self.gamma = gamma
        self.e = epsilon
        self.ownship = ownship
        self.intruder = intruder
        self.q_table = pd.DataFrame(columns=self.actions)
    
    def check_state_exist(self, state):
        if state not in self.q_table.index:
            self.q_table.append(pd.Series([0]*len(self.actions), index=self.q_table.colums, name = state))
    
    def get_curr_state(self):
        d = int(np.sqrt((self.ownship.pos['x'] - self.intruder.pos['x'])**2 + 
                        (self.ownship.pos['y'] - self.intruder.pos['y'])**2))
        rho = ((np.arctan((self.intruder.pos['y'] - self.ownship.pos['y'])/
                         (self.intruder.pos['x'] - self.ownship.pos['x'])))* (180 / np.pi)) // 10
        theta = (self.intruder.angle - self.ownship.angle) // 10
        return {
            'd': d,
            'rho': rho,
            'theta': theta
        }
    
    
    
    # def choose_action(self, observation):
    #     self.check_state_exist()
        
        
    
    
        
        
        