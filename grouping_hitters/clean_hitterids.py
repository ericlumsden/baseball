import pybaseball
import pandas as pd
import numpy as np

'''
This initial section was how I originally identified the hitters w/ missing IDs...
...but once the csv file was made I did not want to keep running this part of the script...
...so while completing the rest of the script I commented it out here

df = pd.read_csv('gather_ids.csv')

df_noIDs = df[df['mlb_id'].isnull()]
df_noIDs = df_noIDs[['First','Last']]
df_noIDs.to_csv('df_noIDs.csv')
'''
# Loading the hitter dataframe; will ammend each individual here and then re-save and overwrite the loaded file
df_hitters = pd.read_csv('gather_ids.csv')

'''
I have loaded each individual player missing IDs below,
commenting each of their names out and I will go through them one-by-one and update their IDs...
'''

#16,J.P.,Arencibia
jp_arencibia = pybaseball.playerid_lookup(last='arencibia')
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'J.P.') & (df_hitters.Last == 'Arencibia')), int(jp_arencibia['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'J.P.') & (df_hitters.Last == 'Arencibia')), str(jp_arencibia['key_retro'].item()), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'J.P.') & (df_hitters.Last == 'Arencibia')), str(jp_arencibia['key_bbref'].item()), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'J.P.') & (df_hitters.Last == 'Arencibia')), int(jp_arencibia['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'J.P.') & (df_hitters.Last == 'Arencibia')), int(jp_arencibia['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'J.P.') & (df_hitters.Last == 'Arencibia')), int(jp_arencibia['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Arencibia'])
#28,Jose,Bautista
jose_bautista = pybaseball.playerid_lookup(last='bautista', first='jose').iloc[1]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Bautista')), int(jose_bautista['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Bautista')), str(jose_bautista['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Bautista')), str(jose_bautista['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Bautista')), int(jose_bautista['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Bautista')), int(jose_bautista['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Bautista')), int(jose_bautista['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Bautista'])

#32,Josh,Bell
josh_bell = pybaseball.playerid_lookup(last='Bell', first='Josh').iloc[1]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Josh') & (df_hitters.Last == 'Bell')), int(josh_bell['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Josh') & (df_hitters.Last == 'Bell')), str(josh_bell['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Josh') & (df_hitters.Last == 'Bell')), str(josh_bell['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Josh') & (df_hitters.Last == 'Bell')), int(josh_bell['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Josh') & (df_hitters.Last == 'Bell')), int(josh_bell['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Josh') & (df_hitters.Last == 'Bell')), int(josh_bell['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Bell'])

#51,Jackie,Bradley Jr.
jackie_bradleyjr = pybaseball.playerid_lookup(last='Bradley', first='Jackie')
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Jackie') & (df_hitters.Last == 'Bradley Jr.')), int(jackie_bradleyjr['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Jackie') & (df_hitters.Last == 'Bradley Jr.')), str(jackie_bradleyjr['key_retro'].item()), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Jackie') & (df_hitters.Last == 'Bradley Jr.')), str(jackie_bradleyjr['key_bbref'].item()), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Jackie') & (df_hitters.Last == 'Bradley Jr.')), int(jackie_bradleyjr['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Jackie') & (df_hitters.Last == 'Bradley Jr.')), int(jackie_bradleyjr['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Jackie') & (df_hitters.Last == 'Bradley Jr.')), int(jackie_bradleyjr['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Bradley Jr.'])

#53,Ryan,Braun
ryan_braun = pybaseball.playerid_lookup(last='Braun', first='Ryan').iloc[1]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Ryan') & (df_hitters.Last == 'Braun')), int(ryan_braun['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Ryan') & (df_hitters.Last == 'Braun')), str(ryan_braun['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Ryan') & (df_hitters.Last == 'Braun')), str(ryan_braun['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Ryan') & (df_hitters.Last == 'Braun')), int(ryan_braun['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Ryan') & (df_hitters.Last == 'Braun')), int(ryan_braun['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Ryan') & (df_hitters.Last == 'Braun')), int(ryan_braun['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Braun'])

