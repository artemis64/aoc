file = open('input15a.txt', 'r')

line = file.readline()
line = line.strip().split(',')
saidNumbers = [] 
turns = []

for i in range(len(line)):
    saidNumbers.append(int(line[i]))
    turns.append([i+1, 0])
lastNumberIndex = len(line)-1


for turn in range(len(line)+1, 30000000+1):
    thisTurnNumber = 0
#print(turns[lastNumberIndex])
    if turns[lastNumberIndex][1] != 0:
        thisTurnNumber = turns[lastNumberIndex][1] - turns[lastNumberIndex][0]
    #print(thisTurnNumber)
    if thisTurnNumber in saidNumbers:
        lastNumberIndex = saidNumbers.index(thisTurnNumber)
        if turns[lastNumberIndex][1] == 0:
            turns[lastNumberIndex][1] = turn
        else:
            turns[lastNumberIndex][0] = turns[lastNumberIndex][1]
            turns[lastNumberIndex][1] = turn
    else:
        lastNumberIndex = len(saidNumbers)
        saidNumbers.append(thisTurnNumber)
        turns.append([turn, 0])
    print("Turn no. {}, this turn number is {}".format(turn,thisTurnNumber))