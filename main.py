# General Packages
import numpy as np
import pandas as pd
import pybaseball as pyb
import seaborn as sns

data=pyb.standings(2022)
data=data[1]
data=data[data['Tm'].isin(['Detroit Tigers','Chicago White Sox'])]

win_diff = int(data[data['Tm']=='Chicago White Sox']['W'])-int(data[data['Tm']=='Detroit Tigers']['W'])

leading_team = data.iloc[0,0]
losing_team = data.iloc[1,0]

print("As of today, the {0} have {2} more wins than the {1}.".format(leading_team, losing_team,win_diff))