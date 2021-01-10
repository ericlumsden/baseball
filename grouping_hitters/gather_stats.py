import pybaseball
import pandas as pd

hitters = pd.read_csv('gather_hitters.csv')
hitters[['First','Last']] = hitters['Name'].str.split(' ',1,expand=True)

for idx, row in hitters.iterrows():
    first = row['First']
    last = row['Last']

    # How to set values while iterating: hitters.at[idx, '']
