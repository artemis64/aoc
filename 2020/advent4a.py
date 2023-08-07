file = open('input4a.txt', 'r')
line = file.readline().strip()
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
valid = 0

while line:
    document = [0,0,0,0,0,0,0,0]
    
    while line != '':
        line = line.split()
        for i in line:
            i = i.split(':')
            document[fields.index(i[0])] = 1
        line = file.readline().strip()
    if sum(document) == 8 or (sum(document) == 7 and document[-1] == 0):
        valid +=1
    line = file.readline().strip()

print(valid)