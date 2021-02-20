import pandas as pd

"""
Save state COVID data to pandas dataframe
"""
url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
df = pd.read_csv(url)
df.head(5)


def getDF(): # return whole US States dataframe
	return (df) 

def getLength(): # return number of rows in DF
	return len(df) 

def getState(rowIndex): # return the state name for a given index
	return df.iloc[rowIndex]["state"]	

def getDate(rowIndex): # return the data of a certain entry
		return df.iloc[rowIndex]["date"]

def getDeathsToDate(rowIndex): #return total deaths in a certain state up to the desired date
	return df.iloc[rowIndex]["deaths"]

def getDailyDeathCount(rowIndex): # get number of deaths that occured on a specific day 
	state = getState(rowIndex) 
	for i in range(rowIndex - 1,-1,-1):
		if getState(i) == state:
			return getDeathsToDate(rowIndex) - getDeathsToDate(i)
	return getDeathsToDate(rowIndex) 	

def getCasesToDate(rowIndex): #return total cases in a certain state up to the desired date
		return df.iloc[rowIndex]["cases"]

def getDailyCaseCount(rowIndex): # get number of cases that occured on a specific day 
	state = getState(rowIndex) 
	for i in range(rowIndex - 1,-1,-1):
		if getState(i) == state:
			return getCasesToDate(rowIndex) - getCasesToDate(i)
	return getCasesToDate(rowIndex)

def getDateIndex(date):
	return df[df["date"]==date].index.values

def getStateIndex(state):
	return df[df["state"]==state].index.values
 