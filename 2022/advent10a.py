file = open('input10.txt', 'r')

X = 1
cycle = 0
mesureCycles = [20, 60, 100, 140, 180, 220]
signalStrenth = 0

for line in file:
	line = line.strip()
	line = line.split()
	if len(line) > 1:
		cycle +=1
		#print("At the beginning of the cycle {} X is {} same as at the end".format(cycle, X))
		if cycle in mesureCycles:
			print("Signal strenth during the cycle {} is {}".format(cycle, cycle*X))
			signalStrenth += cycle*X
		cycle +=1
		#print("At the beginning of the cycle {} X is {}".format(cycle, X))
		if cycle in mesureCycles:
			print("Signal strenth during the cycle {} is {}".format(cycle, cycle*X))
			signalStrenth += cycle*X
		X += int(line[1])
		#print("At the end of the cycle {} X is {}".format(cycle, X))
	else:
		cycle +=1
		#print("At the beginning of the cycle {} X is {} same as at the end".format(cycle, X))
		if cycle in mesureCycles:
			print("Signal strenth during the cycle {} is {}".format(cycle, cycle*X))
			signalStrenth += cycle*X
print(signalStrenth)
print(cycle)