file = open('input7.txt', "r") 
crabPositions = file.readline().strip().split(",")
file.close()

for i in range(len(crabPositions)):
	crabPositions[i] = int(crabPositions[i])

start = min(crabPositions)
end = max(crabPositions)

summs = []

for B in range(start, end + 1):
	summ = 0
	for position in crabPositions:
		summ = summ + (abs(B-position) * (abs(B-position) + 1)) / 2
	summs.append(summ)

print(min(summs))