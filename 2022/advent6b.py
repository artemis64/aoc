file = open('input6.txt', 'r')

for line in file:
	line = line.strip()
	four = ''
	for index in range(len(line)):
		if not line[index] in four:
			four = four + line[index]
			if len(four) == 14:
				print(index + 1)
				break
		else:
			sameIndex = four.index(line[index])
			four = four[(sameIndex + 1):] + line[index]

