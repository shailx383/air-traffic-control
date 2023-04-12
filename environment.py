import random
import time
import numpy as np
import math
from agent import Aircraft
import parameters as p

class State:
    def __init__(self, d: int, rho: int, theta: int):
        self.d = d
        self.rho = rho
        self.theta = theta
class AirTrafficEnvironment:
    def __init__(self, num_planes, num_spawnpoints, num_destinations, lr, gamma, epsilon, thresh_distance = 50, load_q_table=False, num_obstacles = 0):
        self.num_planes = num_planes
        self.num_spawnpoints = num_spawnpoints
        self.num_destinations = num_destinations
        self.num_obstacles = num_obstacles
        self.lr = lr
        self.gamma = gamma
        self.e = epsilon
        self.thresh_distance = thresh_distance
        self.planes = []
    
    def compute_next_state(self, ownship: Aircraft, ownship_action: str, intruder: Aircraft, intruder_action: str):
        ownship.take_action(ownship_action)
        intruder.take_action(intruder_action)
        d = p.d(ownship, intruder)
        rho = p.rho(ownship, intruder)
        theta = p.theta(ownship, intruder)
        return State(d, rho, theta)
        
    # episodes may be short ?
    def generateEpisode(self, ownship: Aircraft, intruder: Aircraft, action_space: list):
        init_d = 50
        init_rho = ((np.arctan((intruder.pos['y'] - ownship.pos['y'])/
                         (intruder.pos['x'] - ownship.pos['x'])))* (180 / np.pi)) // 10
        init_theta = (intruder.angle - ownship.angle) // 10
        init_state = State(init_d, init_rho, init_theta)
        init_ownship_action = np.random.choice(action_space)
        intruder_action = np.random.choice(action_space)
        init_next_state = self.compute_next_state(ownship, init_ownship_action, intruder, intruder_action)
        
        # while (self.plane_distance(ownship, intruder) <= 50 and self.self.plane_distance(ownship, intruder) > 0):
            
        
        
        
        
        
        
        
        
        