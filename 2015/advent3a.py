file = open('input3.txt', 'r')

for line in file:
	line = line.strip()
	positions = [[0, 0]]
	position = [0, 0]
	for direction in line:
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
	print(len(positions))

