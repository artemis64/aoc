file = open('input8a.txt', 'r')
instructions = []

for line in file:
    line = line.strip().split()
    instructions.append([line[0], int(line[1])])
notVisited = [True] * len(instructions)
position = 0
accumulator = 0

def runOperation(operation, size, position, accumulator):
    if operation == 'acc':
        return (position + 1, accumulator + size)
    elif operation == 'jmp':
        return (position + size, accumulator)
    else:
        return (position + 1, accumulator)
    
while notVisited[position]:
    notVisited[position] = False
    (position, accumulator) = runOperation(instructions[position][0], instructions[position][1], position, accumulator)
print(accumulator)