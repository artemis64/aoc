file = open('input10a.txt', 'r')
adapters = []

for line in file:
    line = line.strip()
    adapters.append(int(line))
adapters.append(0)
adapters.append(max(adapters) + 3)
adapters.sort()
differences = []
diff3 = 0
diff2 = 0
diff1 = 0
for i in range(len(adapters)-1):
    if adapters[i+1] - adapters[i] == 1:
        diff1 +=1
        differences.append(1)
    elif adapters[i+1] - adapters[i] == 2:
        diff2 +=1
        differences.append(2)
    else:
        diff3 +=1
        differences.append(3)
print(diff1)
print(diff2)
print(diff3)
print(differences)
sizeDiff1 = []
tmpDiff = 0
for i in differences:
    if i == 1:
        tmpDiff +=1
    elif tmpDiff != 0:
        sizeDiff1.append(tmpDiff)
        tmpDiff = 0
print(sizeDiff1)
numberOfOptions = 1
for i in sizeDiff1:
    if i == 2:
        numberOfOptions *=2
    elif i == 3:
        numberOfOptions *=4
    elif i == 4:
        numberOfOptions *=7
print(numberOfOptions)