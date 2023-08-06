import copy
file = open('input17test.txt', 'r')

jetPattern = file.readline()
jetPattern = jetPattern.strip()

cave = [0, 0, 0, 0, 0, 0, 0]
fallingRocks = [[[2,0,1], [3,0,1], [4,0,1], [5,0,1]], [[2,1,1], [3,0,3], [4,1,1]], [[2,0,1], [3,0,1], [4,0,3]], [[2,0,4]], [[2,0,2], [3,0,2]]] #inside rocks 0- 4, inside each rock - list for each column 0 - column at the beginning, 1 - empty under in the coulumn, 2 - hight
rockCount = 0 #rock that will fall from falling rocks is mod 5
jetCount = 0 #jet that would be used from jetPattern is mod len(jetPattern)
caveDetail = [[0], [0], [0], [0], [0], [0], [0]]

while rockCount < 2022:
	rock = copy.deepcopy(fallingRocks[rockCount % 5])
	print("Rock start {}".format(rock))
	maxHight = max(cave)
	for i in rock:
		i[1] = i[1] + maxHight + 4
	#ready to begin the fall
	rest = False
	
	while not rest: #TODO the moving and falling
		print(jetPattern[jetCount % len(jetPattern)])
		if jetPattern[jetCount % len(jetPattern)] == '<' and rock[0][0]>0:
			canGo = True
			for i in range(rock[0][1], rock[0][1] + rock[0][2]):
				if i in caveDetail[rock[0][0] - 1]:
					canGo = False
					break
			if canGo:
				for i in rock:
					i[0] -=1
		elif jetPattern[jetCount % len(jetPattern)] == '>' and rock[-1][0]<6:
			canGo = True
			for i in range(rock[-1][1], rock[-1][1] + rock[-1][2]):
				if i in caveDetail[rock[-1][0] + 1]:
					canGo = False
					break
			if canGo:
				for i in rock:
					i[0] +=1
		
		jetCount +=1
		for i in rock:
			if i[1] - 1 in  caveDetail[i[0]]:
				rest = True
				break
		if not rest:
			for i in rock:
				i[1] -=1
		print(rock)


	for i in rock:
		cave[i[0]] = max(cave[i[0]], i[1] + i[2] - 1)
		for j in range(i[1], i[1] + i[2]):
			caveDetail[i[0]].append(j)
	rockCount +=1

print(max(cave))	


