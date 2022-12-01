file = open('input14.txt', 'r')
polymer = ''
mapa = [[],[]]
for line in file:
	thisLine = line.strip()
	if '->' in thisLine:
		mapa[0].append(thisLine[:2])
		mapa[1].append(thisLine[-1])
	elif thisLine != '':
		polymer = thisLine
file.close()

for step in range(10):
	add = []
	for i in range(len(polymer)):
		if polymer[i:i+2] in mapa[0]:
			add.append([i+1, mapa[1][mapa[0].index(polymer[i:i+2])]])
	add = sorted(add, key=lambda x: x[0])
	while len(add) > 0:
		inserting = add.pop()
		polymer = polymer[:inserting[0]] + inserting[1] + polymer[inserting[0]:]
	print("End of step {}".format(step + 1))

counts = [[], []]
for c in polymer:
	if c in counts[0]:
		counts[1][counts[0].index(c)] +=1
	else:
		counts[0].append(c)
		counts[1].append(1)
print(max(counts[1]) - min(counts[1]))