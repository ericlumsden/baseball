#Finding a Better Way to Group Baseball Hitters
## DATE

There have been long-standing questions around the best way to sort and group MLB hitters. Scouts use the 20-80 hit tool metric, [explained wonderfully by Kiley McDaniel on Fangraphs](https://blogs.fangraphs.com/scouting-explained-the-20-80-scouting-scale/); Bill James tried to place hitters into families based on their extra-base hits (XBH) ratios and OPS and ended up with [96 different families](https://www.billjamesonline.com/article785/); finally, Jonah Simon used [hierarchical clustering](https://medium.com/analytics-vidhya/grouping-major-league-hitters-with-hierarchical-methods-e7dc35b7f665) to group hitters from the 2019 season. I believe there are aspects of these approaches that could be combined to develop more accurate metrics/families/clusters of hitters and in this project I attempted to do just that.

This blog entry details the entire project and gives a step-by-step guide of how I collected, cleaned and analyzed the data. If you are only interested in the results, you can see my webpage with an interactive version of the data. If you are interested in my process, keep reading. All of my scripts and resulting data files and figures are available in the grouping_hitters folder in my [baseball repository](https://github.com/ericlumsden/baseball) on my github page.

####Collecting the data

SET UP A BIT MORE HERE!!!!!!!!!!!!!!!!!!!!!!

Based on Fangraphs' recommended [sample size](https://library.fangraphs.com/principles/sample-size/), I then culled the list to only include hitters with at least 1610 plate appearances, as I will be using XBH as part of my analysis and wanted the XBH rate to be stable. 
```python
data = pybaseball.batting_stats_range('2008-01-01', '2020-12-31')
data = data[data.PA >= 1610]
```
This left me with 479 hitters, whose basic hitting stats were saved into a csv file for easier access moving forward (gather_hitters.csv). My goal was to collect advanced metrics from statcast for all hitters where applicable, a search that requires each player's MLB key number. So, I loaded the csv file into a new script (gather_ids.py), separated the names into two new columns, `['First], ['Last'],` and then established new columns for all of the IDs that come with a player_id lookup in pybaseball. 
```python
hitters = pd.read_csv('gather_hitters.csv')
hitters[['First','Last']] = hitters['Name'].str.split(' ',1,expand=True)
hitters['mlb_id'] = pd.Series(dtype='int')
hitters['retro_id'] = pd.Series(dtype='str')
hitters['bbref_id'] = pd.Series(dtype='str')
hitters['fangraphs_id'] = pd.Series(dtype='int')
hitters['first_played'] = pd.Series(dtype='int')
hitters['last_played'] = pd.Series(dtype='int')
```
Then I iterated over each row of this dataframe and performed a `player_id` lookup for each individual player. I ran into some issues on my intial runthrough, as there are names that either i) belong to multiple players or ii) have suffixes or other additional pieces outside of first and last that were either not included or included erroneously during my intial name splitting and required cleaning. So, during these iterations I included a `try` clause to initially pull values for players with only one row returned for their `player_id` lookup. I evaluated/cleaned the remaining entries in a later script.
```python
for idx, row in hitters.iterrows():
    first = str(row['First'])
    last = str(row['Last'])
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
```
This updated dataframe with the IDs included was then saved to a new .csv file, 'gather_ids.csv.' However, I was left with 34 hitters without IDs and had to clean each individually. This work was done in clean_hitterids.py and the updated dataframe was saved to a new csv file, 'clean_hitterids.csv.' This work was pretty tedious. I separated out all of the individuals without IDs...
```python
df_noIDs = df[df['mlb_id'].isnull()]
```
...kept just their first and last names in a new dataframe...
```python
df_noIDs = df_noIDs[['First','Last']]
```
...and went through each individually identifying their correct ID values and adding them into the original dataframe. Luckily, there were only 34 players missing their IDs, so it did not take as long as it could have. Plus, once I had written out the lines for the first player, it was mostly cut-and-paste. This work was done in my 'clean_hitterids.py' script.

Once the IDs were all squared away it was time to collect the advanced metrics via statcast.