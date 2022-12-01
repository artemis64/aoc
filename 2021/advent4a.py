file = open('input4.txt', 'r')
drawnNumbers = file.readline().strip().split(",")
file.readline()
#if line.strip() == "": print ("new line")
boards = []
board = []
for line in file:
	line = line.strip()
	if line != "":
		board.append(line.split())
	else:
		boards.append(board)
		board = []
file.close()


markedSum = []
marked = []
for i in range(len(boards)):
	markedSum.append([0,0,0,0,0,0,0,0,0,0])
	marked.append([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

def return_solution():
	for num in drawnNumbers:
		for board in range(len(boards)):
			for row in range(5):
				for col in range(5):
					if num == boards[board][row][col]:
						markedSum[board][row] +=1
						markedSum[board][5 + col] +=1
						marked[board][row][col] = 1
						if markedSum[board][row] == 5 or markedSum[board][5 + col] == 5:

							sumUnmarked = 0
							for i in range(5):
								for j in range(5):
									if marked[board][i][j] == 0:
										sumUnmarked = sumUnmarked + int(boards[board][i][j])

							return(sumUnmarked*int(num))
							#print("win")
							#
							#print(sumUnmarked)
							#print(sumUnmarked*number)
print(return_solution())


						
