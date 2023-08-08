file = open('input6a.txt', 'r')
answerValues = []
answerCounts = []
sumAnswers = 0
groupSize = 0

for line in file:
    line = line.strip()
    
    if line != '':
        groupSize +=1
        for char in line:
            if not char in answerValues:
                answerValues.append(char)
                answerCounts.append(1)
            else:
                answerCounts[answerValues.index(char)] +=1
    else:
        for i in answerCounts:
            if i == groupSize:
                sumAnswers +=1
        answerValues = []
        answerCounts = []
        groupSize = 0
for i in answerCounts:
    if i == groupSize:
        sumAnswers +=1
print(sumAnswers)