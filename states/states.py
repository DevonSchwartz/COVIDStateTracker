import pandas as pd


url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
df = pd.read_csv(url)
df.head(5)


def getDF():
	return (df) 

def getLength():
	return len(df) 

def getState(rowIndex):
	return df.iloc[rowIndex]["state"]	

def getDate(rowIndex):
		return df.iloc[rowIndex]["date"]

def getDeathsToDate(rowIndex):
	return df.iloc[rowIndex]["deaths"]

def getDailyDeathCount(rowIndex,state):
	for i in range(rowIndex - 1,-1,-1):
		if getState(i) == state:
			return getDeathsToDate(rowIndex) - getDeathsToDate(i)	

def getCasesToDate(rowIndex):
		return df.iloc[rowIndex]["cases"]

def getDailyCaseCount(rowIndex,state):
		for i in range(rowIndex - 1,-1,-1):
			if getState(i) == state:
				return getCasesToDate(rowIndex) - getCasesToDate(i)
