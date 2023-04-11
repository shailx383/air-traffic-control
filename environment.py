import random
import time
import numpy as np
import math
import agent.Aircraft as Plane

class AirTrafficEnvironment:
    def __init__(self, num_planes, num_spawnpoints, num_destinations, lr, gamma, epsilon, load_q_table=False, num_obstacles = 0):
        self.num_planes = num_planes
        self.num_spawnpoints = num_spawnpoints
        self.num_destinations = num_destinations
        self.num_obstacles = num_obstacles
        self.lr = lr
        self.gamma = gamma
        self.e = epsilon
        self.planes = []
        
    def generateEpisode(self, ownship: Plane, intruder: Plane, action_space: list):
        init_d = 50
        init_rho = ((np.arctan((self.intruder.pos['y'] - self.ownship.pos['y'])/
                         (self.intruder.pos['x'] - self.ownship.pos['x'])))* (180 / np.pi)) // 10
        init_theta = (self.intruder.angle - self.ownship.angle) // 10
        episode = [{'d': init_d, 'rho': init_rho, 'theta': init_theta}]
        
        
        
        
        
        