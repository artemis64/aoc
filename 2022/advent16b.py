file = open('input16test.txt', 'r')
valves = []
nonZeroValves = []
valveNames = []

for line in file:
	line = line.strip()
	line = line.split()
	leadsTo = line[9:]
	for i in range(len(leadsTo)-1):
		leadsTo[i] = leadsTo[i][:-1]
	valve = dict(name = line[1], rate = int(line[4][5:-1]), leadsTo = leadsTo)
	valveNames.append(valve['name'])
	valves.append(valve)
valves.sort(key = lambda x: x['name'])
valveNames.sort()

mapa = [] #i, j - distance from i to j
for i in range(len(valves)):
	mapLine = []
	for j in range(len(valves)):
		mapLine.append(-1)
	mapa.append(mapLine)

for i in range(len(mapa)):
	mapa[i][i] = 0

for distance in range(1, len(mapa)+1):
	for i in range(len(mapa)):
		for j in range(len(mapa[0])):
			if mapa[i][j] == distance - 1:
				for where in valves[j]['leadsTo']:
					if mapa[i][valveNames.index(where)] == -1 or mapa[i][valveNames.index(where)] > mapa[i][j] + 1:
						mapa[i][valveNames.index(where)] = mapa[i][j] + 1



for i, valve in enumerate(valves):
	if valve['rate'] > 0:
		nonZeroValves.append(i)
toCheck = [[[0, 0, 26, [0]], [0, 0, 26, [0]]]] # 0 -ja [0 - index valve, 1 - potential release, 2 - time remain, 3 indices of opened valves], 1 elephant
maxPressure = 0
while len(toCheck) > 0:
	checkingMe = toCheck.pop(0)
	checkingEl = checking[1]
	checkingMe = checking[0]
	if checkingMe[1]+ checkingEl[1] > maxPressure:
		maxPressure = checkingMe[1]+ checkingEl[1]
	for meGointTo in nonZeroValves:
		if not gointTo == checking[0] and not gointTo in checking[3]:
			cesta = mapa[checking[0]][gointTo]
			if checking[2] - cesta - 1 >= 0:
				openedValves = checking[3].copy()
				openedValves.append(gointTo)
				toCheck.append([gointTo, checking[1] + (checking[2] - cesta - 1)*valves[gointTo]['rate'], checking[2] - cesta - 1, openedValves])

for i in mapa:
	print(i)

print(maxPressure)
