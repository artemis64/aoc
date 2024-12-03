file = open('input17test.txt', 'r')

zMin = 0
zMax = 0
xMin = 0
yMin = 0
cubeMap = {'0': {}}
yIndex = 0
for line in file:
    line = line.strip()
    xIndex = 0
    cubeMap['0'][str(yIndex)] = {}
    for char in line:
        if char == '.':
            cubeMap['0'][str(yIndex)][str(xIndex)] = {'activity' : False, 'visibleActive': 0}
        else:
             cubeMap['0'][str(yIndex)][str(xIndex)] = {'activity' : True, 'visibleActive': 0}
        xIndex +=1
    yIndex +=1
xMax = xIndex - 1
yMax = yIndex - 1
print(cubeMap)
print(xMax)