#75,Chris,Carter
chris_carter = pybaseball.playerid_lookup(last='Carter', first='Chris').iloc[1]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Carter')), int(chris_carter['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Carter')), str(chris_carter['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Carter')), str(chris_carter['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Carter')), int(chris_carter['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Carter')), int(chris_carter['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Carter')), int(chris_carter['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Carter'])

#77,Nicholas,Castellanos
nick_castellanos = pybaseball.playerid_lookup(last='Castellanos', first='Nick')
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Nicholas') & (df_hitters.Last == 'Castellanos')), int(nick_castellanos['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Nicholas') & (df_hitters.Last == 'Castellanos')), str(nick_castellanos['key_retro'].item()), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Nicholas') & (df_hitters.Last == 'Castellanos')), str(nick_castellanos['key_bbref'].item()), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Nicholas') & (df_hitters.Last == 'Castellanos')), int(nick_castellanos['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Nicholas') & (df_hitters.Last == 'Castellanos')), int(nick_castellanos['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Nicholas') & (df_hitters.Last == 'Castellanos')), int(nick_castellanos['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Castellanos'])
#97,C.J.,Cron
cj_cron = pybaseball.playerid_lookup(last='Cron').iloc[0]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'C.J.') & (df_hitters.Last == 'Cron')), int(cj_cron['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'C.J.') & (df_hitters.Last == 'Cron')), str(cj_cron['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'C.J.') & (df_hitters.Last == 'Cron')), str(cj_cron['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'C.J.') & (df_hitters.Last == 'Cron')), int(cj_cron['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'C.J.') & (df_hitters.Last == 'Cron')), int(cj_cron['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'C.J.') & (df_hitters.Last == 'Cron')), int(cj_cron['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Cron'])

#98,Nelson,Cruz
nelson_cruz = pybaseball.playerid_lookup(last='Cruz', first='Nelson').iloc[1]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Nelson') & (df_hitters.Last == 'Cruz')), int(nelson_cruz['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Nelson') & (df_hitters.Last == 'Cruz')), str(nelson_cruz['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Nelson') & (df_hitters.Last == 'Cruz')), str(nelson_cruz['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Nelson') & (df_hitters.Last == 'Cruz')), int(nelson_cruz['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Nelson') & (df_hitters.Last == 'Cruz')), int(nelson_cruz['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Nelson') & (df_hitters.Last == 'Cruz')), int(nelson_cruz['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Cruz'])

#104,Ike,Davis
ike_davis = pybaseball.playerid_lookup(last='Davis', first='Ike').iloc[1]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Ike') & (df_hitters.Last == 'Davis')), int(ike_davis['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Ike') & (df_hitters.Last == 'Davis')), str(ike_davis['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Ike') & (df_hitters.Last == 'Davis')), str(ike_davis['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Ike') & (df_hitters.Last == 'Davis')), int(ike_davis['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Ike') & (df_hitters.Last == 'Davis')), int(ike_davis['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Ike') & (df_hitters.Last == 'Davis')), int(ike_davis['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Davis'])

#113,Delino,DeShields
delino_deshields = pybaseball.playerid_lookup(last='Deshields').iloc[0]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Delino') & (df_hitters.Last == 'DeShields')), int(delino_deshields['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Delino') & (df_hitters.Last == 'DeShields')), str(delino_deshields['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Delino') & (df_hitters.Last == 'DeShields')), str(delino_deshields['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Delino') & (df_hitters.Last == 'DeShields')), int(delino_deshields['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Delino') & (df_hitters.Last == 'DeShields')), int(delino_deshields['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Delino') & (df_hitters.Last == 'DeShields')), int(delino_deshields['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'DeShields'])

