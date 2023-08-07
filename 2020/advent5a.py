file = open('input5a.txt', 'r')
maxID = 0

for line in file:
    line = line.strip()
    rowCode = line[:7]
    columnCode = line[7:]
    rowInterval = [0, 127]
    columnInterval = [0, 7]
    for i in rowCode:
        if i == 'F':
            rowInterval[1] = rowInterval[0] + (rowInterval[1] - rowInterval[0])//2
        else:
            rowInterval[0] = rowInterval[1] - (rowInterval[1] - rowInterval[0])//2
    for i in columnCode:
        if i == 'L':
            columnInterval[1] = columnInterval[0] + (columnInterval[1] - columnInterval[0])//2
        else:
            columnInterval[0] = columnInterval[1] - (columnInterval[1] - columnInterval[0])//2
    seatID = rowInterval[0]*8 + columnInterval[0]
    print(seatID)
    if seatID > maxID:
        maxID = seatID
print(maxID)