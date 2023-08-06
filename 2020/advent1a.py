file = open('input1a.txt', 'r')

report = file.read().strip()
report = report.split()
report = [int(i) for i in report]

for number in report:
    complement = 2020 - number
    if complement in report:
        print(number*complement)
        break