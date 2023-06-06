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

def plot_performance(agent: str, steps: int, csv_path :str):
    log_df = pd.read_csv(csv_path)
    agent_log_df = log_df[log_df['agent'] == AGENT_MAP[agent]]
    y = agent_log_df['score']
    x = list(range(1, len(y)+1))
    plt.figure()
    avs = [sum(y[i - steps:i])/len(y[i-steps:i]) for i in range(steps, len(x), steps)]
    avs_x = [i for i in range(steps, len(x), steps)]
    plt.plot(avs_x, avs, 'b', label = 'Average')
    # plt.plot(x, y, 'r', label = agent)
    plt.xlabel('Episode')
    plt.ylabel('Score')
    plt.legend()
    plt.title('Performance of '+ agent +': '+str(len(x))+ ' episodes')
    plt.savefig('plots/' + agent + '_performance.png')

# plot_performance('BEELINE')
# plot_performance('RANDOM')
<<<<<<< Updated upstream
# plot_performance('SARSA', 750, 'visitorlog_s.csv')
# plot_performance('Q-LEARNING', 35, 'visitorlog_q.csv')
# plot_performance('EXP SARSA', 25, 'visitorlog_esarsa.csv')
# plot_performance('DQ-LEARNING', 5, 'log.csv')
=======
# plot_performance('SARSA')
plot_performance('Q-LEARNING')
# plot_performance('EXP SARSA')
# plot_performance('DQ-LEARNING')
>>>>>>> Stashed changes


def plot_compared_performance(agent1: str, agent2: str, steps: int, csv_path1: str, csv_path2: str):
    log_df1 = pd.read_csv(csv_path1)
    log_df2 = pd.read_csv(csv_path2)
    agent_log_df1 = log_df1[log_df1['agent'] == AGENT_MAP[agent1]]
    agent_log_df2 = log_df2[log_df2['agent'] == AGENT_MAP[agent2]]
    y1 = agent_log_df1['score']
    x1 = list(range(1, len(y1)+1))
    y2 = agent_log_df2['score']
    plt.figure()
    avs1 = [sum(y1[i - steps:i])/len(y1[i-steps:i]) for i in range(steps, len(x1), steps)]
    avs2 = [sum(y2[i - steps:i])/len(y2[i-steps:i]) for i in range(steps, len(x1), steps)]
    avs_x = [i for i in range(steps, len(x1), steps)]
    plt.plot(avs_x, avs1, 'r', label = agent1)
    plt.plot(avs_x, avs2, 'b', label = agent2)
    plt.legend()
    plt.xlabel('Episode')
    plt.ylabel('Score')
    plt.title('Performance of '+ agent1 +' vs ' + agent2 + ': ' + str(len(x1))+ ' episodes')
    plt.savefig('plots/' + agent1 +'_vs_' + agent2 + '_performance.png')

<<<<<<< Updated upstream
# plot_compared_performance("EXP SARSA", "SARSA", 150, 'visitorlog_esarsa_new.csv', 'visitorlog_sarsa_new.csv')
        
def triple_plot_compared_performance(agent1: str, agent2: str, agent3: str, steps: int, csv_path1: str, csv_path2: str, csv_path3: str):
    log_df1 = pd.read_csv(csv_path1)
    log_df2 = pd.read_csv(csv_path2)
    log_df3 = pd.read_csv(csv_path3)
    agent_log_df1 = log_df1[log_df1['agent'] == AGENT_MAP[agent1]]
    agent_log_df2 = log_df2[log_df2['agent'] == AGENT_MAP[agent2]]
    agent_log_df3 = log_df3[log_df3['agent'] == AGENT_MAP[agent3]]
    y1 = agent_log_df1['score']
    y2 = agent_log_df2['score']
    y3 = agent_log_df3['score']
    x1 = list(range(1, min(len(y1), len(y2), len(y3))+1))
    plt.figure()
    avs1 = [sum(y1[i - steps:i])/len(y1[i-steps:i]) for i in range(steps, len(x1), steps)]
    avs2 = [sum(y2[i - steps:i])/len(y2[i-steps:i]) for i in range(steps, len(x1), steps)]
    avs3 = [sum(y3[i - steps:i])/len(y3[i-steps:i]) for i in range(steps, len(x1), steps)]
    avs_x = [i for i in range(steps, len(x1), steps)]
    plt.plot(avs_x, avs1, 'r', label = agent1)
    plt.plot(avs_x, avs2, 'b', label = agent2)
    plt.plot(avs_x, avs3, 'y', label = agent3)
    plt.legend()
    plt.xlabel('Episode')
    plt.ylabel('Score')
    plt.title('Performance of '+ agent1 +' vs ' + agent2 +' vs ' + agent3 + ': ' + str(len(x1))+ ' episodes')
    plt.savefig('plots/' + agent1 +'_vs_' + agent2 + '_vs_' + agent3 + '_performance.png')

