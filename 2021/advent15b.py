file = open('input15.txt', 'r')
tile = []
for line in file:
	thisLine = line.strip()
	if thisLine:
		list(thisLine)
		thisLine = [ int(x) for x in thisLine ]
		tile.append(thisLine)
file.close()


mapa = [ [0]* (5*len(tile[0])) for _ in xrange(5*len(tile)) ]

for i in range(5):
	for j in range(5):
		for row in range(len(tile)):
			for col in range(len(tile[0])):
				mapa[i*len(tile) + row][j*len(tile[0])+col] = (tile[row][col] + i + j) % 9 if tile[row][col] + i + j != 9 else 9

counts = []
for _ in range(len(mapa)):
	counts.append([1000000] * len(mapa[0]))

counts[0][0] = 0
toCheck = [[0,0]]
while len(toCheck) > 0:
	[row, col] = toCheck.pop()
	if col > 0 and counts[row][col-1] > counts[row][col] + mapa[row][col-1]:
		counts[row][col-1] = counts[row][col] + mapa[row][col-1]
		if [row, col-1] not in toCheck:
			toCheck = [[row, col-1]] + toCheck
	if col < len(counts[0])-1 and counts[row][col+1] > counts[row][col] + mapa[row][col+1]:
		counts[row][col+1] = counts[row][col] + mapa[row][col+1]
		if [row, col+1] not in toCheck:
			toCheck = [[row, col+1]] + toCheck
	if row > 0 and counts[row-1][col] > counts[row][col] + mapa[row-1][col]:
		counts[row-1][col] = counts[row][col] + mapa[row-1][col]
		if [row-1, col] not in toCheck:
			toCheck = [[row-1, col]] + toCheck
	if row < len(counts)-1 and counts[row+1][col] > counts[row][col] + mapa[row+1][col]:
		counts[row+1][col] = counts[row][col] + mapa[row+1][col]
		if [row+1, col] not in toCheck:
			toCheck = [[row+1, col]] + toCheck
	print(len(toCheck))
	print("row {} col {}".format(row, col))

print(counts[-1][-1])

