file = open('input11a.txt', 'r')
seatOccupancy = []

for line in file:
    line = line.strip()
    line = list(line)
    seatOccupancy.append(line)

def checkAdjacentSeats(row, col):
    numberOfOccupied = 0
    rowMin = max(0, row - 1)
    rowMax = min(row + 1, len(seatOccupancy)-1)
    colMin = max(0, col -1)
    colMax = min(col + 1, len(seatOccupancy[0])-1)
    for i in range(rowMin, rowMax + 1):
        for j in range(colMin, colMax + 1):
            #print("row {}, col {}".format(i, j))
            if not (i == row and j == col) and seatOccupancy[i][j] == '#':
                    numberOfOccupied +=1
    return numberOfOccupied

def getChanges():
    changesToApply = []
    for i in range(len(seatOccupancy)):
        for j in range(len(seatOccupancy[0])):
            if seatOccupancy[i][j] == 'L' or seatOccupancy[i][j] == '#':
                full = checkAdjacentSeats(i,j)
                if (seatOccupancy[i][j] == 'L' and full == 0) or (seatOccupancy[i][j] == '#' and full >= 4):
                    changesToApply.append([i, j])
    return changesToApply

def applyChanges(seatOccupancy, changes):
    for change in changes:
        if seatOccupancy[change[0]][change[1]] == 'L':
            seatOccupancy[change[0]][change[1]] = '#'
        elif seatOccupancy[change[0]][change[1]] == '#':
            seatOccupancy[change[0]][change[1]] = 'L'
    return seatOccupancy

changesToApply = getChanges()

while len(changesToApply) > 0:
    print(changesToApply)
    print(seatOccupancy)
    seatOccupancy = applyChanges(seatOccupancy, changesToApply)
    changesToApply = getChanges()
print(seatOccupancy)

occupied = 0
for i in seatOccupancy:
    for j in i:
        if j == '#':
            occupied +=1
print(occupied)
