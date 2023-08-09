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
