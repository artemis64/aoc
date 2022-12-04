def checkContains(smaller, bigger):
	if bigger[0] <= smaller[0] and bigger[1] >= smaller[1]:
		return True
	return False

containsCount = 0

file = open('input4.txt', 'r')

for line in file:
	line = line.strip()
	line = line.split(',')
	line = [i.split('-') for i in line]
	assignements = []
	for elf in line:
		assignements.append([int(i) for i in elf])
	if assignements[0][1] - assignements[0][0] > assignements[1][1] - assignements[1][0]:
		if checkContains(assignements[1], assignements[0]):
			containsCount +=1
	else: 
		if checkContains(assignements[0], assignements[1]):
			containsCount +=1
print(containsCount)