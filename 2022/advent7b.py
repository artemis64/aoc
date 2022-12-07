file = open('input7.txt', 'r')

dirs = [ dict(name = "/", dirsIn = [], totalSize = 0, path = []) ]

path = []

line = file.readline()
line = line.strip()
line = line.split()

while len(line) > 1:
	if line[0] == '$':
		if line[1] == 'cd':
			if not line[2] == '..':
				path.append(line[2])
				for i in dirs:
					if i['name'] == line[2] and i['path'] == path[:-1]:
						currentDir = i
						break
			else:
				closeDir = currentDir
				path = path[:-1]
				for i in dirs:
					if i['name'] == path[-1] and i['path'] == path[:-1]:
						currentDir = i
						break
				currentDir['totalSize'] += closeDir['totalSize']
				currentDir['dirsIn'].remove(closeDir['name'])
			line = file.readline()
			line = line.strip()
			line = line.split()
		elif line[1] == 'ls':
			line = file.readline()
			line = line.strip()
			line = line.split()
			while len(line)>0 and not line[0] == '$':
				if line[0] == 'dir':
					if line[1] in currentDir['dirsIn']:
						print("Error - {} directory already exists in the directory {}".format(line[1], currentDir))
					else:
						currentDir['dirsIn'].append(line[1])
						dirs.append(dict(name = line[1], dirsIn = [], totalSize = 0, path = path.copy()))
				else:
					currentDir['totalSize'] += int(line[0])
				line = file.readline()
				line = line.strip()
				line = line.split()
		else:
			print("Error - not ls or cd after $")
	else:
		print("Error - unexpected line - doesn't have $ at the beginning")


print(path)
while not len(path) == 1:
	for i in dirs:
		if i['name'] == path[-1]:
			currentDir = i
			break
	path = path[:-1]
	#print("path {}, closed dir {}".format(path, currentDir))
	for i in dirs:
		if i['name'] == path[-1]:
			i['totalSize'] += currentDir['totalSize']
			break

print(dirs)
needToFree = 30000000 - (70000000 - dirs[0]['totalSize'])
print(needToFree)
bigEnought = []
for folder in dirs:
	if folder['totalSize'] >= needToFree:
		bigEnought.append(folder)
print(bigEnought)
print(len(bigEnought))
minimalSize = 30000000
for folder in bigEnought:
	if folder['totalSize'] < minimalSize:
		minimalSize = folder['totalSize']
print(minimalSize)
	
