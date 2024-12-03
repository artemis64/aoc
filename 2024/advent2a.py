file = open('input2.txt', 'r')  

safeReports = 0  
goodIncrements = [1, 2, 3, -1, -2, -3]                    
for line in file:               
    line = line.strip()
    line = line.split()  
    previous = int(line[0])
    number = int(line[1])
    increment = previous - number
    if increment in goodIncrements:
        previous = number
        for i in range(2, len(line)):
            number = int(line[i])
            newIncrement = previous - number
            if newIncrement in goodIncrements and newIncrement * increment > 0:
                if i == len(line) -1:
                    safeReports +=1
            else:
                break
            previous = number
            increment = newIncrement
print(safeReports)