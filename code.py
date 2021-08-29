import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Importing data

#dataset
raw16 = pd.read_csv('pass-2016.csv', converters = {'Pos': str})
wins = pd.read_csv('NFL -  Wins.csv')

#3) Analyzing data

#Check how data looks
print(raw16.head())
print(wins.head())

## To check the shape of the  i.e. number of rows and columns
print(raw16.shape)
print(wins.shape)

## To know the names of the columns
print(raw16.columns)
print(wins.columns)

##To check the type of data in each column
print(raw16.dtypes)
print(wins.dtypes)

##Missing values count, column drop, recount
##As QBrec in raw16 only has values for QBs this also ensures only data for players in this position remains
print(raw16.isnull().sum())
print(wins.isnull().sum())

#clean raw16 of null values
raw16_1 = raw16.dropna(axis = 1)
#recheck
print(raw16_1.isnull().sum())

#Select target rows and columns
raw16_2 = raw16_1[raw16_1.Pos == 'QB']
print(raw16_2)

stat16 = raw16_2[['Player', 'Tm', 'Age', 'Yds', 'TD', 'Y/G', 'Cmp', 'Lng', "Int"]]

print(stat16.shape)

#COLOR is selected as it contains the same unique team identifier present in pass-2016.csv
wins_1 = wins[['COLOR', '2016', '2015']]
print(wins_1.shape)

#Determine wins for 2016 season (difference between absolute wins in 2016 and absolute wins in 2015)
wins16 = wins_1["2016"] = abs(wins_1['2016'] - wins_1['2015'])

#print(wins16)
print(wins16.shape)

#print(stat16)


#Sort data in descending order of player age, Total Yards, TDs

oldest = stat16.sort_values(by='Age', ascending=False)
#print(oldest)

Yds = stat16.sort_values(by='Yds', ascending=False)
#print(Yds)

TDs = stat16.sort_values(by='TD', ascending=False)
#print(TDs)

#grouping by age (<30 and >30) TBD

youngQB = stat16[stat16['Age'] < 30]
print(youngQB)

#chart QB performance in Yds by age
sns.relplot(x="Age", y="Yds", data=stat16);
sns.relplot(x="Age", y="Yds", hue="TD", data=stat16);

# show the plot
plt.show()

sns.relplot(x="Age", y="Yds", data=youngQB);
sns.relplot(x="Age", y="Yds", hue="TD", data=youngQB);


#completions and completion percentage vs wins