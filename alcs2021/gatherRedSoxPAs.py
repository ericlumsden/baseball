from pybaseball import statcast
from pybaseball import playerid_lookup
import pandas as pd

# First we have to find all of the player_ids for the Red Sox batters to filter to just their at-bats
redsox_batters = [
    ('christian', 'vazquez'), ('christian', 'arroyo'), ('xander', 'bogaerts'), ('rafael', 'devers'), ('alex','verdugo'), ('enrique', 'hernandez'), ('hunter', 'renfroe'), ('kyle', 'schwarber'), ('kevin', 'plawecki')
]
redsox_batters_dict = {"jd+martinez": 502110.0} # Had to look up jd martinez manually because I could not figure out what search parameter to use for his first name
for batter in redsox_batters:
    id = playerid_lookup(batter[1], batter[0])
    redsox_batters_dict[f"{batter[0]}+{batter[1]}"] = float(id['key_mlbam'])

pd.DataFrame.from_dict(data=redsox_batters_dict, orient='index').to_csv('redsox_batters.csv', header=False)

# Now, collect all statcast data from the ALCS dates (15OCT21 thru 22OCT21) and filter based on player_ids found above
data = statcast(start_dt="2021-10-15", end_dt="2021-10-22")
data = data.loc[(data['batter'].isin(redsox_batters_dict.values()))]
data.to_csv('unfilteredAtBats.csv')