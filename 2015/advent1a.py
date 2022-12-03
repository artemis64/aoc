file = open('input1.txt', 'r')

instructions = file.read().strip()
floor = 0

for step in instructions:
	if step == '(':
		floor += 1
	else:
		floor -= 1

print(floor)