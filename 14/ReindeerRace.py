#ReinderRace

speed = 0
flyTime = 1
breakTime = 2
distance = 3
score = 4

#Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
#Cupid can fly 8 km/s for 17 seconds, but then must rest for 114 seconds.
#Prancer can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
#Donner can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
#Dasher can fly 11 km/s for 12 seconds, but then must rest for 125 seconds.
#Comet can fly 21 km/s for 6 seconds, but then must rest for 121 seconds.
#Blitzen can fly 18 km/s for 3 seconds, but then must rest for 50 seconds.
#Vixen can fly 20 km/s for 4 seconds, but then must rest for 75 seconds.
#Dancer can fly 7 km/s for 20 seconds, but then must rest for 119 seconds.

reindeers = [[22,8,165,0,0],[8,17,114,0,0],[18,6,103,0,0],[25,6,145,0,0],[11,12,125,0,0],[21,6,121,0,0],[18,3,50,0,0],[20,4,75,0,0],[7,20,119,0,0]]

for r in reindeers:
	time = 2503
	while(time>0):
		fly = r[flyTime] if (time>r[flyTime]) else time
		r[distance] += r[speed]*fly
		time-=fly
		time-=r[breakTime]
	
	print(r)
print(" ")
for r in reindeers:
	r[distance]=0

for t in range(2503):
	for r in reindeers:
		r[distance]+=r[speed] if ( t % (r[flyTime] + r[breakTime]) < r[flyTime]) else 0
	maxDistance = 0
	for r in reindeers:
		if(r[distance] > maxDistance):
			maxDistance = r[distance]
	
	for r in reindeers:
		if(r[distance] == maxDistance):
			r[score]+=1
	

for r in reindeers:
	print(r)