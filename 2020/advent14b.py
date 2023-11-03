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
        index = bin(int(index))[2:].zfill(36)
        index = list(index)
        print(index)
        
        xIndices = []
        for i, char in enumerate(mask):
            #print(char)
            if char == '1':
                index[i] = '1'
            elif char == 'X':
                index[i] = 'X'
                xIndices.append(i)
        indexVariants = [index]
        for i in xIndices:
            newIndices = []
            for variant in indexVariants:
                print(variant)
                temp0 = variant.copy()
                temp0[i] = '0'
                temp1 = variant.copy()
                temp1[i] = '1'
                newIndices.append(temp0)
                newIndices.append(temp1)
            indexVariants = newIndices
        for i in range(len(indexVariants)):
            indexVariants[i] = int("".join(indexVariants[i]),2)
            if indexVariants[i] in memoryIndices:
                index = memoryIndices.index(indexVariants[i])
                memoryValues[index] = int(line[2])
            else:
                memoryIndices.append(indexVariants[i])
                memoryValues.append(int(line[2]))
        print(indexVariants)
        

print(memoryIndices)
print(memoryValues)
print(sum(memoryValues))