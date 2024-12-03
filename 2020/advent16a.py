file = open('input16a.txt', 'r')
rules = []
myTicket = []
nearbyTickets = []
section = 0
sections = [rules, myTicket,nearbyTickets]

for line in file:
    line = line.strip()
    if line != '':
        sections[section].append(line)
    else:
        section +=1
myTicket.pop(0)
nearbyTickets.pop(0)
print(rules)
print(myTicket)
print(nearbyTickets)

intervals = []
for rule in rules:
    rule = rule.split()
    rule[-1] = rule[-1].split('-')
    intervals.append([int(rule[-1][0]), int(rule[-1][-1])])
    rule[-3] = rule[-3].split('-')
    intervals.append([int(rule[-3][0]), int(rule[-3][-1])])
print(intervals)

numbers = []
for ticket in nearbyTickets:
    ticket = ticket.split(',')
    numbers = numbers + [int(x) for x in ticket]
print(numbers)

def checkInterval(number, interval):
    if interval[0] <= number and interval[1] >= number:
        return True
    else:
        return False

sum = 0
for number in numbers:
    notInclude = False
    for interval in intervals:
        notInclude = checkInterval(number, interval)
        if notInclude:
            break
    if not notInclude:
        sum = sum + number
print(sum)