def readLines():
	lines = []	
	with open('input.txt') as f:
		lines = f.readlines()
	return lines

def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]
	
def contains3Vowels(word):
	sum=0
	for c in "aeiou":
		sum=sum+len(findOccurences(word,c))
	return sum>2

def containsDoubledChars(word):
	oldC = word[0]
	for c in word[1:]:
		if(c==oldC):
			return True
		else:
			oldC = c
	return False

def doesntContainThese(word):
	sum=0
	for c in ['ab', 'cd', 'pq', 'xy']:
		if(c in word):
			sum=sum+1
	return sum==0

lines = readLines()

sum=0
for line in lines:
	if(contains3Vowels(line) and containsDoubledChars(line) and doesntContainThese(line)):
		sum=sum+1

print(sum)