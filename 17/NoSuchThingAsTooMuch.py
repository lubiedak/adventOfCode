data = [50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40]

def sumsTo150(n):
	sum1 = 0
	mini = 0
	for i in range(20):
		if(1 & n == 1):
			sum1+=data[i]
			mini+=1
		n = n >> 1
	if(sum1 == 150 and mini == 4):
		return 1
	return 0

sum1 = 0

for i in range(1024*1024):
	sum1 += sumsTo150(i)
print(sum1)
