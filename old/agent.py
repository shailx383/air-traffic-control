import numpy as np
import pandas as pd
from environment import State

class Aircraft:
    def __init__(self, name, pos, angle, destination, speed = 3):
        self.name = name
        self.airport = destination
        self.pos = pos
        self.speed = speed
        # angle of plane w.r.t positive x-axis
        self.angle = angle
    
    def _move(self):
        real_angle = int((10 * self.angle) * (np.pi/180))
        self.pos['x'] += int(self.speed * np.cos(real_angle))
        self.pos['y'] += int(self.speed * np.sin(real_angle))
    
    def _rotate(self, rot_angle: int):
        '''
        - for clockwise, + for anticlockwise
        '''
        real_rot_angle = rot_angle // 5
        self.angle += real_rot_angle
        if self.angle > 35:
            self.angle -= 36    
    
    def take_action(self, action: str):
        if action == "S":
            self.move()   
        elif action == "HL":
            self.rotate(90)
            self.move()
        elif action == "HR":
            self.rotate(-90)
            self.move()
        elif action == "ML":
            self.rotate(45)
            self.move()
        elif action == "MR":
            self.rotate(-45)
            self.move()
        else:
            pass



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
    
    # def get_curr_state(self) -> State:
    #     d = int(np.sqrt((self.ownship.pos['x'] - self.intruder.pos['x'])**2 + 
    #                     (self.ownship.pos['y'] - self.intruder.pos['y'])**2))
    #     rho = ((np.arctan((self.intruder.pos['y'] - self.ownship.pos['y'])/
    #                      (self.intruder.pos['x'] - self.ownship.pos['x'])))* (180 / np.pi)) // 5
    #     theta = (self.intruder.angle - self.ownship.angle) // 5
    #     state = State(d, rho, theta)
    #     return state
    
    
    
    # def choose_action(self, observation):
    #     self.check_state_exist()
        
        
    
    
        
        
        