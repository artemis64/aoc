file = open('input18.txt', 'r')
elementsToAdd = []
for line in file:
	elementsToAdd.append(list(line.strip()))
file.close()
summa = elementsToAdd.pop(0)

def addTwoSnailNumbers(number1, number2):
	result = []
	result.append('[')
	result = result + number1
	result.append(',')
	result = result + number2
	result.append(']')
	return result

def reduceSnailNumber(number):
	level = 0
	leftNumber = 0
	rightNumber = 0
	leftmostNumber10 = 0
	leftmostNumber10Index = len(number)
	levelFive = False
	levelFiveEnd = False
	fiveIndex = len(number)
	leftNumberIndex = len(number)
	rightNumberIndex = len(number)
	end = True
	for index, char in enumerate(number):
		if char == '[':
			level +=1
			if level == 5 and not levelFive:
				levelFive = True
				fiveIndex = index
		elif char == ']':
			if levelFive:
				levelFiveEnd = True
			level -=1
		elif char.isdigit():
			if int(char) > 9 and leftmostNumber10 == 0:
				leftmostNumber10 = int(char)
				leftmostNumber10Index = index
			if levelFive and rightNumberIndex == len(number) and levelFiveEnd:
				rightNumber = int(char)
				rightNumberIndex = index
				break
			elif not levelFive: 
				leftNumber = int(char)
				leftNumberIndex = index


	if levelFive:
		if leftNumberIndex < len(number):
			number[leftNumberIndex] = str(int(number[fiveIndex + 1]) + leftNumber)
		if rightNumberIndex < len(number):
			number[rightNumberIndex] = str(int(number[fiveIndex + 3]) + rightNumber)
		number[fiveIndex] = '0'
		number.pop(fiveIndex + 4)
		number.pop(fiveIndex + 3)
		number.pop(fiveIndex + 2)
		number.pop(fiveIndex + 1)
		end = False
	elif leftmostNumber10 > 0:
		number[leftmostNumber10Index] = ']'
		number.insert(leftmostNumber10Index, str(leftmostNumber10 / 2 + leftmostNumber10 % 2))
		number.insert(leftmostNumber10Index, ',')
		number.insert(leftmostNumber10Index, str(leftmostNumber10 / 2))
		number.insert(leftmostNumber10Index, '[')
		end = False
	if not end:
		number = reduceSnailNumber(number)
	return number

def countMagnitude(number):
	left = -1
	right = -1
	leftNumber = []
	rightNumberStart = 3
	rightNumber = []
	if number[1].isdigit():
		left = int(number[1])
	else:
		level = 1
		i = 2
		leftNumber.append('[')
		while level > 0:
			if number[i] == '[':
				level +=1
				leftNumber.append('[')
			elif number[i] == ']':
				level -=1
				leftNumber.append(']')
			else:
				leftNumber.append(number[i])
			i +=1
		left = countMagnitude(leftNumber)
		rightNumberStart = len(leftNumber) + 2
	if number[rightNumberStart].isdigit():
		right = int(number[rightNumberStart])
	else:
		level = 1
		i = rightNumberStart + 1
		rightNumber.append('[')
		while level > 0:
			if number[i] == '[':
				level +=1
				rightNumber.append('[')
			elif number[i] == ']':
				level -=1
				rightNumber.append(']')
			else:
				rightNumber.append(number[i])
			i +=1
		right = countMagnitude(rightNumber)

	return 3*left + 2*right


while len(elementsToAdd) > 0:
	summa = addTwoSnailNumbers(summa, elementsToAdd.pop(0))
	summa = reduceSnailNumber(summa)

print(countMagnitude(summa))



