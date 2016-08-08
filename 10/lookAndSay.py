def lookAndSay(word):
	n = 1
	oldC=word[0]
	newWord=""
	for c in word[1:]:
		if(oldC!=c):
			newWord=newWord+str(n)+oldC
			n=0
		oldC=c
		n=n+1
	newWord=newWord+str(n)+oldC
	return newWord

word = "1113222113"
for i in range(50):
	word = lookAndSay(word)
	print("I: " + str(i) + "Length: " + str(len(word)))

print(len(word))