import pandas as pd

'''
Here, I'm aiming to clean up my statcast dataframe some
I had a typo that resulted in empty columns, so I would like to get rid of those
I also have a number of hitters that are missing launch_speed and launch_angle stats so I would like to sort them, and have one csv with all hitters and another with complete data
'''

df = pd.read_csv('gather_statcast.csv', index_col=0)

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df.drop(['bbtype_flyBall', 'bbtype_popUp', 'bbtype_lineDrive', 'bbtype_groundBall'], axis=1)

'''
A couple of other things I would like to do with this dataframe before making a smaller version w/ the statcast data would be to make the following columns/categories per plate appearance:
2B || 3B || HR || BB || IBB || SO
'''

df['2BperPA'] = df['2B'] / df['PA']
df['3BperPA'] = df['3B'] / df['PA']
df['HRperPA'] = df['HR'] / df['PA']
df['BBperPA'] = df['BB'] / df['PA']
df['IBBperPA'] = df['IBB'] / df['PA']
df['SOperPA'] = df['SO'] / df['PA']

df_complete = df[df['launch_speed_mean'].notna()]

df.to_csv('statcast_clean_ALLHITTERS.csv')
df_complete.to_csv('statcast_clean_TRUNCATED.csv')
