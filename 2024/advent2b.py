file = open('input2.txt', 'r')  
safeReports = 0  
goodIncrements = [1, 2, 3, -1, -2, -3] 

def checkReport(report):
    print(report)
    first = report[0]
    second = report[1]
    increment = first - second
    if increment in goodIncrements:
        for i in range(2, len(report)):
            first = second
            second = report[i]
            newIncrement = first - second
            if newIncrement in goodIncrements and increment * newIncrement > 0:
                pass
            else: 
                return i
        return -1
    else:
        return 1


                   
for line in file:               
    line = line.strip()
    line = line.split()  
    line = [int(item) for item in line]
    result = checkReport(line)
    if result == -1:
        safeReports +=1
        print(safeReports)
    else:
        if checkReport(line[:result-1] + line[result:]) == -1:
            safeReports +=1
            print(safeReports)
        elif checkReport(line[:result] + line[result+1:]) == -1:
            safeReports +=1 
            print(safeReports)
        elif checkReport(line[1:]) == -1:
            safeReports +=1 
            print(safeReports)

print(safeReports)