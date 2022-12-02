def scoreTheShape(shape):
	if shape == "X" or shape == "A":
		return 1
	elif shape == "Y" or shape == "B":
		return 2
	elif shape == "Z" or shape == "C":
		return 3
	else:
		print("Error in the shape scoring.")

def getTheScore(oponent, me):
	if oponent == me:
		return (3 + me)
	if abs(oponent - me) == 1:
		if oponent > me:
			return me
		else:
			return (6 + me)
	else:
		if oponent > me:
			return (6 + me)
		else:
			return me



file = open('input2.txt', 'r')

score = 0

for line in file:
	score += getTheScore(scoreTheShape(line[0]), scoreTheShape(line[2]))
print(score)