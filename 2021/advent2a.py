file = open('input2.txt', 'r')
vertical = 0
horizontal = 0
directions = []
up = 0
down = 0
forward = 0
for line in file:
    directions.append(line.split())
    
    directions[len(directions)-1][1] = int(directions[len(directions)-1][1])

file.close()

for move in directions:
	if move[0] == 'forward':
		horizontal = horizontal + move[1]
		forward += 1
	elif move[0] == 'down':
		vertical = vertical + move[1]
		down += 1
	else:
		vertical = vertical - move[1]
		up += 1

print("Final position is vertical: {} and horizontal: {}".format(vertical,horizontal))
print("In total we moved {} times forward, {} times up and {} times down".format(forward,up, down))
print(vertical*horizontal)

