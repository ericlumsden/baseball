import pybaseball
import pandas as pd
import numpy as np

hitters = pd.read_csv('gather_hitters.csv')
hitters[['First','Last']] = hitters['Name'].str.split(' ',1,expand=True)
hitters['mlb_id'] = pd.Series(dtype='int')
hitters['retro_id'] = pd.Series(dtype='str')
hitters['bbref_id'] = pd.Series(dtype='str')
hitters['fangraphs_id'] = pd.Series(dtype='int')
hitters['first_played'] = pd.Series(dtype='int')
hitters['last_played'] = pd.Series(dtype='int')
'''
pid = pybaseball.playerid_lookup('kershaw', 'clayton')
print(pid)
print(pid.key_bbref.item())

'''
for idx, row in hitters.iterrows():
    first = str(row['First'])
    last = str(row['Last'])

    # How to set values while iterating: hitters.at[idx, '']
    pid = pybaseball.playerid_lookup(last, first)

    if len(pid) == 1:
        hitters.at[idx, 'mlb_id'] = int(pid.key_mlbam.item())
        hitters.at[idx, 'retro_id'] = str(pid.key_retro.item())
        hitters.at[idx, 'bbref_id'] = str(pid.key_bbref.item())
        hitters.at[idx, 'fangraphs_id'] = int(pid.key_fangraphs.item())
        hitters.at[idx, 'first_played'] = int(pid.mlb_played_first.item())
        hitters.at[idx, 'last_played'] = int(pid.mlb_played_last.item())
    else:
        continue

hitters.to_csv(gather_stats.csv)
print(hitters.head())
