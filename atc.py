import random
import math
import conf
from utility import *
import numpy as np
import pandas as pd
import pickle
import os

class State:
    def __init__(self,oloc,ohead,iloc,ihead):
        self.oloc = oloc
        self.ohead = ohead
        self.iloc = iloc
        self.ihead = ihead
    
    def __hash__(self) -> int:
        return self.rho()*10000 + self.theta()*100 + self.dist() 

    def rho(self):
        return int((( (np.arctan((self.iloc[1] - self.oloc[1])/(self.iloc[0] - self.oloc[0]) )* (180 / np.pi)) +360  )%360)// 10)
    
    def theta(self):
        return int((((self.ihead - self.ohead)+360)%360) // 10)
    
    def dist(self):
        return int(np.sqrt((self.iloc[0] - self.oloc[0])**2 + (self.iloc[1] - self.oloc[1])**2))

class RandomAgent:
    def __init__(self):
        self.actions = [-90,-45,0,45,90]

    def take_action(self):
        return random.choice(self.actions)
    
class NormalAgent:
    def __init__(self):
        self.actions = [-90,-45,0,45,90]

    def take_action(self):
        return 0
    
class SarsaAgent:
    def __init__(self, load_q_table = None, learning_rate = 0.01, discount_factor = 0.9, epsilon = 0.1):
        self.actions = [-90,-45,0,45,90]
        # self.actionnames = ["state","hl",'ml','n','mr','hr']
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon
        self.Q_table = {}
        if os.path.exists('offline_q_table.pkl'):
            with open('offline_q_table.pkl', 'rb') as f:
                self.Q_table = pickle.load(f)

    def take_action(self,state):
        # self.check_state_exist(state)
        if state not in self.Q_table.keys():
            self.Q_table[state] = [0]* 5
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        else:
            # print(self.Q_table.index)
            # print(self.Q_table)
            # state_index = self.Q_table.index[self.Q_table['state'] == state]
            
            # print(state_index)
            state_action_values = self.Q_table[state]
            shuffled_values = list(enumerate(state_action_values))
            random.shuffle(shuffled_values)
            l = [j for (i,j) in shuffled_values]
            best_action_value_index = [i for (i,j) in shuffled_values][l.index(max(l))]
            best_action = 45*(best_action_value_index-2)
            # state_action = np.max(np.random.permutation(np.array(state_action)))
            return best_action

    # def check_state_exist(self,state):
    #     if state not in self.Q_table.index:
    #         self.Q_table = pd.concat([self.Q_table, pd.Series([state]+
    #                 [0]*len(self.actions),index=self.Q_table.columns,name = state,
    #             )] , axis = 1
    #         )


    def learn(self,s,a,r,s_,a_):
        q_predict = self.Q_table[hash(s)][self.actions.index(a)]
        if not self.isTerminal(s):
            q_target = r + self.gamma * self.Q_table[hash(s_)][self.actions.index(a_)]
        
        else:
            q_target = r
        self.Q_table[hash(s)][self.actions.index(a)] += self.lr * (q_target - q_predict)

    def next_state(self,s,a):
        s.ohead += 360 + a
        s.ohead %= 360
        s.oloc = self.nextLoc(s.oloc,s.ohead)
        s.iloc = self.nextLoc(s.iloc,s.ihead)
        return s

    def update(self,oloc,ohead,iloc,ihead,dest):
        self.dest = dest
        radius = (3 * conf.get()['aircraft']['collision_radius']) ** 2 
        s = State(oloc,ohead,iloc,ihead)
        a = self.take_action(hash(s))
        s_ = s
        s_= self.next_state(s_,a)
        r = -(radius**2 - s.dist()**2)/(radius**2 //500) 
        a_ = self.take_action(hash(s_))
        self.learn(s,a,r,s_,a_)
        return a

    def nextLoc(self, location, heading):
        speed = conf.get()['aircraft']['speed_default']
        x_diff = (speed / conf.get()['aircraft']['speed_scalefactor']) * math.sin(math.radians(heading))
        y_diff = -(speed / conf.get()['aircraft']['speed_scalefactor']) * math.cos(math.radians(heading))
        location = (location[0] + x_diff, location[1] + y_diff)
        return location
    
    def isTerminal(self, state):
        location = state.oloc
        speed = conf.get()['aircraft']['speed_default']
        if Utility.locDistSq(location, self.dest) < ((speed/conf.get()['aircraft']['speed_scalefactor']) ** 2):
            return True
        else:
            return False