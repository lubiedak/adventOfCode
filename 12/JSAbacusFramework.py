def readAll():
	data = ""	
	with open('input.txt') as f:
		data = f.read()
	return data

data=readAll()

sum = 0

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
		sum+=coef*int(strDigits)
	else:
		i+=1
print sum