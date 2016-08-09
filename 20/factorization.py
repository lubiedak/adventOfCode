minimum = 34000000

i=720700
while(True):
	i+=20
	print(i)
	sumOfPresents = i*11
	for j in range(i/2+1)[1:]:
		if(i%j == 0 and i/j < 50):
			sumOfPresents+= j*11
	if(sumOfPresents > minimum):
		break
print(i)