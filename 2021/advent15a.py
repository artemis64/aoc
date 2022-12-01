file = open('input15.txt', 'r')
mapa = []
for line in file:
	thisLine = line.strip()
	if thisLine:
		list(thisLine)
		thisLine = [ int(x) for x in thisLine ]
		mapa.append(thisLine)
file.close()

counts = []
for _ in range(len(mapa)):
	counts.append([1000000] * len(mapa[0]))

counts[0][0] = 0
for row in range(len(counts)):
	for col in range(len(counts[0])):
		if col > 0 and counts[row][col-1] > counts[row][col] + mapa[row][col-1]:
			counts[row][col-1] = counts[row][col] + mapa[row][col-1]
		if col < len(counts[0])-1 and counts[row][col+1] > counts[row][col] + mapa[row][col+1]:
			counts[row][col+1] = counts[row][col] + mapa[row][col+1]
		if row > 0 and counts[row-1][col] > counts[row][col] + mapa[row-1][col]:
			counts[row-1][col] = counts[row][col] + mapa[row-1][col]
		if row < len(counts)-1 and counts[row+1][col] > counts[row][col] + mapa[row+1][col]:
			counts[row+1][col] = counts[row][col] + mapa[row+1][col]

print(counts[-1][-1])