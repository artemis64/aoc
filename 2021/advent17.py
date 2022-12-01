file = open('input17.txt', 'r')
line = file.readline().strip().split()

file.close()
import math
xTarget = line[2][2:].split('..')
yTarget = line[3][2:].split('..')
xTarget[1] = xTarget[1][:-1]
xTarget = [ int(x) for x in xTarget ]
yTarget = [ int(x) for x in yTarget ]

minX = (-1 + math.sqrt(1 + 8 * xTarget[0]))/2
minX = int(minX) if int(minX) == minX else int(minX) + 1
maxX = xTarget[1]
minY = yTarget[0]
maxY = abs(yTarget[0])-1
print(minX, maxX, minY, maxY)

numberOfSolutions = 0
velocityValues = []

for y in range(minY, maxY+1):
	i = 1
	isToTry=[]
	while int(i*y - 0.5 * (i*i-i)) >= yTarget[0]:
		if int(i*y - 0.5 * (i*i-i)) <= yTarget[1]:
			isToTry.append(i)
			print("y {} i {}".format(y, i))
		i += 1
	print("y {} i {}".format(y, isToTry))
	for x in range(minX, maxX+1):
		for i in isToTry:
			if i<x and int(i*x - 0.5 * (i*i-i)) >= xTarget[0] and int(i*x - 0.5 * (i*i-i)) <= xTarget[1] and (x,y) not in velocityValues:
				numberOfSolutions += 1
				velocityValues.append((x,y))
				print(x,y)
			elif i>=x and int(0.5*(x*x+x)) >= xTarget[0] and int(0.5*(x*x+x)) <= xTarget[1]and (x,y) not in velocityValues:
				numberOfSolutions +=1
				velocityValues.append((x,y))
				print(x,y)
print(numberOfSolutions)
