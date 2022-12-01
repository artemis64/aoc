file = open('input11.txt', 'r')
octopuses = []
for line in file:
	octopuses.append(list(line.strip()))
file.close()

for row in range(len(octopuses)):
	for col in range(len(octopuses[0])):
		octopuses[row][col] = int(octopuses[row][col])

i = 0
while True:
	i +=1
	count = 0
	flash = []
	for row in range(len(octopuses)):
		for col in range(len(octopuses[0])):
			octopuses[row][col] +=1
			if octopuses[row][col] > 9:
				flash = [[row,col]] + flash
	while len(flash) > 0:
		flashing = flash.pop()
		positions = [flashing[0]>0, flashing[0]<len(octopuses)-1, flashing[1]>0, flashing[1]<len(octopuses[0])-1]
		if positions[0]:
			octopuses[flashing[0]-1][flashing[1]] +=1
			if octopuses[flashing[0]-1][flashing[1]] == 10:
				flash = [[flashing[0]-1, flashing[1]]] + flash
			if positions[2]:
				octopuses[flashing[0]-1][flashing[1]-1] +=1
				if octopuses[flashing[0]-1][flashing[1]-1] == 10:
					flash = [[flashing[0]-1, flashing[1]-1]] + flash
			if positions[3]:
				octopuses[flashing[0]-1][flashing[1]+1] +=1
				if octopuses[flashing[0]-1][flashing[1]+1] == 10:
					flash = [[flashing[0]-1, flashing[1]+1]] + flash
		if positions[1]:
			octopuses[flashing[0]+1][flashing[1]] +=1
			if octopuses[flashing[0]+1][flashing[1]] == 10:
				flash = [[flashing[0]+1, flashing[1]]] + flash
			if positions[2]:
				octopuses[flashing[0]+1][flashing[1]-1] +=1
				if octopuses[flashing[0]+1][flashing[1]-1] == 10:
					flash = [[flashing[0]+1, flashing[1]-1]] + flash
			if positions[3]:
				octopuses[flashing[0]+1][flashing[1]+1] +=1
				if octopuses[flashing[0]+1][flashing[1]+1] == 10:
					flash = [[flashing[0]+1, flashing[1]+1]] + flash
		if positions[2]:
			octopuses[flashing[0]][flashing[1]-1] +=1
			if octopuses[flashing[0]][flashing[1]-1] == 10:
				flash = [[flashing[0], flashing[1]-1]] + flash
		if positions[3]:
			octopuses[flashing[0]][flashing[1]+1] +=1
			if octopuses[flashing[0]][flashing[1]+1] == 10:
				flash = [[flashing[0], flashing[1]+1]] + flash
	print("count {}".format(count))
	for row in range(len(octopuses)):
		for col in range(len(octopuses[0])):
			if octopuses[row][col] > 9:
				octopuses[row][col] = 0
				count +=1
	print(count)
	if count == len(octopuses) * len(octopuses[0]):
		print(i)
		break


