import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
AGENT_MAP = {
            'BEELINE': 0,
            'RANDOM': 1,
            'SARSA':  2,
            'Q-LEARNING': 3,
            'EXP SARSA':  4,
            'DQ-LEARNING': 5,
        }

def plot_performance(agent: str):
    log_df = pd.read_csv('visitorlog.csv')
    agent_log_df = log_df[log_df['agent'] == AGENT_MAP[agent]]
    x = agent_log_df['id']
    y = agent_log_df['score']
    plt.figure()
    plt.plot(x, y, 'r')
    plt.xlabel('Episode')
    plt.ylabel('Score')
    plt.title(agent)
    plt.savefig('plots/' + agent + '_performance.png')

plot_performance('BEELINE')
plot_performance('RANDOM')
plot_performance('SARSA')
plot_performance('Q-LEARNING')
plot_performance('EXP SARSA')
plot_performance('DQ-LEARNING')


def plot_compared_performance(agent1: str, agent2: str):
    log_df = pd.read_csv('visitorlog.csv')
    agent_log_df1 = log_df[log_df['agent'] == AGENT_MAP[agent1]]
    agent_log_df2 = log_df[log_df['agent'] == AGENT_MAP[agent2]]
    x1 = agent_log_df1['id']
    y1 = agent_log_df1['score']
    y2 = agent_log_df2['score']
    x2 = agent_log_df2['id']
    plt.figure()
    plt.plot(x1[:28], y1[:28], 'r', label = agent1)
    plt.plot(x1[:28], y2[:28], 'b', label = agent2)
    plt.legend()
    plt.xlabel('Episode')
    plt.ylabel('Score')
    plt.title(agent1 +' vs ' + agent2)
    plt.savefig('plots/' + agent1 +'_vs_' + agent2 + '_performance.png')

plot_compared_performance("SARSA", "DQ-LEARNING")
        