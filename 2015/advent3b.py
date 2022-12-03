def santaMove(positions, position, direction):
	if direction == '^':
			position[1] +=1
			if not position in positions:
				positions.append(position.copy())
	elif direction == 'v':
		position[1] -=1
		if not position in positions:
			positions.append(position.copy())
	elif direction == '<':
		position[0] -=1
		if not position in positions:
			positions.append(position.copy())
	else:
		position[0] +=1
		if not position in positions:
			positions.append(position.copy())
	return positions, position

file = open('input3.txt', 'r')

for line in file:
	line = line.strip()
	positions = [[0, 0]]
	position = [0, 0]
	RoboPosition = [0, 0]
	for i in range(len(line)):
		if i % 2 == 0:
			positions, position = santaMove(positions, position, line[i])
		else:
			positions, RoboPosition = santaMove(positions, RoboPosition, line[i])
		
	print(len(positions))

