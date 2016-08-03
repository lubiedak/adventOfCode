def nextPosition(pos, direction):
	if(direction=='>'):
		pos[0] = pos[0]+1
	elif(direction=='<'):
		pos[0] = pos[0]-1
	elif(direction=='^'):
		pos[1] = pos[1]+1
	elif(direction=='v'):
		pos[1] = pos[1]-1
	return pos

def posToStr(pos):
	return str(pos[0]) + " " + str(pos[1])

def readLines():
	data = ""	
	with open('input.txt') as f:
		data = f.read()
	return data

data = readLines()
posS = [0,0]
posR = [0,0]
homes = set()
homes.add(posToStr(posS))
i = 0
for direction in data:
	if(i%2==0):
		posS = nextPosition(posS, direction)
		homes.add(posToStr(posS))
	else:
		posR = nextPosition(posR, direction)
		homes.add(posToStr(posR))
	i=i+1

print(len(homes))