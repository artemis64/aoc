file = open('input19test2D.txt', 'r')
scanners = []

for line in file:
	line = line.strip()
	if len(line) > 0:
		if line[0:3] == '---':
			scanners.append([])
			#print(line[12])
		else:
			line = line.split(',')
			line = [int(i) for i in line]
			scanners[-1].append(line)
print(scanners)