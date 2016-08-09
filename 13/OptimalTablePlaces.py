from itertools import permutations

def readLines():
	data = ""	
	with open('input.txt') as f:
		data = f.readlines()
	return data

allNames = set()
	
def parseData(data):
	sittingPreferences = {}
	for line in data:
		words = line.split(' ')
		name1 = words[0]
		allNames.add(name1)
		name2 = words[-1][:-2]
		pref = int(words[3]) * (-1 if (words[2] == "lose") else 1)
		
		sittingPreferences[name1+name2] = pref
	return sittingPreferences
	
data = readLines()
preferences = parseData(data)

allPerms = list(permutations(allNames))

best = 0
sum = 0
print(preferences["MalloryGeorge"])
for perm in allPerms:
	sum=0
	for i in range(len(perm)):
		left = i-1 if(i>0) else len(perm)-1
		right = i+1 if(i<len(perm)-1) else 0
		sum+=preferences[perm[i]+perm[left]] + preferences[perm[i]+perm[right]]
	if(sum > best):
		best = sum
		print best
		print perm
