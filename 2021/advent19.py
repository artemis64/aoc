file = open('input19test.txt', 'r')
scanners = []
scanner = []
for line in file:
	thisLine = line.strip()
	if '---' in thisLine:
		if len(scanner) > 0:
			scanners.append(scanner)
		scanner = []
	elif thisLine != '':
		thisLine = thisLine.split(',')
		thisLine = [ int(x) for x in thisLine ]
		scanner.append(tuple(thisLine))
scanners.append(scanner)
file.close()

def beaconDistance(beacon1, beacon2):
	distance = []
	distance.append(beacon1[0]-beacon2[0])
	distance.append(beacon1[1]-beacon2[1])
	distance.append(beacon1[2]-beacon2[2])
	return tuple(distance)

def containSameElements(list1, list2):
	count = 0
	for el in list1:
		if el in list2:
			count +=1
	return count

relativePositions = []

for s in range(len(scanners)):
	scanner = []
	for b in range(len(scanners[s])):
		beacons = []
		for b2 in range(len(scanners[s])):
			if b != b2:
				beacons.append(beaconDistance(scanners[s][b], scanners[s][b2]))
		scanner.append(beacons)
	relativePositions.append(scanner)

relativePositionsSorted = []
for s in relativePositions:
	scanner = []
	for b in s:
		beacon = []
		for l in b:
			sor = list(l)
			sor = [ abs(x) for x in sor ]
			beacon.append(tuple(sorted(sor)))
		scanner.append(beacon)
	relativePositionsSorted.append(scanner)	

end = False
for s1 in range(len(relativePositionsSorted)):
	for s2 in range(len(relativePositionsSorted)):
		for b1 in renge(len(relativePositionsSorted[s1])):
			for b2 in renge(len(relativePositionsSorted[s2])):
				if not end and s1 != s2:
					end = True if containSameElements(relativePositionsSorted[s1][b1], relativePositionsSorted[s2][b2]) > 10
				if end:
					for i in len(relativePositionsSorted[s1][b1]):
						if relativePositionsSorted[s1][b1][i] in relativePositionsSorted[s2][b2]:
							j = relativePositionsSorted[s2][b2].index(relativePositionsSorted[s1][b1][i])

