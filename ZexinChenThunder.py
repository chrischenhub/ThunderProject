# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 22:20:13 2022

@author: Chris
"""

"""The following code demonstrate how I get the numbers for team A, for team B I simply just change all the A to B"""
import pandas as pd
data = pd.read_csv('C:/Users/Chris/Downloads/shots_data.csv')
team_A = data[0:280]
team_B = data[280:505]

teamA3 = team_A.loc[team_A['y'] > 7.8]
counter3 = 0
counter3m=0
for index, row in teamA3.iterrows():
    if row["x"]**2+row["y"]**2>23.75**2:
        counter3+=1
        if row["fgmade"]==1:
            counter3m+=1


countercn3=0 
countercn3m=0
teamAconer3 = team_A.loc[team_A['y'] <= 7.8]
for index, row in teamAconer3.iterrows():
    if row["x"]**2+row["y"]**2>22**2:
        countercn3+=1
        if row["fgmade"]==1:
            countercn3m+=1


nc3 = (counter3m + (0.5*(counter3m+countercn3m)))/counter3
c3 = (countercn3m + (0.5*(counter3m+countercn3m)))/countercn3

counter2m=0
counter2=0
for index, row in teamA3.iterrows():
    if row["x"]**2+row["y"]**2<23.75**2:
        counter2+=1
        if row["fgmade"]==1:
            counter2m+=1
            
for index, row in teamAconer3.iterrows():
    if row["x"]**2+row["y"]**2<22**2:
        counter2+=1
        if row["fgmade"]==1:
            counter2m+=1

ef2 = (counter2m + (0.5*(counter3m+countercn3m)))/counter2