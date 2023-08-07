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
            document[fields.index(i[0])] = i[1]
        line = file.readline().strip()
    allMandatory = True
    for i in range(7):
        if document[i] == 0:
            allMandatory = False
            break
    
    if allMandatory:
        if int(document[0]) >= 1920 and int(document[0]) <= 2002:
            print('byr')
            if int(document[1]) >= 2010 and int(document[1]) <= 2020:
                print('iyr')
                if int(document[2]) >= 2020 and int(document[2]) <= 2030:
                    print('eyr')
                    if (document[3][-2:] == 'in' and int(document[3][:-2]) >= 59 and int(document[3][:-2]) <= 76) or (document[3][-2:] == 'cm' and int(document[3][:-2]) >= 150 and int(document[3][:-2]) <= 193):
                        print('hgt')
                        if document[4][0] == '#' and len(document[4]) == 7:
                            dictionary = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
                            properChar = 0
                            for j in document[4][1:]:
                                if j in dictionary:
                                    properChar +=1
                            if properChar == 6:
                                print('hcl')
                                colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                                if document[5] in colors:
                                    if len(document[6]) == 9 and document[6].isdigit():
                                        valid +=1
                
    line = file.readline().strip()

print(valid)