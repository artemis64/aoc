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

import copy

def eraseNode(node, mapa):
	mapa.pop(node)
	for key in mapa.keys():
		for i in mapa[key]:
			if i == node:
				mapa[key].remove(i)
		if len(mapa[key]) == 0:
			eraseNode(key, mapa)
	return mapa


saveStart = copy.deepcopy(mapa['start'])
eraseNode('start', mapa)
mapa['start'] = saveStart


paths = [['start']]
ended = 0
while ended < len(paths):
	newPaths = []
	toRemove = []
	for path in paths:
		if path[-1] != 'end':
			canGoTo = []
			for i in mapa[path[-1]]:
				if i.isupper():
					canGoTo.append(i)
				else:
					if i not in path:
						canGoTo.append(i)
					else:
						doubleVisit = {}
						for j in path:
							if not j.isupper():
								if j in doubleVisit.keys():
									doubleVisit[j] +=1
								else:
									doubleVisit[j] = 1
						canAppend = True
						for value in doubleVisit.values():
							if value > 1:
								canAppend = False
								break
						if canAppend:
							canGoTo.append(i)
			if path == ['start', 'b', 'A', 'c', 'A', 'b']:
				print("goto")
				print(canGoTo)
			for i in canGoTo:
				newPaths.append(path + [i])
			if path == ['start', 'b', 'A', 'c', 'A', 'b']:
				print("newP")
				print(newPaths)

			if path == ['start', 'b', 'A', 'c', 'A', 'b']:
				print("remove")
				print(toRemove)
	#print("removing")
	#print(len(paths))
	for i in range(len(paths)):
		if paths[i][-1] != 'end':
			toRemove.append(i)
	toRemove.sort()
	while len(toRemove) > 0:
		paths.pop(toRemove.pop())
	ended = len(paths)
	#print("paths")
	#print(paths)
	#print("new")
	#print(newPaths)
	paths = paths + newPaths
print(paths)
print(ended)