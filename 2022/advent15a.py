file = open('input15.txt', 'r')
yVIP = 2000000
noBeacon = [] #list of closed intervals

def manageIntervals(intervals):
	intervals.sort()
	for index in range(len(intervals)-1):
		if intervals[index][1] >= intervals[index + 1][0]:
			intervals[index] = [intervals[index][0], max(intervals[index][1], intervals[index + 1][1])]
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
	if sensor[1] - distance <= yVIP and yVIP <= sensor[1] + distance:
		noBeaconInterval = [sensor[0] - distance + abs(sensor[1] - yVIP),  sensor[0] + distance - abs(sensor[1] - yVIP)]
		intervalDistance = 2 * (distance - abs(sensor[1] - yVIP)) + 1
		if not abs(noBeaconInterval[1] - noBeaconInterval[0]) + 1 == intervalDistance:
			print("Error - interval distance {}, interval {}, distance {}".format(intervalDistance, noBeaconInterval, distance))
		if beacon[1] == yVIP:
			if beacon[0] == noBeaconInterval[0] and intervalDistance == 1:
				noBeaconInterval = []
			elif beacon[0] == noBeaconInterval[0]:
				noBeaconInterval[0] = beacon[0] + 1
			else:
				noBeaconInterval[1] = beacon[0] - 1
		print(noBeaconInterval)
		if len(noBeaconInterval) > 0:
			noBeacon.append(noBeaconInterval)
			noBeacon = manageIntervals(noBeacon)

count = 0
for interval in noBeacon:
	count = count + (interval[1] - interval[0]) + 1
print(count)

