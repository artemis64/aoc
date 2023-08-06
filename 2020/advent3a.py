file = open('input3a.txt', 'r')
pattern = []

for line in file:
    pattern.append(line.strip())
modulo = len(pattern[0])
finish = len(pattern)
currentPosition = [0,0]
trees = 0

while currentPosition[1] < finish:
    print(currentPosition)
    if pattern[currentPosition[1]][currentPosition[0]] == '#':
        trees +=1
    currentPosition[0] = (currentPosition[0] + 3) % modulo
    currentPosition[1] +=1
print(trees)