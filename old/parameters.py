import numpy as np

from agent import Aircraft

def rho(ownship: Aircraft, intruder: Aircraft) -> int:
    return (((np.arctan((intruder.pos['y'] - ownship.pos['y'])/(intruder.pos['x'] - ownship.pos['x'])))* (180 / np.pi))) // 5

def theta(ownship: Aircraft, intruder: Aircraft) -> int:
    return (intruder.angle - ownship.angle) // 5

def d(ownship: Aircraft, intruder: Aircraft) -> int:
    return int(np.sqrt((ownship.pos['x'] - intruder.pos['x'])**2 + 
                        (ownship.pos['y'] - intruder.pos['y'])**2))