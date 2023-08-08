file = open('input7a.txt', 'r')
outsideBag = []
insideBag = []

for line in file:
    line = line.strip().split()
    out = line[0] + line[1]
    numberIn = 0
    if len(line) != 7:
        numberIn = len(line) // 4 - 1
        inside = []
    else:
        inside = [[0,'nobags']]
    line = line[4:]
    
    for i in range(numberIn):
        inside += [[int(line[i*4]), line[i*4 + 1] + line[i*4 + 2]]]
    insideBag += inside
    for i in range(len(inside)):
        outsideBag.append(out)

def checkInsideBags(numberOfBags, color):
    bagsInside = 0
    for j in range(len(outsideBag)):
        if outsideBag[j] == color and insideBag[j][0] > 0:
            bagsInside += checkInsideBags(insideBag[j][0], insideBag[j][1])
    bagsInside +=1
    return numberOfBags * bagsInside

print(checkInsideBags(1, 'shinygold'))
                
