import pickle
import os

def main():
    Q_table = {}
    if os.path.exists("3offline_q_table.pkl"):
        with open("3offline_q_table.pkl", 'rb') as f:
            Q_table = pickle.load(f)
    print(len(Q_table))

if __name__ == "__main__":
    main()