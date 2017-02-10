
def paperNeededForABox(a,b,c):
	list = [a,b,c]
	lists = sorted(list)
	return lists[0]*lists[1] + 2*(a*b + b*c + a*c)

def ribbonNeeded(a,b,c):
	list = [a,b,c]
	lists = sorted(list)
	return 2*(lists[0]+lists[1]) + a*b*c

def readLines():
	lines = []	
	with open('input.txt') as f:
		lines = f.readlines()
	return lines


########### MAIN ###########
lines = readLines()
sum = 0
sumr = 0
stri = None
for line in lines:
	abc = line.split('x')
	a = int(abc[0])
	b = int(abc[1])
	c = int(abc[2])
	paper = paperNeededForABox(a,b,c)
	ribbon = ribbonNeeded(a,b,c)

	sum = sum + paper
	sumr = sumr + ribbon

print(sum)
print(sumr)
