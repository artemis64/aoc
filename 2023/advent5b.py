file = open('input5test.txt', 'r')
plantingChains = []

seedsLine = file.readline()
seedsLine = seedsLine.split()
seedsLine = seedsLine[1:]
seedsLine = [int(i) for i in seedsLine]

for i in range(len(seedsLine) // 2):
    plantingChains.append([[seedsLine[2*i], seedsLine[2*i] + seedsLine[2*i + 1]-1]])
file.readline()

while len(plantingChains[0])<8:
    file.readline()
    line = file.readline()
    line = line.strip()
    chainLen = len(plantingChains[0])
    while len(line)>0:
        if line[0].isdigit():
            line = line.split()
            line = [int(i) for i in line]
            sourceStart = line[1]
            sourceEnd = line[1] + line[2] - 1
            for chain in plantingChains:
                if len(chain) == chainLen:
                    if chain[-1][0]>=sourceStart and chain[-1][1] <= sourceEnd:
                        chain.append([line[0] + chain[-1][0] - sourceStart, line[0] + chain[-1][1] - sourceStart])




        line = file.readline()
        line = line.strip()
    for chain in plantingChains:
        if len(chain) == chainLen:
            chain.append(chain[-1].copy())


minLocation = plantingChains[0][-1][0]
for chain in plantingChains:
    if chain[-1][0] < minLocation:
        minLocation = chain[-1][0]
print(plantingChains)
print(minLocation)
