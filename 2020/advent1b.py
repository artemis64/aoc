file = open('input1a.txt', 'r')

report = file.read().strip()
report = report.split()
report = [int(i) for i in report]

for i in range(len(report)):
    for j in range(i+1,len(report)):
        if 2020 - (report[i] + report[j]) in report:
            print(report[i]*report[j]*(2020-report[i]-report[j]))
            break