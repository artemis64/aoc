def countLights(lights):
	count = 0
	for line in lights:
		for light in line:
			count += light
	return count

lights = [[0 for i in range(1000)] for j in range(1000)]

file = open('input6.txt', 'r')

for line in file:
	line = line.strip()
	line = line.split()
	action = line.pop(0)
	if action == 'turn':
		action += line.pop(0)
	start = line.pop(0).split(',')
	start = [int(i) for i in start]
	end = line.pop(-1).split(',')
	end = [int(i) for i in end]
	if action == 'turnon':
		for i in range(start[0], end[0]+1):
			for j in range(start[1], end[1]+1):
				lights[i][j] = 1
	elif action == 'toggle':
		for i in range(start[0], end[0]+1):
			for j in range(start[1], end[1]+1):
				lights[i][j] = (lights[i][j] + 1) % 2
	else:
		for i in range(start[0], end[0]+1):
			for j in range(start[1], end[1]+1):
				lights[i][j] = 0

print(countLights(lights))


