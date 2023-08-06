file = open('input2a.txt', 'r')
valid = 0

for line in file:
    line = line.split()
    password = line[-1].strip()
    letter = line[1][:-1]
    interval = line[0].split('-')
    interval = [int(i) for i in interval]

    if password.count(letter) >= interval[0] and password.count(letter) <= interval[1]:
        valid += 1

print(valid)