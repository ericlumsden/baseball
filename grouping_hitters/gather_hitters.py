import pybaseball
import pandas as pd

# Gather all hitter data from 2015 thru 2020
data = pybaseball.batting_stats_range('2008-01-01', '2020-12-31')

# Cull list to only include hitters w/ @ least 1610 PAs
# Desired sample size based on XBH stabilization (https://library.fangraphs.com/principles/sample-size/)
data = data[data.PA >= 1610]

# Saving this data to a csv file for easier access
data.to_csv('./data/gather_hitters.csv')