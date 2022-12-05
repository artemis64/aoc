file = open('input5.txt', 'r')

line = file.readline()
numberOfStacks = int(len(line) / 4)
stacks = []
for i in range(numberOfStacks):
	stacks.append([])

while not line[1] == '1':
	index = 0
	for char in line:
		if char == '[':
			stacks[int(index/4)].insert(0, line[index + 1])
		index +=1
	line = file.readline()


file.readline()

for line in file:
	line = line.strip()
	line = line.split()
	for move in range(int(line[1])):
		moving = stacks[int(line[3])-1].pop(-1)
		stacks[int(line[5])-1].append(moving)
	#print(stacks)

topCrates = ''
for stack in stacks:
	topCrates += stack[-1]
print(topCrates)