# triple_plot_compared_performance("SARSA", "EXP SARSA", "RANDOM", 35, 'visitorlog_s.csv', 'visitorlog_e.csv', 'visitorlog.csv')

def time_plots(agent: str, csv_path: str, steps: int):
    log_df = pd.read_csv(csv_path)
    agent_df = log_df[log_df['agent'] == AGENT_MAP[agent]]
    y1 = agent_df['score']
    y2 = agent_df['time']
    x = list(range(1, len(y1)+1))
    avs1 = [sum(y1[i - steps:i])/len(y1[i-steps:i]) for i in range(steps, len(x), steps)]
    avs2 = [sum(y2[i - steps:i])/len(y2[i-steps:i]) for i in range(steps, len(x), steps)]
    avs_x = [i for i in range(steps, len(x), steps)]
    plt.figure()
    plt.plot(avs_x, avs1, 'r', label = agent)
    plt.plot(avs_x, avs2, 'b', label = 'Time per episode')
    plt.legend()
    plt.xlabel('Episode')
    plt.ylabel('Score/Time')
    plt.savefig('plots/timeplot_'+agent+'.png')

# time_plots("SARSA", 'visitorlog_s.csv', 10)
    
def f(csv_path):
    df = pd.read_csv(csv_path)
    df['agent'] = 5
    df.to_csv('test.csv')
    
# f('visitorlog_dq.csv')

def all_plot(steps):
    log_df0 = pd.read_csv('visitorlog.csv')
    log_df1 = pd.read_csv('visitorlog.csv')
    log_df2 = pd.read_csv('visitorlog_s.csv')
    log_df3 = pd.read_csv('visitorlog_q.csv')
    log_df4 = pd.read_csv('visitorlog_e.csv')
    log_df5 = pd.read_csv('test.csv')
    agent_log_df0 = log_df0[log_df0['agent'] == 0]
    agent_log_df1 = log_df1[log_df1['agent'] == 1]
    agent_log_df2 = log_df2[log_df2['agent'] == 2]
    agent_log_df3 = log_df3[log_df3['agent'] == 3]
    agent_log_df4 = log_df4[log_df4['agent'] == 4]
    agent_log_df5 = log_df5[log_df5['agent'] == 5]
    print(len(agent_log_df0), len(agent_log_df1), len(agent_log_df2), len(agent_log_df3), len(agent_log_df4), len(agent_log_df5))
    y0 = agent_log_df0['score']
    y1 = agent_log_df1['score']
    y2 = agent_log_df2['score']
    y3 = agent_log_df3['score']
    y4 = agent_log_df4['score']
    y5 = agent_log_df5['score']
    x1 = list(range(1, min(len(y1), len(y0), len(y2), len(y3), len(y4), len(y5))+1))
    plt.figure()
    avs0 = [sum(y0[i - steps:i])/len(y0[i-steps:i]) for i in range(steps, len(x1), steps)]
    avs1 = [sum(y1[i - steps:i])/len(y1[i-steps:i]) for i in range(steps, len(x1), steps)]
    avs2 = [sum(y2[i - steps:i])/len(y2[i-steps:i]) for i in range(steps, len(x1), steps)]
    avs4 = [sum(y4[i - steps:i])/len(y4[i-steps:i]) for i in range(steps, len(x1), steps)]
    avs5 = [sum(y5[i - steps:i])/len(y5[i-steps:i]) for i in range(steps, len(x1), steps)]
    avs3 = [sum(y3[i - steps:i])/len(y3[i-steps:i]) for i in range(steps, len(x1), steps)]
    avs_x = [i for i in range(steps, len(x1), steps)]
    plt.plot(avs_x, avs0, 'r', label = 'BEELINE')
    plt.plot(avs_x, avs1, 'b', label = 'RANDOM')
    plt.plot(avs_x, avs2, 'g', label = 'SARSA')
    plt.plot(avs_x, avs3, 'y', label = 'Q-LEARNING')
    plt.plot(avs_x, avs4, 'c', label = 'EXP SARSA')
    plt.plot(avs_x, avs5, 'm', label = 'DQ-LEARNING')
    plt.legend()
    plt.xlabel('Episode')
    plt.ylabel('Score')
    plt.title('Performance of all agents: ' + str(len(x1))+ ' episodes')
    plt.savefig('plots/performance.png')
    
all_plot(100)
=======
# plot_compared_performance("SARSA", "RANDOM", 10)
        
>>>>>>> Stashed changes
