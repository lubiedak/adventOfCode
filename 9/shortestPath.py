from itertools import permutations
#Faerun to Tristram = 65
#Faerun to Tristram = 65
def readLines():
	with open('input.txt') as f:
		return f.readlines()

allCities = set()

def parseData(data):
	distances = {}
	for line in data:
		words = line.split(' ')
		name1 = words[0]
		allCities.add(name1)
		name2 = words[2]
		dist = int(words[-1])
		
		distances[name1+name2] = dist
		distances[name2+name1] = dist
	return distances

data = readLines()
distances = parseData(data)

allCities.add("Arbre")
allPerms = list(permutations(allCities))

best = 0
sump = 0



for perm in allPerms:
	sump=0
	for i in range(len(perm)-1):
		sump+=distances[perm[i]+perm[i+1]]
	if(sump > best):
		best = sump
		print best
		print perm
