file = open('input9.txt', 'r')
steps = []

for line in file:
	line = line.strip()
	line = line.split()
	line[1] = int(line[1])
	steps.append(line)

dimensions = [0, 0, 0, 0] #right, left, up, down
current = [0, 0]

for step in steps:
	if step[0] == 'R':
		current[0] += step[1]
		if current[0] > dimensions[0]:
			dimensions[0] = current[0]
	elif step[0] == 'L':
		current[0] -= step[1]
		if current[0] < dimensions[1]:
			dimensions[1] = current[0]
	elif step[0] == 'U':
		current[1] += step[1]
		if current[1] > dimensions[2]:
			dimensions[2] = current[1]
	elif step[0] == 'D':
		current[1] -= step[1]
		if current[1] < dimensions[3]:
			dimensions[3] = current[1]

print(dimensions)

visited = [] #first - up down, second - left right

for i in range(dimensions[2] - dimensions[3] + 1):
	visitedLine = []
	for j in range(dimensions[0] - dimensions[1] + 1):
		visitedLine.append(0)
	visited.append(visitedLine)
visited[0][0] = 1

def moveHead(head, direction):
	if direction == 'R':
		head[0] +=1
	elif direction == 'L':
		head[0] -=1
	elif direction == 'U':
		head[1] +=1
	elif direction == 'D':
		head[1] -=1
	return head

def moveTail(tail, head):
	if head[0] == tail[0]:
		if abs(head[1] - tail[1]) > 1:
			if head[1] > tail[1]:
				tail[1] +=1
			else:
				tail[1] -=1
	elif head[1] == tail[1]:
		if abs(head[0] - tail[0]) > 1:
			if head[0] > tail[0]:
				tail[0] +=1
			else:
				tail[0] -=1
	elif abs(head[1] - tail[1]) + abs(head[0] - tail[0]) > 2:
		if head[0] > tail[0]:
			tail[0] +=1
		else:
			tail[0] -=1
		if head[1] > tail[1]:
			tail[1] +=1
		else:
			tail[1] -=1
	return tail

knots = []

for i in range(10):
	knots.append([0,0])

for step in steps:
	for i in range(step[1]):
		knots[0] = moveHead(knots[0], step[0])
		for i in range(1,10):
			knots[i] = moveTail(knots[i], knots[i-1])
		visited[knots[-1][1]][knots[-1][0]] = 1

visitedPlaces = 0
for i in range(len(visited)):
	for j in range(len(visited[0])):
		visitedPlaces += visited[i][j]

print(knots)
print(visitedPlaces)