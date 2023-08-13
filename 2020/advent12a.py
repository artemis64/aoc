file = open('input12a.txt', 'r')
instructions = []

for line in file:
    line = line.strip()
    instructions.append([line[0], int(line[1:])])

shipStatus = [0, 0, 'E']
sides = ['E', 'S', 'W', 'N']

for instruction in instructions:
    if instruction[0] == 'N':
        shipStatus[1] += instruction[1]
    elif instruction[0] == 'S':
        shipStatus[1] -= instruction[1]
    elif instruction[0] == 'E':
        shipStatus[0] += instruction[1]
    elif instruction[0] == 'W':
        shipStatus[0] -= instruction[1]
    elif instruction[0] == 'L':
        direction = sides.index(shipStatus[2])
        direction = (direction - (instruction[1] // 90)) % 4
        shipStatus[2] = sides[direction]
    elif instruction[0] == 'R':
        direction = sides.index(shipStatus[2])
        direction = (direction + (instruction[1] // 90)) % 4
        shipStatus[2] = sides[direction]
    elif instruction[0] == 'F':
        if shipStatus[2] == 'N':
            shipStatus[1] += instruction[1]
        elif shipStatus[2] == 'S':
            shipStatus[1] -= instruction[1]
        elif shipStatus[2] == 'E':
            shipStatus[0] += instruction[1]
        elif shipStatus[2] == 'W':
            shipStatus[0] -= instruction[1]
    print(shipStatus)
print(max(shipStatus[0], -shipStatus[0])+ max(shipStatus[1], -shipStatus[1]))

