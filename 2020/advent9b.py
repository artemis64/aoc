file = open('input9a.txt', 'r')
data = []
preambleSize = 25
invalidNumber = 0

for line in file:
    line = line.strip()
    data.append(int(line))

for i in range(preambleSize,len(data)):
    foundSum = False
    for j in range(i-preambleSize, i):
        for k in range(j+1, i):
            if data[i] == data[j] + data[k]:
                foundSum = True
    if not foundSum:
        invalidNumber = data[i]
        break
print(invalidNumber)

for i in range(len(data)):
    sum = data[i]
    j = 1
    while sum < invalidNumber:
        sum += data[i+j]
        j +=1
    if sum == invalidNumber:
        interval = [i, i+j]
        break

min = data[interval[0]]
max = data[interval[0]]
for i in range(interval[0], interval[1]):
    if min > data[i]:
        min = data[i]
    if max < data[i]:
        max = data[i]
print(min+max)
