import pickle

with open('2offline_q_table.pkl', 'rb') as f: 
    qtable = pickle.load(f)
    print(len(qtable))