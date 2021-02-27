# Covid State Tracker
This is a Python package that makes it easy to figure out COVID statistics by state. The documentation for this package is below.

## getDF()
Use this function to get all of the data in this dataframe. Only use this if you can't find anything else in the package that helps you!

**PARAMETERS**: None.
**RETURNS**: Dataframe that has all the data in the COVID dataset.

## getLength()
This function gives you the number of entries in the dataset.

**PARAMETERS**: None.\
**RETURNS**: Integer representing the number of entries

## getState(entryNumber)
This function gives the name of the state of the entry number given. 

**PARAMETERS**: Integer that is the entry number (index) of the state you want to find \
**RETURNS**: String name of the state

## getDate(entryNumber)
This function gives the date at the entry number given. 

**PARAMETERS**: Integer that is the entry number (index) of the date you want to find \
**RETURNS**: String date of the entry

## getDeathsToDate(entryNumber)
This function gives the total deaths at the time the data entry was taken.

**PARAMETERS**: Integer that is the entry number (index) of the deaths to date you want to find \
**RETURNS**: Integer number of deaths

## getDailyDeathCount(entryNumber)
Get the number of deaths that occured *only* on the entry number specified.

**PARAMETERS**: Integer that is the entry number (index) of the daily death count you want to find \
**RETURNS**: Integer number of deaths only on that day

## getDateIndex(date)
Gets a list of the entry numbers that a date was recorded on

**PARAMETERS**: String that is the date \
**RETURNS**: An array of all the entry numbers (indexes) that the data for that date was recorded

## getStateIndex(state)
Gets a list of entry numbers that a given state is found on

**PARAMETERS**: String that is the state \
**RETURNS**: An array of all the entry numbers (indexes) that the data for that state was recorded

## graphDatesCases(state,dates)
Create a line graph with dates on the x-axis and daily cases on the y-axis for a given state

**PARAMETERS**: String that is the state, a list of dates \

## graphDatesDeaths(state,dates)
Create a line graph with dates on the x-axis and daily deaths on the y-axis for a given state

**PARAMETERS**: String that is the state, a list of dates \

## getDateRange(startDate,endDate)
Create a list of dates between the start and end date (inclusive)
**PARAMETERS**: String that is the start date, String that is the end date \