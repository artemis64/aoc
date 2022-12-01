file = open('input16.txt', 'r')

hexInput = file.readline().strip()

file.close()

binInput = str(bin(int(hexInput, 16)))
binInput = binInput[2:].zfill(4*len(hexInput))

versionSum = 0

def processLiteralPackage(package):
	number = ''
	while int(package[0]) != 0:
		number += package[:5]
		package = package[5:]
	number += package[:5]
	number = int(number,2)
	return number

def processOperatorPackageByLength(package):
	versionSum = 0
	while len(package)>0:
		if int(package[3:6],2) == 4:
			versionSum += int(package[:3],2)
			i = 6
			while int(package[i]) != 0:
				i += 5
			i += 5
			processLiteralPackage(package[6:i])
			package = package[i:]
		else:
			if int(package[6]) == 0:
				length = int(package[7:22],2)
				versionSum += int(package[:3],2)
				versionSum += processOperatorPackageByLength(package[22: 22+length])
				package = package[22+length:]
			else:
				subNumber = int(package[7:18],2)
				versionSum += int(package[:3],2)
				results = processOperatorPackageByNumber(package[18:], subNumber)
				versionSum += results[0]
				package = package[18 + results[1]:]
	return versionSum

def processOperatorPackageByNumber(package, number):
	versionSum = 0
	totalLength = 0
	for _ in range(number):
		if int(package[3:6],2) == 4:
			versionSum += int(package[:3],2)
			i = 6
			while int(package[i]) != 0:
				i += 5
			i += 5
			processLiteralPackage(package[6:i])
			package = package[i:]
			totalLength += i
		else:
			if int(package[6]) == 0:
				length = int(package[7:22],2)
				versionSum += int(package[:3],2)
				versionSum += processOperatorPackageByLength(package[22: 22+length])
				package = package[22+length:]
				totalLength += 22+length
			else:
				subNumber = int(package[7:18],2)
				versionSum += int(package[:3],2)
				results = processOperatorPackageByNumber(package[18:], subNumber)
				versionSum += results[0]
				package = package[18 + results[1]:]
				totalLength += 18 + results[1]
	return (versionSum, totalLength)


if int(binInput[3:6],2) == 4:
	versionSum += int(binInput[:3],2)
	i = 6
	while int(binInput[i]) != 0:
		i += 5
	i += 5
	processLiteralPackage(binInput[6:i])
else:
	if int(binInput[6]) == 0:
		length = int(binInput[7:22],2)
		versionSum += int(binInput[:3],2)
		versionSum += processOperatorPackageByLength(binInput[22: 22+length])
	else:
		subNumber = int(binInput[7:18],2)
		versionSum += int(binInput[:3],2)
		results = processOperatorPackageByNumber(binInput[18:], subNumber)
		versionSum += results[0]

print(versionSum)





