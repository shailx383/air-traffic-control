import pickle
import os

def main():
    Q_table = {}
    if os.path.exists("4offline_q_table.pkl"):
        with open("4offline_q_table.pkl", 'rb') as f:
            Q_table = pickle.load(f)
    print(Q_table)

if __name__ == "__main__":
    main()