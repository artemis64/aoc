file = open('input7.txt', "r") 
crabPositions = file.readline().strip().split(",")
file.close()

for i in range(len(crabPositions)):
	crabPositions[i] = int(crabPositions[i])

def computeSum(position):
	summa = 0
	for crab in crabPositions:
		summa = summa + abs(crab - position)
	return summa

start = [min(crabPositions), computeSum(min(crabPositions))]
end = [max(crabPositions), computeSum(max(crabPositions))]
point1 = [end[0] / 3, computeSum(end[0] / 3)]
point2 = [2 * (end[0] / 3), computeSum(2 * (end[0] / 3))]

while end[0] - start[0] > 1:
	changes = []
	changes.append(True if start[1] < point1[1] else False)
	changes.append(True if point1[1] < point2[1] else False)
	changes.append(True if point2[1] < end[1] else False)
	
	if changes[0] != changes[1]:
		if point1[0] - start[0] > point2[0] - point1[0]:
			end = point2
			point2 = point1
			point1 = [start[0] + (point2[0]-start[0])/2, computeSum(start[0] + (point2[0]-start[0])/2)]
		else:
			end = point2
			point2 = [point1[0] + (point2[0] - point1[0]) / 2, computeSum(point1[0] + (point2[0] - point1[0]) / 2)]
	elif changes[1] != changes[2]:
		if point2[0] - point1[0] > end[0] - point2[0]:
			start = point1
			point1 = [start[0] + (point2[0] - start[0]) / 2, computeSum(start[0] + (point2[0] - start[0]) / 2)]
		else:
			start = point1
			point1 = point2
			point2 = [point1[0] + (end[0] - point1[0]) / 2, computeSum(point1[0] + (end[0] - point1[0]) / 2)]
	else:
		if end[1] > start[1]:
			if point1[0] - start[0] > point2[0] - point1[0]:
				end = point2
				point2 = point1
				point1 = [start[0] + (point2[0]-start[0])/2, computeSum(start[0] + (point2[0]-start[0])/2)]
			else:
				end = point2
				point2 = [point1[0] + (point2[0] - point1[0]) / 2, computeSum(point1[0] + (point2[0] - point1[0]) / 2)]
		else:
			if point2[0] - point1[0] > end[0] - point2[0]:
				start = point1
				point1 = [start[0] + (point2[0] - start[0]) / 2, computeSum(start[0] + (point2[0] - start[0]) / 2)]
			else:
				start = point1
				point1 = point2
				point2 = [point1[0] + (end[0] - point1[0]) / 2, computeSum(point1[0] + (end[0] - point1[0]) / 2)]




print(min(start[1], end[1], point1[1], point2[1]))