#122,J.D.,Drew
jd_drew = pybaseball.playerid_lookup(last='Drew', first='J. D.')
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'J.D.') & (df_hitters.Last == 'Drew')), int(jd_drew['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'J.D.') & (df_hitters.Last == 'Drew')), str(jd_drew['key_retro'].item()), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'J.D.') & (df_hitters.Last == 'Drew')), str(jd_drew['key_bbref'].item()), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'J.D.') & (df_hitters.Last == 'Drew')), int(jd_drew['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'J.D.') & (df_hitters.Last == 'Drew')), int(jd_drew['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'J.D.') & (df_hitters.Last == 'Drew')), int(jd_drew['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Drew'])

#126,Matt,Duffy
matt_duffy = pybaseball.playerid_lookup(last='Duffy', first='Matt').iloc[1]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Matt') & (df_hitters.Last == 'Duffy')), int(matt_duffy['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Matt') & (df_hitters.Last == 'Duffy')), str(matt_duffy['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Matt') & (df_hitters.Last == 'Duffy')), str(matt_duffy['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Matt') & (df_hitters.Last == 'Duffy')), int(matt_duffy['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Matt') & (df_hitters.Last == 'Duffy')), int(matt_duffy['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Matt') & (df_hitters.Last == 'Duffy')), int(matt_duffy['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Duffy'])

#130,Adam,Eaton
adam_eaton = pybaseball.playerid_lookup(last='Eaton', first='Adam').iloc[1]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Adam') & (df_hitters.Last == 'Eaton')), int(adam_eaton['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Adam') & (df_hitters.Last == 'Eaton')), str(adam_eaton['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Adam') & (df_hitters.Last == 'Eaton')), str(adam_eaton['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Adam') & (df_hitters.Last == 'Eaton')), int(adam_eaton['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Adam') & (df_hitters.Last == 'Eaton')), int(adam_eaton['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Adam') & (df_hitters.Last == 'Eaton')), int(adam_eaton['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Eaton'])

#131,A.J.,Ellis
aj_ellis = pybaseball.playerid_lookup(last='Ellis', first='A. J.')
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'A.J.') & (df_hitters.Last == 'Ellis')), int(aj_ellis['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'A.J.') & (df_hitters.Last == 'Ellis')), str(aj_ellis['key_retro'].item()), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'A.J.') & (df_hitters.Last == 'Ellis')), str(aj_ellis['key_bbref'].item()), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'A.J.') & (df_hitters.Last == 'Ellis')), int(aj_ellis['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'A.J.') & (df_hitters.Last == 'Ellis')), int(aj_ellis['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'A.J.') & (df_hitters.Last == 'Ellis')), int(aj_ellis['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Ellis'])

#169,Alex,Gonzalez
alex_gonzalez = pybaseball.playerid_lookup(last='Gonzalez', first='Alex').iloc[0]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Alex') & (df_hitters.Last == 'Gonzalez')), int(alex_gonzalez['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Alex') & (df_hitters.Last == 'Gonzalez')), str(alex_gonzalez['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Alex') & (df_hitters.Last == 'Gonzalez')), str(alex_gonzalez['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Alex') & (df_hitters.Last == 'Gonzalez')), int(alex_gonzalez['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Alex') & (df_hitters.Last == 'Gonzalez')), int(alex_gonzalez['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Alex') & (df_hitters.Last == 'Gonzalez')), int(alex_gonzalez['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Gonzalez'])

#178,Vladimir,Guerrero
vlad_guerrero = pybaseball.playerid_lookup(last='Guerrero', first='Vladimir').iloc[1]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Vladimir') & (df_hitters.Last == 'Guerrero')), int(vlad_guerrero['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Vladimir') & (df_hitters.Last == 'Guerrero')), str(vlad_guerrero['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Vladimir') & (df_hitters.Last == 'Guerrero')), str(vlad_guerrero['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Vladimir') & (df_hitters.Last == 'Guerrero')), int(vlad_guerrero['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Vladimir') & (df_hitters.Last == 'Guerrero')), int(vlad_guerrero['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Vladimir') & (df_hitters.Last == 'Guerrero')), int(vlad_guerrero['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Guerrero'])

#183,Jerry,Hairston
jerry_hairston = pybaseball.playerid_lookup(last='Hairston').iloc[0]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Jerry') & (df_hitters.Last == 'Hairston')), int(jerry_hairston['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Jerry') & (df_hitters.Last == 'Hairston')), str(jerry_hairston['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Jerry') & (df_hitters.Last == 'Hairston')), str(jerry_hairston['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Jerry') & (df_hitters.Last == 'Hairston')), int(jerry_hairston['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Jerry') & (df_hitters.Last == 'Hairston')), int(jerry_hairston['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Jerry') & (df_hitters.Last == 'Hairston')), int(jerry_hairston['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Hairston'])

#185,Billy,Hamilton
billy_hamilton = pybaseball.playerid_lookup(last='Hamilton', first='Billy').iloc[0]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Billy') & (df_hitters.Last == 'Hamilton')), int(billy_hamilton['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Billy') & (df_hitters.Last == 'Hamilton')), str(billy_hamilton['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Billy') & (df_hitters.Last == 'Hamilton')), str(billy_hamilton['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Billy') & (df_hitters.Last == 'Hamilton')), int(billy_hamilton['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Billy') & (df_hitters.Last == 'Hamilton')), int(billy_hamilton['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Billy') & (df_hitters.Last == 'Hamilton')), int(billy_hamilton['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Hamilton'])

#189,J.J.,Hardy
jj_hardy = pybaseball.playerid_lookup(last='Hardy', first='J. J.')
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'J.J.') & (df_hitters.Last == 'Hardy')), int(jj_hardy['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'J.J.') & (df_hitters.Last == 'Hardy')), str(jj_hardy['key_retro'].item()), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'J.J.') & (df_hitters.Last == 'Hardy')), str(jj_hardy['key_bbref'].item()), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'J.J.') & (df_hitters.Last == 'Hardy')), int(jj_hardy['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'J.J.') & (df_hitters.Last == 'Hardy')), int(jj_hardy['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'J.J.') & (df_hitters.Last == 'Hardy')), int(jj_hardy['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Hardy'])

#198,Cesar,Hernandez
cesar_hernandez = pybaseball.playerid_lookup(last='Hernandez', first='Cesar').iloc[0]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Cesar') & (df_hitters.Last == 'Hernandez')), int(cesar_hernandez['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Cesar') & (df_hitters.Last == 'Hernandez')), str(cesar_hernandez['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Cesar') & (df_hitters.Last == 'Hernandez')), str(cesar_hernandez['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Cesar') & (df_hitters.Last == 'Hernandez')), int(cesar_hernandez['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Cesar') & (df_hitters.Last == 'Hernandez')), int(cesar_hernandez['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Cesar') & (df_hitters.Last == 'Hernandez')), int(cesar_hernandez['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Hernandez'])

#200,Ramon,Hernandez
ramon_hernandez = pybaseball.playerid_lookup(last='Hernandez', first='Ramon').iloc[1]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Ramon') & (df_hitters.Last == 'Hernandez')), int(ramon_hernandez['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Ramon') & (df_hitters.Last == 'Hernandez')), str(ramon_hernandez['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Ramon') & (df_hitters.Last == 'Hernandez')), str(ramon_hernandez['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Ramon') & (df_hitters.Last == 'Hernandez')), int(ramon_hernandez['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Ramon') & (df_hitters.Last == 'Hernandez')), int(ramon_hernandez['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Ramon') & (df_hitters.Last == 'Hernandez')), int(ramon_hernandez['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Hernandez'])

#227,Chris,Johnson
chris_johnson = pybaseball.playerid_lookup(last='Johnson', first='Chris').iloc[0]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Johnson')), int(chris_johnson['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Johnson')), str(chris_johnson['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Johnson')), str(chris_johnson['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Johnson')), int(chris_johnson['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Johnson')), int(chris_johnson['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Johnson')), int(chris_johnson['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Johnson'])

#274,J.D.,Martinez
jd_martinez = pybaseball.playerid_lookup(last='Martinez', first='J. D.')
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'J.D.') & (df_hitters.Last == 'Martinez')), int(jd_martinez['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'J.D.') & (df_hitters.Last == 'Martinez')), str(jd_martinez['key_retro'].item()), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'J.D.') & (df_hitters.Last == 'Martinez')), str(jd_martinez['key_bbref'].item()), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'J.D.') & (df_hitters.Last == 'Martinez')), int(jd_martinez['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'J.D.') & (df_hitters.Last == 'Martinez')), int(jd_martinez['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'J.D.') & (df_hitters.Last == 'Martinez')), int(jd_martinez['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Martinez'])

#336,A.J.,Pierzynski
aj_pierzynski = pybaseball.playerid_lookup(last='Pierzynski', first='A. J.')
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'A.J.') & (df_hitters.Last == 'Pierzynski')), int(aj_pierzynski['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'A.J.') & (df_hitters.Last == 'Pierzynski')), str(aj_pierzynski['key_retro'].item()), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'A.J.') & (df_hitters.Last == 'Pierzynski')), str(aj_pierzynski['key_bbref'].item()), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'A.J.') & (df_hitters.Last == 'Pierzynski')), int(aj_pierzynski['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'A.J.') & (df_hitters.Last == 'Pierzynski')), int(aj_pierzynski['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'A.J.') & (df_hitters.Last == 'Pierzynski')), int(aj_pierzynski['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Pierzynski'])

#355,Jose,Ramirez
jose_ramirez = pybaseball.playerid_lookup(last='Ramirez', first='Jose').iloc[1]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Ramirez')), int(jose_ramirez['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Ramirez')), str(jose_ramirez['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Ramirez')), str(jose_ramirez['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Ramirez')), int(jose_ramirez['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Ramirez')), int(jose_ramirez['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Ramirez')), int(jose_ramirez['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Ramirez'])

#358,J.T.,Realmuto
jt_realmuto = pybaseball.playerid_lookup(last='Realmuto', first='J. T.')
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'J.T.') & (df_hitters.Last == 'Realmuto')), int(jt_realmuto['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'J.T.') & (df_hitters.Last == 'Realmuto')), str(jt_realmuto['key_retro'].item()), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'J.T.') & (df_hitters.Last == 'Realmuto')), str(jt_realmuto['key_bbref'].item()), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'J.T.') & (df_hitters.Last == 'Realmuto')), int(jt_realmuto['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'J.T.') & (df_hitters.Last == 'Realmuto')), int(jt_realmuto['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'J.T.') & (df_hitters.Last == 'Realmuto')), int(jt_realmuto['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Realmuto'])

#363,Jose,Reyes
jose_reyes = pybaseball.playerid_lookup(last='Reyes', first='Jose').iloc[1]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Reyes')), int(jose_reyes['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Reyes')), str(jose_reyes['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Reyes')), str(jose_reyes['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Reyes')), int(jose_reyes['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Reyes')), int(jose_reyes['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Jose') & (df_hitters.Last == 'Reyes')), int(jose_reyes['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Reyes'])

#386,Yolmer,Sanchez
yolmer_sanchez = pybaseball.playerid_lookup(last='Sanchez', first='Carlos')
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Yolmer') & (df_hitters.Last == 'Sanchez')), int(yolmer_sanchez['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Yolmer') & (df_hitters.Last == 'Sanchez')), str(yolmer_sanchez['key_retro'].item()), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Yolmer') & (df_hitters.Last == 'Sanchez')), str(yolmer_sanchez['key_bbref'].item()), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Yolmer') & (df_hitters.Last == 'Sanchez')), int(yolmer_sanchez['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Yolmer') & (df_hitters.Last == 'Sanchez')), int(yolmer_sanchez['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Yolmer') & (df_hitters.Last == 'Sanchez')), int(yolmer_sanchez['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Sanchez'])

