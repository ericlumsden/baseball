import pandas as pd
import matplotlib.pyplot as plt

plate_hw = 0.71 #plate 1/2 width for defining strike zone horizontally (vertically will be done by batter sz_top and sz_bot)
df = pd.read_csv('unfilteredAtBats.csv')
df_hitters = pd.read_csv('redsox_batters.csv', names=['name', 'id'])

for index, row in df_hitters.iterrows():
    df_temp = df[df['batter'] == row['id']]
    num_abs = df_temp[(df_temp['balls'] == 0) & (df_temp['strikes'] == 0)]['index'].count() + 1
    fig, axs = plt.subplots(nrows=1, ncols=num_abs, sharex=True, sharey=True)
    count = 0
    sz_top_ls = []
    sz_bot_ls = []
    for index, row in df_temp.iterrows():
        # This is where I iterate over all of the pitches and add them to the appropriate at-bat
        if (row['strikes'] == 0) and (row['balls'] == 0):
            count += 1
        sz_top_ls.append(row['sz_top'])
        sz_bot_ls.append(row['sz_bot'])
        axs[count].scatter(row['plate_x'], row['plate_z'])
    sz_t = sum(sz_top_ls)/len(sz_top_ls)
    sz_b = sum(sz_bot_ls)/len(sz_bot_ls)
    for x in range(num_abs):
        axs[x].plot([plate_hw, plate_hw], (sz_b, sz_t), color='k', alpha=0.7)
        axs[x].plot([-plate_hw, -plate_hw], (sz_b, sz_t), color='k', alpha=0.7)
        axs[x].plot([-plate_hw, plate_hw], (sz_b, sz_b), color='k', alpha=0.7)
        axs[x].plot([-plate_hw, plate_hw], (sz_t, sz_t), color='k', alpha=0.7)
    
    plt.title(row.name)
    plt.savefig(f"{row.name}_ABs.png")