import numpy as np

from agent import Aircraft
import parameters as p

class State:
    def __init__(self, d: int, rho: int, theta: int):
        self.d = d
        self.rho = rho
        self.theta = theta
        
class TimeStep:
    def __init__(self, s: State, a: str, r: float, s_: State, a_: str):
        self.s = s
        self.a = a
        self.r = r
        self.s_ = s_
        self.a_ = a_
        
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
    
    def compute_reward(self, ownship: Aircraft, intruder: Aircraft, destination: dict):
        intruder_reward = - (self.thresh_distance ** 2 - p.d(ownship, intruder) ** 2) / (self.thresh_distance ** 2 / 500)
        destination_reward = 100 - np.sqrt((ownship.pos['x'] - destination['x']) ** 2 + (ownship.pos['y'] - destination['y']) ** 2)
        return intruder_reward + destination_reward
    
     
    # # episodes may be short ?
    # def generateEpisode(self, ownship: Aircraft, intruder: Aircraft, action_space: list):
    #     init_d = 50
    #     init_rho = ((np.arctan((intruder.pos['y'] - ownship.pos['y'])/
    #                      (intruder.pos['x'] - ownship.pos['x'])))* (180 / np.pi)) // 5
    #     init_theta = (intruder.angle - ownship.angle) // 5
    #     init_state = State(init_d, init_rho, init_theta) # s
    #     init_ownship_action = np.random.choice(action_space) # a
    #     init_intruder_action = np.random.choice(action_space)
    #     init_next_state = self.compute_next_state(ownship, init_ownship_action, intruder, init_intruder_action) # s_
    #     init_reward = self.compute_reward(ownship, intruder, ownship.airport) # r
    #     init_next_ownship_action = np.random.choice(action_space) # a_
    #     timestep1 = TimeStep(init_state, init_ownship_action, init_reward, init_next_state, init_next_ownship_action)
    #     init_next_intruder_action = np.random.choice(action_space)
        
    #     episode = [timestep1]
        
    #     # while (p.d(ownship, intruder) <= 50 and p.d(ownship, intruder) > 0):
    
    
            
        
        
        
        
        
        
        
        
        