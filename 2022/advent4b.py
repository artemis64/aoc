def checkOverlap(first, second):
	if first[1] >= second[0]:
		return True
	return False

overlapCount = 0

file = open('input4.txt', 'r')

for line in file:
	line = line.strip()
	line = line.split(',')
	line = [i.split('-') for i in line]
	assignements = []
	for elf in line:
		assignements.append([int(i) for i in elf])
	if assignements[0][0] > assignements[1][0]:
		#print("second starts sooner")
		if checkOverlap(assignements[1], assignements[0]):
			overlapCount +=1
	else:
		#print("starts the same or first sooner")
		if checkOverlap(assignements[0], assignements[1]):
			overlapCount +=1
print(overlapCount)