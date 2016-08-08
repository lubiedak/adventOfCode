#Alice would gain 2 happiness units by sitting next to Bob.

def readLines():
	data = ""	
	with open('input.txt') as f:
		data = f.readlines()
	return data

allNames = []
	
def parseData(data):
	sittingPreferences = {}
	for line in data:
		words = line.split(' ')
		name1 = words[0]
		allNames.append(name1)
		name2 = words[-1][:-2]
		pref = int(words[3]) * (-1 if (words[2] == "lose") else 1)
		
		sittingPreferences[name1+name2] = pref
	return sittingPreferences
	
data = readLines()
preferences = parseData(data)
