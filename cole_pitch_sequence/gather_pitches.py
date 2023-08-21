from pybaseball import playerid_lookup, statcast_pitcher

# Gather Gerrit Cole's mlbam key for gathering statcast from his game against Boston
cole_ids = playerid_lookup('cole', 'gerrit')
cole_mlbam = cole_ids["key_mlbam"][0]

cole_vs_boston = statcast_pitcher('2023-08-19', '2023-08-21', cole_mlbam)
# Save this table as a .csv so there is no need to continuously call to statcast
cole_vs_boston.to_csv("./cole_pitches_vs_boston.csv")

# Repeat with his full season in a separate table
cole_season = statcast_pitcher('2023-01-01', '2023-08-18', cole_mlbam)
cole_season.to_csv("./cole_pitches_SEASON.csv")