#416,Steven,Souza Jr.
steven_souzajr = pybaseball.playerid_lookup(last='Souza', first='Steven')
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Steven') & (df_hitters.Last == 'Souza Jr.')), int(steven_souzajr['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Steven') & (df_hitters.Last == 'Souza Jr.')), str(steven_souzajr['key_retro'].item()), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Steven') & (df_hitters.Last == 'Souza Jr.')), str(steven_souzajr['key_bbref'].item()), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Steven') & (df_hitters.Last == 'Souza Jr.')), int(steven_souzajr['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Steven') & (df_hitters.Last == 'Souza Jr.')), int(steven_souzajr['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Steven') & (df_hitters.Last == 'Souza Jr.')), int(steven_souzajr['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Souza Jr.'])

#432,Michael,A. Taylor
michael_taylor = pybaseball.playerid_lookup(last='Taylor', first='Michael').iloc[0]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Michael') & (df_hitters.Last == 'A. Taylor')), int(michael_taylor['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Michael') & (df_hitters.Last == 'A. Taylor')), str(michael_taylor['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Michael') & (df_hitters.Last == 'A. Taylor')), str(michael_taylor['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Michael') & (df_hitters.Last == 'A. Taylor')), int(michael_taylor['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Michael') & (df_hitters.Last == 'A. Taylor')), int(michael_taylor['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Michael') & (df_hitters.Last == 'A. Taylor')), int(michael_taylor['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'A. Taylor'])

