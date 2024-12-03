import re
file = open('input3a.txt', 'r')
suma = 0
line = file.readline().strip()

while line != '':
    print(line)
    multiplicationStrings = re.findall(r"mul\(\d+\,\d+\)",line)
    for mulStr in multiplicationStrings:
        numbers = mulStr[4:-1].split(",")
        numbers = [int(item) for item in numbers]
        suma += numbers[0] * numbers[1]
        
        
    line = file.readline().strip()
print(suma)