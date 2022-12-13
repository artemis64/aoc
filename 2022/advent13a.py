file = open('input13.txt', 'r')

packageCounter = 0
orderedSum = 0

def findListEnd(string):
	brackets = 0
	for index, i in enumerate(string):
		if i == '[':
			brackets +=1
		elif i == ']':
			brackets -=1
		if brackets == 0:
			return index

def compareItems(first, second):
	print("Comparing items {} and {}".format(first, second))
	if type(first) == int and type(second) == int:
		if first < second:
			return 1
		elif first == second:
			return 0
		else:
			return -1
	elif type(first) == int:
		first = [ first ]
	elif type(second) == int:
		second = [ second ]
	return compareLists(first, second)

def compareLists(first, second):
	print("Comparing lists {} and {}".format(first, second))
	ordered = 0
	while len(first) > 0 and len(second) > 0 and ordered == 0:
		f = first.pop(0)
		s = second.pop(0)
		ordered = compareItems(f,s)
	if (ordered == 0 and len(first) < len(second)) or ordered == 1:
		return 1
	elif ordered == 0 and len(first) == len(second):
		return 0
	else:
		return -1

def getListItems(string): #input string inside the list
	items = []
	while len(string)>0:
		print(string)
		if string[0] == '[':
			end = findListEnd(string)
			items.append(getListItems(string[1:end]))
			string = string[end+1:]
			if len(string) > 0 and string[0] == ',':
				string = string[1:]
		else:
			i = 1
			while len(string) > i and not string[i] == ',':
				i +=1
			items.append(int(string[:i]))
			string = string[i+1:]
	return items


for line in file:
	packageCounter +=1
	first = line.strip()
	second = file.readline()
	second = second.strip()
	file.readline()
	first = getListItems(first[1:-1])
	second = getListItems(second[1:-1])
	print("Package pair no. {}".format(packageCounter))
	print(first)
	print(second)
	if compareLists(first, second) == 1:
		orderedSum += packageCounter
	print(orderedSum)


