file = open('input16test.txt', 'r')
rules = []
myTicket = []
nearbyTicketStrings = []
section = 0
sections = [rules, myTicket,nearbyTicketStrings]

for line in file:
    line = line.strip()
    if line != '':
        sections[section].append(line)
    else:
        section +=1
myTicket.pop(0)
nearbyTicketStrings.pop(0)
print(rules)
myTicket = myTicket[0].split(',')
myTicket = [int(x) for x in myTicket]
print(myTicket)
print(nearbyTicketStrings)

intervals = []
for rule in rules:
    rule = rule.split()
    rule[-1] = rule[-1].split('-')
    intervals.append([int(rule[-1][0]), int(rule[-1][-1])])
    rule[-3] = rule[-3].split('-')
    intervals.append([int(rule[-3][0]), int(rule[-3][-1])])
print(intervals)

nearbyTickets = []
for ticket in nearbyTicketStrings:
    ticket = ticket.split(',')
    ticket = [int(x) for x in ticket]
    nearbyTickets.append(ticket)
print(nearbyTickets)

def checkTicket(ticket):  
    for number in ticket:
        validNumber = False
        for interval in intervals:
            if interval[0] <= number and interval[1] >= number:
                validNumber = True
                break
        if not validNumber:
            return False
    return True

for i in reversed(range(len(nearbyTickets))):
    if not checkTicket(nearbyTickets[i]):
        nearbyTickets.pop(i)
nearbyTickets.append(myTicket)
print(nearbyTickets)

for i in range(len(rules)):
    rules[i] = rules[i].split()
    if len(rules[i]) == 4:
        rules[i] = rules[i][0][:-1]
    else:
        rules[i] = rules[i][0] + ' ' + rules[i][1][:-1]
print(rules)