#449,Melvin,Upton Jr.
melvin_uptonjr = pybaseball.playerid_lookup(last='Upton').iloc[0]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Melvin') & (df_hitters.Last == 'Upton Jr.')), int(melvin_uptonjr['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Melvin') & (df_hitters.Last == 'Upton Jr.')), str(melvin_uptonjr['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Melvin') & (df_hitters.Last == 'Upton Jr.')), str(melvin_uptonjr['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Melvin') & (df_hitters.Last == 'Upton Jr.')), int(melvin_uptonjr['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Melvin') & (df_hitters.Last == 'Upton Jr.')), int(melvin_uptonjr['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Melvin') & (df_hitters.Last == 'Upton Jr.')), int(melvin_uptonjr['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Upton Jr.'])

#472,Chris,Young
chris_young = pybaseball.playerid_lookup(last='Young', first='Chris').iloc[1]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Young')), int(chris_young['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Young')), str(chris_young['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Young')), str(chris_young['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Young')), int(chris_young['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Young')), int(chris_young['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Chris') & (df_hitters.Last == 'Young')), int(chris_young['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Young'])

#474,Eric,Young Jr.
eric_youngjr = pybaseball.playerid_lookup(last='Young', first='Eric').iloc[0]
df_hitters['mlb_id'] = np.where( ((df_hitters.First == 'Eric') & (df_hitters.Last == 'Young Jr.')), int(eric_youngjr['key_mlbam'].item()), df_hitters['mlb_id'] )
df_hitters['retro_id'] = np.where( ((df_hitters.First == 'Eric') & (df_hitters.Last == 'Young Jr.')), str(eric_youngjr['key_retro']), df_hitters['retro_id'] )
df_hitters['bbref_id'] = np.where( ((df_hitters.First == 'Eric') & (df_hitters.Last == 'Young Jr.')), str(eric_youngjr['key_bbref']), df_hitters['bbref_id'] )
df_hitters['fangraphs_id'] = np.where( ((df_hitters.First == 'Eric') & (df_hitters.Last == 'Young Jr.')), int(eric_youngjr['key_fangraphs'].item()), df_hitters['fangraphs_id'] )
df_hitters['first_played'] = np.where( ((df_hitters.First == 'Eric') & (df_hitters.Last == 'Young Jr.')), int(eric_youngjr['mlb_played_first'].item()), df_hitters['first_played'] )
df_hitters['last_played'] = np.where( ((df_hitters.First == 'Eric') & (df_hitters.Last == 'Young Jr.')), int(eric_youngjr['mlb_played_last'].item()), df_hitters['last_played'] )
print(df_hitters[df_hitters['Last'] == 'Young Jr.'])

df_hitters.to_csv('gather_ids.csv')