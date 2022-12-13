import copy
file = open('input13.txt', 'r')

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

packages = []
for line in file:
	first = line.strip()
	second = file.readline()
	second = second.strip()
	file.readline()
	first = getListItems(first[1:-1])
	second = getListItems(second[1:-1])
	packages.append(first)
	packages.append(second)

dividerPacket1 = [[2]]
dividerPacket2 = [[6]]

dividerPacket1Position = 1
dividerPacket2Position = 2

for package in packages:
	print(package)
	if compareLists(copy.deepcopy(package), copy.deepcopy(dividerPacket1)) == 1:
		print("Pacakge {} is smaller than devider package [[2]]".format(package))
		dividerPacket1Position +=1
		dividerPacket2Position +=1
	elif compareLists(copy.deepcopy(package), copy.deepcopy(dividerPacket2)) == 1:
		print("Pacakge {} is smaller than devider package [[6]]".format(package))
		dividerPacket2Position +=1

print(dividerPacket1Position)
print(dividerPacket2Position)
print(dividerPacket1Position*dividerPacket2Position)
