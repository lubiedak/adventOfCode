#turn off 245,754 through 818,851
#turn on 298,419 through 824,634
#toggle 868,687 through 969,760
size = 1000
lights = [[0 for i in range(size)] for j in range(size)]

def readLines():
	lines = []
	with open('input.txt') as f:
		lines = f.readlines()
	return lines


def fun(a,b,c,d, command):
	for i in range(b-a+1):
		for j in range(d-c+1):
			if(command==commands[0]):
				lights[a+i][c+j] = 0 if(lights[a+i][c+j]==0) else lights[a+i][c+j]-1
			elif(command==commands[1]):
				lights[a+i][c+j] = lights[a+i][c+j]+1
			elif(command==commands[2]):
				lights[a+i][c+j] = lights[a+i][c+j] + 2



##################### MAIN #####################

commands = ["turn off ", "turn on ", "toggle "]
posSep = " through "



lines = readLines();

for line in lines:
	for command in commands:
		if(command in line):
			cmd = line.split(command)
			abcd = cmd[1].split(posSep)
			ab = abcd[0]
			cd = abcd[1]
			a = int(ab.split(",")[0])
			b = int(ab.split(",")[1])
			c = int(cd.split(",")[0])
			d = int(cd.split(",")[1])
			fun(a,c,b,d,command)
			break

suml = 0
for lightLine in lights:
	for light in lightLine:
		#print(light)
		suml=suml+light


print(suml)
			
