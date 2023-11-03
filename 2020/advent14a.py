file = open('input14a.txt', 'r')

mask = ''
memoryIndices = []
memoryValues = []

for line in file:
    line = line.strip()
    if line[:4] == 'mask':
        line = line.split()
        mask = line[2]
        print(mask)
    else:
        line = line.split()
        index = int(line[0][line[0].index('[')+1:-1])
        print(index)
        if index in memoryIndices:
            memoryIndex = memoryIndices.index(index)
        else:
            memoryIndex = len(memoryIndices)
            memoryIndices.append(index)
            memoryValues.append(0)
    
        memoryValues[memoryIndex] = bin(int(line[2]))[2:].zfill(36)
        print(memoryValues[memoryIndex])
        for i, char in enumerate(mask):
            print(char)
            if char != 'X':
                memoryValues[memoryIndex] = list(memoryValues[memoryIndex])
                memoryValues[memoryIndex][i] = char
                memoryValues[memoryIndex] = "".join(memoryValues[memoryIndex])
                print(memoryValues[memoryIndex])
        memoryValues[memoryIndex] = int(memoryValues[memoryIndex],2)
        print(memoryValues[memoryIndex])
print(memoryIndices)
print(memoryValues)
print(sum(memoryValues))

