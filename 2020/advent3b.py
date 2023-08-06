file = open('input3a.txt', 'r')
pattern = []

for line in file:
    pattern.append(line.strip())
modulo = len(pattern[0])
finish = len(pattern)
steps = [[1,1], [3,1], [5,1], [7,1], [1,2]]
result = 1

for step in steps:
    currentPosition = [0,0]
    trees = 0

    while currentPosition[1] < finish:
        if pattern[currentPosition[1]][currentPosition[0]] == '#':
            trees +=1
        currentPosition[0] = (currentPosition[0] + step[0]) % modulo
        currentPosition[1] += step[1]
    print(trees)
    result *=trees
print(result)