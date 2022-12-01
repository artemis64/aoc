file = open('input12.txt', 'r')
mapa = {}
for line in file:
	[A, B] = line.strip().split("-")
	if A not in mapa:
		mapa[A] = []
	if B not in mapa:
		mapa[B] = []
	if B not in mapa[A]:
		mapa[A].append(B)
		mapa[B].append(A)
file.close()

def eraseNode(node, mapa):
	mapa.pop(node)
	for key in mapa.keys():
		for i in mapa[key]:
			if i == node:
				mapa[key].remove(i)
		if len(mapa[key]) == 0:
			eraseNode(key, mapa)
	return mapa

for key in mapa.keys():
	if len(mapa.get(key)) == 1 and not mapa.get(key)[0].isupper():
		eraseNode(key,mapa)

paths = [['start']]
ended = 0
while ended < len(paths):
	newPaths = []
	for path in paths:
		if path[-1] != 'end':
			canGoTo = []
			for i in mapa[path[-1]]:
				if i.isupper():
					canGoTo.append(i)
				else:
					if i not in path:
						canGoTo.append(i)
			for i in canGoTo:
				newPaths.append(path + [i])
	print("removing")
	print(len(paths))
	toRemove = []
	for i in range(len(paths)):
		if paths[i][-1] != 'end':
			toRemove.append(i)
	while len(toRemove) > 0:
		paths.pop(toRemove.pop())
	ended = len(paths)
	print("paths")
	print(paths)
	print("new")
	print(newPaths)
	paths = paths + newPaths
print(paths)
print(ended)