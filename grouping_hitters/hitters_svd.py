import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
seaborn.set(style='ticks')

# First, load in the csv files as two separate dataframes
df_all = pd.read_csv('./data/statcast_clean_ALLHITTERS.csv', index_col=0)
df_statcast = pd.read_csv('./data/statcast_clean_TRUNCATED.csv', index_col=0)

# Then, select the columns I'll be using for SVD
all_list = ['Name', 'R', '2B', '3B', 'HR', 'BB', 'IBB', 'SO', 'BA', 'OBP', 'SLG', 'OPS', 'bbType_flyBall', 'bbType_groundBall', 'bbType_lineDrive', 'bbType_popUp', '2BperPA', '3BperPA', 'HRperPA', 'BBperPA', 'IBBperPA', 'SOperPA']
df_all = df_all[all_list]

statcast_list_median = all_list + ['launch_speed_median','launch_angle_median']
statcast_list_mean = all_list + ['launch_speed_mean','launch_angle_mean']
df_trunc_median = df_statcast[statcast_list_median]
df_trunc_mean = df_statcast[statcast_list_mean]

# Then convert those selected dataframes to arrays
all_array = df_all.to_numpy()
statcast_array_median = df_trunc_median.to_numpy()
statcast_array_mean = df_trunc_mean.to_numpy()

# Then run the SVDs! Just on the columns 12+ (bbType_flyBall onward)
u_all, sig_all, v_all = np.linalg.svd(all_array[:, 12:].astype(float))
u_median, sig_median, v_median = np.linalg.svd(statcast_array_median[:, 12:].astype(float))
u_mean, sig_mean, v_mean = np.linalg.svd(statcast_array_mean[:, 12:].astype(float))

# Now, will make lists of the sigma values for the two approaches to graph and compare
s_all_running_count = 0
s_all_list = []
for s in sig_all:
    s_all_running_count += s
    s_all_list.append(s_all_running_count / np.sum(sig_all))

s_trunc_median_count = 0
s_trunc_median_list = []
for s in sig_median:
    s_trunc_median_count += s
    s_trunc_median_list.append(s_trunc_median_count / np.sum(sig_median))

s_trunc_mean_count = 0
s_trunc_mean_list = []
for s in sig_mean:
    s_trunc_mean_count += s
    s_trunc_mean_list.append(s_trunc_mean_count / np.sum(sig_mean))

plt.figure(1)
plt.plot(range(len(s_all_list)), s_all_list, c='r', label='All Players')
plt.plot(range(len(s_trunc_median_list)), s_trunc_median_list, c='k', label='Truncated Players [median]')
plt.plot(range(len(s_trunc_mean_list)), s_trunc_mean_list, c='b', label='Truncated Players [mean]')
plt.xlabel('s#')
plt.ylabel('% variance explained')
plt.title('comparing % variance')
plt.legend()
plt.savefig('./figs/var_explained.png')

# Now, I want to look at the scatters of each projection
V_r_all = v_all[:,:4]
V_r_median = v_median[:,:4]
V_r_mean = v_mean[:,:4]

a_all = np.matmul(all_array[:,12:].astype(float), V_r_all)
a_median = np.matmul(statcast_array_median[:,12:].astype(float), V_r_median)
a_mean = np.matmul(statcast_array_mean[:,12:].astype(float), V_r_mean)

# Now make a new dataframe that has both the projection points and each player's OPS to be able to color based on OPS
a_all_df = pd.DataFrame(a_all[:, :2], columns=[1,2])
a_all_df['OPS'] = df_all['OPS']

a_median_df = pd.DataFrame(a_median[:, :2], columns=[1,2])
a_median_df['OPS'] = df_trunc_median['OPS']

a_mean_df = pd.DataFrame(a_mean[:, :2], columns=[1,2])
a_mean_df['OPS'] = df_trunc_mean['OPS']

# Add the first 4 projection columns to the respective dataframes (then be sure to save these as both csv and json files for later)
for x in range(4):
    df_all[f"p{x+1}"] = a_all[:,x]
    df_trunc_median[f"p{x+1}"] = a_median[:,x]
    df_trunc_mean[f"p{x+1}"] = a_mean[:,x]

df_all.to_csv('./data/statcast_clean_ALLHITTERS_projections.csv')
df_all.to_json('./data/statcast_clean_ALLHITTERS_projections.json')

df_trunc_median.to_csv('./data/statcast_clean_TRUNCATEDmedian.csv')
df_trunc_median.to_json('./data/statcast_clean_TRUNCATEDmedian.json')

df_trunc_mean.to_csv('./data/statcast_clean_TRUNCATEDmean.csv')
df_trunc_mean.to_json('./data/statcast_clean_TRUNCATEDmean.json')


plt.figure(2)
plt.plot(a_all[:,0], a_all[:,1], '.k')
plt.title('projection - all')
plt.xlabel('p1')
plt.ylabel('p2')
plt.savefig('./figs/projection_all.png')

plt.figure(3)
plt.plot(a_median[:,0], a_median[:,1], '.k')
plt.title('projection - median')
plt.xlabel('p1')
plt.xlabel('p1')
plt.ylabel('p2')
plt.savefig('./figs/projection_median.png')

plt.figure(4)
plt.plot(a_mean[:,0], a_mean[:,1], '.k')
plt.title('projection - mean')
plt.xlabel('p1')
plt.ylabel('p2')
plt.savefig('./figs/projection_mean.png')

plt.figure(5)
fig, ax = plt.subplots()
sc = ax.scatter(a_all_df[1], a_all_df[2], c=a_all_df['OPS'], cmap='copper')
fig.colorbar(sc, ax=ax)
ax.set_aspect('equal')
plt.title('projection - all')
plt.xlabel('p1')
plt.ylabel('p2')
plt.savefig('./figs/projection_all_heat.png')

plt.figure(6)
fig, ax = plt.subplots()
sc = ax.scatter(a_median_df[1], a_median_df[2], c=a_median_df['OPS'], cmap='copper')
fig.colorbar(sc, ax=ax)
ax.set_aspect('equal')
plt.title('projection - median')
plt.xlabel('p1')
plt.ylabel('p2')
plt.savefig('./figs/projection_median_heat.png')

plt.figure(7)
fig, ax = plt.subplots()
sc = ax.scatter(a_mean_df[1], a_mean_df[2], c=a_mean_df['OPS'], cmap='copper')
fig.colorbar(sc, ax=ax)
ax.set_aspect('equal')
plt.title('projection - median')
plt.xlabel('p1')
plt.ylabel('p2')
plt.savefig('./figs/projection_mean_heat.png')
plt.show()