def scoreTheShape(shape):
	if shape == "A":
		return 1
	elif shape == "B":
		return 2
	elif shape == "C":
		return 3
	else:
		print("Error in the shape scoring.")

def scoreTheResult(result):
	if result == "X":
		return 0
	elif result == "Y":
		return 3
	elif result == "Z":
		return 6
	else:
		print("Error in the result scoring.")

def getTheScore(oponent, result):
	if result == 0:
		if oponent - 1 > 0:
			return (result + oponent - 1)
		else:
			return (result + 3)
	elif result == 3:
		return (result + oponent)
	else:
		if oponent + 1 > 3:
			return (result + 1)
		else: 
			return (result + oponent + 1)



file = open('input2.txt', 'r')

score = 0

for line in file:
	score += getTheScore(scoreTheShape(line[0]), scoreTheResult(line[2]))
print(score)