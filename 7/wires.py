# lx -> a
# lw OR lv -> lx
# lc LSHIFT 1 -> lw
# 1 AND lu -> lv
# lb OR la -> lc
# lr AND lt -> lu

class Wire:
	name = ""
	value = None
	def __init__(self, name):
		self.name = name
	
	def __repr__(self):
		return self.name + "=" + str(self.value)

class WireConnection:
	arg1 = Wire("X")
	arg2 = Wire("X")
	out = Wire("X")
	operation = "ASS"
	hasBeenUsed = False
	def hasValue(self):
		return self.out.value is not None
		
	def __repr__(self):
		return str(self.arg1) + " " + self.operation + " " + str(self.arg2) + " -> " + str(self.out)
	
	def tryToCalculateOutValue(self):
		if(self.hasValue()):
			return False
		if(self.arg1.value is not None):
			if(self.operation=="ASS"):
				self.out.value = self.arg1.value
			elif(self.operation=="NOT"):
				self.out.value = ~self.arg1.value
			if(self.arg2.value is not None):
				if(self.operation=="RSHIFT"):
					self.out.value = self.arg1.value >> self.arg2.value
				elif(self.operation=="LSHIFT"):
					self.out.value = self.arg1.value << self.arg2.value
				elif(self.operation=="OR"):
					self.out.value = self.arg1.value | self.arg2.value
				elif(self.operation=="AND"):
					self.out.value = self.arg1.value & self.arg2.value
	
	def containsArg(self, name):
		return name == self.arg1.name or name == self.arg2.name
	
	def setArg(self, wire):
		self.arg1 = wire if(wire.name==self.arg1.name) else self.arg1
		self.arg2 = wire if(wire.name==self.arg2.name) else self.arg2

def readLines():
	data = ""	
	with open('input.txt') as f:
		data = f.readlines()
	return data


def tryParseToInt(strVal):
	val = 0
	try:
		val = int(strVal)
		return val
	except ValueError:
		return strVal	


def tryToGetValueForWire(strVal):
	value = tryParseToInt(strVal)
	if type(value) is int:
		wire = Wire("X")
		wire.value = value
		return wire
	else:
		return Wire(strVal)
	
def parseCommand(cmd):
	elements = cmd.split(' ')
	connection = WireConnection()
	if(len(elements)==3): # Simple
		connection.arg1 = tryToGetValueForWire(elements[0])
		connection.out = Wire(elements[2][:-1])
	elif(len(elements)==4): # NOT
		connection.operation = "NOT"
		connection.arg1 = tryToGetValueForWire(elements[1])
		connection.out = Wire(elements[3][:-1])
	elif(len(elements)==5):
		connection.operation = elements[1]
		connection.arg1 = tryToGetValueForWire(elements[0])
		connection.arg2 = tryToGetValueForWire(elements[2])
		connection.out = Wire(elements[4][:-1])
	return connection




lines = readLines()
connections = []
for line in lines:
	con = parseCommand(line)
	print con
	connections.append(con)

print(" ")
while(connections[0].hasValue()==False):
	for connection in connections:
		if(connection.hasValue() and connection.hasBeenUsed == False):
			connection.hasBeenUsed == True
			for con1 in connections:
				if(con1.containsArg(connection.out.name)):
					con1.setArg(connection.out)
					print con1
		else:
			connection.tryToCalculateOutValue()

print connections[0]