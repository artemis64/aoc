file = open('input7a.txt', 'r')
outsideBag = []
insideBag = []

for line in file:
    line = line.strip().split()
    out = line[0] + line[1]
    numberIn = 0
    if len(line) != 7:
        numberIn = len(line) // 4 - 1
    line = line[4:]
    inside = []
    for i in range(numberIn):
        inside += [line[i*4 + 1] + line[i*4 + 2]]
    insideBag += inside
    for i in range(len(inside)):
        outsideBag.append(out)

bagsToCheck = ['shinygold']
coverBags = []
while len(bagsToCheck)>0:
    checking = bagsToCheck.pop(0)
    for i in range(len(insideBag)):
        if checking == insideBag[i] and not outsideBag[i] in coverBags:
            bagsToCheck.append(outsideBag[i])
            coverBags.append(outsideBag[i])
print(len(coverBags))
