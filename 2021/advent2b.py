file = open('input2.txt', 'r')
vertical = 0
horizontal = 0
aim = 0
directions = []
for line in file:
    directions.append(line.split())
    
    directions[len(directions)-1][1] = int(directions[len(directions)-1][1])

file.close()

for move in directions:
	if move[0] == 'forward':
		horizontal = horizontal + move[1]
		vertical = vertical + aim * move[1]
	elif move[0] == 'down':
		aim = aim + move[1]
	else:
		aim = aim - move[1]

print("Final position is vertical: {} and horizontal: {}".format(vertical,horizontal))
print(vertical*horizontal)
