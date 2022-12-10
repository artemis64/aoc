file = open('input8.txt', 'r')

treeMap = []

for line in file:
	line = line.strip()
	line = [int(i) for i in line]
	treeMap.append(line)
print(treeMap)

visible = 2*len(treeMap) + 2*(len(treeMap[0])-2)
print(visible)

def checkVisibility(row, col, treeHight):
	stillVisible = True
	for index, tree in enumerate(treeMap[row]):
		if index < col and stillVisible:
			stillVisible = True if tree < treeHight else False
		elif index > col and stillVisible:
			stillVisible = True if tree < treeHight else False
		elif index == col:
			if stillVisible:
				print("Tree hight {} at the position {}, {} is visible from the left".format(treeHight, row, col))
				return True #can se from left
			stillVisible = True
	if stillVisible:
		print("Tree hight {} at the position {}, {} is visible from the right".format(treeHight, row, col))
		return True #can see from right

	stillVisible = True
	for index, treeLine in enumerate(treeMap):
		if index < row and stillVisible:
			stillVisible = True if treeLine[col] < treeHight else False
		elif index > row and stillVisible:
			stillVisible = True if treeLine[col] < treeHight else False
		elif index == row:
			if stillVisible:
				print("Tree hight {} at the position {}, {} is visible from the top".format(treeHight, row, col))
				return True #can se from top
			stillVisible = True
	if stillVisible:
		print("Tree hight{} at the position {}, {} is visible from the bottom".format(treeHight, row, col))
		return True #can see from bottom
	return False

for i in range(1,len(treeMap)-1):
	for j in range(1, len(treeMap[0])-1):
		print("Checking {} at the position {}, {}".format(treeMap[i][j], i, j))
		if checkVisibility(i, j, treeMap[i][j]):
			visible +=1
print(visible)
