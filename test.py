from states import states
print (states.getDF())
texasIndexes = states.getStateIndex("Texas")
dates = states.getDateRange("2021-01-21", "2021-02-21")


states.graphDatesCases("Texas",dates)
