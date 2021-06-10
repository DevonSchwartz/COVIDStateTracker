from states import states 


print (states.getDF()) 


lst = states.getDateRange("2021-05-01","2021-05-25") 
datesBegin = states.getDateIndex("2021-05-01")
datesEnd = states.getDateIndex("2021-05-24")
start = 0
end = 0 
for i in datesBegin:
	if states.getState(i) == "Texas" :
		start = i 
		break 

for i in datesEnd:
	if states.getState(i) == "Texas" :
		end = i + 1
		break 

print (start,end)

for i in range(start,end):
	if (states.getState(i) == "Texas"):
		print (i, states.getState(i), states.getDate(i), str(states.getDailyCaseCount(i))) 