import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# First, load in the csv files as two separate dataframes
df_all = pd.read_csv('statcast_clean_ALLHITTERS.csv', index_col=0)
df_statcast = pd.read_csv('statcast_clean_TRUNCATED.csv', index_col=0)

# Then, select the columns I'll be using for SVD
all_list = ['Name', 'R', '2B', '3B', 'HR', 'BB', 'IBB', 'SO', 'BA', 'OBP', 'SLG', 'OPS', 'bbType_flyBall', 'bbType_groundBall', 'bbType_lineDrive', 'bbType_popUp', '2BperPA', '3BperPA', 'HRperPA', 'BBperPA', 'IBBperPA', 'SOperPA']
df_all = df_all[all_list]

statcast_list = all_list + ['launch_speed_median','launch_speed_mean','launch_angle_median','launch_angle_mean']
df_trunc = df_statcast[statcast_list]

# Then convert those selected dataframes to arrays
all_array = df_all.to_numpy()
statcast_array = df_trunc.to_numpy()

# Then run the SVDs! Just on the columns 12+ (bbType_flyBall onward)
u_all, sig_all, v_all = np.linalg.svd(df_all[:, 12:])
u_trunc, sig_trunc, v_trunc = np.linalg.svd(df_trunc[:, 12:])

plt.figure(0)
s_all_running_count = 0
x_count = 0
for s in sig_all:
    s_all_running_count += s
    x_count += 1
    plt.plot(x_count, s_all_running_count)

plt.figure(1)

plt.figure(2)
s_trunc_running_count = 0
x_count2 = 0
for s in sig_all:
    s_trunc_running_count += s
    x_count2 += 1
    plt.plot(x_count2, s_trunc_running_count)