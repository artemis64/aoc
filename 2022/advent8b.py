file = open('input8.txt', 'r')

treeMap = []

for line in file:
	line = line.strip()
	line = [int(i) for i in line]
	treeMap.append(line)
print(treeMap)

maxScenicScore = 0


def checkScenicScore(row, col):
	scenicScore = [0, 0, 0, 0]
	for index in range(col-1, -1, -1):
		scenicScore[0] +=1
		if treeMap[row][col]<=treeMap[row][index]:
			break
	print("Scenic score left {} of tree at {}, {}".format(scenicScore[0], row, col))

	for index in range(col+1, len(treeMap[row])):
		scenicScore[1] +=1
		if treeMap[row][col]<=treeMap[row][index]:
			break
	print("Scenic score right {} of tree at {}, {}".format(scenicScore[1], row, col))

	for index in range(row-1, -1, -1):
		scenicScore[2] +=1
		if treeMap[row][col]<=treeMap[index][col]:
			break
	print("Scenic score top {} of tree at {}, {}".format(scenicScore[2], row, col))

	for index in range(row+1, len(treeMap)):
		scenicScore[3] +=1
		if treeMap[row][col]<=treeMap[index][col]:
			break
	print("Scenic score bottom {} of tree at {}, {}".format(scenicScore[2], row, col))


	scenicScore = scenicScore[0]*scenicScore[1]*scenicScore[2]*scenicScore[3]
	return scenicScore

for i in range(1,len(treeMap)-1):
	for j in range(1, len(treeMap[0])-1):
		print("Checking {} at the position {}, {}".format(treeMap[i][j], i, j))
		maxScenicScore = checkScenicScore(i, j) if checkScenicScore(i, j) > maxScenicScore else maxScenicScore

print(maxScenicScore)
