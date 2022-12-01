file = open('input13.txt', 'r')
dots = []
folds = []
for line in file:
	thisLine = line.strip()
	if thisLine.startswith('fold') :
		fold = thisLine.split()[-1]
		fold = [fold[0], int(fold[2:])]
		folds.append(fold)
	elif thisLine == '':
		pass
	else:
		dot = 	thisLine.split(',')
		dot = [ int(x) for x in dot ]
		dots.append(dot)
file.close()


while len(folds) > 0:
	fold = folds.pop(0)
	dimension = 0 if fold[0] == 'x' else 1
	for dot in dots:
		if dot[dimension] > fold[1]:
			dot[dimension] = fold[1]*2 - dot[dimension]

	toRemove = []
	for i in range(len(dots)):
		for j in range(len(dots)):
			if i!=j and dots[i] == dots[j] and i not in toRemove:
				toRemove.append(j)
	toRemove = sorted(toRemove)
	while len(toRemove) > 0:
		dots.pop(toRemove.pop())
dots = sorted(dots, key=lambda x: x[1])
maxY = dots[-1][1]
dots = sorted(dots, key=lambda x: x[0])
maxX = dots[-1][0]
print(maxX)
print(maxY)
display = []
for y in range(maxY+1):
	line = ''
	for x in range(maxX+1):
		line = line + '.'
	line = list(line)
	display.append(line)

for dot in dots:
	display[dot[1]][dot[0]] = '#'

for y in range(maxY+1):
	print(display[y])