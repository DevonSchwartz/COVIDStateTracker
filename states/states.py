import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 

from datetime import timedelta, date

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

def getDateIndex(date): #get list of indexes of a certain date
	return df[df["date"]==date].index.values

def getStateIndex(state): #get list of indexes of a certain state
	return df[df["state"]==state].index.values


def graphDatesCases(state, dates): #graph Dates on x axis and Cases in a state on Y Axis

	try:

		X = dates
		Y = []

		for date in dates:
			dateIndexes = getDateIndex(date)
			for index in dateIndexes:
				if getState(index) == state:
					Y.append(getDailyCaseCount(index)) 



		plt.figure(dpi=50, figsize=(20,14)) 
	
		ax = plt.axes() 
		ax.grid(linewidth=0.2, color='#8f8f8f')  
		
		ax.set_facecolor("black")  
		ax.set_xlabel('Date\n',size=14,color='#4bb4f2') 
		ax.set_ylabel('Number of Confirmed Cases in ' + state + '\n', size=14,color='#4bb4f2') 
		
		plt.xticks(rotation='vertical',size='12',color='white') 
		plt.yticks(size=12,color='white') 
		plt.tick_params(size=10,color='white') 
		
		for i in range (0,len(X)):
			plt.annotate(str(Y[i]), (X[i], Y[i]), color='white',size='12')
		
		plt.title("COVID-19: Daily Confrimed Cases\n", 
				size=20,color='#28a9ff') 
		
		ax.plot(X,Y, 
				color='#1F77B4', 
				marker='o', 
				linewidth=1, 
				markersize=7, 
				markeredgecolor='#035E9B')
		plt.show() 

	except ValueError:
		print ("This is too early in the pandemic to have a case count every day for every state") 


def graphDatesDeaths(state, dates): #graph Dates on x axis and deaths in a state on Y Axis

	try:

		X = dates
		Y = []

		for date in dates:
			dateIndexes = getDateIndex(date)
			for index in dateIndexes:
				if getState(index) == state:
					Y.append(getDailyDeathCount(index)) 

	

		plt.figure(dpi=60, figsize=(20,14)) 
	
		ax = plt.axes() 
		ax.grid(linewidth=0.2, color='#8f8f8f')  
		
		ax.set_facecolor("black")  
		ax.set_xlabel('Date\n',size=14,color='#4bb4f2') 
		ax.set_ylabel('Number of Confirmed Deaths in ' + state + '\n', size=14,color='#4bb4f2') 
		
		plt.xticks(rotation='vertical',size='12',color='white') 
		plt.yticks(size=12,color='white') 
		plt.tick_params(size=10,color='white')  

		for i in range (0,len(X)):
			plt.annotate(str(Y[i]), (X[i], Y[i]), color='white',size='12')
		
		plt.title("COVID-19: Daily Confrimed Deaths\n", 
				size=20,color='#28a9ff') 
		
		ax.plot(X,Y, 
				color='#1F77B4', 
				marker='o', 
				linewidth=1, 
				markersize=7, 
				markeredgecolor='#035E9B')
		plt.show() 
		
	except ValueError:
		print ("This is too early in the pandemic to have a death count every day for every state")



def getDateRange(startDate, endDate): #get a list of dates in a given range (inclusive) 

	startDate = startDate.split("-")
	startDate = date(int(startDate[0]),int(startDate[1]),int(startDate[2]))


	endDate = endDate.split("-")
	endDate = date(int(endDate[0]),int(endDate[1]),int(endDate[2]))

	

	lst = []
	for n in range(int ((endDate - startDate).days)+1):
		dt = startDate + timedelta(n)

		lst.append(dt.strftime("%Y-%m-%d"))
	return lst