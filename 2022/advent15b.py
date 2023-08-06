file = open('input15.txt', 'r')
maxCoordinate = 4000000
noBeacon = [] #list of closed intervals
for i in range(maxCoordinate + 1):
	noBeacon.append([])

def manageIntervals(intervals):
	intervals.sort()
	for index in range(len(intervals)-1):
		if intervals[index][1] >= intervals[index + 1][0]:
			intervals[index] = [intervals[index][0], max(intervals[index][1], intervals[index + 1][1])]
			intervals.pop(index + 1)
			intervals = manageIntervals(intervals)
			break
		elif intervals[index][1] + 1 == intervals[index + 1][0]:
			intervals[index] = [intervals[index][0], intervals[index + 1][1]]
			intervals.pop(index + 1)
			intervals = manageIntervals(intervals)
			break
	return intervals

for line in file:
	line = line.strip()
	line = line.split()
	sensor = [int(line[2][2:-1]), int(line[3][2:-1])]
	beacon = [int(line[8][2:-1]), int(line[9][2:])]
	print("sensor {}, beacon {}".format(sensor,beacon))
	distance = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
	if sensor[1] - distance <= maxCoordinate and 0 <= sensor[1] + distance:
		for i in range(max(sensor[1] - distance, 0), min(sensor[1] + distance, maxCoordinate)+1):
			noBeaconInterval = [sensor[0] - distance + abs(sensor[1] - i),  sensor[0] + distance - abs(sensor[1] - i)]
			intervalDistance = 2 * (distance - abs(sensor[1] - i)) + 1
			if not abs(noBeaconInterval[1] - noBeaconInterval[0]) + 1 == intervalDistance:
				print("Error - interval distance {}, interval {}, distance {}".format(intervalDistance, noBeaconInterval, distance))
			noBeaconInterval = [max(noBeaconInterval[0],0), min(noBeaconInterval[1], maxCoordinate)]
			if not noBeaconInterval[0] > noBeaconInterval[1]:
				noBeacon[i].append(noBeaconInterval)
				noBeacon[i] = manageIntervals(noBeacon[i])
tuningFrequency = 0
for i, line in enumerate(noBeacon):
	if len(line) > 1:
		tuningFrequency = (line[0][1] + 1) * 4000000 + i
		index = [line[0][1] + 1, i]
		break
print(index)
print(tuningFrequency)

