def readLines():
	lines = []	
	with open('input.txt') as f:
		lines = f.readlines()
	return lines

def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]
	
def contains3Vowels(word):
	sumv=0
	for c in "aeiou":
		sumv=sumv+len(findOccurences(word,c))
	return sumv>2

def containsDoubledChars(word):
	oldC = word[0]
	for c in word[1:]:
		if(c==oldC):
			return True
		else:
			oldC = c
	return False

def doesntContainThese(word):
	sumc=0
	for c in ['ab', 'cd', 'pq', 'xy']:
		if(c in word):
			sumc=sumc+1
	return sumc==0

def containsAAA(word):
	wordSize = len(word)
	for i in range(wordSize)[1:wordSize-1]:
		if(word[i-1]==word[i+1] and word[i-1]==word[i]):
			return True
	return False
	
def contains2PairsOfLetters(word):
	if(containsAAA(word)):
		return False
	wordSize = len(word[:-1])
	pairs = set()
	for i in range(wordSize):
		pair = word[i]+word[i+1]
		pairs.add(pair)

	sizeOfSets = len(pairs)-1
	print(str(wordSize) + " " + str(sizeOfSets) + " " + str(word))
	return sizeOfSets < wordSize-1
	
def containsLetterBetweenPair(word):
	wordSize = len(word)
	for i in range(wordSize)[1:wordSize-1]:
		if(word[i-1]==word[i+1]):
			return True
	return False


	
def isNice2(word):
	return contains2PairsOfLetters(word) and containsLetterBetweenPair(word)

lines = readLines()

sum1=0
sum2=0
for line in lines:
	if(contains3Vowels(line) and containsDoubledChars(line) and doesntContainThese(line)):
		sum1=sum1+1
	if(isNice2(line)):
		sum2=sum2+1


print(str(sum1) + " nice words.")
print(str(sum2) + " nice words by 2nd algorithms.")
