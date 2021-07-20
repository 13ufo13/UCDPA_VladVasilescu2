import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Importing data

#dataset
wins = pd.read_csv('NFL -  Wins.csv')

#3) Analyzing data

#check how it looks
#print(raw16.head())
#print(wins.head())

## To check the shape of the  i.e. number of rows and columns
#print(raw16.shape)
print(wins.shape)

## To know the names of the columns
#print(raw16.columns)
print(wins.columns)


##To check the type of data in each column
#print(raw.dtypes)
#print(wins.dtypes)

##Missing values count, column drop, recount
#print(raw16.isnull().sum())
#print(wins.isnull().sum())

#clean raw16 of null values
#raw16_2 = raw16.dropna(axis = 1)
#recheck
#print(raw16_2.isnull().sum())


#Select target columns
#stat16 = raw16[['Player', 'Tm', 'Age', 'Yds', 'TD', 'Y/G', 'Cmp', 'Lng', "Int"]].head()

wins_1 = wins[['2000']].head()
print(wins_1)

#Determine wins for 2016 season (difference between absolute wins in 2016 and absolute wins in 2015)
#wins16 = wins_1["2016"] = abs(wins_1['2016'] - wins_1['2015'])

#print(wins16)
#print(wins16.shape)
#print(stat16)
#print(wins_1)

#Sort data in descending order of player age, Total Yards, TDs

#oldest = stat16.sort_values(by='Age', ascending=False)
#print(oldest)

#Yds = stat16.sort_values(by='Yds', ascending=False)
#print(Yds)

#TDs = stat16.sort_values(by='TD', ascending=False)
#print(TDs)

#grouping by age (<30 and >30)

#youngQB = stat16.groupby('Age')

#print(youngQB)/pycharm/