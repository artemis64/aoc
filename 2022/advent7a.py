file = open('input7.txt', 'r')

dirs = [ dict(name = "/", dirsIn = [], totalSize = 0, path = []) ]

path = []
total = 0

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
				if closeDir['totalSize']<=100000:
					total +=closeDir['totalSize']
				path = path[:-1]
				for i in dirs:
					if i['name'] == path[-1] and i['path'] == path[:-1]:
						currentDir = i
						break
				currentDir['totalSize'] += closeDir['totalSize']
				currentDir['dirsIn'].remove(closeDir['name'])
				dirs.remove(closeDir)
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

#print(dirs)
print(total)
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

print(total)

	
