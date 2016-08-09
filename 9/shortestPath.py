from itertools import permutations
#Faerun to Tristram = 65
#Faerun to Tristram = 65
def readLines():
	data = ""	
	with open('input.txt') as f:
		data = f.readlines()
	return data

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
sum = 0



for perm in allPerms:
	sum=0
	for i in range(len(perm)-1):
		sum+=distances[perm[i]+perm[i+1]]
	if(sum > best):
		best = sum
		print best
		print perm