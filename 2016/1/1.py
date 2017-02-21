import math

class Pointer:
    direction = 0
    originalX = 0
    originalY = 0
    
    x = 0
    y = 0
    def move(self, command):
        turnDirection = command[0]
        nOfSteps = int(command[1:])
        self.turn(turnDirection)
        self.goForward(nOfSteps)
    
    def turn(self, turnDirection):
        if(turnDirection == 'L'):
            self.direction-=1
        elif(turnDirection == 'R'):
            self.direction+=1
    
    def goForward(self, nOfSteps):
        direction = self.direction % 4
        if(direction == 0):
            self.y+=nOfSteps
        if(direction == 2):
            self.y-=nOfSteps
        if(direction == 1):
            self.x+=nOfSteps
        if(direction == 3):
            self.x-=nOfSteps
    
    def howFarFromOriginalPosition(self):
        return math.fabs(self.originalX - self.x) + math.fabs(self.originalY - self.y)
 
with open('input.txt') as f:            
    commands = f.read().split(", ")

    
p = Pointer()
for c in commands:
    p.move(c)

print p.howFarFromOriginalPosition()