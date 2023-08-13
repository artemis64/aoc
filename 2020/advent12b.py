file = open('input12a.txt', 'r')
instructions = []

for line in file:
    line = line.strip()
    instructions.append([line[0], int(line[1:])])

shipPosition = [0, 0]
wayPointPosition = [10, 1]
sides = ['E', 'S', 'W', 'N']

for instruction in instructions:
    if instruction[0] == 'N':
        wayPointPosition[1] += instruction[1]
    elif instruction[0] == 'S':
        wayPointPosition[1] -= instruction[1]
    elif instruction[0] == 'E':
        wayPointPosition[0] += instruction[1]
    elif instruction[0] == 'W':
        wayPointPosition[0] -= instruction[1]
    elif instruction[0] == 'L':
        rotation = (instruction[1] // 90) % 4
        if rotation == 1:
            newWaypoint = [-1 * wayPointPosition[1], wayPointPosition[0]]
            wayPointPosition = newWaypoint
        elif rotation == 2:
            newWaypoint = [-1 * wayPointPosition[0], -1 * wayPointPosition[1]]
            wayPointPosition = newWaypoint
        elif rotation == 3:
            newWaypoint = [wayPointPosition[1], -1 * wayPointPosition[0]]
            wayPointPosition = newWaypoint
    elif instruction[0] == 'R':
        rotation = (instruction[1] // 90) % 4
        if rotation == 1:
            newWaypoint = [wayPointPosition[1], -1 * wayPointPosition[0]]
            wayPointPosition = newWaypoint
        elif rotation == 2:
            newWaypoint = [-1 * wayPointPosition[0], -1 * wayPointPosition[1]]
            wayPointPosition = newWaypoint
        elif rotation == 3:
            newWaypoint = [-1 * wayPointPosition[1], wayPointPosition[0]]
            wayPointPosition = newWaypoint
    elif instruction[0] == 'F':
        shipPosition[0] = shipPosition[0]+ instruction[1] * wayPointPosition[0]
        shipPosition[1] = shipPosition[1]+ instruction[1] * wayPointPosition[1]
print(shipPosition)
print(max(shipPosition[0], -shipPosition[0])+ max(shipPosition[1], -shipPosition[1]))

