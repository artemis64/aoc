file = open('input14.txt', 'r')
rocks = []												#min X needs to be bigger than the source of sand
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

rocks.sort(key = lambda x: x[1])
maxY = rocks[-1][1] + 2

positions = [[500, 0, 0]]
count = 0

def moveSand(count):
	positionX = positions[-1][0]
	positionY = positions[-1][1]
	direction = positions[-1][2]
	if positionY + 1 < maxY:
		if direction == 0 and not [positionX, positionY + 1] in rocks:
			positions[-1][2] = 1
			positions.append([positionX, positionY + 1, 0])
		elif direction <= 1 and not [positionX - 1, positionY + 1] in rocks:
			positions[-1][2] = 2
			positions.append([positionX - 1, positionY + 1, 0])
		elif direction <= 2 and not [positionX + 1, positionY + 1] in rocks:
			positions[-1][2] = 3
			positions.append([positionX + 1, positionY + 1, 0])
		else:
			rocks.append([positionX, positionY])
			positions.pop(-1)
			count +=1
	else:
		rocks.append([positionX, positionY])
		positions.pop(-1)
		count +=1
	return count

while len(positions) > 0:
	count = moveSand(count)
	print(count)
	

