file = open('input9.txt', 'r')
matrix = []
for line in file:
	matrix.append(line.strip())
file.close()


def returnRisk(row, col):
	if (col > 0 and matrix[row][col - 1] > matrix[row][col]) or col == 0:
		if (col < len(matrix[row]) - 1 and matrix[row][col + 1] > matrix[row][col]) or col == len(matrix[row]) - 1:
			if (row > 0 and matrix[row-1][col] > matrix[row][col]) or row == 0:
				if (row < len(matrix) - 1 and matrix[row + 1][col] > matrix[row][col]) or row == len(matrix) - 1:
					return (int(matrix[row][col]) + 1)

	return 0

basinSizes = []
for row in range(len(matrix)):
	for col in range(len(matrix[0])):
		if returnRisk(row,col) > 0:
			basin = []
			goToNext = [[row, col]]
			saw = [[row, col]]
			while len(goToNext) > 0:
				checking = goToNext.pop()

				if checking[0] > 0 and matrix[checking[0]-1][checking[1]] != "9" and [checking[0]-1, checking[1]] not in saw:
					goToNext = [[checking[0]-1, checking[1]]] + goToNext
					saw.append([checking[0]-1, checking[1]])
				if checking[0]+1 < len(matrix) and matrix[checking[0]+1][checking[1]] != "9" and [checking[0]+1, checking[1]] not in saw:
					goToNext = [[checking[0]+1, checking[1]]] + goToNext
					saw.append([checking[0]+1, checking[1]])
				if checking[1] > 0 and matrix[checking[0]][checking[1]-1] != "9" and [checking[0], checking[1]-1] not in saw:
					goToNext = [[checking[0], checking[1]-1]] + goToNext
					saw.append([checking[0], checking[1]-1])
				if checking[1]+1 < len(matrix[0]) and matrix[checking[0]][checking[1]+1] != "9" and [checking[0], checking[1]+1] not in saw:
					goToNext = [[checking[0], checking[1]+1]] + goToNext
					saw.append([checking[0], checking[1]+1])

				if checking not in basin:
					basin.append(checking)
			basinSizes.append(len(basin))

basinSizes.sort()
multip = 1
for i in range(3):
	multip = multip * basinSizes.pop()
print(multip)




