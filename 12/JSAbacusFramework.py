def readAll():
	with open('input.txt') as f:
		return f.read()

data=readAll()

sumD = 0

i = 0
while( i < len(data)):
	if(data[i].isdigit()):
		coef = -1 if(data[i-1]=='-') else 1
		digits = [data[i]]
		i+=1
		while(data[i].isdigit()):
			digits.append(data[i])
			i+=1
		strDigits = ''.join(digits)
		sumD+=coef*int(strDigits)
	else:
		i+=1
print sumD
