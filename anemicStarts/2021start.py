import pybaseball
import numpy
import matplotlib.pyplot as plt

data = pybaseball.schedule_and_record(2021, 'BOS')
# Probably have to make a sublist w/ all complete games and then look for player stats from each day and total up hits, etc
print(data)