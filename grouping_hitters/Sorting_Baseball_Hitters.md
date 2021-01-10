#Finding a Better Way to Group Baseball Hitters
##

There have been long-standing questions around the best way to sort and group MLB hitters together. Scouts use the 20-80 hit tool metric, [explained wonderfully by Kiley McDaniel on Fangraphs] (https://blogs.fangraphs.com/scouting-explained-the-20-80-scouting-scale/). Bill James tried to place hitters into families based on their extra-base hits (XBH) ratios and OPS and ended up with [96 different families](https://www.billjamesonline.com/article785/)). Finally, Jonah Simon used [hierarchical clustering](https://medium.com/analytics-vidhya/grouping-major-league-hitters-with-hierarchical-methods-e7dc35b7f665) to group hitters from the 2019 season. I believe there are aspects of these approaches that could be combined to develop more accurate metrics/families/clusters of hitters.

Based on Fangraphs' recommended [sample size](https://library.fangraphs.com/principles/sample-size/), I then culled the list to only include hitters with at least 1610 plate appearances, as I will be using XBH as part of my analysis and wanted the XBH rate to be stable. 
```python
data = pybaseball.batting_stats_range('2008-01-01', '2020-12-31')
data = data[data.PA >= 1610]
```
This left me with 479 hitters, whose basic hitting stats were saved into a csv file for easier access moving forward (gather_hitters.csv).