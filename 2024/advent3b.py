import re
file = open('input3.txt', 'r')
suma = 0
line = file.readline().strip()

while line != '':
    try:
        doLineEnd = line.index("don't()")
    except:
        doLineEnd = -1 
    multiplicationStrings = re.findall(r"mul\(\d+\,\d+\)",line[:doLineEnd])
    rest = line[doLineEnd:]
    conti = True
    doLineStart = 0
    doLineEnd = 0
    while conti:
        print(multiplicationStrings)
        print(rest)
        print(doLineStart)
        print(doLineEnd)
        if doLineStart == -1 or doLineEnd == 3:
            conti = False
        for mulStr in multiplicationStrings:
            numbers = mulStr[4:-1].split(",")
            numbers = [int(item) for item in numbers]
            suma += numbers[0] * numbers[1]
        try:
            doLineStart = rest.index("do()")
        except:
            doLineStart = -1
        try:
            doLineEnd = rest[4:].index("don't()") + 4
        except: 
            doLineEnd = 3
        if doLineEnd == 3:
            multiplicationStrings = re.findall(r"mul\(\d+\,\d+\)",rest[doLineStart:])    
            rest = rest[-2:]
        else:
            multiplicationStrings = re.findall(r"mul\(\d+\,\d+\)",rest[doLineStart:doLineEnd])
            rest = rest[doLineEnd:]
               

    line = file.readline().strip()
print(suma)