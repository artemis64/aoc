import math

class Monkey:
	def __init__(self, name, items, inspection, test, testTrue, testFalse):
		self.name = name
		self.items = items
		self.inspection = inspection
		self.test = test
		self.testTrue = testTrue
		self.testFalse = testFalse
		self.inspectedItems = 0

	def __str__(self):
		return f"{self.name}: items inspected {self.inspectedItems}"
		
	def inspectItem(self, item, lcm):
		newWorryLevel = 0
		if self.inspection[0] == '*':
			if self.inspection[1] > 0:
				newWorryLevel = item * self.inspection[1]
			else:
				newWorryLevel = item * item
		else:
			if self.inspection[1] > 0:
				newWorryLevel = item + self.inspection[1]
			else:
				newWorryLevel = item + item
		newWorryLevel = newWorryLevel % lcm
		return newWorryLevel

	def throwItems(self, monkeys):
		#print("Throwing monkey: {} can throw to monekys {} or {}".format(self, monkeys[self.testTrue], monkeys[self.testFalse]))
		for item in self.items:
			if item % self.test == 0:
				#print("test true")
				monkeys[self.testTrue].items.append(item)
			else:
				#print("test false, item {}, throw to {}".format(item, monkeys[testFalse]))
				monkeys[self.testFalse].items.append(item)
		self.items = []

monkeys = []
file = open('input11.txt', 'r')
line = file.readline()
line = line.strip()
while len(line) > 0:
	name = line[:-1]

	line = file.readline()
	line = line.strip()
	line = line.split()
	items = []
	for i in range(2, len(line)-1):
		items.append(int(line[i][:-1]))
	items.append(int(line[-1]))

	line = file.readline()
	line = line.strip()
	line = line.split()
	if line[-1] == 'old':
		inspection = [line[-2], -1]
	else:
		inspection = [line[-2], int(line[-1])]

	line = file.readline()
	line = line.strip()
	line = line.split()
	test = int(line[-1])

	line = file.readline()
	line = line.strip()
	line = line.split()
	testTrue = int(line[-1])

	line = file.readline()
	line = line.strip()
	line = line.split()
	testFalse = int(line[-1])

	monkeys.append(Monkey(name, items, inspection, test, testTrue, testFalse))

	line = file.readline()
	line = file.readline()
	line = line.strip()
tests = []
for monkey in monkeys:
	tests.append(monkey.test)
	print(monkey)
lcm = math.lcm(*tests)
print(lcm)
print(tests)
for i in range(10000):
	print(i)
	for monkey in monkeys:
		for index, item in enumerate(monkey.items):
			monkey.items[index] = monkey.inspectItem(item, lcm)
			monkey.inspectedItems +=1
		#print(monkey.items)
		monkey.throwItems(monkeys)
		#for monkey in monkeys:
		#	print(monkey)
totalInspectedItems = []
for monkey in monkeys:
	totalInspectedItems.append(monkey.inspectedItems)
totalInspectedItems.sort()
print(totalInspectedItems)
monkeyBusiness = totalInspectedItems[-1] * totalInspectedItems[-2]
print(monkeyBusiness)

