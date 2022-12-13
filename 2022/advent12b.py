import string

file = open('input12.txt', 'r')
alphabet = list(string.ascii_lowercase)
hightMap = []

for line in file:
	line = line.strip()
	hightMap.append(list(line))

starts = []
for i in range(len(hightMap)):
	for j in range(len(hightMap[0])):
		if hightMap[i][j] == 'S':
			hightMap[i][j] = 'a'
		if hightMap[i][j] == 'E':
			end = [i, j]
			hightMap[i][j] = 'z'
		if hightMap[i][j] =='a':
			starts.append([i,j])

for i in range(len(hightMap)):
	for j in range(len(hightMap[0])):			
		hightMap[i][j] = alphabet.index(hightMap[i][j])
max0 = len(hightMap)-1
max1 = len(hightMap[0])-1

def moving(currentPosition, hight):
	if currentPosition[0] > 0:
		if hightMap[currentPosition[0]-1][currentPosition[1]] <= hight + 1:
			yield [currentPosition[0]-1, currentPosition[1]]
	if currentPosition[0] < max0:
		if hightMap[currentPosition[0]+1][currentPosition[1]] <= hight + 1:
			yield [currentPosition[0]+1, currentPosition[1]]
	if currentPosition[1] > 0:
		if hightMap[currentPosition[0]][currentPosition[1]-1] <= hight + 1:
			yield [currentPosition[0], currentPosition[1]-1]
	if currentPosition[1] < max1:
		if hightMap[currentPosition[0]][currentPosition[1]+1] <= hight + 1:
			yield [currentPosition[0], currentPosition[1]+1]




minHike = len(hightMap)*len(hightMap[0])

while len(starts)>0:
	start = starts.pop(0)
	visitedMap = []
	for i in range(len(hightMap)):
		visitedLine = []
		for j in range(len(hightMap[0])):
			visitedLine.append(len(hightMap)*len(hightMap[0]))
		visitedMap.append(visitedLine)
	visitedMap[start[0]][start[1]] = 0
	positions = [ start ]

	while len(positions)>0:
		currentPosition = positions.pop(0)
		moves = moving(currentPosition, hightMap[currentPosition[0]][currentPosition[1]])
		moves = list(moves)
		for move in moves:
			if visitedMap[move[0]][move[1]] > visitedMap[currentPosition[0]][currentPosition[1]]+1:
				visitedMap[move[0]][move[1]] = visitedMap[currentPosition[0]][currentPosition[1]]+1
				positions.append(move)
	if minHike > visitedMap[end[0]][end[1]]:
		minHike = visitedMap[end[0]][end[1]]

print(minHike)