import pybaseball
import pandas as pd
import numpy as np

# Load the id dataframe and add columns for data from statcast
df = pd.read_csv('./data/gather_ids.csv')
''' 
I was hoping to include some more descriptive stats, but these were not readily available from the statcast data...
... or will require some extra work that I might come back to later
df['pull_tend'] = pd.Series(dtype='float')
df['straightaway_tend'] = pd.Series(dtype='float')
df['opp_tend'] = pd.Series(dtype='float')
df['qoc_barrel'] = pd.Series(dtype='float')
df['qoc_solid'] = pd.Series(dtype='float')
df['qoc_flare'] = pd.Series(dtype='float')
df['qoc_poorUnder'] = pd.Series(dtype='float')
df['qoc_poorTop'] = pd.Series(dtype='float')
df['qoc_poorWeak'] = pd.Series(dtype='float')
'''
#df['bbtype_flyBall'] = pd.Series(dtype='float')
#df['bbtype_popUp'] = pd.Series(dtype='float')
#df['bbtype_lineDrive'] = pd.Series(dtype='float')
#df['bbtype_groundBall'] = pd.Series(dtype='float')
df['launch_speed_median'] = pd.Series(dtype='float')
df['launch_speed_mean'] = pd.Series(dtype='float')
df['launch_angle_median'] = pd.Series(dtype='float')
df['launch_angle_mean'] = pd.Series(dtype='float')
'''
For pitching-based stats, need to go through and isolate all of pitch types and look @ tendency for hit v miss or take
df['pitch_name'] = pd.Series(dtype='float')
df['release_speed'] = pd.Series(dtype='float')
df['release_pos_x'] = pd.Series(dtype='float')
df['release_pos_y'] = pd.Series(dtype='float')
df['release_pos_z'] = pd.Series(dtype='float')
'''

# I need to make a dictionary to easily sort/store pitch-types and batted-ball types
# No, I will just need to separate out by pitch type later... keep this but EDIT!!!!!!!!!
pitch_num = {
    '4-Seam Fastball': 0,
    '2-Seam Fastball': 1,
    'Cutter': 2,
    'Sinker': 3,
    'Knuckle Curve': 4,
    'Changeup': 5,
    'Curveball': 6,
    'Slider': 7,
    'Split-Finger': 8,
    'Sinker': 9
}

# For the hitting stats, I only care about non-bunted balls in play, so will filter statcast data based on that
ball_in_play = ['hit_into_play', 'hit_into_play_score', 'hit_into_play_no_out']

bb_types = ['ground_ball', 'fly_ball', 'line_drive', 'popup']

# Now, will fill each row w/ the respective statcast data
for idx, row in df.iterrows():
    name = row.Name
    id = int(row.mlb_id)
    start = int(row.first_played)
    end = int(row.last_played)
    stats = pybaseball.statcast_batter(f'{start}-01-01', f'{end}-12-31', id)
    # This is where I will filter out all events that do not result in a ball in play
    stats = stats[(stats.description.isin(ball_in_play))]

    groundBallRate = len(stats[stats.bb_type == bb_types[0]]) / len(stats)
    flyBallRate = len(stats[stats.bb_type == bb_types[1]]) / len(stats)
    lineDriveRate = len(stats[stats.bb_type == bb_types[2]]) / len(stats)
    popUpRate = len(stats[stats.bb_type == bb_types[3]]) / len(stats)
    print(groundBallRate, flyBallRate, lineDriveRate, popUpRate)

    df.at[idx, 'bbType_flyBall'] = flyBallRate
    df.at[idx, 'bbType_groundBall'] = groundBallRate
    df.at[idx, 'bbType_lineDrive'] = lineDriveRate
    df.at[idx, 'bbType_popUp'] = popUpRate

    try: # This part did not work for all hitters as many had NaNs for these values; almost certainly from hitters pre collection of this data... hopefully I got enough...
        df.at[idx, 'launch_speed_median'] = stats['launch_speed'].median()
        df.at[idx, 'launch_speed_mean'] = stats['launch_speed'].mean()
        df.at[idx, 'launch_angle_median'] = stats['launch_angle'].median()
        df.at[idx, 'launch_angle_mean'] = stats['launch_angle'].mean()
    except:
        continue

df.to_csv('./data/gather_statcast.csv')