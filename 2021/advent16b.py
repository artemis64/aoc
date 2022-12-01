file = open('input16.txt', 'r')

hexInput = file.readline().strip()

file.close()

binInput = str(bin(int(hexInput, 16)))
binInput = binInput[2:].zfill(4*len(hexInput))

def combineNumbers(numbers, typeId):
	if typeId == 0:
		number = 0
		for i in numbers:
			number += i
	elif typeId == 1:
		number = 1
		for i in numbers:
			number = number * i
	elif typeId == 2:
		number = min(numbers)
	elif typeId == 3:
		number = max(numbers)
	elif typeId == 5:
		number = 1 if numbers[0]>numbers[1] else 0
	elif typeId == 6:
		number = 1 if numbers[0]<numbers[1] else 0
	elif typeId == 7:
		number = 1 if numbers[0] == numbers[1] else 0
	else:
		number = ''
	return number


def processLiteralPackage(package):
	print(package)
	number = ''
	while int(package[0]) != 0:
		number += package[1:5]
		package = package[5:]
	number += package[1:5]
	number = int(number,2)
	print("number from a literal {}".format(number))
	return number

def processOperatorPackageByLength(package, typeI):
	versionSum = 0
	numbers = []
	while len(package)>0:
		if int(package[3:6],2) == 4:
			i = 6
			while int(package[i]) != 0:
				i += 5
			i += 5
			numbers.append(processLiteralPackage(package[6:i]))
			package = package[i:]
		else:
			if int(package[6]) == 0:
				typeId = int(package[3:6],2)
				length = int(package[7:22],2)
				numbers.append(processOperatorPackageByLength(package[22: 22+length], typeId))
				package = package[22+length:]
			else:
				subNumber = int(package[7:18],2)
				typeId = int(package[3:6],2)
				results = processOperatorPackageByNumber(package[18:], subNumber, typeId)
				numbers.append(results[0])
				package = package[18 + results[1]:]
	number = combineNumbers(numbers, typeI)
	print("number from operator by length {}, numbers {}, typeID {}".format(number,numbers,typeI))
	return number

def processOperatorPackageByNumber(package, numberSub, typeI):
	numbers = []
	totalLength = 0
	for _ in range(numberSub):
		if int(package[3:6],2) == 4:
			i = 6
			while int(package[i]) != 0:
				i += 5
			i += 5
			numbers.append(processLiteralPackage(package[6:i]))
			package = package[i:]
			totalLength += i
		else:
			if int(package[6]) == 0:
				typeId = int(package[3:6],2)
				length = int(package[7:22],2)
				numbers.append(processOperatorPackageByLength(package[22: 22+length],typeId))
				package = package[22+length:]
				totalLength += 22+length
			else:
				subNumber = int(package[7:18],2)
				typeId = int(package[3:6],2)
				results = processOperatorPackageByNumber(package[18:], subNumber, typeId)
				numbers.append(results[0])
				package = package[18 + results[1]:]
				totalLength += 18 + results[1]
	number = combineNumbers(numbers, typeI)
	print("number from operator by number {}, numbers {}, typeID {}, number of subpackages {}".format(number,numbers,typeI, numberSub))
	return (number, totalLength)


if int(binInput[3:6],2) == 4:
	i = 6
	while int(binInput[i]) != 0:
		i += 5
	i += 5
	finalNumber = processLiteralPackage(binInput[6:i])
	print("literal")
else:
	if int(binInput[6]) == 0:
		length = int(binInput[7:22],2)
		typeId = int(binInput[3:6],2)
		finalNumber = processOperatorPackageByLength(binInput[22: 22+length],typeId)
		print("length")
	else:
		subNumber = int(binInput[7:18],2)
		typeId = int(binInput[3:6],2)
		results = processOperatorPackageByNumber(binInput[18:], subNumber, typeId)
		finalNumber = results[0]
		print("subp")

print(finalNumber)





