file = open('input1a.txt', 'r')

elfs = []
elf = 0

for line in file:
	line = line.strip()
	if line == '':
		elfs.append(elf)
		elf = 0
	else:
		elf += int(line)
elfs.append(elf)
elfs.sort(reverse=True)
max3Elfs = 0
for e in elfs[0:3]:
	max3Elfs += e
print(elfs[0:3])	
print(max3Elfs)