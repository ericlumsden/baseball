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
u_all, sig_all, v_all = np.linalg.svd(all_array[:, 12:].astype(float))
u_trunc, sig_trunc, v_trunc = np.linalg.svd(statcast_array[:, 12:].astype(float))

# Now, will make lists of the sigma values for the two approaches to graph and compare
s_all_running_count = 0
s_all_list = []
for s in sig_all:
    s_all_running_count += s
    s_all_list.append(s_all_running_count / np.sum(sig_all))

s_trunc_running_count = 0
s_trunc_list = []
for s in sig_trunc:
    s_trunc_running_count += s
    s_trunc_list.append(s_trunc_running_count / np.sum(sig_trunc))

plt.figure(1)
plt.plot(range(len(s_all_list)), s_all_list, c='k', label='All Players')
plt.plot(range(len(s_trunc_list)), s_trunc_list, c='r', label='Truncated Players')
plt.xlabel('s#')
plt.ylabel('% variance explained')
plt.title('comparing % variance')
plt.legend()

# Now, I want to look at the scatters of each projection
V_r_all = v_all[:,:2]
V_r_trunc = v_trunc[:,:2]

a_all = np.matmul(all_array[:,12:].astype(float), V_r_all)
a_trunc = np.matmul(statcast_array[:,12:].astype(float), V_r_trunc)

plt.figure(2)
plt.plot(a_all[:,0], a_all[:,1], '.k')

plt.figure(3)
plt.plot(a_trunc[:,0], a_trunc[:,1], '.k')

plt.show()