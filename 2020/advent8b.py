file = open('input8a.txt', 'r')
instructions = []

for line in file:
    line = line.strip().split()
    instructions.append([line[0], int(line[1])])

accumulator = 0
finish = len(instructions)

def checkPrevious(path, swapPlace):
    position = path[0]
    newPaths = []
    if instructions[position - 1][0] == 'acc':
        newPaths.append([[position - 1] + path, swapPlace])
    elif instructions[position - 1][0] == 'nop':
        newPaths.append([[position - 1] + path, swapPlace])
    elif instructions[position - 1][0] == 'jmp' and swapPlace == -1:
        newPaths.append([[position - 1] + path, position - 1])

    for i in range(len(instructions)):
        if instructions[i][0] == 'jmp' and i + instructions[i][1] == position and i != position:
            newPaths.append([[i] + path, swapPlace])
        elif swapPlace == -1 and instructions[i][0] == 'nop' and i + instructions[i][1] == position and i != position:
            newPaths.append([[i] + path, i])
    return newPaths
    
paths = []
path = [[finish], -1]

while path[0][0] != 0:
    paths = paths + checkPrevious(path[0], path[1])
    path = paths.pop(0)

for i in range(len(path[0])-1):
    if instructions[path[0][i]][0] == 'acc':
        accumulator += instructions[path[0][i]][1]
print(path)
print(accumulator)