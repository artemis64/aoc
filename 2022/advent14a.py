file = open('input14.txt', 'r')
rocks = []
minX = 500 													#min X needs to be smaller than the source of sand
maxX = 500 													#min X needs to be bigger than the source of sand
maxY = 0 													#minY is source of sand 0 - this is bellow - bigger number

for line in file:
	line = line.strip() 									#get rid of the "empty" caracter around the line (ex. new line)
	line = line.split(' -> ') 								#split the line by " -> " - line is list where each item is in format "496,6"
	line = [x.split(',') for x in line] 					#split the pieces inside line by "," - each string item "496,6" we switch to the list ["496", "6"]
	line = [[int(x[0]), int(x[1])] for x in line]			#line is list of lists - the items of the inside lists: string -> int
	for i in range(len(line)-1):							
		if line[i][0] == line[i+1][0]: 
			for y in range(min(line[i][1], line[i+1][1]), max(line[i][1], line[i+1][1]) + 1):
				if not [line[i][0], y] in rocks:
					rocks.append([line[i][0], y])
		else:
			for x in range(min(line[i][0], line[i+1][0]), max(line[i][0], line[i+1][0]) + 1):
				if not [x, line[i][1]] in rocks:
					rocks.append([x, line[i][1]])
rocks.sort()
minX = rocks[0][0]
maxX = rocks[-1][0]
rocks.sort(key = lambda x: x[1])
maxY = rocks[-1][1]
print(minX)
print(maxX)
print(maxY)

sandStart = [500,0]

def findRestPlace(position):
	#print("Entering finding with position {}".format(position))
	if position[0] < minX or position[0]>maxX or position[1] == -1:
		return [position[0], -1]
	rocksUnder = []
	for rock in rocks:
		if rock[0] == position[0]:
			rocksUnder.append(rock)
	rocksUnder.sort(key = lambda x: x[1])
	for i,rock in enumerate(rocksUnder):
		if rock[1] > position[1]:
			break
	if rocksUnder[i][1] - position[1] > 1:
		return findRestPlace([position[0], rocksUnder[i][1] - 1])
	elif not [position[0]-1, position[1]+1] in rocks:
		return findRestPlace([position[0]-1, position[1]+1])
	elif not [position[0]+1, position[1]+1] in rocks:
		return findRestPlace([position[0]+1, position[1]+1])
	else:
		return position

count = 0
while True:
	newSand = findRestPlace(sandStart)
	if newSand[1] == -1:
		break
	else:
		rocks.append(newSand)
		count +=1
print(count)

