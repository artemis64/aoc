file = open('input1.txt', 'r')

instructions = file.read().strip()
position = 1
floor = 0

for step in instructions:
	if step == '(':
		floor += 1
	else:
		floor -= 1
	if floor < 0:
		break
	else:
		position += 1

print(position)