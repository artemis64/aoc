file = open('input13a.txt', 'r')

earliestPickup = file.readline()
earliestPickup = int(earliestPickup.strip())
line = file.readline()
line = line.strip().split(',')
busLines = []
for i in range(len(line)):
    if line[i] != 'x':
        busLines.append(int(line[i]))

leaveIn = 10000
firstBus = 0
for bus in busLines:
    busLeftBefore = earliestPickup % bus
    leavingIn = bus - busLeftBefore
    if leaveIn > leavingIn:
        leaveIn = leavingIn
        firstBus = bus
print(firstBus * leaveIn)