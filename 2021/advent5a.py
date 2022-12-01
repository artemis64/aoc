mapa = [[0]]

class Line:
  def __init__(self, x1, y1, x2, y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
    self.vertical = True if self.x1 == self.x2 else False
    self.horizontal = True if self.y1 == self.y2 else False
    if not (self.horizontal or self.vertical):
    	self.positive = True if ((x1<x2 and y1<y2) or (x1>x2 and y1>y2)) else False

lines = []
file = open('input5.txt', 'r')
for line in file:
	newLine = line.strip().split(" -> ")
	[x1, y1] = newLine[0].split(",")
	[x2, y2] = newLine[1].split(",")
	lines.append(Line(int(x1),int(y1),int(x2),int(y2)))

file.close()
def expandMap(xLast, yLast, mapa):
	for yLine in mapa:
		while len(yLine) <= xLast:
			yLine.append(0)
	while len(mapa) <= yLast:
		mapa.append([0] * len(mapa[0]))
	return mapa
			

for line in lines:
	if line.x1 > line.x2:
		minX = line.x2
		maxX = line.x1
	else:
		minX = line.x1
		maxX = line.x2
	if line.y1 > line.y2:
		minY = line.y2
		maxY = line.y1
	else:
		minY = line.y1
		maxY = line.y2
	if maxX >= len(mapa[0]) or maxY >= len(mapa):
		mapa = expandMap(maxX, maxY, mapa)
	
	if line.vertical:
		for i in range(minY, maxY+1):
			mapa[i][minX] +=1
	elif line.horizontal:
		for i in range(minX, maxX+1):
			mapa[minY][i] +=1
	else:
		if line.positive:
			print("DRAW POSITIVE")
			print("{}, {} -> {}, {}".format(minX, minY, maxX, maxY))
			for i in range(maxY-minY + 1):
				print("{}, {}".format(minX + i, minY + i))
				mapa[minY + i][minX + i] +=1
		else:
			for i in range(maxY-minY +1):
				mapa[maxY - i][minX + i] +=1


count = 0
for y in mapa:
	for x in range(len(mapa[0])):
		if y[x]>1:
			count +=1

print(count)




