import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import os
'''
It seems to me like the best way to do this is to find every first pitch in the subdivided dataframe,
divide the dataframe by the indices from between first pitches, including the first pitch of that at-bat,
then plot the scatter from that onto the subplots...
'''

plate_hw = 0.71 #plate 1/2 width for defining strike zone horizontally (vertically will be done by batter sz_top and sz_bot)
df = pd.read_csv('unfilteredAtBats.csv')
df.iloc[::-1] # the dataframe is from most to least recent pitch, so I want to reverse to better order the at-bats from game to game
df_hitters = pd.read_csv('redsox_batters.csv', names=['name', 'id'])
pitch_type_dict = {}
pitch_types = df['pitch_type'].unique()
cmap = cm.get_cmap('jet')
#colors = cmap.colors

for x in range(len(pitch_types)):
    pitch_type_dict[pitch_types[x]] = x
df['markers'] = df['pitch_type'].map(pitch_type_dict)

def multi_AB_game(num_abs, df_ex, name, date):
    start_AB = df[df['pitch_number'] == 1].index.tolist()
    fig, axs = plt.subplots(nrows=1, ncols=num_abs, sharex=True, sharey=True, figsize=(15,5))
    for n in range(len(start_AB)-1):
        df_ex_temp = df_ex.iloc[start_AB[n]:start_AB[n+1]]
        ax=axs[n].scatter(df_ex_temp['plate_x'], df_ex_temp['plate_z'], marker=df_ex_temp['markers'], cmap=cmap)
    df_ex_final = df_ex.iloc[start_AB[-1]:]
    ax=axs[num_abs].scatter(df_ex_final['plate_x'], df_ex_final['plate_z'], marker=df_ex_final['markers'], cmap=cmap)
    sz_t = (df_ex[sz_t].sum())/len(df_ex)
    sz_b = (df_ex[sz_b].sum())/len(df_ex)
    if (sz_t == 0) & (sz_b == 0):
        sz_t = 3.5
        sz_b = 1.5
    for x in range(num_abs):
        axs[x].plot([plate_hw, plate_hw], (sz_b, sz_t), color='k', alpha=0.7)
        axs[x].plot([-plate_hw, -plate_hw], (sz_b, sz_t), color='k', alpha=0.7)
        axs[x].plot([-plate_hw, plate_hw], (sz_b, sz_b), color='k', alpha=0.7)
        axs[x].plot([-plate_hw, plate_hw], (sz_t, sz_t), color='k', alpha=0.7)

    plt.title(f"{name}, {date}")
    fig.colorbar(ax, label="pitch_speed(mph)")
    plt.tight_layout()
    plt.savefig(f"./{name}_ABs/{date}.png", dpi=500)
        

def single_AB_game(df_ex, name, date):
    plt.figure(figsize=(15,5))
    sz_top_ls = []
    sz_bot_ls = []
    for index, row in df_ex.iterrows():
        ax=plt.scatter(row['plate_x'], row['plate_z'], marker=pitch_type_dict[row['pitch_type']], linewidths=4, c=row['release_speed'], cmap=cmap, label=f"{row['pitch_type']}")
    if (len(sz_top_ls) != 0) & (len(sz_bot_ls) != 0):
        sz_t = sum(sz_top_ls)/len(sz_top_ls)
        sz_b = sum(sz_bot_ls)/len(sz_bot_ls)
    else:
        sz_t = 3.5
        sz_b = 3.5
    plt.plot([plate_hw, plate_hw], (sz_b, sz_t), color='k', alpha=0.7)
    plt.plot([-plate_hw, -plate_hw], (sz_b, sz_t), color='k', alpha=0.7)
    plt.plot([-plate_hw, plate_hw], (sz_b, sz_b), color='k', alpha=0.7)
    plt.plot([-plate_hw, plate_hw], (sz_t, sz_t), color='k', alpha=0.7)

    plt.title(f"{name}, {date}")
    plt.colorbar(ax, label="pitch_speed(mph)")
    plt.tight_layout()
    plt.savefig(f"./{name}_ABs/{date}.png", dpi=500)

for index, row in df_hitters.iterrows():
    df_temp = df[df['batter'] == row['id']]
    batter_name = row['name']
    print(batter_name)
    batter_id = row.id
    game_dates = df_temp['game_date'].unique()
    print(game_dates)
    os.makedirs(f"./{batter_name}_ABs", exist_ok=True)
    for game_date in game_dates:
        df_date = df_temp[df_temp['game_date'] == game_date]
        num_abs = df_date[(df_date['balls'] == 0) & (df_date['strikes'] == 0)]['index'].count() + 1
        if num_abs == 1:
            continue
        elif num_abs == 2:
            single_AB_game(df_date, row['name'], game_date)
        else:
            multi_AB_game(num_abs, df_date, row['name'], game_date)
        '''fig, axs = plt.subplots(nrows=1, ncols=num_abs, sharex=True, sharey=True, squeeze=False)
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
        if (len(sz_top_ls) != 0) & (len(sz_bot_ls) != 0):
            sz_t = sum(sz_top_ls)/len(sz_top_ls)
            sz_b = sum(sz_bot_ls)/len(sz_bot_ls)
        else:
            sz_t = 3.5
            sz_b = 1.5
        for x in range(num_abs):
            axs[x].plot([plate_hw, plate_hw], (sz_b, sz_t), color='k', alpha=0.7)
            axs[x].plot([-plate_hw, -plate_hw], (sz_b, sz_t), color='k', alpha=0.7)
            axs[x].plot([-plate_hw, plate_hw], (sz_b, sz_b), color='k', alpha=0.7)
            axs[x].plot([-plate_hw, plate_hw], (sz_t, sz_t), color='k', alpha=0.7)
        
        plt.title(row.name)
        plt.savefig(f"./{batter_id}_ABs/{game_date}.png")'''
