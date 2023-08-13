file = open('input10a.txt', 'r')
adapters = []

for line in file:
    line = line.strip()
    adapters.append(int(line))
adapters.append(0)
adapters.append(max(adapters) + 3)
#print(adapters)
adapters.sort()
#print(adapters)
diff3 = 0
diff2 = 0
diff1 = 0
for i in range(len(adapters)-1):
    if adapters[i+1] - adapters[i] == 1:
        diff1 +=1
    elif adapters[i+1] - adapters[i] == 2:
        diff2 +=1
    else:
        diff3 +=1
print(diff1*diff3)