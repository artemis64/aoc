file = open('input11a.txt', 'r')
seatOccupancy = []

for line in file:
    line = line.strip()
    row = []
    for i in line:
        if i == '.':
            row.append(-1)
        elif i == 'L':
            row.append(0)
    seatOccupancy.append(row)
seatVisibility = []

for i in range(len(seatOccupancy)):
    seatLine = []
    for j in range(len(seatOccupancy[0])):
        print([i,j])
        visibleSeats = []
        for k in range(1, min(i,j) + 1):
            if seatOccupancy[i-k][j-k] == 0:
                visibleSeats.append([i-k,j-k])
                break
        for k in range(1, min(i, len(seatOccupancy[0])-j-1)+1):
            if seatOccupancy[i-k][j+k] == 0:
                visibleSeats.append([i-k,j+k])
                break
        for k in range(1,i+1):
            if seatOccupancy[i-k][j] == 0:
                visibleSeats.append([i-k,j])
                break
        for k in range(1,j+1):
            if seatOccupancy[i][j-k] == 0:
                visibleSeats.append([i,j-k])
                break
        for k in range(1, len(seatOccupancy[0])-j):
            if seatOccupancy[i][j+k] == 0:
                visibleSeats.append([i,j+k])
                break
        for k in range(1,len(seatOccupancy)-i):
            if seatOccupancy[i+k][j] == 0:
                visibleSeats.append([i+k,j])
                break
        for k in range(1, min(j,len(seatOccupancy)-i-1)+1):
            if seatOccupancy[i+k][j-k] == 0:
                visibleSeats.append([i+k,j-k])
                break
        for k in range(1, min(len(seatOccupancy[0])-j, len(seatOccupancy)-i)):
            if seatOccupancy[i+k][j+k] == 0:
                visibleSeats.append([i+k,j+k])
                break
        seatLine.append(visibleSeats)
    seatVisibility.append(seatLine)

def getVisibleOccupiedSeats(visibleSeats):
    occupied = 0
    for seat in visibleSeats:
        occupied += seatOccupancy[seat[0]][seat[1]]
    return occupied

def getChanges():
    changes = []
    for i in range(len(seatOccupancy)):
        for j in range(len(seatOccupancy[0])):
            if seatOccupancy[i][j]>-1:
                occupied = getVisibleOccupiedSeats(seatVisibility[i][j])
                if seatOccupancy[i][j] == 0 and occupied == 0:  
                    changes.append([i,j])
                elif seatOccupancy[i][j] == 1 and occupied >= 5:
                    changes.append([i,j])
    return changes

def applyChanges(changes, seatOccupancy):
    for change in changes:
        seatOccupancy[change[0]][change[1]] = (seatOccupancy[change[0]][change[1]] + 1) % 2
    return seatOccupancy

changesToApply = getChanges()

while len(changesToApply) > 0:
    seatOccupancy = applyChanges(changesToApply, seatOccupancy)
    changesToApply = getChanges()

occupied = 0
for i in range(len(seatOccupancy)):
    for j in range(len(seatOccupancy[0])):
        if seatOccupancy[i][j] > -1:
            occupied += seatOccupancy[i][j]
print(occupied)