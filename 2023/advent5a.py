file = open('input5.txt', 'r')
plantingChains = []

seedsLine = file.readline()
seedsLine = seedsLine.split()
for seed in seedsLine[1:]:
    plantingChains.append([int(seed)])
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
                if len(chain) == chainLen and chain[-1] >= sourceStart and chain[-1] <= sourceEnd:
                    chain.append(line[0] + chain[-1] - sourceStart)
        line = file.readline()
        line = line.strip()
    for chain in plantingChains:
        if len(chain) == chainLen:
            chain.append(chain[-1])

print(plantingChains)
minLocation = plantingChains[0][-1]
for chain in plantingChains:
    if chain[-1] < minLocation:
        minLocation = chain[-1]
print(minLocation)
