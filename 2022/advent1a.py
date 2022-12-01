file = open('input1a.txt', 'r')

maxElf = 0
elf = 0

for line in file:
	line = line.strip()
	if line == '':
		if maxElf < elf:
			maxElf = elf
		elf = 0
	else:
		elf += int(line)

print(maxElf)
