file = open('input2a.txt', 'r')
valid = 0

for line in file:
    line = line.split()
    password = line[-1].strip()
    letter = line[1][:-1]
    positions = line[0].split('-')
    positions = [int(i) for i in positions]

    if password[positions[0]-1] == letter:
        if password[positions[1]-1] != letter:
            valid += 1
    elif password[positions[1]-1] == letter:
        valid +=1

print(valid)