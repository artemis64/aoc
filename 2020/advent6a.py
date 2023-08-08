file = open('input6a.txt', 'r')
groupAnswers = []
sumAnswers = 0

for line in file:
    line = line.strip()
    
    if line != '':
        for char in line:
            if not char in groupAnswers:
                groupAnswers.append(char)
    else:
        sumAnswers +=len(groupAnswers)
        groupAnswers = []
sumAnswers +=len(groupAnswers)
print(sumAnswers)