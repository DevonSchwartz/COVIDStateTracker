from states import states
print (states.getDF())
lstOfStates = states.getStateIndex("Texas")

for i in lstOfStates:
	print (states.getDailyCaseCount(i), states.getDailyDeathCount(i),states.getDate(i)) 