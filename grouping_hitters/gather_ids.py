import pybaseball
import pandas as pd

# Load hitters data from csv; split names and data types for id gathering

hitters = pd.read_csv('./data/gather_hitters.csv')
hitters[['First','Last']] = hitters['Name'].str.split(' ',1,expand=True)
hitters['mlb_id'] = pd.Series(dtype='int')
hitters['retro_id'] = pd.Series(dtype='str')
hitters['bbref_id'] = pd.Series(dtype='str')
hitters['fangraphs_id'] = pd.Series(dtype='int')
hitters['first_played'] = pd.Series(dtype='int')
hitters['last_played'] = pd.Series(dtype='int')

'''

Example from pybaseball github on gathering ids:
pid = pybaseball.playerid_lookup('kershaw', 'clayton')
print(pid)
print(pid.key_bbref.item())

'''

# Iterate over dataframe to gather first & last names and then get their ids
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

# Save the updated dataframe to a new csv file
hitters.to_csv('./data/gather_ids.csv')
print(hitters.head())
